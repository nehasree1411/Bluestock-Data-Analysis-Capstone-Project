from pathlib import Path
import requests
import pandas as pd

SCHEME_CODE = 125497
URL = f"https://api.mfapi.in/mf/{SCHEME_CODE}"

BASE_DIR = Path(r'D:\BlueStock_Project').resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

from pathlib import Path
import requests
import pandas as pd
import json
import time

BASE_DIR = Path(r'D:\BlueStock_Project').resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://api.mfapi.in/mf"

KEY_SCHEMES = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841,
}

session = requests.Session()
session.headers.update({"User-Agent": "mf-nav-ingestion/1.0"})

def fetch_json(url: str) -> dict:
    response = session.get(url, timeout=30)
    response.raise_for_status()
    return response.json()

def save_json(payload: dict, file_path: Path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

def flatten_nav_response(payload: dict, source_url: str) -> pd.DataFrame:
    meta = payload.get("meta", {})
    data = payload.get("data", [])

    if isinstance(data, dict):
        data = [data]
    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)

    for key, value in meta.items():
        df[key] = value

    df["source_url"] = source_url
    return df

def fetch_history_csv(scheme_code: int, out_name: str):
    url = f"{BASE_URL}/{scheme_code}"
    payload = fetch_json(url)

    save_json(payload, RAW_DIR / f"{out_name}_{scheme_code}_history.json")

    df = flatten_nav_response(payload, url)
    if not df.empty:
        df.to_csv(RAW_DIR / f"{out_name}_{scheme_code}_history.csv", index=False)
        print(f"Saved history CSV: {out_name}_{scheme_code}_history.csv | shape={df.shape}")
    else:
        print(f"No history data returned for {scheme_code}")

def fetch_latest_csv(scheme_code: int, out_name: str):
    url = f"{BASE_URL}/{scheme_code}/latest"
    payload = fetch_json(url)

    save_json(payload, RAW_DIR / f"{out_name}_{scheme_code}_latest.json")

    df = flatten_nav_response(payload, url)
    if not df.empty:
        df.to_csv(RAW_DIR / f"{out_name}_{scheme_code}_latest.csv", index=False)
        print(f"Saved latest CSV: {out_name}_{scheme_code}_latest.csv | shape={df.shape}")
        print(df.head())
    else:
        print(f"No latest NAV data returned for {scheme_code}")

def main():
    print("Fetching HDFC Top 100 Direct full NAV history...")
    fetch_history_csv(125497, "hdfc_top_100_direct_nav_raw")

    print("\nFetching latest NAV for 5 key schemes...")
    for name, code in KEY_SCHEMES.items():
        try:
            fetch_latest_csv(code, name)
            time.sleep(0.5)
        except Exception as e:
            print(f"Error fetching {name} ({code}): {e}")

if __name__ == "__main__":
    main()