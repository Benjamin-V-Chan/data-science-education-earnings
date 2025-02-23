import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load preprocessed dataset
df = pd.read_csv("../data/cleaned_labor_force_earnings.csv")

# Fit ARIMA model for earnings prediction
model = ARIMA(df['overall_weekly_median_earnings_(ages_15_and_above)'], order=(1,1,1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=10)

# Save predictions
forecast.to_csv("../outputs/earnings_forecast.csv")

# Plot forecast
plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['overall_weekly_median_earnings_(ages_15_and_above)'], label='Historical')
plt.plot(range(df['year'].max()+1, df['year'].max()+11), forecast, label='Forecast', linestyle='dashed')
plt.xlabel("Year")
plt.ylabel("Earnings ($)")
plt.title("Earnings Forecast")
plt.legend()
plt.savefig("../outputs/earnings_forecast.png")
plt.close()
