import numpy as np
import matplotlib.pyplot as plt

# Mock rainfall and runoff data
rain = np.arange(10)
flow = rain * 0.5 + np.random.normal(0, 0.1, 10)

# "Bayesian" parameter estimation (mock sampling)
param_samples = np.random.normal(0.5, 0.05, 1000)

# Plot results
plt.hist(param_samples, bins=30)
plt.title("Mock Posterior Distribution")
plt.xlabel("Parameter Value")
plt.ylabel("Frequency")
plt.show()
