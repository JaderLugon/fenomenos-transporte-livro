"""
utils.py — Funções auxiliares transversais aos módulos.

Contém validações, conversões e ferramentas matemáticas
usadas em múltiplos capítulos do livro.
"""

import numpy as np
from typing import Union, Tuple

# ============================================================================
# CONVERSÕES DE UNIDADES
# ============================================================================

def celsius_para_kelvin(T_C: float) -> float:
    """Converte temperatura de Celsius para Kelvin."""
    return T_C + 273.15


def kelvin_para_celsius(T_K: float) -> float:
    """Converte temperatura de Kelvin para Celsius."""
    return T_K - 273.15


def mm_para_m(valor_mm: float) -> float:
    """Converte milímetros para metros."""
    return valor_mm * 1e-3


def polegadas_para_m(valor_in: float) -> float:
    """Converte polegadas para metros."""
    return valor_in * 0.0254


def L_s_para_m3_s(valor_L_s: float) -> float:
    """Converte litros por segundo para m³/s."""
    return valor_L_s * 1e-3


def m3_s_para_L_s(valor_m3_s: float) -> float:
    """Converte m³/s para litros por segundo."""
    return valor_m3_s * 1000


def cSt_para_m2_s(valor_cSt: float) -> float:
    """Converte centistokes para m²/s (viscosidade cinemática)."""
    return valor_cSt * 1e-6


def bar_para_Pa(valor_bar: float) -> float:
    """Converte bar para Pascal."""
    return valor_bar * 1e5


def Pa_para_bar(valor_Pa: float) -> float:
    """Converte Pascal para bar."""
    return valor_Pa * 1e-5


# ============================================================================
# VALIDAÇÕES
# ============================================================================

def validar_positivo(valor: float, nome: str = "valor") -> None:
    """Lança ValueError se o valor não for positivo."""
    if valor <= 0:
        raise ValueError(f"{nome} deve ser positivo. Recebido: {valor}")


def validar_nao_negativo(valor: float, nome: str = "valor") -> None:
    """Lança ValueError se o valor for negativo."""
    if valor < 0:
        raise ValueError(f"{nome} deve ser não-negativo. Recebido: {valor}")


def validar_intervalo(valor: float, minimo: float, maximo: float,
                      nome: str = "valor") -> None:
    """Lança ValueError se o valor estiver fora do intervalo [min, max]."""
    if not (minimo <= valor <= maximo):
        raise ValueError(
            f"{nome} deve estar em [{minimo}, {maximo}]. Recebido: {valor}"
        )


# ============================================================================
# FERRAMENTAS MATEMÁTICAS
# ============================================================================

def media_logaritmica(T1: float, T2: float, tol: float = 1e-6) -> float:
    """
    Calcula a média logarítmica unificada (LMTD).
    
    Trata o caso limite T1 ≈ T2 (evita divisão por zero).
    
    Parâmetros
    ----------
    T1, T2 : float
        Diferenças de temperatura nas extremidades [K ou °C].
    tol : float, opcional
        Tolerância para considerar T1 ≈ T2.
    
    Retorna
    -------
    float
        Média logarítmica [mesma unidade de T1, T2].
    
    Exemplo
    -------
    >>> media_logaritmica(40, 20)
    28.853900817779268
    >>> media_logaritmica(30, 30)
    30.0
    """
    if abs(T1 - T2) < tol:
        return (T1 + T2) / 2.0
    return (T1 - T2) / np.log(T1 / T2)


def numero_reynolds(U: float, L: float, nu: float) -> float:
    """
    Calcula o número de Reynolds.
    
    Re = U * L / ν
    
    Parâmetros
    ----------
    U : float
        Velocidade característica [m/s].
    L : float
        Comprimento característico [m].
    nu : float
        Viscosidade cinemática [m²/s].
    
    Retorna
    -------
    float
        Número de Reynolds [adimensional].
    """
    validar_positivo(nu, "viscosidade cinemática (nu)")
    return U * L / nu


def classificar_regime(Re: float, Re_lam: float = 2000,
                       Re_turb: float = 2400) -> str:
    """
    Classifica o regime de escoamento em tubo circular.
    
    Parâmetros
    ----------
    Re : float
        Número de Reynolds.
    Re_lam : float, opcional
        Limite inferior da transição (padrão: 2000).
    Re_turb : float, opcional
        Limite superior da transição (padrão: 2400).
    
    Retorna
    -------
    str
        'laminar', 'transicao' ou 'turbulento'.
    """
    if Re < Re_lam:
        return "laminar"
    elif Re > Re_turb:
        return "turbulento"
    else:
        return "transicao"