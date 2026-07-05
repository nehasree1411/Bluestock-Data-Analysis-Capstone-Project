import pandas as pd
import numpy as np

# ================= FILE PATHS =================
NAV_PATH = r"D:\BlueStock_Project\Data\Processed\02_nav_history_cleaned.csv"
FUND_PATH = r"D:\BlueStock_Project\Data\Processed\01_fund_master_cleaned.csv"


# ================= LOAD DATA =================
def load_data():
    try:
        print("Loading data...")

        nav = pd.read_csv(NAV_PATH)
        fund = pd.read_csv(FUND_PATH)

        # Standardize types
        nav['amfi_code'] = nav['amfi_code'].astype(str).str.strip()
        fund['amfi_code'] = fund['amfi_code'].astype(str).str.strip()

        print("Data loaded successfully")
        return nav, fund

    except Exception as e:
        print("Error loading data:", e)
        return None, None


# ================= COMPUTE RETURNS =================
def compute_returns(nav):
    nav['date'] = pd.to_datetime(nav['date'])
    nav = nav.sort_values(['amfi_code', 'date'])

    nav['return'] = nav.groupby('amfi_code')['nav'].pct_change()
    nav = nav.dropna()

    return nav


# ================= CALCULATE SHARPE =================
def calculate_sharpe(nav):
    sharpe_df = nav.groupby('amfi_code')['return'].agg(['mean', 'std']).reset_index()

    sharpe_df['sharpe_ratio'] = (sharpe_df['mean'] / sharpe_df['std']) * np.sqrt(252)

    return sharpe_df


# ================= RECOMMENDER =================
def recommend_funds(risk_level, nav, fund):
    try:
        # Ensure datatype consistency
        nav['amfi_code'] = nav['amfi_code'].astype(str)
        fund['amfi_code'] = fund['amfi_code'].astype(str)

        # Calculate Sharpe (ONLY from nav)
        sharpe_df = calculate_sharpe(nav)

        # Merge fund details
        final_df = sharpe_df.merge(
            fund[['amfi_code', 'scheme_name', 'risk_category']],
            on='amfi_code'
        )

        # Filter by risk
        filtered = final_df[
            final_df['risk_category'].str.lower() == risk_level.lower()
        ]

        if filtered.empty:
            print(f"No funds found for risk level: {risk_level}")
            return pd.DataFrame()

        # Top 3 funds
        top3 = filtered.sort_values('sharpe_ratio', ascending=False).head(3)

        return top3[['amfi_code', 'scheme_name', 'risk_category', 'sharpe_ratio']]

    except Exception as e:
        print("Error in recommendation:", e)
        return pd.DataFrame()


# ================= MAIN =================
if __name__ == "__main__":

    nav, fund = load_data()

    if nav is None or fund is None:
        print("Exiting due to data error")
        exit()

    # 🚨 MUST: compute returns before recommendation
    nav = compute_returns(nav)

    print("\nEnter Risk Level (Low / Moderate / High):")
    risk_input = input().strip()

    recommendations = recommend_funds(risk_input, nav, fund)

    if not recommendations.empty:
        print("\n🎯 Top 3 Recommended Funds:\n")
        print(recommendations.to_string(index=False))

    else:
        print("No recommendations available.")

    print("\n✅ Recommender Completed")