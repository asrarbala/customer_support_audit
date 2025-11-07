# src/visualize_audit.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import os

# ---------- 📁 Setup Paths ----------
data_path = "data/processed/cleaned_support_data.csv"  # 👈 change path here for cleaned or raw dataset
visuals_path = "visuals/"
os.makedirs(visuals_path, exist_ok=True)

# Automatically detect raw or cleaned
report_prefix = "cleaned" if "cleaned" in data_path else "raw"

# ---------- 📥 Load Data ----------
df = pd.read_csv(data_path)
print(f"📂 Loaded {report_prefix.capitalize()} dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# ---------- 🎨 Visualization Style ----------
sns.set(style="whitegrid", font_scale=1.1)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.titleweight"] = "bold"

# ---------- 1️⃣ Missing Value Heatmap ----------
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='YlGnBu')
plt.title(f"Missing Value Heatmap — {report_prefix.capitalize()} Dataset")
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, f"missing_values_heatmap_{report_prefix}.png"))
plt.close()
print(f"✅ Saved: missing_values_heatmap_{report_prefix}.png")

# ---------- 2️⃣ Missing Percentage Bar Plot ----------
missing_percent = (df.isnull().sum() / len(df)) * 100
missing_percent = missing_percent[missing_percent > 0].sort_values(ascending=False)

if not missing_percent.empty:
    plt.figure(figsize=(10, 6))
    missing_percent.plot(kind='bar', color='coral')
    plt.title(f"Percentage of Missing Values per Column — {report_prefix.capitalize()} Dataset")
    plt.ylabel("Percent Missing (%)")
    plt.xlabel("Columns")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(visuals_path, f"missing_percent_barplot_{report_prefix}.png"))
    plt.close()
    print(f"✅ Saved: missing_percent_barplot_{report_prefix}.png")
else:
    print("✅ No missing values to visualize (dataset fully complete).")

# ---------- 3️⃣ CSAT Score Distribution ----------
if "CSAT Score" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["CSAT Score"], bins=5, kde=True, color='skyblue')
    plt.title(f"CSAT Score Distribution — {report_prefix.capitalize()} Dataset")
    plt.xlabel("CSAT Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(visuals_path, f"csat_distribution_{report_prefix}.png"))
    plt.close()
    print(f"✅ Saved: csat_distribution_{report_prefix}.png")
else:
    print("⚠️ Column 'CSAT Score' not found, skipping distribution plot.")

# ---------- 4️⃣ Missingno Matrix ----------
msno.matrix(df, color=(0.2, 0.4, 0.6))
plt.title(f"Missing Data Matrix — {report_prefix.capitalize()} Dataset", fontsize=13, weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, f"missingno_matrix_{report_prefix}.png"))
plt.close()
print(f"✅ Saved: missingno_matrix_{report_prefix}.png")

print(f"\n🎨 Visualization complete for {report_prefix.upper()} dataset! All charts saved in 'visuals/' folder.")
