import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def py_bivariate_normal_pdf(domain, mean, variance):
    # Create the grid of points (X, Y)
    X = [[-mean + x * variance for x in range(int((-domain + mean) // variance), 
                                               int((domain + mean) // variance) + 1)] 
         for _ in range(int((-domain + mean) // variance), 
                        int((domain + mean) // variance) + 1)]
    Y = [*map(list, zip(*X))]  # Transpose X to get Y values
    R = [[math.sqrt(a**2 + b**2) for a, b in zip(c, d)] for c, d in zip(X, Y)]  # Radial distance
    Z = [[(1. / math.sqrt(2 * math.pi)) * math.exp(-0.5 * r**2) for r in r_sub] for r_sub in R]  # Gaussian function values
    X = [*map(lambda a: [b + mean for b in a], X)]  # Shift X by mean
    Y = [*map(lambda a: [b + mean for b in a], Y)]  # Shift Y by mean
    return np.array(X), np.array(Y), np.array(Z)

# Generate the X, Y, Z values
X, Y, Z = py_bivariate_normal_pdf(6, 4, 0.25)

# Create the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Add a color bar to the plot
fig.colorbar(surf)

# Set plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Density')
ax.set_title('3D Bivariate Gaussian Distribution')

# Show the plot
plt.show()