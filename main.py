
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create synthetic observed data
time = np.arange(0, 24)
obs_flow = 3 + np.sin(time/3) + np.random.normal(0, 0.2, len(time))

# Step 2: Simple MCMC to adjust parameter (mock)
param = 2.5
best_param = param
best_error = float("inf")
for i in range(1000):
    test_param = param + np.random.normal(0, 0.1)
    sim_flow = test_param + np.sin(time/3) + np.random.normal(0, 0.3, len(time))
    error = np.sum((obs_flow - sim_flow)**2)
    if error < best_error:
        best_param, best_error = test_param, error

print(f"Best parameter found: {best_param:.2f}")

# Step 3: Plot results
best_sim_flow = best_param + np.sin(time/3)
plt.plot(time, obs_flow, label="Observed")
plt.plot(time, best_sim_flow, label="Simulated", linestyle="--")
plt.xlabel("Time (h)")
plt.ylabel("Flow (m³/s)")
plt.title("Observed vs Simulated Hydrograph")
plt.legend()
plt.tight_layout()
plt.savefig("calibration.png")
print("Calibration plot saved to calibration.png")
