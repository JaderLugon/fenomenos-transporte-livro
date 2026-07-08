"""
meio_poroso.py — Transporte em meio poroso.

Cobre:
- Lei de Darcy
- Modelo de van Genuchten-Mualem
- Curva de retenção e condutividade não-saturada
- Esquema implícito para Richards
"""

import numpy as np
from .utils import validar_positivo, validar_intervalo

# ============================================================================
# LEI DE DARCY
# ============================================================================

def fluxo_darcy(K: float, gradiente_h: float) -> float:
    """
    Fluxo de Darcy (velocidade aparente).
    
    q = -K · ∇h [m/s]
    
    Parâmetro
    ---------
    gradiente_h : float
        Gradiente de carga hidráulica [m/m, adimensional].
        Positivo se h cresce no sentido do escoamento.
    """
    validar_positivo(K, "condutividade hidráulica (K)")
    return -K * gradiente_h


def condutividade_hidraulica(k_intrinseca: float, rho: float,
                              mu: float, g: float = 9.81) -> float:
    """
    Converte permeabilidade intrínseca em condutividade hidráulica.
    
    K = k · ρ · g / μ [m/s]
    """
    validar_positivo(k_intrinseca, "permeabilidade intrínseca")
    validar_positivo(rho, "densidade")
    validar_positivo(mu, "viscosidade dinâmica")
    return k_intrinseca * rho * g / mu


def velocidade_intersticial(q: float, eta: float) -> float:
    """Velocidade real nos poros: u = q / η."""
    validar_positivo(eta, "porosidade (eta)")
    if eta > 1:
        raise ValueError("Porosidade deve ser ≤ 1")
    return q / eta


# ============================================================================
# VAN GENUCHTEN-MUALEN
# ============================================================================

def saturacao_efetiva(theta: float, theta_r: float, theta_s: float) -> float:
    """Saturação efetiva: Se = (θ - θr) / (θs - θr)."""
    validar_intervalo(theta, theta_r, theta_s, "theta")
    return (theta - theta_r) / (theta_s - theta_r)


def van_genuchten_theta(psi: float, theta_r: float, theta_s: float,
                        alpha: float, n: float) -> float:
    """
    Curva de retenção de van Genuchten: θ(ψ).
    
    θ = θr + (θs - θr) / [1 + (α·|ψ|)^n]^m
    
    Parâmetros
    ----------
    psi : float
        Potencial matricial [m]. Negativos em solo não-saturado.
    """
    m = 1 - 1 / n
    psi_abs = abs(psi)
    return theta_r + (theta_s - theta_r) / (1 + (alpha * psi_abs) ** n) ** m


def van_genuchten_K(theta: float, theta_r: float, theta_s: float,
                    K_sat: float, n: float, L: float = 0.5) -> float:
    """
    Condutividade hidráulica não-saturada de Mualem.
    
    K(θ) = Ksat · Se^L · [1 - (1 - Se^(1/m))^m]^2
    """
    Se = saturacao_efetiva(theta, theta_r, theta_s)
    m = 1 - 1 / n
    termo_interno = 1 - (1 - Se ** (1 / m)) ** m
    return K_sat * (Se ** L) * (termo_interno ** 2)


def curva_retencao(psi_array, theta_r, theta_s, alpha, n):
    """
    Gera a curva de retenção θ(ψ) para um array de ψ.
    
    Retorna
    -------
    tuple
        (psi, theta, Se)
    """
    psi_array = np.atleast_1d(psi_array)
    theta = np.array([van_genuchten_theta(p, theta_r, theta_s, alpha, n)
                      for p in psi_array])
    Se = np.array([saturacao_efetiva(t, theta_r, theta_s) for t in theta])
    return psi_array, theta, Se


# ============================================================================
# ESQUEMA IMPLÍCITO PARA RICHARDS (LINEARIZADO)
# ============================================================================

def montar_matriz_richards(N: int, dx: float, dt: float,
                            D0: float, u0: float) -> dict:
    """
    Monta a matriz tridiagonal A e vetor b para o esquema
    implícito da equação de Richards linearizada.
    
    ∂θ/∂t + u0·∂θ/∂x = D0·∂²θ/∂x²
    
    Retorna
    -------
    dict
        {'A': matriz tridiagonal, 'a': subdiagonal,
         'b': diagonal, 'c': superdiagonal,
         'alpha_A': número advectivo, 'alpha_D': número difusivo}
    """
    alpha_A = u0 * dt / dx
    alpha_D = D0 * dt / dx**2
    
    # Coeficientes
    a = -alpha_D * np.ones(N)       # subdiagonal
    b = (1 + 2 * alpha_D + alpha_A) * np.ones(N)  # diagonal
    c = -(alpha_D - alpha_A) * np.ones(N)  # superdiagonal
    
    # Monta matriz densa (para fins didáticos)
    A = np.diag(b) + np.diag(a[1:], -1) + np.diag(c[:-1], 1)
    
    return {
        "A": A,
        "a": a, "b": b, "c": c,
        "alpha_A": alpha_A,
        "alpha_D": alpha_D
    }


def resolver_tridiagonal(a, b, c, d):
    """
    Resolve sistema tridiagonal Ax = d pelo algoritmo de Thomas.
    
    Parâmetros
    ----------
    a : array
        Subdiagonal (a[0] ignorado).
    b : array
        Diagonal principal.
    c : array
        Superdiagonal (c[-1] ignorado).
    d : array
        Vetor do lado direito.
    
    Retorna
    -------
    array
        Solução x.
    """
    n = len(d)
    c_ = np.zeros(n)
    d_ = np.zeros(n)
    
    # Eliminação para frente
    c_[0] = c[0] / b[0]
    d_[0] = d[0] / b[0]
    for i in range(1, n):
        denom = b[i] - a[i] * c_[i - 1]
        c_[i] = c[i] / denom
        d_[i] = (d[i] - a[i] * d_[i - 1]) / denom
    
    # Substituição para trás
    x = np.zeros(n)
    x[-1] = d_[-1]
    for i in range(n - 2, -1, -1):
        x[i] = d_[i] - c_[i] * x[i + 1]
    
    return x