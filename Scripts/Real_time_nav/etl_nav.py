import requests
import pandas as pd
from datetime import datetime

URL = "https://api.mfapi.in/mf/119551"

def fetch_nav():
    response = requests.get(URL)
    data = response.json()

    # 🔥 HANDLE BOTH CASES
    if isinstance(data, dict):
        nav_data = data.get('data', [])
    elif isinstance(data, list):
        nav_data = data
    else:
        raise ValueError("Unexpected API format")

    df = pd.DataFrame(nav_data)

    df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y", errors='coerce')
    df['nav'] = pd.to_numeric(df['nav'], errors='coerce')

    df = df.dropna()

    df.to_csv(r"D:\BlueStock_Project\Scripts\Real_time_nav\nav_data.csv", index=False)

    print("NAV updated:", datetime.now())

if __name__ == "__main__":
    fetch_nav()