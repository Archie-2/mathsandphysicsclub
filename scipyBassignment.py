import numpy as np
from scipy.integrate import quad

# Function to integrate
def integrand(t):
    x = np.sqrt(3) * np.cos(t)
    y = np.sqrt(3) * np.sin(t)
    f = x**2 + y**4
    ds = np.sqrt(3)
    return f * ds

# Integrate over [0, 2*pi]
result, _ = quad(integrand, 0, 2 * np.pi)

# Output the result
print("The value of the line integral is:", result)
