import numpy as np
from scipy.stats import skew, kurtosis

# Sample data (list of returns)
returns = [0.02, 0.03, -0.01, 0.05, 0.07, -0.04, 0.01, 0.03, 0.06, -0.02]

# 1. Mean
mean = np.mean(returns)

# 2. Variance
variance = np.var(returns)

# 3. Skewness
skewness = skew(returns)

# 4. Kurtosis
kurt = kurtosis(returns)

# Display the results
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurt}")
