"""
dispersao.py — Transporte de massa e calor em corpos hídricos.

Cobre:
- Coeficientes de dispersão (Liu, Elder, Jobson-Sayre)
- Soluções analíticas (instantâneo e contínuo)
- Comprimento de mistura transversal
- Número de Péclet
"""

import numpy as np
from scipy.special import erfc
from .utils import validar_positivo

# ============================================================================
# COEFICIENTES DE DISPERSÃO
# ============================================================================

def velocidade_atrito(D: float, S0: float, g: float = 9.81) -> float:
    """Velocidade de atrito: U* = √(g·D·S0)."""
    validar_positivo(D, "profundidade (D)")
    validar_positivo(S0, "declividade (S0)")
    return np.sqrt(g * D * S0)


def dispersao_longitudinal_liu(U: float, B: float, D: float,
                                U_star: float,
                                beta: float = 0.011) -> float:
    """
    Dispersão longitudinal pela correlação de Liu (1977).
    
    EL = β · U²·B² / (D·U*) [m²/s]
    """
    validar_positivo(U, "velocidade (U)")
    validar_positivo(B, "largura (B)")
    validar_positivo(D, "profundidade (D)")
    validar_positivo(U_star, "U*")
    return beta * (U**2 * B**2) / (D * U_star)


def dispersao_transversal_elder(D: float, U_star: float,
                                 phi: float = 0.23) -> float:
    """
    Dispersão transversal pela correlação de Elder (1959).
    
    ET = φ · D · U* [m²/s]
    
    φ ≈ 0.15-0.20 (canais retos)
    φ ≈ 0.40-0.80 (canais com curvas)
    """
    return phi * D * U_star


def dispersao_vertical_jobson_sayre(D: float, U_star: float,
                                     kappa: float = 0.067) -> float:
    """Dispersão vertical: EV = κ · D · U* [m²/s]."""
    return kappa * D * U_star


# ============================================================================
# NÚMERO DE PÉCLET
# ============================================================================

def numero_peclet(U: float, L: float, E: float) -> float:
    """
    Número de Péclet: Pe = U·L / E.
    
    Pe >> 1 → advecção dominante
    Pe << 1 → difusão dominante
    """
    validar_positivo(E, "coeficiente de dispersão (E)")
    return U * L / E


def classificar_transporte(Pe: float) -> str:
    """Classifica o regime de transporte pelo número de Péclet."""
    if Pe > 10:
        return "advecção dominante"
    elif Pe < 0.1:
        return "difusão dominante"
    else:
        return "misto (advecção e difusão comparáveis)"


# ============================================================================
# COMPRIMENTO DE MISTURA TRANSVERSAL
# ============================================================================

def comprimento_mistura_transversal(U: float, B: float, ET: float,
                                     margem: bool = True) -> float:
    """
    Distância para mistura completa na seção transversal.
    
    LT = K · U · B² / ET
    
    Parâmetro
    ---------
    margem : bool
        True → lançamento na margem (K ≈ 0.28)
        False → lançamento no centro (K ≈ 0.10)
    """
    K = 0.28 if margem else 0.10
    return K * U * B**2 / ET


# ============================================================================
# SOLUÇÕES ANALÍTICAS
# ============================================================================

def solucao_instantanea_1d(x: float, t: float, M: float, A: float,
                            U: float, EL: float,
                            k_dec: float = 0.0) -> float:
    """
    Solução analítica para lançamento instantâneo em 1D.
    
    C(x,t) = M / (A·√(4π·EL·t)) · exp[-(x-U·t)²/(4·EL·t)] · exp(-k·t)
    
    Parâmetros
    ----------
    x : float ou array
        Posição [m].
    t : float
        Tempo [s] (deve ser > 0).
    M : float
        Massa lançada [kg].
    A : float
        Área da seção transversal [m²].
    U : float
        Velocidade média [m/s].
    EL : float
        Dispersão longitudinal [m²/s].
    k_dec : float, opcional
        Coeficiente de decaimento de 1ª ordem [1/s].
    """
    if t <= 0:
        raise ValueError("Tempo deve ser positivo")
    
    x = np.atleast_1d(x)
    prefactor = M / (A * np.sqrt(4 * np.pi * EL * t))
    gaussiana = np.exp(-(x - U * t)**2 / (4 * EL * t))
    decaimento = np.exp(-k_dec * t)
    return prefactor * gaussiana * decaimento


def solucao_instantanea_2d(x: float, y: float, t: float,
                            M: float, D: float,
                            xs: float, ys: float,
                            U: float, EL: float, ET: float,
                            k_dec: float = 0.0) -> float:
    """
    Solução analítica 2D (integrada na vertical) para lançamento instantâneo.
    
    C(x,y,t) = M / (4π·t·D·√(EL·ET)) ·
               exp[-(x-xs-U·t)²/(4·EL·t) - (y-ys)²/(4·ET·t)] · exp(-k·t)
    """
    if t <= 0:
        raise ValueError("Tempo deve ser positivo")
    
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    prefactor = M / (4 * np.pi * t * D * np.sqrt(EL * ET))
    termo_x = np.exp(-(x - xs - U * t)**2 / (4 * EL * t))
    termo_y = np.exp(-(y - ys)**2 / (4 * ET * t))
    decaimento = np.exp(-k_dec * t)
    return prefactor * termo_x * termo_y * decaimento


def solucao_continua_1d(x: float, t: float, C0: float,
                         U: float, EL: float) -> float:
    """
    Solução analítica para lançamento contínuo em x=0.
    
    C(x,t) = (C0/2) · {erfc[(x-U·t)/√(4·EL·t)] +
                       exp(U·x/EL)·erfc[(x+U·t)/√(4·EL·t)]}
    """
    if t <= 0:
        return np.where(x < 0, C0, 0.0)
    
    x = np.atleast_1d(x)
    sqrt_term = np.sqrt(4 * EL * t)
    termo1 = erfc((x - U * t) / sqrt_term)
    termo2 = np.exp(U * x / EL) * erfc((x + U * t) / sqrt_term)
    return (C0 / 2) * (termo1 + termo2)


# ============================================================================
# TEMPO DE VIAGEM
# ============================================================================

def tempo_viagem(x: float, U: float) -> float:
    """Tempo de viagem advecivo: t = x / U [s]."""
    validar_positivo(U, "velocidade (U)")
    return x / U