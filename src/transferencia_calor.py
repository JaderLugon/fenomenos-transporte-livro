"""
transferencia_calor.py — Transferência de calor: fundamentos, trocadores e aletas.

Cobre:
- Resistências térmicas em série
- LMTD unificada
- Método ε-NTU (várias configurações)
- Aletas: eficiência, efetividade, calor dissipado
- Correlações convectivas (Dittus-Boelter, Churchill-Chu)
"""

import numpy as np
from scipy.special import iv as besseli  # Bessel modificada I_n
from .utils import (validar_positivo, validar_intervalo,
                    celsius_para_kelvin, media_logaritmica)

# ============================================================================
# RESISTÊNCIAS TÉRMICAS
# ============================================================================

def R_conveccao(h: float, A: float) -> float:
    """Resistência térmica por convecção: R = 1/(h·A) [K/W]."""
    validar_positivo(h, "coeficiente convectivo (h)")
    validar_positivo(A, "área (A)")
    return 1.0 / (h * A)


def R_conducao_plana(L: float, k: float, A: float) -> float:
    """Resistência térmica por condução em parede plana: R = L/(k·A) [K/W]."""
    validar_positivo(L, "espessura (L)")
    validar_positivo(k, "condutividade (k)")
    validar_positivo(A, "área (A)")
    return L / (k * A)


def R_conducao_cilindrica(Di: float, De: float, k: float, L: float) -> float:
    """
    Resistência térmica por condução em cilindro (por comprimento L).
    
    R = ln(De/Di) / (2·π·k·L) [K/W]
    """
    validar_positivo(Di, "Diâmetro interno")
    validar_positivo(De, "Diâmetro externo")
    if De <= Di:
        raise ValueError("De deve ser maior que Di")
    return np.log(De / Di) / (2 * np.pi * k * L)


def circuito_termico_serie(R_list: list) -> float:
    """Soma resistências térmicas em série."""
    return sum(R_list)


# ============================================================================
# LMTD UNIFICADA
# ============================================================================

def lmtd(Th_in: float, Th_out: float, Tc_in: float, Tc_out: float,
         tipo: str = "contracorrente") -> float:
    """
    Calcula a Diferença Média Logarítmica de Temperatura (LMTD).
    
    Parâmetros
    ----------
    Th_in, Th_out : float
        Temperaturas de entrada e saída do fluido quente [°C ou K].
    Tc_in, Tc_out : float
        Temperaturas de entrada e saída do fluido frio [°C ou K].
    tipo : str
        'contracorrente' ou 'paralelo'.
    
    Retorna
    -------
    float
        LMTD [mesma unidade das temperaturas].
    """
    if tipo == "contracorrente":
        dT1 = Th_in - Tc_out
        dT2 = Th_out - Tc_in
    elif tipo == "paralelo":
        dT1 = Th_in - Tc_in
        dT2 = Th_out - Tc_out
    else:
        raise ValueError("tipo deve ser 'contracorrente' ou 'paralelo'")
    
    if dT1 <= 0 or dT2 <= 0:
        raise ValueError(
            "Diferenças de temperatura devem ser positivas. "
            "Verifique se as temperaturas são coerentes."
        )
    
    return media_logaritmica(dT1, dT2)


# ============================================================================
# MÉTODO ε-NTU
# ============================================================================

def epsilon_ntu(NTU: float, Cr: float,
                tipo: str = "contracorrente") -> float:
    """
    Calcula a efetividade ε de um trocador de calor.
    
    Parâmetros
    ----------
    NTU : float
        Número de Unidades de Transferência.
    Cr : float
        Razão de capacidades térmicas Cmin/Cmax (0 ≤ Cr ≤ 1).
    tipo : str
        'contracorrente', 'paralelo', 'condensador' ou 'cruzado'.
    
    Retorna
    -------
    float
        Efetividade ε (0 < ε ≤ 1).
    """
    validar_positivo(NTU, "NTU")
    validar_intervalo(Cr, 0, 1, "Cr")
    
    if tipo == "condensador" or Cr == 0:
        # Mudança de fase: Cmax → ∞, Cr = 0
        return 1 - np.exp(-NTU)
    
    elif tipo == "contracorrente":
        exp_term = np.exp(-NTU * (1 - Cr))
        return (1 - exp_term) / (1 - Cr * exp_term)
    
    elif tipo == "paralelo":
        return (1 - np.exp(-NTU * (1 + Cr))) / (1 + Cr)
    
    elif tipo == "cruzado":
        # Ambos fluidos não misturados (aproximação)
        return 1 - np.exp(
            (np.exp(-NTU**0.22 * Cr) - 1) / (NTU**-0.22 * Cr)
        )
    
    else:
        raise ValueError(f"Tipo '{tipo}' não reconhecido")


