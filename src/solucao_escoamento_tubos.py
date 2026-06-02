"""
pipe_flow_solver.py
Solução de escoamento em tubulações: Darcy-Weisbach, Colebrook-White (Newton-Raphson),
Swamee-Jain (explícito), cálculo de potência e custo de bombeamento.
Ref: Vol I, Cap. 4, Exercícios 1 e 2
"""
import numpy as np
from scipy.optimize import newton

# Constantes padrão
G = 9.81  # m/s²
NU_WATER = 1e-6  # m²/s @ 20°C
RHO_WATER = 998.0  # kg/m³
GAMMA = RHO_WATER * G  # N/m³

def colebrook_white(f, Re, eps_D):
    """Função implícita de Colebrook-White para Newton-Raphson."""
    return 1/np.sqrt(f) + 2*np.log10(eps_D/3.7 + 2.51/(Re*np.sqrt(f)))

def solve_friction_factor(Re, eps_D, method='swamee', tol=1e-8, max_iter=50):
    """Calcula o fator de atrito f."""
    if method == 'swamee':
        return 0.25 / (np.log10(eps_D/3.7 + 5.74/Re**0.9))**2
    elif method == 'colebrook':
        f_guess = 0.02  # Chute inicial típico
        return newton(colebrook_white, f_guess, args=(Re, eps_D), tol=tol, maxiter=max_iter)
    else:
        raise ValueError("Método inválido. Use 'swamee' ou 'colebrook'.")

def pipe_head_loss(Q, D, L, eps, nu=NU_WATER, method='swamee'):
    """Perda de carga distribuída h_f."""
    A = np.pi * D**2 / 4
    V = Q / A
    Re = V * D / nu
    eps_D = eps / D
    f = solve_friction_factor(Re, eps_D, method=method)
    hf = f * (L/D) * (V**2 / (2*G))
    return hf, Re, f, V

def pump_cost(Q, H_b, eta, hours_per_day, tariff, days=30):
    """Custo mensal de bombeamento."""
    P_hid = GAMMA * Q * H_b  # W
    P_el = P_hid / eta  # W
    energy_kWh = (P_el / 1000) * hours_per_day * days
    cost = energy_kWh * tariff
    return P_el/1000, energy_kWh, cost

if __name__ == "__main__":
    # Exemplo Vol 1, Cap 4, Ex 1
    hf, Re, f, V = pipe_head_loss(Q=0.003, D=0.075, L=80, eps=0.00015)
    print(f"Re={Re:.1e}, f={f:.4f}, V={V:.3f} m/s, hf={hf:.3f} m")
    
    # Exemplo Vol 1, Cap 4, Ex 2
    P_kw, E_kWh, cost = pump_cost(Q=0.005, H_b=30, eta=0.70, hours_per_day=6, tariff=0.90)
    print(f"Potência: {P_kw:.3f} kW | Energia: {E_kWh:.1f} kWh | Custo: R$ {cost:.2f}")