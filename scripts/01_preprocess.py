import pandas as pd

# Load dataset
df = pd.read_csv("../data/labor_force_earnings.csv")

# Rename columns for clarity
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Convert year to integer
df['year'] = df['year'].astype(int)

# Save cleaned dataset
df.to_csv("../data/cleaned_labor_force_earnings.csv", index=False)