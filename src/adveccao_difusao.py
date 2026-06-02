"""
Módulo: Advecção e Dispersão em Rios
Referência: Volume II, Capítulo 6
"""
import numpy as np

def dispersion_coefficients(U: float, B: float, D: float, S0: float,
                            beta: float = 0.011, phi: float = 0.23, kappa: float = 0.067,
                            g: float = 9.81) -> dict:
    U_star = np.sqrt(g * D * S0)
    EL = beta * (U**2 * B**2) / (D * U_star)
    ET = phi * D * U_star
    EV = kappa * D * U_star
    return {"U_star": U_star, "EL": EL, "ET": ET, "EV": EV}

def mixing_length(U: float, B: float, ET: float, K: float = 0.28) -> float:
    return K * U * B**2 / ET

def gaussian_2d(M: float, U: float, EL: float, ET: float, t: float,
                x: np.ndarray, y: np.ndarray, xs: float = 0, ys: float = 0) -> np.ndarray:
    dx = x - xs - U*t
    dy = y - ys
    coef = M / (4 * np.pi * t * np.sqrt(EL * ET))
    expo = - (dx**2 / (4*EL*t) + dy**2 / (4*ET*t))
    return coef * np.exp(expo)

if __name__ == "__main__":
    coeffs = dispersion_coefficients(0.20, 42.2, 0.71, 0.0005)
    print(coeffs)
    print("LT:", mixing_length(0.20, 42.2, coeffs["ET"]))
    X, Y = np.meshgrid(np.linspace(3000, 5000, 10), np.linspace(0, 42, 10))
    C = gaussian_2d(35, 0.20, coeffs["EL"], coeffs["ET"], 3600, X, Y, 3000, 2)
    print("C_max:", C.max(), "kg/m³")