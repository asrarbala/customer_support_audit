import pandas as pd
import os

data_path = "data/raw/Customer_support_data.csv"
save_path = "data/processed/cleaned_support_data.csv"

df = pd.read_csv(data_path)

# Clean up column names (remove spaces)
df.columns = df.columns.str.strip()

# --- Handle missing values ---
# Drop columns with ~80% missing
threshold = 0.8
tolerance = 0.001
important_cols = ['Item_price']   # keep even if missing ratio ~80%

missing_ratio = df.isnull().mean()
# Drop columns >= (threshold - tolerance) except those explicitly important
drop_cols = [   #using list comprehension
    col for col in missing_ratio.index
    if missing_ratio[col] >= (threshold - tolerance) and col not in important_cols
]
df = df.drop(columns=drop_cols)
print(f"Dropped columns (≥{(threshold - tolerance)*100:.1f}% missing): {drop_cols}")


# Fill missing text with placeholder
df['Customer Remarks'] = df['Customer Remarks'].fillna('No Remarks')

# Convert dates to datetime
date_cols = ['order_date_time', 'Issue_reported at', 'issue_responded', 'Survey_response_Date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)

#Fill missing numerical values
if 'Item_price' in df.columns:
    df['Item_price_missing'] = df['Item_price'].isna().astype(int)

#Fill missing values with a placeholder 
if 'Order_id' in df.columns:
    df['Order_id'] = df['Order_id'].fillna('Unknown')

os.makedirs("data/processed", exist_ok=True)
df.to_csv(save_path, index=False)
print(f"✅ Cleaned data saved to: {save_path}")
