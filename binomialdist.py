from scipy.stats import binom

# Parameters
n = 30   # Number of trials
k = 20   # Number of successes
p = 0.5  # Probability of success in each trial

# Calculate the probability
prob = binom.pmf(k, n, p)  # pmf = Probability Mass Function
print(f"P(X = {k}) = {prob:.4f}")
