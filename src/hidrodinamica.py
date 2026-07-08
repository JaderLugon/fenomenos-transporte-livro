"""
hidrodinamica.py — Hidrodinâmica de tubulações e canais abertos.

Cobre:
- Equação de Manning para profundidade normal
- Condição CFL para águas rasas
- Número de Froude
- Perda de carga (Darcy-Weisbach, Swamee-Jain, Colebrook-White)
"""

import numpy as np
from scipy.optimize import brentq
from .utils import validar_positivo, classificar_regime, numero_reynolds

# ============================================================================
# MANNING E CANAIS ABERTOS
# ============================================================================

def manning_vazão(n: float, A: float, Rh: float, S0: float) -> float:
    """
    Calcula a vazão pela equação de Manning (SI).
    
    Q = (1/n) * A * Rh^(2/3) * S0^(1/2)
    
    Parâmetros
    ----------
    n : float
        Coeficiente de rugosidade de Manning [s/m^(1/3)].
    A : float
        Área molhada [m²].
    Rh : float
        Raio hidráulico [m].
    S0 : float
        Declividade do fundo [m/m, adimensional].
    
    Retorna
    -------
    float
        Vazão [m³/s].
    
    Exemplo
    -------
    >>> manning_vazão(0.035, 30.0, 0.71, 1e-4)
    6.80...
    """
    validar_positivo(n, "n (Manning)")
    validar_positivo(A, "área molhada (A)")
    validar_positivo(Rh, "raio hidráulico (Rh)")
    validar_nao_negativo(S0, "declividade (S0)")
    return (1.0 / n) * A * (Rh ** (2.0 / 3.0)) * (S0 ** 0.5)


def geometria_trapezoidal(b: float, m: float, h: float) -> dict:
    """
    Calcula propriedades geométricas de seção trapezoidal.
    
    Parâmetros
    ----------
    b : float
        Largura de fundo [m].
    m : float
        Inclinação do talude (H:V). Use m=0 para retangular.
    h : float
        Profundidade da lâmina d'água [m].
    
    Retorna
    -------
    dict
        {'A': área, 'P': perímetro, 'Rh': raio hidráulico,
         'B': largura da superfície livre}
    """
    validar_positivo(h, "profundidade (h)")
    A = (b + m * h) * h
    P = b + 2 * h * np.sqrt(1 + m**2)
    Rh = A / P
    B = b + 2 * m * h
    return {"A": A, "P": P, "Rh": Rh, "B": B}


def profundidade_normal(Q: float, n: float, b: float, m: float,
                        S0: float, h_max: float = 50.0) -> float:
    """
    Calcula a profundidade normal (hn) de um canal trapezoidal
    resolvendo Manning iterativamente.
    
    Parâmetros
    ----------
    Q : float
        Vazão [m³/s].
    n : float
        Rugosidade de Manning [s/m^(1/3)].
    b : float
        Largura de fundo [m].
    m : float
        Inclinação do talude (H:V).
    S0 : float
        Declividade do fundo [m/m].
    h_max : float, opcional
        Limite superior para busca [m].
    
    Retorna
    -------
    float
        Profundidade normal [m].
    """
    validar_positivo(Q, "vazão (Q)")
    
    def residual(h):
        geo = geometria_trapezoidal(b, m, h)
        Q_calc = manning_vazão(n, geo["A"], geo["Rh"], S0)
        return Q_calc - Q
    
    # Busca raiz no intervalo (1e-6, h_max)
    return brentq(residual, 1e-6, h_max)


def numero_froude(U: float, h: float, g: float = 9.81) -> float:
    """
    Calcula o número de Froude para canal com superfície livre.
    
    Fr = U / √(g·h)
    
    Retorna
    -------
    str ou float
        Se Fr < 1: 'subcritico' (fluvial)
        Se Fr = 1: 'critico'
        Se Fr > 1: 'supercritico' (torrencial)
    """
    Fr = U / np.sqrt(g * h)
    if Fr < 0.95:
        return Fr, "subcritico"
    elif Fr > 1.05:
        return Fr, "supercritico"
    else:
        return Fr, "critico"


# ============================================================================
# CONDIÇÃO CFL (ÁGUAS RASAS)
# ============================================================================

def celeridade_onda(h: float, g: float = 9.81) -> float:
    """Celeridade da onda gravitacional em águas rasas: c = √(g·h)."""
    validar_positivo(h, "lâmina d'água (h)")
    return np.sqrt(g * h)


