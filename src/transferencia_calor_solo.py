"""
CAPÍTULO 8: TRANSFERÊNCIA DE CALOR EM SOLOS
Programa didático de simulação 1D implícita para perfil térmico diurno.
Baseado nas Seções 8.1 a 8.8 do livro "Fenômenos de Transporte: Vol II"

Autor: Jader Lugon Junior
Licença: MIT / CC-BY-NC-SA 4.0
Repositório: https://github.com/JaderLugon/fenomenos-transporte-livro
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. PARÂMETROS DO MODELO (Seção 8.8.1 - Descrição do Problema)
# =============================================================================
H = 1.0              # Profundidade da coluna de solo [m]
N = 21               # Número de nós espaciais
dz = H / (N - 1)     # Espaçamento vertical [m]
T_sim = 24 * 3600    # Tempo total de simulação: 24 h [s]
dt = 300             # Passo de tempo: 5 min [s]
steps = int(T_sim / dt)

# Propriedades térmicas do solo franco-arenoso
rho_b = 1500.0       # Densidade aparente [kg/m³]
cp = 800.0           # Calor específico [J/(kg·K)]
k_dry = 0.3          # Condutividade térmica seca [W/(m·K)]
k_sat = 1.8          # Condutividade térmica saturada [W/(m·K)]
kappa = 1.5          # Parâmetro do modelo Côté & Konrad (2005)

# Conteúdo de umidade (acoplamento one-way, Seção 8.5)
theta_r = 0.058      # Umidade residual [m³/m³]
theta_s = 0.41       # Umidade na saturação [m³/m³]
theta = np.full(N, 0.25)  # Umidade prescrita constante (perfil médio) [m³/m³]

# Condições de contorno e atmosfera
T_bottom = 15.0 + 273.15  # Temperatura na base (Dirichlet) [K]
h_conv = 15.0             # Coeficiente convectivo [W/(m²·K)]
alpha_s = 0.85            # Absortividade solar
epsilon_s = 0.95          # Emissividade térmica
sigma = 5.67e-8           # Constante de Stefan-Boltzmann [W/(m²·K⁴)]
Lv = 2.45e6               # Calor latente de vaporização [J/kg]
E_rate = 0.0              # Taxa de evaporação [kg/(m²·s)] (desprezada no caso)

# =============================================================================
# 2. FUNÇÕES AUXILIARES
# =============================================================================

def calc_k_thermal(theta_local):
    """
    Modelo de condutividade térmica Côté & Konrad (2005)
    Ref: Seção 8.4.2 e Tabela 8.1
    """
    Se = (theta_local - theta_r) / (theta_s - theta_r)
    Se = np.clip(Se, 0.0, 1.0)
    Ke = (kappa * Se) / (1.0 + (kappa - 1.0) * Se)
    return k_dry + (k_sat - k_dry) * Ke

def calc_surface_flux(T_surf, t):
    """
    Balanço energético superficial (Eq. 8.3)
    Retorna o fluxo líquido ENTRANDO no solo [W/m²]
    """
    # Radiação solar incidente
    if 6*3600 <= t <= 18*3600:
        R_s = 800.0 * np.sin(np.pi * (t - 6*3600) / (12*3600))
    else:
        R_s = 0.0
        
    # Temperatura do ar
    T_air = 25.0 + 10.0 * np.sin(np.pi * (t - 6*3600) / (12*3600)) + 273.15
    
    # Fluxos (positivos para cima/fora do solo)
    q_rad_in = alpha_s * R_s
    q_rad_out = epsilon_s * sigma * (T_surf**4 - (T_air - 10)**4)  # Céu noturno ~ T_ar-10
    q_conv = h_conv * (T_surf - T_air)
    q_evap = Lv * E_rate
    
    # Fluxo líquido que entra no solo (Seção 8.6)
    return q_rad_in - q_rad_out - q_conv - q_evap

def tdma_solve(a, b, c, d):
    """
    Algoritmo TDMA (Thomas) para sistemas tridiagonais
    Usado para resolver a Eq. (8.4) de forma implícita
    """
    n = len(d)
    c_prime = np.zeros(n)
    d_prime = np.zeros(n)
    
    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]
    
    for i in range(1, n-1):
        denom = b[i] - a[i] * c_prime[i-1]
        c_prime[i] = c[i] / denom
        d_prime[i] = (d[i] - a[i] * d_prime[i-1]) / denom
        
    d_prime[-1] = (d[-1] - a[-1] * d_prime[-2]) / (b[-1] - a[-1] * c_prime[-2])
    
    x = np.zeros(n)
    x[-1] = d_prime[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]
    return x

# =============================================================================
# 3. DISCRETIZAÇÃO E CONDIÇÕES INICIAIS
# =============================================================================
z = np.linspace(0, H, N)
# Perfil inicial linear entre superfície (25°C) e base (15°C)
T = np.linspace(25.0 + 273.15, T_bottom, N)

# Pré-calcular condutividades nas interfaces
k_interface = np.zeros(N-1)
for i in range(N-1):
    k_interface[i] = (calc_k_thermal(theta[i]) + calc_k_thermal(theta[i+1])) / 2.0

# Fator de estabilidade implícito (incondicionalmente estável, Seção 8.7)
C_factor = dt / (rho_b * cp * dz**2)

# Armazenamento de resultados para análise
T_history = np.zeros((steps, N))
T_history[0, :] = T

# =============================================================================
# 4. LOOP TEMPORAL (Resolução Implícita da Eq. 8.4)
# =============================================================================
print("Iniciando simulação térmica 1D...")
for n in range(1, steps):
    t = n * dt
    
    # --- Condição de Contorno Superior (Robin/Neumann não-linear) ---
    # Linearização do termo radiativo usando temperatura do passo anterior
    q_surf = calc_surface_flux(T[0], t)
    
    # Matriz tridiagonal (a: inferior, b: diagonal, c: superior, d: RHS)
    a = np.zeros(N)
    b = np.ones(N)
    c = np.zeros(N)
    d = np.copy(T)
    
    # Nó 0 (Superfície): Balanço de energia + difusão
    # Eq: (1 + C*k1/2)T0 - C*k1/2 T1 = T0^n + (dt*q_surf)/(rho*cp*dz)
    b[0] = 1.0 + C_factor * k_interface[0]
    c[0] = -C_factor * k_interface[0]
    d[0] = T[0] + (dt * q_surf) / (rho_b * cp * dz)
    
    # Nós internos 1 a N-2
    for i in range(1, N-1):
        a[i] = -C_factor * k_interface[i-1]
        b[i] = 1.0 + C_factor * (k_interface[i-1] + k_interface[i])
        c[i] = -C_factor * k_interface[i]
        d[i] = T[i]  # Sem fonte volumétrica interna
        
    # Nó N-1 (Base): Dirichlet T = T_bottom
    a[-1] = 0.0
    b[-1] = 1.0
    c[-1] = 0.0
    d[-1] = T_bottom
    
    # Resolver sistema linear
    T = tdma_solve(a, b, c, d)
    T_history[n, :] = T

print("Simulação concluída.")

# =============================================================================
# 5. VISUALIZAÇÃO E ANÁLISE (Seção 8.8.2 - Resultados)
# =============================================================================
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 5.1 Evolução da temperatura superficial e a 30 cm
t_hours = np.linspace(0, 24, steps)
axes[0, 0].plot(t_hours, T_history[:, 0] - 273.15, 'r-', linewidth=2, label='Superfície (z=0)')
axes[0, 0].plot(t_hours, T_history[:, 6] - 273.15, 'b--', linewidth=2, label='z=0.30 m')
axes[0, 0].set_xlabel('Tempo [h]')
axes[0, 0].set_ylabel('Temperatura [°C]')
axes[0, 0].set_title('Evolução Temporal da Temperatura')
axes[0, 0].legend()
axes[0, 0].set_xlim(0, 24)

# 5.2 Perfil térmico em horários-chave
times_plot = [6*3600, 12*3600, 18*3600, 24*3600]  # 6h, 12h, 18h, 24h
labels = ['06:00', '12:00 (Pico)', '18:00', '24:00']
colors = ['gray', 'orange', 'purple', 'black']
for i, (t_idx, lbl, col) in enumerate(zip(times_plot, labels, colors)):
    idx = int(t_idx / dt)
    axes[0, 1].plot(T_history[idx, :] - 273.15, z, color=col, linewidth=2, label=lbl)
axes[0, 1].set_xlabel('Temperatura [°C]')
axes[0, 1].set_ylabel('Profundidade [m]')
axes[0, 1].set_title('Perfis Verticais em Diferentes Horários')
axes[0, 1].legend()
axes[0, 1].invert_yaxis()

# 5.3 Mapa de contorno espaço-temporal
T_C = T_history - 273.15
T_min, T_max = np.min(T_C), np.max(T_C)
contour = axes[1, 0].imshow(T_C, aspect='auto', origin='lower', 
                            extent=[0, 24, H, 0], cmap='coolwarm', 
                            vmin=T_min, vmax=T_max)
axes[1, 0].set_xlabel('Tempo [h]')
axes[1, 0].set_ylabel('Profundidade [m]')
axes[1, 0].set_title('Mapa de Temperatura (°C)')
fig.colorbar(contour, ax=axes[1, 0], label='Temperatura [°C]')

# 5.4 Amortecimento e Atraso de Fase
surf_amp = (np.max(T_history[:, 0]) - np.min(T_history[:, 0])) / 2.0
depth_amp = []
depth_lag = []
for i in range(N):
    amp = (np.max(T_history[:, i]) - np.min(T_history[:, i])) / 2.0
    depth_amp.append(amp)
    # Atraso: índice do pico menos índice do pico superficial
    peak_surf = np.argmax(T_history[:, 0])
    peak_i = np.argmax(T_history[:, i])
    lag_h = (peak_i - peak_surf) * dt / 3600
    depth_lag.append(lag_h if lag_h >= 0 else 0)

axes[1, 1].plot(depth_amp, z, 'r-', linewidth=2, label='Amplitude')
ax2 = axes[1, 1].twinx()
ax2.plot(depth_lag, z, 'b--', linewidth=2, label='Atraso de Fase [h]')
axes[1, 1].set_xlabel('Amplitude [°C]')
axes[1, 1].set_ylabel('Profundidade [m]')
ax2.set_ylabel('Atraso [h]')
axes[1, 1].invert_yaxis()
axes[1, 1].legend(loc='upper left')
ax2.legend(loc='upper right')
axes[1, 1].set_title('Amortecimento e Atraso com a Profundidade')

plt.tight_layout()
plt.show()

# =============================================================================
# 6. ANÁLISE QUANTITATIVA (Exercícios Seção 8.8.2)
# =============================================================================
print("\n--- ANÁLISE QUANTITATIVA ---")
alpha_mean = np.mean(calc_k_thermal(theta)) / (rho_b * cp)
omega = 2 * np.pi / (24*3600)
d_analytical = np.sqrt(2 * alpha_mean / omega)
print(f"Difusividade térmica média (α): {alpha_mean:.2e} m²/s")
print(f"Profundidade de penetração teórica (d ≈ √(2α/ω)): {d_analytical:.2f} m")
print(f"Atraso de fase a 0.10 m: {depth_lag[2]:.2f} h (Teórico esperado: ~2-3 h)")
print(f"Amplitude superficial: {surf_amp:.2f} °C")
print(f"Amplitude a 0.30 m: {depth_amp[6]:.2f} °C (amortecimento de ~{surf_amp/depth_amp[6]:.1f}x)")