import numpy as np

# Example list of values
values = [5,2,4,2,3]

# Population standard deviation
std_population = np.std(values)**2
print(f"Population Standard Deviation: {std_population:.4f}")

# Sample standard deviation
std_sample = np.std(values, ddof=1) **2  # Set ddof=1 for sample std dev
print(f"Sample Standard Deviation: {std_sample:.4f}")
