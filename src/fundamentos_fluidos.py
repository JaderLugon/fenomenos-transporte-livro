"""
Módulo: Fundamentos dos Fluidos e Viscosidade
Referência: Volume I, Capítulo 2
"""
import numpy as np

def newton_shear_stress(mu: float, U: float, h: float) -> float:
    """Tensão de cisalhamento para escoamento de Couette plano."""
    return mu * U / h

def kinematic_viscosity(mu: float, rho: float) -> tuple[float, float]:
    """Retorna viscosidade cinemática em m²/s e centistokes."""
    nu = mu / rho
    return nu, nu * 1e6

def herschel_bulkley(tau0: float, K: float, n: float, gamma_dot: float) -> tuple[float, float]:
    """Tensão e viscosidade aparente para modelo Herschel-Bulkley."""
    if gamma_dot <= 0:
        return np.inf, np.inf
    tau = tau0 + K * gamma_dot**n
    return tau, tau / gamma_dot

def sutherland_viscosity(T_K: float, mu0: float = 1.716e-5, T0: float = 273.0, S: float = 111.0) -> float:
    """Viscosidade dinâmica de gases via fórmula de Sutherland."""
    return mu0 * (T_K / T0)**1.5 * (T0 + S) / (T_K + S)

if __name__ == "__main__":
    print("τ =", newton_shear_stress(0.04, 0.8, 0.002), "Pa")
    print("ν =", kinematic_viscosity(0.15, 850), "m²/s / cSt")
    print("HB:", herschel_bulkley(15, 8, 0.6, 50))
    print("μ(50°C):", sutherland_viscosity(323.15), "Pa·s")