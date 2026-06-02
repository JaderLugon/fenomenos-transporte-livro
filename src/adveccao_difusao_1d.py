"""
advection_diffusion_1d.py
Solução analítica gaussiana e numérica (FTCS implícito) para equação 1D:
∂C/∂t + U ∂C/∂x = E ∂²C/∂x²
Ref: Vol I, Cap. 3, Ex 3 & Vol II, Cap. 5
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

def analytical_gaussian(M, U, E, t, x, x0=0.0):
    """Solução analítica para lançamento instantâneo pontual."""
    sigma = np.sqrt(2*E*t)
    return (M / (np.sqrt(2*np.pi)*sigma)) * np.exp(-(x - x0 - U*t)**2 / (2*sigma**2))

def solve_crank_nicolson(U, E, L, T, Nx, Nt, IC='gaussian'):
    """Esquema Crank-Nicolson incondicionalmente estável."""
    dx = L / Nx
    dt = T / Nt
    x = np.linspace(0, L, Nx+1)
    C = np.zeros(Nx+1)
    
    # Condição inicial
    if IC == 'gaussian':
        C = 100 * np.exp(-(x - L/2)**2 / (0.1**2))
    
    alpha = U*dt/(2*dx)
    beta = E*dt/(2*dx**2)
    
    # Matriz tridiagonal
    main = 1 + 2*beta
    off = -beta
    A = np.diag(np.full(Nx-1, main)) + np.diag(np.full(Nx-2, off), -1) + np.diag(np.full(Nx-2, off), 1)
    
    for n in range(Nt):
        # Termo convectivo explícito (upwind para estabilidade)
        b = C[1:-1].copy() - alpha*(C[2:]-C[:-2]) + beta*(C[2:]-2*C[1:-1]+C[:-2])
        b[0] += alpha*C[0] - beta*C[0]
        b[-1] += beta*C[-1]
        
        C[1:-1] = np.linalg.solve(A, b)
        C[0] = C[1]  # BC Neumann homogênea
        C[-1] = C[-2]
        
    return x, C

if __name__ == "__main__":
    # Validação analítica vs numérica
    x = np.linspace(0, 50, 500)
    C_anal = analytical_gaussian(M=10, U=0.5, E=8, t=3600, x=x)
    
    x_num, C_num = solve_crank_nicolson(U=0.5, E=8, L=50, T=3600, Nx=100, Nt=1000)
    
    plt.figure(figsize=(8,4))
    plt.plot(x, C_anal, 'k--', label='Analítica (Gaussiana)')
    plt.plot(x_num, C_num, 'b-', label='Crank-Nicolson (Numérica)')
    plt.xlabel('Distância (m)'); plt.ylabel('Concentração')
    plt.legend(); plt.grid(); plt.tight_layout()
    plt.show()