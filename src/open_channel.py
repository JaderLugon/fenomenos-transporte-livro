"""
Módulo: Hidrodinâmica de Canais Abertos
Referência: Volume I, Capítulo 5
"""
import numpy as np

def rect_geometry(B: float, h: float) -> dict:
    A = B * h
    P = B + 2*h
    Rh = A / P
    return {"A": A, "P": P, "Rh": Rh}

def manning_slope(Q: float, A: float, Rh: float, n: float) -> float:
    return (n * Q * abs(Q)) / (A**2 * Rh**(4/3))

def froude_number(V: float, h: float, g: float = 9.81) -> float:
    return V / np.sqrt(g * h)

def preissmann_scheme(L: float, T: float, dx: float, dt: float, theta: float = 1.0) -> dict:
    """Retorna parâmetros do esquema Preissmann implícito."""
    Nx = int(L/dx) + 1
    Nt = int(T/dt) + 1
    return {"Nx": Nx, "Nt": Nt, "theta": theta, "unconditional_stable": theta >= 0.5}

if __name__ == "__main__":
    geo = rect_geometry(10, 1.5)
    print(geo, "Sf:", manning_slope(12, geo["A"], geo["Rh"], 0.030))
    print("Fr:", froude_number(0.8, 1.5))
    print(preissmann_scheme(6300, 6*3600, 50, 30, theta=0.75))