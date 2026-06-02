"""
Módulo: Escoamento em Tubulações e Bombeamento
Referência: Volume I, Capítulo 4
"""
import numpy as np
from scipy.optimize import newton

G = 9.81
NU_WATER = 1e-6
GAMMA = 998.0 * G

def colebrook(f: float, Re: float, eps_D: float) -> float:
    return 1/np.sqrt(f) + 2*np.log10(eps_D/3.7 + 2.51/(Re*np.sqrt(f)))

def swamee_jain(Re: float, eps_D: float) -> float:
    return 0.25 / (np.log10(eps_D/3.7 + 5.74/Re**0.9))**2

def friction_factor(Re: float, eps_D: float, method: str = "swamee") -> float:
    if Re < 2000:
        return 64/Re
    if method == "colebrook":
        return newton(colebrook, 0.02, args=(Re, eps_D), tol=1e-8, maxiter=20)
    return swamee_jain(Re, eps_D)

def head_loss(Q: float, D: float, L: float, eps: float, nu: float = NU_WATER, method: str = "swamee") -> dict:
    A = np.pi * D**2 / 4
    V = Q / A
    Re = V * D / nu
    eps_D = eps / D
    f = friction_factor(Re, eps_D, method)
    hf = f * (L/D) * (V**2 / (2*G))
    return {"Re": Re, "V": V, "f": f, "hf": hf}

def pump_power_cost(Q: float, H_B: float, eta: float, h_day: float, tariff: float, days: int = 30) -> dict:
    P_hid = GAMMA * Q * H_B
    P_el = P_hid / eta
    E_kWh = (P_el / 1000) * h_day * days
    return {"P_el_kW": P_el/1000, "E_kWh": E_kWh, "cost_BRL": E_kWh * tariff}

if __name__ == "__main__":
    print(head_loss(0.003, 0.075, 80, 0.00015))
    print(pump_power_cost(0.005, 30, 0.70, 6, 0.90))