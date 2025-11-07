# src/data_audit.py

import pandas as pd
import os

# ---------------- Load Dataset ----------------
data_path = "data/processed/cleaned_support_data.csv"   # change to raw path if needed
df = pd.read_csv(data_path)

# Automatically detect prefix
report_prefix = "cleaned" if "cleaned" in data_path else "raw"

# ---------------- BASIC INFO ----------------
print("Dataset Shape:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())

# ---------------- DATA TYPES ----------------
print("\nData Types:\n", df.dtypes)

# ---------------- MISSING VALUES ----------------
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100
missing_df = pd.concat([missing_count, missing_percent], axis=1)
missing_df.columns = ["Missing Values", "Percent Missing"]
missing_df = missing_df[missing_df["Missing Values"] > 0]
missing_df["Percent Missing"] = missing_df["Percent Missing"].round(2)  # ✅ round percentages
missing_df = missing_df.sort_values("Percent Missing", ascending=False)  # ✅ sort highest first

print("\nMissing Value Summary:\n", missing_df)

# ---------------- DUPLICATES ----------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# ---------------- SUMMARY STATS ----------------
print("\nSummary Statistics:\n", df.describe(include="all"))

# ---------------- SAVE REPORT ----------------
os.makedirs("reports", exist_ok=True)
summary_path = f"reports/data_summary_{report_prefix}.csv"
report_path = f"reports/data_audit_report_{report_prefix}.md"

# Clean and format missing summary
missing_df = missing_df.round(2)
missing_df = missing_df.rename_axis("Column Name").reset_index()
missing_df = missing_df.sort_values("Percent Missing", ascending=False)

# Convert DataFrame to Markdown format
md_table = missing_df.to_markdown(index=False, tablefmt="pipe", numalign="right", stralign="left")

# Save as a .md-formatted summary file
summary_path = f"reports/data_summary_{report_prefix}.md"
with open(summary_path, "w", encoding="utf-8") as f:
    f.write(md_table)

print(f"✅ Markdown summary saved to: {summary_path}")

with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"# 🧾 Data Quality Audit Report — {report_prefix.capitalize()} Dataset\n\n")

    # ----- Dataset Overview -----
    f.write("## 📊 Dataset Overview\n")
    f.write(f"- **Rows:** {df.shape[0]}\n")
    f.write(f"- **Columns:** {df.shape[1]}\n")
    f.write(f"- **Duplicate Rows:** {duplicates}\n\n")

    # ----- Missing Values -----
    f.write("## 🚨 Missing Values Summary\n")
    if missing_df.empty:
        f.write("✅ No missing values detected!\n\n")
    else:
        f.write(missing_df.to_markdown())
        f.write("\n\n")

    # ----- Data Types -----
    f.write("## 🧩 Data Types\n")
    dtype_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
    #or dtype_df = df.dtypes.rename_axis("Column Name").reset_index(name="Data Type")

    f.write(dtype_df.to_markdown())
    f.write("\n\n")

    # ----- Summary -----
    f.write("## 🧠 Summary & Next Steps\n")
    f.write(
        "This audit report highlights missing values, data types, and duplication levels. "
        "Columns with excessive missing data will be reviewed for removal or flagged with missingness indicators "
        "in the cleaning stage.\n\n"
        "Next step: Compare this report with `data_audit_report_raw.md` and "
        "`data_audit_report_cleaned.md` to evaluate improvements in data completeness."
    )

print(f"✅ Audit report saved to: {report_path}")
print(f"✅ Missing summary saved to: {summary_path}")
