"""
Módulo: Condução, Convecção e Radiação
Referência: Volume II, Capítulo 3
"""
import numpy as np

SIGMA = 5.67e-8

def R_cond(k: float, L: float, A: float) -> float:
    return L / (k * A)

def R_cond_cyl(k: float, Di: float, Do: float, L: float = 1.0) -> float:
    return np.log(Do/Di) / (2 * np.pi * k * L)

def R_conv(h: float, A: float) -> float:
    return 1 / (h * A)

def radiation_flux(eps: float, Ts: float, Tinf: float, linearize: bool = False) -> float:
    if linearize:
        Tm = (Ts + Tinf) / 2
        h_rad = 4 * eps * SIGMA * Tm**3
        return h_rad * (Ts - Tinf)
    return eps * SIGMA * (Ts**4 - Tinf**4)

def thermal_network(R_list: list[float], dT: float) -> float:
    return dT / sum(R_list)

if __name__ == "__main__":
    Rs = [R_cond(0.7, 0.15, 10), R_cond(0.025, 0.05, 10), R_cond(0.5, 0.02, 10)]
    print("Q:", thermal_network(Rs, 20), "W")
    print("Radiação exata:", radiation_flux(0.90, 313.15, 263.15))
    print("Radiação linearizada:", radiation_flux(0.90, 313.15, 263.15, linearize=True))