import pandas as pd
from pathlib import Path
from datetime import datetime


RAW_DATA_PATH = Path("data/raw_marketing_data.csv")
CLEANED_DATA_PATH = Path("data/cleaned_marketing_data.csv")
REPORT_PATH = Path("reports/data_quality_report.txt")


def load_data(file_path):
    """Load raw marketing data from a CSV file."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)


def standardize_text_columns(df):
    """Clean and standardize text-based columns."""
    text_columns = [
        "Product_ID",
        "Product_Name",
        "Product_Family",
        "Region",
        "Channel",
        "Campaign",
        "Owner",
        "Status",
    ]

    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].fillna("").astype(str).str.strip()

    region_mapping = {
        "emea": "EMEA",
        "europe": "EMEA",
        "apac": "APAC",
        "americas": "Americas",
        "usa": "Americas",
    }

    df["Region"] = df["Region"].str.lower().replace(region_mapping)

    df["Status"] = df["Status"].str.lower().replace(
        {
            "active": "Active",
            "review": "Review",
            "paused": "Paused",
            "completed": "Completed",
        }
    )

    return df


def remove_duplicates(df):
    """Remove duplicate records based on Product_ID and Campaign."""
    before_count = len(df)

    df = df.drop_duplicates(
        subset=["Product_ID", "Campaign"],
        keep="first"
    )

    after_count = len(df)
    duplicates_removed = before_count - after_count

    return df, duplicates_removed


def add_data_quality_checks(df):
    """Flag incomplete and outdated records."""
    required_columns = [
        "Product_ID",
        "Product_Name",
        "Product_Family",
        "Region",
        "Owner",
        "Last_Updated",
        "Status",
    ]

    df["Data_Quality_Flag"] = df[required_columns].apply(
        lambda row: "Incomplete" if any(value == "" for value in row) else "Complete",
        axis=1,
    )

    df["Last_Updated"] = pd.to_datetime(df["Last_Updated"], errors="coerce")

    today = pd.Timestamp(datetime.today().date())

    df["Update_Status"] = df["Last_Updated"].apply(
        lambda date: "Needs Update"
        if pd.isnull(date) or (today - date).days > 30
        else "Up-to-date"
    )

    return df


def calculate_metrics(df):
    """Calculate basic marketing performance metrics."""
    numeric_columns = ["Leads", "Clicks", "Impressions", "Budget_EUR"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)

    df["Click_Through_Rate"] = df.apply(
        lambda row: row["Clicks"] / row["Impressions"]
        if row["Impressions"] != 0
        else 0,
        axis=1,
    )

    df["Cost_Per_Lead"] = df.apply(
        lambda row: row["Budget_EUR"] / row["Leads"]
        if row["Leads"] != 0
        else 0,
        axis=1,
    )

    return df


def generate_report(df, duplicates_removed):
    """Generate a text-based data quality report."""
    total_records = len(df)
    complete_records = (df["Data_Quality_Flag"] == "Complete").sum()
    incomplete_records = (df["Data_Quality_Flag"] == "Incomplete").sum()
    needs_update = (df["Update_Status"] == "Needs Update").sum()

    total_leads = df["Leads"].sum()
    total_budget = df["Budget_EUR"].sum()
    average_ctr = df["Click_Through_Rate"].mean()
    average_cost_per_lead = df["Cost_Per_Lead"].mean()

    report = f"""
Marketing Data Quality Report
=============================

Total cleaned records: {total_records}
Duplicates removed: {duplicates_removed}

Data Quality
------------
Complete records: {complete_records}
Incomplete records: {incomplete_records}
Records needing update: {needs_update}

Marketing Performance
---------------------
Total leads: {total_leads}
Total budget: {total_budget:.2f} EUR
Average click-through rate: {average_ctr:.2%}
Average cost per lead: {average_cost_per_lead:.2f} EUR

Purpose
-------
This report was generated automatically using Python to demonstrate basic
data cleaning, data validation, and reporting for marketing/product data.
"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        file.write(report)

    return report


def main():
    """Run the full data cleaning workflow."""
    print("Loading raw marketing data...")
    df = load_data(RAW_DATA_PATH)

    print("Standardizing text fields...")
    df = standardize_text_columns(df)

    print("Removing duplicates...")
    df, duplicates_removed = remove_duplicates(df)

    print("Adding data quality checks...")
    df = add_data_quality_checks(df)

    print("Calculating metrics...")
    df = calculate_metrics(df)

    CLEANED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)

    print("Generating report...")
    report = generate_report(df, duplicates_removed)

    print(report)
    print(f"Cleaned CSV saved to: {CLEANED_DATA_PATH}")
    print(f"Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()