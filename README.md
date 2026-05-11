# Marketing Data Quality Toolkit

This project demonstrates basic data cleaning, validation, and reporting using Python. It was created as a practical preparation project for working student roles involving data governance, application engineering, marketing data, and automation.

## Project Overview

The dataset contains fictional semiconductor-related marketing/product data, including product IDs, product families, regions, campaigns, leads, clicks, impressions, budgets, owners, update dates, and status values.

The Python script automates common data quality tasks and generates both a cleaned CSV file and a text-based data quality report.

## Features

- Loads raw CSV marketing data
- Standardizes inconsistent text values
- Removes duplicate records
- Flags incomplete records
- Flags outdated records
- Calculates click-through rate
- Calculates cost per lead
- Exports a cleaned CSV file
- Generates an automated data quality report

## Folder Structure

```text
marketing-data-quality-toolkit/
│
├── data/
│   ├── raw_marketing_data.csv
│   └── cleaned_marketing_data.csv
│
├── reports/
│   └── data_quality_report.txt
│
├── clean_marketing_data.py
│
└── README.md

## Screenshots

### Excel Dashboard
![Excel Dashboard](screenshots/excel-dashboard.png)

### Python Report Output
![Python Report](screenshots/python-report.png)
