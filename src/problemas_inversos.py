"""
problemas_inversos.py — Estimação de parâmetros via problemas inversos.

Implementa:
- Levenberg-Marquardt (LM)
- Matriz de covariância e intervalos de confiança
- Sensibilidades por diferenças finitas
"""

import numpy as np
from .utils import validar_positivo

# ============================================================================
# LEVENBERG-MARQUARDT
# ============================================================================

def levenberg_marquardt(modelo, P0: np.ndarray, y_obs: np.ndarray,
                        x_data: np.ndarray = None,
                        max_iter: int = 100,
                        tol: float = 1e-8,
                        mu0: float = 1e-3,
                        delta_P: float = 0.01,
                        verbose: bool = False) -> dict:
    """
    Método de Levenberg-Marquardt para estimação de parâmetros.
    
    Parâmetros
    ----------
    modelo : callable
        Função que recebe (P, x_data) e retorna y_calc.
        Assinatura: y_calc = modelo(P, x_data)
    P0 : array
        Estimativa inicial dos parâmetros.
    y_obs : array
        Dados observados.
    x_data : array, opcional
        Variáveis independentes (passadas ao modelo).
    max_iter : int
        Número máximo de iterações.
    tol : float
        Tolerância para convergência (norma do gradiente).
    mu0 : float
        Parâmetro de amortecimento inicial.
    delta_P : float
        Perturbação relativa para cálculo de sensibilidades (1%).
    verbose : bool
        Se True, imprime histórico de iterações.
    
    Retorna
    -------
    dict
        {'P': parâmetros estimados,
         'iteracoes': número de iterações,
         'historico': lista de normas do resíduo,
         'cov': matriz de covariância,
         'sigma_P': desvios padrão dos parâmetros,
         'correlacao': matriz de correlação}
    """
    P = np.array(P0, dtype=float)
    mu = mu0
    historico = []
    
    for k in range(max_iter):
        # 1. Avaliar modelo e resíduo
        y_calc = modelo(P, x_data) if x_data is not None else modelo(P)
        r = y_obs - y_calc
        
        # 2. Calcular Jacobiana por diferenças finitas
        J = _jacobiana_finita(modelo, P, x_data, delta_P)
        
        # 3. Atualização LM
        JTJ = J.T @ J
        JTr = J.T @ r
        I = np.eye(len(P))
        
        # Tenta passo; se reduzir resíduo, aceita; senão, aumenta mu
        dP = np.linalg.solve(JTJ + mu * I, JTr)
        P_novo = P + dP
        
        y_novo = modelo(P_novo, x_data) if x_data is not None else modelo(P_novo)
        r_novo = y_obs - y_novo
        
        if np.sum(r_novo**2) < np.sum(r**2):
            P = P_novo
            mu = max(mu / 3, 1e-10)  # reduz amortecimento
        else:
            mu = min(mu * 5, 1e10)   # aumenta amortecimento
        
        norma_r = np.linalg.norm(r)
        historico.append(norma_r)
        
        if verbose:
            print(f"Iter {k+1:3d} | ||r|| = {norma_r:.6e} | P = {P}")
        
        if np.linalg.norm(dP) < tol:
            break
    
    # Matriz de covariância (aproximação)
    J_final = _jacobiana_finita(modelo, P, x_data, delta_P)
    JTJ_final = J_final.T @ J_final
    sigma2 = np.sum(r**2) / max(1, len(y_obs) - len(P))
    cov = sigma2 * np.linalg.inv(JTJ_final)
    sigma_P = np.sqrt(np.diag(cov))
    
    # Matriz de correlação
    D = np.diag(1.0 / sigma_P)
    correlacao = D @ cov @ D
    
    return {
        "P": P,
        "iteracoes": k + 1,
        "historico": historico,
        "cov": cov,
        "sigma_P": sigma_P,
        "correlacao": correlacao
    }


def _jacobiana_finita(modelo, P, x_data, delta_P):
    """Calcula a Jacobiana por diferenças finitas centrais."""
    n_params = len(P)
    y0 = modelo(P, x_data) if x_data is not None else modelo(P)
    n_obs = len(y0)
    J = np.zeros((n_obs, n_params))
    
    for j in range(n_params):
        dP = np.zeros(n_params)
        dP[j] = max(abs(P[j]) * delta_P, 1e-12)
        y_plus = modelo(P + dP, x_data) if x_data is not None else modelo(P + dP)
        y_minus = modelo(P - dP, x_data) if x_data is not None else modelo(P - dP)
        J[:, j] = (y_plus - y_minus) / (2 * dP[j])
    
    return J


# ============================================================================
# ANÁLISE DE INCERTEZA
# ============================================================================

def intervalo_confianca(P_est: np.ndarray, sigma_P: np.ndarray,
                        nivel: float = 0.95) -> tuple:
    """
    Calcula intervalo de confiança para os parâmetros estimados.
    
    Assume distribuição normal.
    
    Retorna
    -------
    tuple
        (P_inferior, P_superior)
    """
    from scipy.stats import norm
    z = norm.ppf((1 + nivel) / 2)
    return P_est - z * sigma_P, P_est + z * sigma_P


def analisar_identificabilidade(cov: np.ndarray,
                                 nomes: list = None) -> dict:
    """
    Analisa a identificabilidade dos parâmetros a partir da
    matriz de covariância.
    
    Retorna
    -------
    dict
        {'sigma_P': desvios padrão,
         'cv': coeficientes de variação (%),
         'correlacao': matriz de correlação,
         'pares_correlacionados': lista de pares com |ρ| > 0.7}
    """
    sigma_P = np.sqrt(np.diag(cov))
    D = np.diag(1.0 / sigma_P)
    correlacao = D @ cov @ D
    
    # Identifica pares altamente correlacionados
    pares = []
    n = len(sigma_P)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(correlacao[i, j]) > 0.7:
                nome_i = nomes[i] if nomes else f"P{i}"
                nome_j = nomes[j] if nomes else f"P{j}"
                pares.append((nome_i, nome_j, correlacao[i, j]))
    
    return {
        "sigma_P": sigma_P,
        "correlacao": correlacao,
        "pares_correlacionados": pares
    }