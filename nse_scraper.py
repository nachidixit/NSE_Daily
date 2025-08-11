import pandas as pd
import requests
from io import StringIO
from datetime import datetime
import os

def fetch_data():
    today = datetime.now().strftime('%d-%m-%Y')
    url = f'https://www.nseindia.com/content/nsccl/fao_participant_oi_{today}.csv'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    session = requests.Session()
    session.headers.update(headers)

    # Step 1: Get cookies from homepage
    try:
        session.get("https://www.nseindia.com", timeout=10)
    except Exception as e:
        print("⚠ Warning: Could not fetch homepage cookies:", e)

    # Step 2: Download CSV
    try:
        response = session.get(url, timeout=15)
        response.encoding = 'utf-8'

        if "<html" in response.text.lower():
            print("❌ Received HTML instead of CSV. Saving error page.")
            os.makedirs("data", exist_ok=True)
            with open("data/error_response.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            return

        df = pd.read_csv(StringIO(response.text), skiprows=1, on_bad_lines='skip')
        os.makedirs("data", exist_ok=True)
        df.to_csv('data/nifty.csv', index=False)
        print("✅ Data fetched and saved to 'data/nifty.csv'.")

        generate_readme(df)
    except Exception as e:
        print("❌ Failed to fetch data from NSE:", e)

def generate_readme(df):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_date = df['Date'].min() if 'Date' in df.columns else "N/A"
    end_date = df['Date'].max() if 'Date' in df.columns else "N/A"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"""# 📊 NSE Daily Auto Update

This GitHub repository auto-fetches **Nifty 50** data daily from NSE and plots visual analytics.

## 📆 Data Range  
**From:** {start_date}  
**To:** {end_date}  

🕒 **Last Updated:** {now}

---

## 📈 Line Chart with SMA

Shows Nifty 50 close prices with 20-day and 50-day Simple Moving Averages.

![Line SMA Chart](outputs/line_with_sma.png)

---

## 🕯 Candlestick Chart

A classic candlestick chart to visualize daily open, high, low, and close trends.

![Candlestick Chart](outputs/candlestick.png)

---

## 📉 MACD + RSI Indicators

Used for momentum analysis and trend signals.

![MACD RSI Chart](outputs/macd_rsi.png)

---

## 📁 Data

- Historical Data CSV: [`data/nifty.csv`](data/nifty.csv)
- Charts saved under: [`outputs/`](outputs/)

---

### 🔁 Auto-Update

This project is automatically updated every 1 hour between **9:30 AM – 4:00 PM IST** using [GitHub Actions](https://docs.github.com/en/actions).

---
**⭐ Star the repo if you find this useful!**
""")
    print("📘 README.md updated.")

if __name__ == "__main__":
    fetch_data()