def passo_tempo_cfl(U: float, h: float, dx: float,
                    Cmax: float = 0.8, g: float = 9.81) -> float:
    """
    Calcula o passo de tempo máximo para estabilidade CFL
    em esquemas explícitos de águas rasas.
    
    CFL = (|U| + √(g·h)) · Δt / Δx ≤ Cmax
    
    Parâmetros
    ----------
    U : float
        Velocidade média [m/s].
    h : float
        Lâmina d'água [m].
    dx : float
        Espaçamento espacial [m].
    Cmax : float, opcional
        Número de Courant máximo (padrão: 0.8).
    g : float, opcional
        Aceleração da gravidade [m/s²].
    
    Retorna
    -------
    float
        Δt máximo [s].
    """
    c = celeridade_onda(h, g)
    v_max = abs(U) + c
    return Cmax * dx / v_max


# ============================================================================
# PERDA DE CARGA (TUBULAÇÕES)
# ============================================================================

def fator_atrito_laminar(Re: float) -> float:
    """Fator de atrito para regime laminar: f = 64/Re."""
    validar_positivo(Re, "Reynolds")
    return 64.0 / Re


def fator_atrito_swamee_jain(Re: float, eps_D: float) -> float:
    """
    Fator de atrito pela correlação explícita de Swamee-Jain.
    
    Válida para 5000 < Re < 10^8 e 10^-6 < ε/D < 10^-2.
    """
    validar_positivo(Re, "Reynolds")
    validar_nao_negativo(eps_D, "rugosidade relativa (ε/D)")
    
    termo1 = eps_D / 3.7
    termo2 = 5.74 / (Re ** 0.9)
    log_arg = termo1 + termo2
    return 0.25 / (np.log10(log_arg) ** 2)


def fator_atrito_colebrook(Re: float, eps_D: float,
                           tol: float = 1e-8, max_iter: int = 100) -> float:
    """
    Fator de atrito pela equação implícita de Colebrook-White,
    resolvida por iteração de ponto fixo.
    
    1/√f = -2·log10(ε/(3.7D) + 2.51/(Re·√f))
    """
    validar_positivo(Re, "Reynolds")
    
    # Estimativa inicial via Swamee-Jain
    f = fator_atrito_swamee_jain(Re, eps_D)
    
    for _ in range(max_iter):
        f_novo = 1.0 / (-2.0 * np.log10(eps_D / 3.7 + 2.51 / (Re * np.sqrt(f)))) ** 2
        if abs(f_novo - f) < tol:
            return f_novo
        f = f_novo
    
    raise RuntimeError(f"Colebrook não convergiu em {max_iter} iterações")


def perda_carga_darcy(f: float, L: float, D: float,
                      V: float, g: float = 9.81) -> float:
    """
    Perda de carga distribuída pela equação de Darcy-Weisbach.
    
    hf = f · (L/D) · (V²/(2g))
    """
    validar_positivo(f, "fator de atrito (f)")
    validar_positivo(L, "comprimento (L)")
    validar_positivo(D, "diâmetro (D)")
    return f * (L / D) * (V**2 / (2 * g))


def perda_carga_localizada(K: float, V: float, g: float = 9.81) -> float:
    """Perda de carga localizada: hs = K · V²/(2g)."""
    validar_nao_negativo(K, "coeficiente K")
    return K * (V**2 / (2 * g))


# ============================================================================
# POTÊNCIA DE BOMBA
# ============================================================================

def potencia_bomba(gamma: float, Q: float, HB: float,
                   eta: float = 1.0) -> dict:
    """
    Calcula potência hidráulica e elétrica de uma bomba.
    
    Parâmetros
    ----------
    gamma : float
        Peso específico do fluido [N/m³].
    Q : float
        Vazão [m³/s].
    HB : float
        Altura manométrica [m].
    eta : float, opcional
        Rendimento global da bomba (0 < η ≤ 1).
    
    Retorna
    -------
    dict
        {'P_hid': potência hidráulica [W],
         'P_el': potência elétrica [W],
         'P_cv': potência em cv}
    """
    validar_positivo(eta, "rendimento (eta)")
    if eta > 1.0:
        raise ValueError("Rendimento não pode exceder 1.0")
    
    P_hid = gamma * Q * HB
    P_el = P_hid / eta
    return {
        "P_hid": P_hid,
        "P_el": P_el,
        "P_cv": P_el / 735.5
    }