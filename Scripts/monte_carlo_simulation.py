import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\BlueStock_Project\Data\Processed\02_nav_history_cleaned.csv")

returns = df['nav'].pct_change().dropna()

mean = returns.mean()
std = returns.std()

days = 252 * 5   # 5 years
simulations = 100

last_nav = df['nav'].iloc[-1]

results = []

for _ in range(simulations):
    prices = [last_nav]
    for _ in range(days):
        shock = np.random.normal(mean, std)
        price = prices[-1] * (1 + shock)
        prices.append(price)
    results.append(prices)

results = np.array(results)

# Plot
plt.plot(results.T, alpha=0.1)
plt.title("Monte Carlo Simulation (5 Years)")
plt.show()