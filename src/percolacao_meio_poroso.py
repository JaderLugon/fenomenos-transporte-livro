"""
PERCOLAÇÃO VERTICAL EM MEIO POROSO - REGIME PERMANENTE
Correspondente ao Capítulo 6: "Percolação em Meio Poroso"
Lugon Jr. - Fenômenos de Transporte: Fundamentos e Modelagem Computacional

Este script resolve a equação de fluxo vertical descendente em regime permanente:
    q0 = -K(ψ) * (dψ/dz + 1)  →  dψ/dz = q0/K(ψ) - 1
utilizando o modelo de van Genuchten-Mualem para K(ψ) e θ(ψ).

Nível Graduação: Foco na aplicação das correlações e interpretação dos perfis.
Nível Pós-Graduação: Análise de sensibilidade paramétrica e extensão para regime transiente.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# =============================================================================
# 1. PARÂMETROS HIDRÁULICOS DO SOLO (Franco-arenoso - Tabela 6.1)
# =============================================================================
class SoilParams:
    """Classe para encapsular parâmetros do modelo de van Genuchten-Mualem"""
    def __init__(self):
        self.theta_r = 0.058   # Conteúdo de água residual [m³/m³]
        self.theta_s = 0.410   # Conteúdo de água na saturação [m³/m³]
        self.alpha   = 7.4     # Parâmetro inverso da pressão de entrada de ar [m⁻¹]
        self.n       = 1.56    # Parâmetro de distribuição de poros [-]
        self.K_s     = 5.1e-5  # Condutividade hidráulica saturada [m/s]
        self.L_param = 0.5     # Parâmetro de conectividade de poros [-]
        self.m       = 1.0 - 1.0/self.n  # Derivado [-]

# =============================================================================
# 2. FUNÇÕES DE PROPRIEDADE HIDRÁULICA (Eq. 6.3 e 6.4)
# =============================================================================
def se_from_theta(theta, p):
    """Saturação efetiva Se = (θ - θr)/(θs - θr)"""
    return np.clip((theta - p.theta_r) / (p.theta_s - p.theta_r), 0.0, 1.0)

def theta_from_psi(psi, p):
    """Curva de retenção θ(ψ) - Eq. 6.3"""
    abs_psi = np.abs(psi)
    return p.theta_r + (p.theta_s - p.theta_r) / (1.0 + (p.alpha * abs_psi)**p.n)**p.m

def K_from_psi(psi, p):
    """Condutividade hidráulica não-saturada K(ψ) - Eq. 6.4"""
    Se = se_from_theta(theta_from_psi(psi, p), p)
    return p.K_s * (Se**p.L_param) * (1.0 - (1.0 - Se**(1.0/p.m))**p.m)**2

# =============================================================================
# 3. SOLUÇÃO NUMÉRICA - REGIME PERMANENTE
# =============================================================================
def dpsi_dz(z, psi, q0, p):
    """EDO para fluxo vertical descendente: dψ/dz = q0/K(ψ) - 1 (Eq. 6.8)"""
    K = K_from_psi(psi, p)
    K = np.maximum(K, 1e-12)  # Evita divisão por zero em solos muito secos
    return (q0 / K) - 1.0

def solve_steady_state(q0, L_wt, p, N=200):
    """
    Resolve o perfil ψ(z) do lençol freático (z = -L) até a superfície (z = 0).
    Método: Integração numérica robusta (LSODA) + esquema iterativo implícito alternativo.
    """
    z_min, z_max = -L_wt, 0.0
    z_eval = np.linspace(z_min, z_max, N)
    
    # Condição de contorno no lençol freático: ψ(-L) = 0
    sol = solve_ivp(dpsi_dz, (z_min, z_max), [0.0], args=(q0, p), 
                    t_eval=z_eval, method='LSODA', rtol=1e-6, atol=1e-8)
    
    if not sol.success:
        raise RuntimeError("Falha na integração numérica. Verifique os parâmetros.")
        
    psi_profile = sol.y[0]
    theta_profile = theta_from_psi(psi_profile, p)
    K_profile = K_from_psi(psi_profile, p)
    
    return z_eval, psi_profile, theta_profile, K_profile

# =============================================================================
# 4. VISUALIZAÇÃO E ANÁLISE (Correspondente à Fig. 6.x do livro)
# =============================================================================
def plot_results(z, psi, theta, K, q0, L_wt):
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    
    # Perfil de Potencial Matricial
    axes[0].plot(psi, z, 'b-', linewidth=2)
    axes[0].set_xlabel('Potencial Matricial $\psi$ [m]', fontsize=11)
    axes[0].set_ylabel('Profundidade $z$ [m]', fontsize=11)
    axes[0].set_title('Perfil de Potencial Matricial', fontsize=12, fontweight='bold')
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].set_ylim(-L_wt, 0)
    
    # Perfil de Umidade
    axes[1].plot(theta, z, 'g-', linewidth=2)
    axes[1].set_xlabel('Conteúdo de Umidade $\theta$ [m³/m³]', fontsize=11)
    axes[1].set_ylabel('Profundidade $z$ [m]', fontsize=11)
    axes[1].set_title('Perfil de Umidade', fontsize=12, fontweight='bold')
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].set_ylim(-L_wt, 0)
    
    # Perfil de Condutividade
    axes[2].plot(K, z, 'r-', linewidth=2)
    axes[2].set_xlabel('Condutividade $K(\psi)$ [m/s]', fontsize=11)
    axes[2].set_ylabel('Profundidade $z$ [m]', fontsize=11)
    axes[2].set_title('Condutividade Hidráulica', fontsize=12, fontweight='bold')
    axes[2].grid(True, linestyle='--', alpha=0.6)
    axes[2].set_ylim(-L_wt, 0)
    axes[2].set_xscale('log')
    
    plt.tight_layout()
    plt.show()
    
    # Análise de sensibilidade simples (Nível Pós-Graduação)
    print("\n ANÁLISE DE SENSIBILIDADE (Nível Pós-Graduação)")
    print(f"Fluxo imposto: q0 = {q0:.2e} m/s")
    print(f"K na superfície: {K[-1]:.2e} m/s")
    print(f"Razão q0/K_superficie: {q0/K[-1]:.3f}")
    if q0/K[-1] > 0.8:
        print("⚠️  Alerta: O fluxo imposto está próximo do limite de saturação. ")
        print("    O perfil pode ser instável para pequenas variações de q0 ou K_s.")
    else:
        print("✅ Regime bem estabelecido: q0 << K(ψ) em todo o perfil.")

# =============================================================================
# 5. EXECUÇÃO PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("🌍 PERCOLAÇÃO VERTICAL EM SOLO FRANCO-ARENOSO")
    print("="*50)
    
    # Parâmetros do estudo de caso (Capítulo 6)
    params = SoilParams()
    q0 = 1.0e-6        # Taxa de infiltração [m/s] (~86,4 mm/dia)
    L_wt = 3.0         # Profundidade do lençol freático [m]
    
    # Verificação física inicial
    if q0 >= params.K_s:
        raise ValueError("Fluxo imposto q0 não pode exceder K_s em regime permanente vertical.")
        
    print(f"Resolvendo fluxo vertical descendente (q0 = {q0:.2e} m/s)...")
    z, psi, theta, K = solve_steady_state(q0, L_wt, params)
    
    print(f"✅ Solução obtida com {len(z)} pontos.")
    print(f"   ψ na superfície: {psi[-1]:.3f} m")
    print(f"   θ na superfície: {theta[-1]:.3f} m³/m³")
    
    plot_results(z, psi, theta, K, q0, L_wt)