import numpy as np
import matplotlib.pyplot as plt
import sdeint

# Parameters
r_B = 0.05  # Growth rate of biomass
K_B = 1000  # Carrying capacity for biomass
alpha = 0.1  # Grazing intensity factor
k = 0.6  # Grazing reduction factor due to parasites
sigma_B = 0.05  # Noise in biomass dynamics
H = 100  # Host density (constant)
P_vals = [0, 0.1, 0.3]  # Parasite prevalence levels

# Drift function for biomass dynamics
def drift(P_current):
    def drift_inner(B, t):
        G = alpha * H * (1 - k * P_current)
        dB = r_B * B * (1 - B / K_B) - G
        return np.array([dB])  # Ensure drift returns a numpy array 
    return drift_inner

# Diffusion function for stochastic effects, accepts P_current (but doesn't use it here)
def diffusion(P_current):
    def diffusion_inner(B, t):
        return np.array([[sigma_B]])  # Ensure diffusion is returned as a numpy array
    return diffusion_inner

# Initial condition and time points
B0 = [500]  # Initial biomass
t = np.linspace(0, 100, 1000)  # Simulation time points

# Simulate for different parasite prevalence levels
plt.figure(figsize=(10, 6))
for P_current in P_vals:
    # Get the drift and diffusion functions with the current P
    drift_func = drift(P_current)
    diffusion_func = diffusion(P_current)
    
    # Simulate using sdeint with the updated drift and diffusion functions
    result = sdeint.itoint(drift_func, diffusion_func, B0, t)
    plt.plot(t, result, label=f"Parasite Prevalence: P = {P_current}")

# Plot results
plt.xlabel("Time")
plt.ylabel("Biomass")
plt.title("Effect of Parasite Prevalence on Biomass Dynamics under Drought")
plt.legend()
plt.grid()
plt.show()
