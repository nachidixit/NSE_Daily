import pandas as pd
import requests
from io import StringIO
from datetime import datetime

def fetch_data():
    today = datetime.now().strftime('%d-%m-%Y')
    url = f'https://www1.nseindia.com/content/nsccl/fao_participant_oi_{today}.csv'
    
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://www1.nseindia.com/'
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # Ensure proper encoding

    # Detect if response is HTML (not CSV)
    if "<html" in response.text.lower():
        print("❌ Received HTML instead of CSV. Possible access issue or invalid date.")
        with open("data/error_response.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        return

    # Try to read CSV, skipping first row if necessary
    try:
        df = pd.read_csv(StringIO(response.text), skiprows=1, on_bad_lines='skip')  # Robust fallback
        df.to_csv('data/nifty.csv', index=False)
        print("✅ Data fetched and saved to 'data/nifty.csv'.")
    except Exception as e:
        print("❌ Failed to parse CSV:", e)

if __name__ == "__main__":
    fetch_data()
