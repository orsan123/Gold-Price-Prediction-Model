#join csv files



import pandas as pd

# Load the original and new datasets
df_old = pd.read_csv("only_gold.csv")
df_new = pd.read_csv("only_gold_1.csv")

# Convert 'Date' column to datetime format
df_old['Date'] = pd.to_datetime(df_old['Date'])
df_new['Date'] = pd.to_datetime(df_new['Date'])

# Concatenate the two DataFrames
df_combined = pd.concat([df_old, df_new])

# Drop duplicate rows if any (based on Date)
df_combined = df_combined.drop_duplicates(subset='Date', keep='last')

# Sort by Date in ascending order
df_combined = df_combined.sort_values(by='Date').reset_index(drop=True)

# (Optional) Save to a new CSV
df_combined.to_csv("only_gold_combined.csv", index=False)

print("Combined dataset shape:", df_combined.shape)
