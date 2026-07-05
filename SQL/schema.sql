CREATE TABLE dim_fund (
    fund_id SERIAL PRIMARY KEY,
    amfi_code TEXT UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_category TEXT
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    date DATE UNIQUE,
    month INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_id SERIAL PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
    transaction_id SERIAL PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    amount_inr REAL,
    transaction_type TEXT,
    state TEXT,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    performance_id SERIAL PRIMARY KEY,
    fund_id INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum (
    aum_id SERIAL PRIMARY KEY,
    date_id INTEGER,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER,
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);