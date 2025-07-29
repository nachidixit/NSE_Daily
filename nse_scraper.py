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
        'Connection': 'keep-alive'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    df = pd.read_csv(StringIO(response.text), skiprows=1)
    df.to_csv('data/nifty.csv', index=False)
    print("Data fetched and saved.")

if __name__ == "__main__":
    fetch_data()
