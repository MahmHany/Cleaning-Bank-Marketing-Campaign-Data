# 🏦 Bank Marketing Data Cleaning & Export

This project focuses on transforming raw bank marketing campaign data into three clean, analysis-ready datasets using Python and pandas. The data is restructured into client-level, campaign-level, and macroeconomic feature sets, making it suitable for downstream reporting, segmentation, and modeling.

---

## 📌 Project Objective

To preprocess and restructure the original dataset in order to:

- Clean and convert categorical and boolean values
- Standardize text data for consistency
- Generate proper date fields from separate day/month columns
- Calculate derived dates like last contact review
- Export cleaned subsets into CSV files for further analysis

---

## 📁 Data Source

**`bank_marketing.csv`**  
Contains full client records, contact history, campaign response data, and economic indicators.

---

## 🔧 Key Features

### 🧹 Data Cleaning & Transformation

- **Boolean Conversion**: Converted `"yes"`/`"no"` strings in `credit_default`, `mortgage`, `previous_outcome`, and `campaign_outcome` into proper boolean data types.
- **Text Normalization**: Replaced `.` with `_` in `job` and `education` columns; converted `"unknown"` values to `NaN`.
- **Date Reconstruction**: Merged `month` and `day` columns into a single datetime column using a fixed base year (`2022`) to compute `last_contact_date` from `contact_duration`.

### 🧮 Derived Metrics

- **`last_contact_date`**: Calculated by subtracting `contact_duration` in days from `full_date`.
- **`last_review`**: A formatted version of `last_contact_date` in `YYYY-MM-DD` format.

---

## 📊 Modular Outputs

### `client.csv`

Includes personal and demographic client information:
- `client_id`, `age`, `job`, `marital`, `education`, `credit_default`, `mortgage`

### `campaign.csv`

Includes contact and campaign response history:
- `client_id`, `number_contacts`, `contact_duration`, `previous_campaign_contacts`, `previous_outcome`, `campaign_outcome`, `last_contact_date`

### `economics.csv`

Contains macroeconomic indicators per client:
- `client_id`, `cons_price_idx`, `euribor_three_months`

---

## 💻 Tech Stack

- **Python (pandas, NumPy)** – data manipulation and type conversion
- **CSV File Handling** – for reading and exporting datasets
- **Datetime & Timedelta** – for constructing and subtracting date information
- **Text Cleaning** – for formatting job titles and education levels

---

## 📈 Why This Project?

This project simulates a real-world data preparation pipeline where raw marketing campaign data is cleaned, transformed, and segmented into specific output files for targeted analysis. The final output can be used in BI dashboards, customer segmentation models, or campaign performance reporting.

---

## 📎 Sample Outputs

### `client.csv`

| client_id | age | job     | credit_default | education    |
|-----------|-----|---------|----------------|--------------|
| 1001      | 35  | admin_  | True           | university   |

### `campaign.csv`

| client_id | contact_duration | last_contact_date | campaign_outcome |
|-----------|------------------|-------------------|------------------|
| 1001      | 235              | 2021-08-20        | False            |

### `economics.csv`

| client_id | cons_price_idx | euribor_three_months |
|-----------|----------------|----------------------|
| 1001      | 93.2           | 4.857                |

---

## 📂 Files Generated

- `client.csv`
- `campaign.csv`
- `economics.csv`
