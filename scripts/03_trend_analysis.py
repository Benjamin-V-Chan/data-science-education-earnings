import pandas as pd
import matplotlib.pyplot as plt

# Load preprocessed dataset
df = pd.read_csv("../data/cleaned_labor_force_earnings.csv")

# Compute moving averages
df['earnings_ma'] = df['overall_weekly_median_earnings_(ages_15_and_above)'].rolling(window=5).mean()

# Plot moving averages
plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['earnings_ma'], label='5-Year Moving Avg (Earnings)', color='red')
plt.xlabel("Year")
plt.ylabel("Earnings ($)")
plt.title("5-Year Moving Average of Earnings")
plt.legend()
plt.savefig("../outputs/earnings_moving_avg.png")
plt.close()