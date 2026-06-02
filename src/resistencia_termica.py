"""
thermal_resistance.py
Redes de resistência térmica: série/paralelo, aletas, radiação não-linear.
Ref: Vol II, Cap. 2
"""
import numpy as np

def R_plane(k, L, A): return L/(k*A)
def R_cyl(k, Di, Do, L=1.0): return np.log(Do/Di)/(2*np.pi*k*L)
def R_conv(h, A): return 1/(h*A)

def solve_network(R_list, T_hot, T_cold):
    """Calcula fluxo de calor em série: Q = ΔT / ΣR"""
    R_total = sum(R_list)
    Q = (T_hot - T_cold) / R_total
    return Q, R_total

def fin_efficiency_rect(h, P, k, Ac, L):
    """Eficiência de aleta retangular (ponta adiabática)."""
    m = np.sqrt(h*P/(k*Ac))
    Lc = L + 0.5*np.sqrt(Ac)  # Correção de comprimento
    return np.tanh(m*Lc)/(m*Lc)

def radiation_flux(eps, T_s, T_inf, h_conv=0, sigma=5.67e-8):
    """Fluxo líquido (radiação + convecção opcional)."""
    return eps*sigma*(T_s**4 - T_inf**4) + h_conv*(T_s - T_inf)

if __name__ == "__main__":
    # Ex 1: Parede composta
    R_tij = R_plane(0.7, 0.15, 10)
    R_iso = R_plane(0.025, 0.05, 10)
    R_ges = R_plane(0.5, 0.02, 10)
    Q, Rtot = solve_network([R_tij, R_iso, R_ges], 25, 5)
    print(f"Parede: Q={Q:.1f} W, R_total={Rtot:.4f} K/W")
    
    # Ex 3: Radiação
    q_rad = radiation_flux(eps=0.90, T_s=313.15, T_inf=263.15)
    print(f"Radiação líquida: {q_rad:.1f} W/m²")