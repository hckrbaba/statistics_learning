import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create the x-axis for Z-scores
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Create the figure and plot
plt.figure(figsize=(12, 6))

# Plot the normal distribution curve
plt.plot(x, y, label="Normal Distribution")

# Shade for one-tailed test (95% confidence)
x_one_tailed = np.linspace(1.645, 4, 100)
y_one_tailed = norm.pdf(x_one_tailed, 0, 1)
plt.fill_between(x_one_tailed, y_one_tailed, color="blue", alpha=0.3, label="One-Tailed (95%)")

# Shade for two-tailed test (95% confidence)
x_two_tailed_left = np.linspace(-4, -1.96, 100)
y_two_tailed_left = norm.pdf(x_two_tailed_left, 0, 1)
x_two_tailed_right = np.linspace(1.96, 4, 100)
y_two_tailed_right = norm.pdf(x_two_tailed_right, 0, 1)
plt.fill_between(x_two_tailed_left, y_two_tailed_left, color="green", alpha=0.3, label="Two-Tailed Left (95%)")
plt.fill_between(x_two_tailed_right, y_two_tailed_right, color="green", alpha=0.3, label="Two-Tailed Right (95%)")

# Add annotations
plt.axvline(1.645, color="blue", linestyle="--", label="Z = 1.645 (One-Tailed)")
plt.axvline(-1.96, color="green", linestyle="--", label="Z = -1.96 (Two-Tailed)")
plt.axvline(1.96, color="green", linestyle="--", label="Z = 1.96 (Two-Tailed)")

# Customize the plot
plt.title("Z-Values for One-Tailed and Two-Tailed Tests")
plt.xlabel("Z-Score")
plt.ylabel("Density")
plt.legend(loc="upper left")
plt.grid(alpha=0.3)
plt.show()
