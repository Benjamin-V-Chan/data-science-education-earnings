import pandas as pd
import matplotlib.pyplot as plt

# Load preprocessed dataset
df = pd.read_csv("../data/cleaned_labor_force_earnings.csv")

# Summary statistics
summary = df.describe()
summary.to_csv("../outputs/summary_statistics.csv")

# Plot trends over time
plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['overall_weekly_median_earnings_(ages_15_and_above)'], label='Median Weekly Earnings')
plt.xlabel("Year")
plt.ylabel("Earnings ($)")
plt.title("Median Weekly Earnings Over Time")
plt.legend()
plt.savefig("../outputs/earnings_trend.png")
plt.close()