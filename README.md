# Marketing Data Quality Toolkit

This project demonstrates basic data cleaning, validation, and reporting using Python. The goal was to automate the repetitive parts of cleaning a marketing dataset: standardising inconsistent text, removing duplicates, flagging records that are incomplete or out of date, and producing a summary report.

<img width="1920" height="1080" alt="DataScrub_preview" src="https://github.com/user-attachments/assets/d3789513-d929-4409-a342-2d5b271b041e" />

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
├── screenshots/
│   ├── dashboard.png
│   └── clean_data.png
│   └── terminal_running.png
│
├── clean_marketing_data.py
│
└── README.md
