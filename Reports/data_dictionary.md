# Mutual Fund Analysis - Data Dictionary

## Overview
This document describes all tables and columns in the Mutual Fund Star Schema.

---

## 1. dim_fund (Dimension Table)

| Column Name       | Data Type     | Nullable | Description | Source |
|-------------------|---------------|----------|-------------|--------|
| fund_id           | SERIAL (PK)   | No       | Unique surrogate key | Auto-generated |
| amfi_code         | TEXT (Unique) | Yes      | AMFI scheme code | 07_scheme_performance, 02_nav_history |
| scheme_name       | TEXT          | Yes      | Full name of the mutual fund scheme | 07_scheme_performance |
| fund_house        | TEXT          | Yes      | Asset Management Company | 07_scheme_performance, 03_aum |
| category          | TEXT          | Yes      | Fund category (Large Cap, Mid Cap, etc.) | 07_scheme_performance |
| risk_category     | TEXT          | Yes      | Risk level | 07_scheme_performance |

## 2. dim_date (Dimension Table)

| Column Name | Data Type     | Nullable | Description | Source |
|-------------|---------------|----------|-------------|--------|
| date_id     | SERIAL (PK)   | No       | Surrogate key | Auto |
| date        | DATE (Unique) | No       | Calendar date | Derived |
| month       | INTEGER       | Yes      | Month (1-12) | Derived |
| year        | INTEGER       | Yes      | Year | Derived |

## 3. fact_nav

| Column Name | Data Type | Nullable | Description | Source |
|-------------|-----------|----------|-------------|--------|
| nav_id      | SERIAL (PK) | No     | Unique ID | Auto |
| fund_id     | INTEGER (FK) | No    | Link to fund | 02_nav_history |
| date_id     | INTEGER (FK) | No    | Link to date | 02_nav_history |
| nav         | REAL      | Yes      | Net Asset Value | 02_nav_history |

## 4. fact_transactions

| Column Name      | Data Type | Nullable | Description | Source |
|------------------|-----------|----------|-------------|--------|
| transaction_id   | SERIAL (PK) | No     | Unique ID | Auto |
| fund_id          | INTEGER (FK) | Yes    | Link to fund | 08_investor_transactions |
| date_id          | INTEGER (FK) | Yes    | Link to date | 08_investor_transactions |
| amount_inr       | REAL      | Yes      | Amount in INR | 08_investor_transactions |
| transaction_type | TEXT      | Yes      | SIP / LUMPSUM / REDEMPTION | 08_investor_transactions |
| state            | TEXT      | Yes      | State of investor | 08_investor_transactions |

## 5. fact_performance

| Column Name       | Data Type | Nullable | Description | Source |
|-------------------|-----------|----------|-------------|--------|
| performance_id    | SERIAL (PK) | No     | Unique ID | Auto |
| fund_id           | INTEGER (FK) | No    | Link to fund | 07_scheme_performance |
| return_1yr_pct    | REAL      | Yes      | 1 Year Return % | 07_scheme_performance |
| return_3yr_pct    | REAL      | Yes      | 3 Year Return % | 07_scheme_performance |
| return_5yr_pct    | REAL      | Yes      | 5 Year Return % | 07_scheme_performance |
| expense_ratio_pct | REAL      | Yes      | Expense Ratio % | 07_scheme_performance |

## 6. fact_aum

| Column Name     | Data Type | Nullable | Description | Source |
|-----------------|-----------|----------|-------------|--------|
| aum_id          | SERIAL (PK) | No     | Unique ID | Auto |
| date_id         | INTEGER (FK) | No    | Link to date | 03_aum_by_fund_house |
| fund_house      | TEXT      | Yes      | Fund House | 03_aum_by_fund_house |
| aum_lakh_crore  | REAL      | Yes      | AUM in Lakh Crore | 03_aum_by_fund_house |
| aum_crore       | REAL      | Yes      | AUM in Crore | 03_aum_by_fund_house |
| num_schemes     | INTEGER   | Yes      | Number of schemes | 03_aum_by_fund_house |

---

**Last Updated:** July 01, 2026
