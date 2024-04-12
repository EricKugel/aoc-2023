import numpy as np
x = [6, 10, 50, 100, 500, 1000, 5000]
y = [16, 50, 1594, 6536, 167004, 668697, 16733044]

coefficients = np.polyfit(x, y, 2)

print(coefficients)