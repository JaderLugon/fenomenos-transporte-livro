"""
Módulo: Aletas e Trocadores de Calor
Referência: Volume II, Capítulos 4-5
"""
import numpy as np

def fin_efficiency_rect(h: float, P: float, k: float, Ac: float, L: float) -> float:
    m = np.sqrt(h * P / (k * Ac))
    Lc = L + 0.5 * np.sqrt(Ac)
    return np.tanh(m * Lc) / (m * Lc)

def fin_effectiveness(h: float, P: float, k: float, Ac: float, L: float, Ab: float) -> float:
    m = np.sqrt(h * P / (k * Ac))
    q = np.sqrt(h * P * k * Ac) * np.tanh(m * L)
    return q / (h * Ab)

def LMTD_counter(Th_in: float, Th_out: float, Tc_in: float, Tc_out: float) -> float:
    dT1, dT2 = Th_in - Tc_out, Th_out - Tc_in
    if abs(dT1 - dT2) < 1e-9:
        return dT1
    return (dT1 - dT2) / np.log(dT1 / dT2)

def epsilon_NTU_counter(NTU: float, Cr: float) -> float:
    if abs(Cr - 1.0) < 1e-9:
        return NTU / (1 + NTU)
    return (1 - np.exp(-NTU * (1 - Cr))) / (1 - Cr * np.exp(-NTU * (1 - Cr)))

if __name__ == "__main__":
    Ac, P, L, h, k, Ab = 1.8e-4, 0.126, 0.04, 50, 205, 1.8e-4
    print("η:", fin_efficiency_rect(h, P, k, Ac, L))
    print("ε:", fin_effectiveness(h, P, k, Ac, L, Ab))
    print("LMTD:", LMTD_counter(150, 90, 30, 70))
    print("ε-NTU:", epsilon_NTU_counter(2.7, 0.5))