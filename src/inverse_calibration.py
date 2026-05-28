"""
inverse_calibration.py
Estimativa de parâmetros por mínimos quadrados não-lineares (Levenberg-Marquardt).
Calcula matriz de covariância, erros padrão e correlação.
Ref: Vol II, Apêndice
"""
import numpy as np
from scipy.optimize import least_squares

def model_linear(x, a, b): return a*x + b

def residuals(params, x, y):
    a, b = params
    return model_linear(x, a, b) - y

def calibrate(x, y, p0, bounds=(-np.inf, np.inf)):
    result = least_squares(residuals, p0, args=(x, y), bounds=bounds)
    J = result.jac
    cov = np.linalg.inv(J.T @ J) * np.sum(result.fun**2) / (len(y) - len(p0))
    std = np.sqrt(np.diag(cov))
    corr = cov[0,1]/np.sqrt(cov[0,0]*cov[1,1])
    return result.x, std, corr

if __name__ == "__main__":
    # Dados sintéticos: y = 2.5x + 1.0 + ruído
    x = np.linspace(0, 10, 20)
    y_true = 2.5*x + 1.0
    y_meas = y_true + np.random.normal(0, 0.5, size=x.shape)
    
    p_est, std, corr = calibrate(x, y_meas, p0=[1.0, 0.5])
    print(f"a = {p_est[0]:.3f} ± {std[0]:.3f}")
    print(f"b = {p_est[1]:.3f} ± {std[1]:.3f}")
    print(f"Correlação: ρ = {corr:.3f}")