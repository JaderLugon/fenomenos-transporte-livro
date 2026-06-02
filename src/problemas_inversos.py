"""
Módulo: Problemas Inversos e Calibração
Referência: Apêndice / Cap. 6 (Vol II)
"""
import numpy as np
from scipy.optimize import least_squares

def levenberg_marquardt(residual_func, p0, args=(), bounds=(-np.inf, np.inf), max_nfev=500):
    result = least_squares(residual_func, p0, args=args, bounds=bounds,
                          method='trf', xtol=1e-8, ftol=1e-8, max_nfev=max_nfev)
    J = result.jac
    n_params = len(result.x)
    n_obs = len(result.fun)
    sigma2 = np.sum(result.fun**2) / max(n_obs - n_params, 1)
    cov = sigma2 * np.linalg.inv(J.T @ J + 1e-10*np.eye(n_params))
    std = np.sqrt(np.diag(cov))
    corr = cov[0,1] / np.sqrt(cov[0,0]*cov[1,1]) if n_params >= 2 else 0.0
    return result.x, std, corr, result.cost*2, result.success

def sensitivity_fd(model_func, p, x_obs, delta=1e-5):
    """Jacobian por diferenças finitas."""
    n_p = len(p)
    n_obs = len(x_obs)
    J = np.zeros((n_obs, n_p))
    for j in range(n_p):
        p_plus = p.copy()
        p_plus[j] += delta
        J[:, j] = (model_func(p_plus, x_obs) - model_func(p, x_obs)) / delta
    return J

if __name__ == "__main__":
    def dummy_residual(p, x):
        return p[0]*x + p[1] - (2.5*x + 1.0 + 0.1*np.random.randn(len(x)))
    
    p_est, std, corr, cost, ok = levenberg_marquardt(dummy_residual, [1.0, 0.0], args=(np.linspace(0,10,20),))
    print("p:", p_est, "±", std)
    print("ρ:", corr, "| Custo:", cost, "| OK:", ok)