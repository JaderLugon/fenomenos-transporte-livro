"""
Módulo: Balanços de Conservação e Números Adimensionais
Referência: Volume I, Capítulo 3
"""
import numpy as np

def tank_balance(Q_ent: float, Q_sai: float, A: float, h0: float, hf: float) -> float:
    """Tempo para atingir nível hf em tanque de base constante."""
    dhdt = (Q_ent - Q_sai) / A
    if dhdt == 0:
        return np.inf if hf != h0 else 0.0
    return abs(hf - h0) / abs(dhdt)

def dimensionless_numbers(U: float, L: float, nu: float, D: float | None = None,
                          alpha: float | None = None, g: float = 9.81) -> dict:
    """Calcula Re, Fr e, se fornecidos, Pe, Pr, Sc."""
    out = {"Re": U * L / nu, "Fr": U / np.sqrt(g * L)}
    if D is not None:
        out["Pe"] = U * L / D
        out["Sc"] = nu / D
    if alpha is not None:
        out["Pe_heat"] = U * L / alpha
        out["Pr"] = nu / alpha
    return out

def classify_regime(Re: float, Pe: float | None = None) -> str:
    if Re < 2000: regime = "Laminar"
    elif Re < 2400: regime = "Transição"
    else: regime = "Turbulento"
    if Pe is None:
        return regime
    transp = "Advectivo" if Pe > 1 else "Difusivo"
    return f"{regime} | {transp}"

if __name__ == "__main__":
    print("Tempo:", tank_balance(8e-4, 5e-4, 4, 0.5, 1.2), "s")
    print("Números:", dimensionless_numbers(0.6, 15, 1e-6, D=8))
    print("Regime:", classify_regime(5.09e4, 1.125))