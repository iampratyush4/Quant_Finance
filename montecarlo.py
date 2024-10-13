# Monte carlo simulation 
import numpy as np
import matplotlib.pyplot as plt

# Parameters 
S0 = 100         # Initial stock price
mu = 0.05        # Expected return (annualized)
sigma = 0.2      # Volatility (annualized)
T = 1            # Time in years
N = 252          # Number of time steps (days)
simulations = 10000  # Number of simulations

# Time step size
dt = T / N

# Simulating stock price
S = np.zeros((N + 1, simulations))
S[0] = S0  # Initial stock price

# Generate random numbers from a normal distribution for each simulation
Z = np.random.normal(0, 1, (N, simulations))

# Simulate the stock price paths
for t in range(1, N + 1):
    S[t] = S[t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[t - 1])

# Plot a few of the simulation paths
plt.figure(figsize=(10, 6))
plt.plot(S[:, :10])  # Plot only 10 simulation paths for clarity
plt.title('Monte Carlo Simulation of Stock Prices')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()

# Final stock prices at time T
final_prices = S[-1]

# Calculate the mean and 5% quantile for Value-at-Risk (VaR)
mean_price = np.mean(final_prices)
VaR_5_percent = np.percentile(final_prices, 5)

print(f"Mean final price: {mean_price:.2f}")
print(f"5% Value-at-Risk: {VaR_5_percent:.2f}")
