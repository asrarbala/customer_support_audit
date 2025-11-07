# 🧾 Multilingual Customer Support Data Quality Audit

This project performs a **comprehensive data quality audit and cleaning** on the Kaggle dataset  
[*Multilingual Customer Support Tickets*](https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets).  

The goal was to assess, visualize, and improve the **integrity, completeness, and usability** of real-world customer support data — and to demonstrate a measurable improvement in data quality.

---

## 🎯 Objective

To evaluate and improve data quality by:
- Detecting missing, inconsistent, and duplicate values  
- Dropping or flagging unreliable data  
- Creating reproducible audit and visualization reports  
- Comparing data integrity **before vs after cleaning**

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Missingno |
| Reporting | Markdown, CSV |
| Environment | PyCharm / Jupyter Notebook |

---

## 📁 Project Structure

customer_support_audit/
│
├── data/
│ ├── raw/
│ │ └── Customer_support_data.csv
│ └── processed/
│ └── cleaned_support_data.csv
│
├── reports/
│ ├── data_audit_report_raw.md
│ ├── data_audit_report_cleaned.md
│ ├── data_summary_raw.md
│ ├── data_summary_cleaned.md
│ └── missing_comparison_raw_vs_cleaned.csv
│
├── visuals/
│ ├── missing_values_heatmap_raw.png
│ ├── missing_values_heatmap_cleaned.png
│ ├── missing_percent_barplot_raw.png
│ ├── missing_percent_barplot_cleaned.png
│ ├── missing_comparison_raw_vs_cleaned.png
│ └── csat_distribution_cleaned.png
│
└── src/
├── data_audit.py
├── clean_data.py
├── visualize_audit.py
└── compare_missing_visuals.py


---

## 🧪 Process & Methodology

| Phase | Description | Key Output |
|--------|--------------|-------------|
| **1️⃣ Data Audit (Raw)** | Profiled dataset structure, types, missing values, duplicates, and summary stats | `data_audit_report_raw.md` |
| **2️⃣ Visualization (Raw)** | Heatmap + bar plot of missing values | `missing_values_heatmap_raw.png` |
| **3️⃣ Data Cleaning** | Removed highly missing columns (>80%) and added missingness flags | `cleaned_support_data.csv` |
| **4️⃣ Audit (Cleaned)** | Re-profiled cleaned dataset | `data_audit_report_cleaned.md` |
| **5️⃣ Visualization (Cleaned)** | Plotted post-cleaning missingness and CSAT score distribution | `missing_values_heatmap_cleaned.png` |
| **6️⃣ Comparison** | Side-by-side missing % plot for raw vs cleaned | `missing_comparison_raw_vs_cleaned.png` |

---

## 📊 Key Findings (Before Cleaning)

| Column | Missing % | Action |
|---------|------------|---------|
| connected_handling_time | 99.7% | Dropped |
| Customer_City | 80.1% | Dropped |
| Product_category | 80.0% | Dropped |
| order_date_time | 79.9% | Dropped |
| Item_price | 79.9% | Kept + added flag |
| Customer Remarks | 66.5% | Kept |
| Order_id | 21.2% | Kept |

---

## 🧹 Data Cleaning Summary

| Action | Description |
|--------|--------------|
| 🔹 Dropped | Columns with >80% missing data |
| 🔹 Flagged | Added `Item_price_missing` (binary missingness flag) |
| 🔹 Preserved | Kept original NaN values for numeric integrity |
| 🔹 Verified | Re-audit showed drastic reduction in missingness |
| 🔹 Duplicates | None found (0 duplicate rows) |

---

## 🧮 Results & Impact

| Metric | Raw | Cleaned |
|---------|------|----------|
| Columns | 20 | 13 |
| Avg. Missing % | ~70% | ~10% |
| Duplicates | 0 | 0 |
| Quality Improvement | ✅ Major reduction in missingness |

---

## 🎨 Visual Results

| Visualization | Description |
|----------------|--------------|
| 🔵 **Missing Value Heatmap (Raw)** | Large missing regions |
| 🟢 **Missing Value Heatmap (Cleaned)** | Noticeably improved completeness |
| 🧮 **Missing % Comparison Chart** | Side-by-side improvement visualization |
| 📈 **CSAT Score Distribution** | Shows customer satisfaction spread (1–5 scale) |

---

## 📁 Deliverables

| File | Description |
|------|--------------|
| `data_audit_report_raw.md` | Raw dataset profiling |
| `data_audit_report_cleaned.md` | Cleaned dataset profiling |
| `data_summary_raw.md` | Missing values (raw) |
| `data_summary_cleaned.md` | Missing values (cleaned) |
| `cleaned_support_data.csv` | Final cleaned dataset |
| `missing_comparison_raw_vs_cleaned.png` | Before/After visual comparison |

---

## 🧠 Key Learnings

- Profiling data **before** cleaning helps target issues precisely.  
- High-missing columns (>80%) should be **dropped, not imputed**.  
- **Missingness flags** preserve information without distorting statistics.  
- Visual audits (heatmaps, missingno) make quality improvements tangible.  
- A clean documentation trail (`.md` + `.csv`) makes your work auditable.

---

## 🚀 Next Steps (Future Work)

- Perform **Exploratory Data Analysis (EDA)** on cleaned data  
  → e.g., *average CSAT by agent, issue category, or channel*  
- Build **Power BI / Python dashboards** for management insights  
- Automate the **entire audit pipeline** for repeated quality checks  

---

## 🏁 Conclusion

This project demonstrates a **complete data quality workflow**:  
> **Raw → Audit → Visualize → Clean → Re-Audit → Compare**

By systematically identifying, visualizing, and remediating quality issues,  
the dataset became ready for **exploratory analysis and reporting** —  
a critical step in any real-world data analytics process.  

---

### 👤 Author  
**Asrar Ahmad Bala**  
_Data Quality & QA Engineer | Data Analyst (in progress)_  
📧 _[optional: add your email or LinkedIn link here]_