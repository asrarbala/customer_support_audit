import pandas as pd
import os

data_path = "data/raw/Customer_support_data.csv"
save_path = "data/processed/cleaned_support_data.csv"

df = pd.read_csv(data_path)

# Clean up column names (remove spaces)
df.columns = df.columns.str.strip()

# --- Handle missing values ---
# Drop columns with >80% missing
df = df.loc[:, df.isnull().mean() < 0.8]

# Fill missing text with placeholder
df['Customer Remarks'] = df['Customer Remarks'].fillna('No Remarks')

# Convert dates to datetime
date_cols = ['order_date_time', 'Issue_reported at', 'issue_responded', 'Survey_response_Date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)

# Fill missing numerical values
df['Item_price_missing'] = df['Item_price'].isna().astype(int)

os.makedirs("data/processed", exist_ok=True)
df.to_csv(save_path, index=False)
print(f"✅ Cleaned data saved to: {save_path}")
