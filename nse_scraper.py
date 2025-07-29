import pandas as pd
import datetime
import os

URL = "https://www1.nseindia.com/content/nsccl/fao_participant_oi_{}.csv"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def fetch_data():
    today = datetime.datetime.now().strftime("%d%m%Y")
    url = URL.format(today)
    df = pd.read_csv(url, skiprows=1)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/nifty.csv", index=False)

if __name__ == "__main__":
    fetch_data()