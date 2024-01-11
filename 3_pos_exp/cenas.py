import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Parameters
a = -5         # Skewness parameter (a > 0 means right skew, a < 0 means left skew)
loc = 0       # Mean
scale = 1     # Standard Deviation

# Create a skewed normal distribution
dist = skewnorm(a, loc, scale)
dist2 = skewnorm(-10, loc, scale)
dist3 = skewnorm(-20, loc, scale)
dist4 = skewnorm(-100, loc, scale)

# Plot the PDF
x = np.linspace(-5, 1, 100)
y = dist.pdf(x)
plt.plot(x, y, 'k', linewidth=2, label="Skew={}".format(a), color='b')
plt.plot(x, dist2.pdf(x), 'r', linewidth=2, label="Skew={}".format(-10), color='r')
plt.plot(x, dist3.pdf(x), 'g', linewidth=2, label="Skew={}".format(-20), color='g')
plt.plot(x, dist4.pdf(x), 'y', linewidth=2, label="Skew={}".format(-100), color='orange')
plt.legend()
plt.show()
