# R function tranlations
# pbinom -> st.binom.cdf - cumulative distribution function
# dbinom -> st.binom.pmf - probability mass function
# qbinom -> st.binom.ppf - percent point function
# rbinom -> st.binom.rvs - random variates
# The same applies for different distributions (eg. ppoisson -> st.poisson.cdf)

#Close pop-up window to proceed to the next exercise

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Exercise 1
print("Exercise 1")

n = 10
p = 0.7

print(f"P(X ≤ 3) = {st.binom.cdf(3, n, p)}")
print(f"P(X < 3) = {st.binom.cdf(2, n, p)}")
print(f"P(X > 4) = {1 - st.binom.cdf(4, n, p)}")
print(f"P(X = 7) = {st.binom.pmf(7, n, p)}")
print(f"Median: {st.binom.ppf(0.5, n, p)}")
print()

# visualization
df = pd.DataFrame()
df["k"] = np.arange(0, n + 1)
df["prob_density"] = st.binom.pmf(df["k"], n, p)

plt.stem(df["k"], df["prob_density"])
plt.xlabel("k")
plt.ylabel("P(X = k)")
plt.title(f"Ex1 Binomial Distribution (n={n}, p={p})")
plt.show()

# Exercise 2
print("\nExercise 2:")

la = 1.6  # lambda

print(f"a) {1 - st.poisson.cdf(5, la)}")
print(f"b) {st.poisson.cdf(8, la*5)}")

# visualization
df = pd.DataFrame()
df["lambda"] = np.arange(0, 11)
df["prob_density"] = st.poisson.pmf(df["lambda"], la)

plt.stem(df["lambda"], df["prob_density"])
plt.xlabel("k")
plt.ylabel("P(X = k)")
plt.title(f"Poisson (la={la})")
plt.show()

# Exercise 3
print("\nExercise 3:")

print(f"Probability is: {st.binom.pmf(2, 6, 0.05)}")

# visualization:
df = pd.DataFrame()
df["k"] = np.arange(0, 7)
df["prob_density"] = st.binom.pmf(df["k"], 6, 0.05)

plt.stem(df["k"], df["prob_density"])
plt.xlabel("k")
plt.ylabel("P(X = k)")
plt.title(f"Binomial Distribution (n={6}, p={0.05})")
plt.show()


# Exercise 4
print("\nExercise 4:")

# a) Probability of compliance with standards
mu = 26.4
sigma = 2.34
x = 29
z = (x - mu) / sigma

print(f"Probability of compliance with standards: {st.norm.cdf(z)}")

# b) Probability of breaking distance between 26 and 24
x1 = 26
x2 = 24
z1 = (x1 - mu) / sigma
z2 = (x2 - mu) / sigma

print(f"Probability of breaking distance between 26 and 24: {st.norm.cdf(z1) - st.norm.cdf(z2)}")

# visualization:

df = pd.DataFrame()
df["x"] = np.linspace(20, 40, 100)
df["prob_density"] = st.norm.pdf(df["x"], mu, sigma)

plt.plot(df["x"],df["prob_density"])
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title(f'Normal Distribution (mu={mu}, sigma={sigma})')

#shade area under curve
plt.fill_between(df["x"], df["prob_density"], where = (df["x"] < x), color = "green")
plt.fill_between(df["x"], df["prob_density"], where = (df["x"] > x2) & (df["x"] < x1), color = "red")
plt.show()
