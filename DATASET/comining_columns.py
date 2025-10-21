#TO JOIN COLUMNS FROM TWO CSV FILES
# This script merges two CSV files based on a common column 'Date'.
import pandas as pd

# File paths
gold = r"C:\Users\pc\OneDrive\Desktop\Final year project\prophet_gold_price\GOLD.csv"
usdx = r"C:\Users\pc\OneDrive\Desktop\Final year project\prophet_gold_price\usdx_final.csv"

# Load the CSV files into pandas DataFrames
df1 = pd.read_csv(gold)
df2 = pd.read_csv(usdx)


# Strip spaces from column names (to avoid issues)
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Ensure 'Date' column is in datetime format in both DataFrames for accurate merging
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])


# Merge the two DataFrames on the 'Date' column
merged_df = pd.merge(df1, df2, on='Date', how='inner')

# Specify where you want to save the merged DataFrame
merged_file = r"C:\Users\pc\OneDrive\Desktop\Final year project\prophet_gold_price\gold_and_usdx.csv"

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(merged_file, index=False)

print(f"Files merged successfully. The output is saved at {merged_file}")