def calcular_trocador(U: float, A: float, C_h: float, C_c: float,
                      Th_in: float, Tc_in: float,
                      tipo: str = "contracorrente") -> dict:
    """
    Dimensiona um trocador de calor via método ε-NTU.
    
    Retorna temperaturas de saída e carga térmica.
    """
    C_min = min(C_h, C_c)
    C_max = max(C_h, C_c)
    Cr = C_min / C_max
    NTU = U * A / C_min
    eps = epsilon_ntu(NTU, Cr, tipo)
    
    Q_max = C_min * (Th_in - Tc_in)
    Q = eps * Q_max
    
    # Temperaturas de saída
    Th_out = Th_in - Q / C_h
    Tc_out = Tc_in + Q / C_c
    
    return {
        "NTU": NTU,
        "Cr": Cr,
        "epsilon": eps,
        "Q": Q,
        "Th_out": Th_out,
        "Tc_out": Tc_out
    }


# ============================================================================
# ALETAS
# ============================================================================

def parametro_aleta(h: float, P: float, k: float, Ac: float) -> float:
    """
    Calcula o parâmetro m da aleta.
    
    m = √(h·P / (k·Ac)) [m^-1]
    """
    validar_positivo(h, "h")
    validar_positivo(P, "perímetro (P)")
    validar_positivo(k, "condutividade (k)")
    validar_positivo(Ac, "área da seção (Ac)")
    return np.sqrt(h * P / (k * Ac))


def eficiencia_aleta_retangular(m: float, L: float, t: float = 0.0) -> float:
    """
    Eficiência de aleta retangular com ponta adiabática.
    
    η = tanh(m·Lc) / (m·Lc)
    
    Parâmetros
    ----------
    m : float
        Parâmetro da aleta [m^-1].
    L : float
        Comprimento real [m].
    t : float, opcional
        Espessura da aleta [m] (para correção Lc = L + t/2).
    """
    Lc = L + t / 2.0
    mLc = m * Lc
    return np.tanh(mLc) / mLc


def eficiencia_aleta_cilindrica(m: float, L: float) -> float:
    """Eficiência de aleta cilíndrica (pin): η = tanh(m·L) / (m·L)."""
    mL = m * L
    return np.tanh(mL) / mL


def eficiencia_aleta_anular(r1: float, r2: float, t: float,
                            h: float, k: float) -> float:
    """
    Eficiência de aleta anular (aproximação via Schmidt).
    
    Usa a metodologia do gráfico de eficiência de aletas anulares
    via parâmetro mLc e razão r2c/r1.
    """
    L = r2 - r1
    Lc = L + t / 2.0
    r2c = r1 + Lc
    Ac = 2 * np.pi * r1 * t  # aproximação
    P = 2 * np.pi * ((r1 + r2) / 2)  # perímetro médio
    m = parametro_aleta(h, P, k, Ac)
    # Aproximação via aleta reta equivalente
    return np.tanh(m * Lc) / (m * Lc)


def calor_aleta(m: float, h: float, P: float, k: float, Ac: float,
                theta_b: float, L: float) -> float:
    """
    Calor dissipado por aleta com ponta adiabática.
    
    q = √(h·P·k·Ac) · θb · tanh(m·L)
    """
    return np.sqrt(h * P * k * Ac) * theta_b * np.tanh(m * L)


def efetividade_aleta(q_fin: float, h: float, Ab: float,
                      theta_b: float) -> float:
    """
    Efetividade da aleta.
    
    ε = q_fin / (h · Ab · θb)
    """
    return q_fin / (h * Ab * theta_b)


# ============================================================================
# CORRELAÇÕES CONVECTIVAS
# ============================================================================

def nusselt_dittus_boelter(Re: float, Pr: float,
                           aquecimento: bool = True) -> float:
    """
    Número de Nusselt pela correlação de Dittus-Boelter.
    
    Nu = 0.023 · Re^0.8 · Pr^n
    n = 0.4 (aquecimento) ou 0.3 (resfriamento)
    
    Válida para Re > 10^4 e 0.6 < Pr < 160.
    """
    if Re < 10000:
        raise ValueError("Dittus-Boelter válida apenas para Re > 10^4")
    n = 0.4 if aquecimento else 0.3
    return 0.023 * (Re ** 0.8) * (Pr ** n)


def nusselt_churchill_chu(Ra: float, Pr: float) -> float:
    """
    Número de Nusselt pela correlação de Churchill-Chu
    para convecção natural em placa vertical.
    """
    termo = 1 + (0.492 / Pr) ** (9 / 16)
    return (0.825 + 0.387 * (Ra ** (1 / 6)) / (termo ** (8 / 27))) ** 2


def coeficiente_tubo(D: float, k_fluido: float, Re: float, Pr: float,
                     aquecimento: bool = True) -> float:
    """
    Coeficiente convectivo h para escoamento interno turbulento.
    
    h = Nu · k / D
    """
    Nu = nusselt_dittus_boelter(Re, Pr, aquecimento)
    return Nu * k_fluido / D