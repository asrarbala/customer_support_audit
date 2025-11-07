# src/compare_missing_visuals.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- 📁 File Paths ----------
raw_path = "data/raw/Customer_support_data.csv"
cleaned_path = "data/processed/cleaned_support_data.csv"
visuals_path = "visuals/"
os.makedirs(visuals_path, exist_ok=True)

# ---------- 📥 Load Datasets ----------
df_raw = pd.read_csv(raw_path)
df_clean = pd.read_csv(cleaned_path)

# ---------- 📊 Calculate Missing Percentages ----------
raw_missing = (df_raw.isnull().sum() / len(df_raw)) * 100
cleaned_missing = (df_clean.isnull().sum() / len(df_clean)) * 100

# Combine into one DataFrame
compare_df = pd.concat(
    [raw_missing.rename("Raw Dataset"), cleaned_missing.rename("Cleaned Dataset")],
    axis=1
).fillna(0)  # columns dropped in cleaned will appear as 0%

# Round for neatness
compare_df = compare_df.round(2)

# ---------- 📈 Plot Side-by-Side Bar Chart ----------
sns.set(style="whitegrid", font_scale=1.1)
plt.figure(figsize=(12, 7))
compare_df.sort_values("Raw Dataset", ascending=False).plot(
    kind="bar", width=0.8, figsize=(12, 7)
)
plt.title("📊 Missing Data Comparison — Raw vs Cleaned Dataset", fontsize=15, weight="bold")
plt.ylabel("Percent Missing (%)")
plt.xlabel("Columns")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Dataset")
plt.tight_layout()

# Save the combined chart
output_path = os.path.join(visuals_path, "missing_comparison_raw_vs_cleaned.png")
plt.savefig(output_path)
plt.close()
print(f"✅ Saved: {output_path}")

# ---------- 🧾 Optional: Save Data as CSV ----------
compare_df.to_csv("reports/missing_comparison_raw_vs_cleaned.csv", index=True)
print("✅ Saved: reports/missing_comparison_raw_vs_cleaned.csv")

print("\n🎯 Comparison complete! Visual and data saved successfully.")
