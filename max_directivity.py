import numpy as np
import matplotlib.pyplot as plt

def pattern_function(L, theta):
    beta = np.pi * L
    numerator = np.cos(beta * np.cos(theta)) - np.cos(beta)
    denominator = np.sin(theta)
    F = np.where(np.abs(denominator) < 1e-6, 0, numerator / denominator)
    return F

def compute_max_directivity(L):
    theta = np.linspace(1e-6, np.pi - 1e-6, 1000)
    F = pattern_function(L, theta)
    U = np.abs(F) ** 2
    dtheta = theta[1] - theta[0]
    integral = np.sum(U * np.sin(theta)) * dtheta
    D = 2 * np.max(U) / integral
    return 10 * np.log10(D)

lengths = np.linspace(0.1, 2.5, 100)
directivities = [compute_max_directivity(L) for L in lengths]

plt.figure(figsize=(10, 5))
plt.plot(lengths, directivities, color='green')
plt.xlabel('Dipole Length (λ)')
plt.ylabel('Max Directivity (dBi)')
plt.title('Maximum Directivity of Dipole Antenna vs Length')
plt.grid(True)
plt.show()