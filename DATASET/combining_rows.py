#join csv files in rows 

import pandas as pd

# Load the original and new datasets
df1 = pd.read_csv(r"C:\Users\pc\OneDrive\Desktop\Final year project\prophet_gold_price\usdx_11.csv")
df2 = pd.read_csv(r"C:\Users\pc\OneDrive\Desktop\Final year project\prophet_gold_price\usdx_3.csv")

# Convert 'Date' column to datetime format
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

# Concatenate the two DataFrames
df_combined = pd.concat([df1, df2])

# Drop duplicate rows if any (based on Date)
df_combined = df_combined.drop_duplicates(subset='Date', keep='last')

# Sort by Date in ascending order
df_combined = df_combined.sort_values(by='Date').reset_index(drop=True)

# (Optional) Save to a new CSV
df_combined.to_csv("usdx_final.csv", index=False)

print("Combined dataset shape:", df_combined.shape)
