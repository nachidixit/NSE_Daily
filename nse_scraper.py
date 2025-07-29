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
    response.encoding = 'utf-8'

    if "<html" in response.text.lower():
        print("❌ Received HTML instead of CSV. Possible access issue or invalid date.")
        with open("data/error_response.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        return

    try:
        df = pd.read_csv(StringIO(response.text), skiprows=1, on_bad_lines='skip')
        df.to_csv('data/nifty.csv', index=False)
        print("✅ Data fetched and saved to 'data/nifty.csv'.")
        
        generate_readme(df)
    except Exception as e:
        print("❌ Failed to parse CSV:", e)

def generate_readme(df):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_date = df['Date'].min() if 'Date' in df.columns else "N/A"
    end_date = df['Date'].max() if 'Date' in df.columns else "N/A"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"""# 📊 NSE Daily Auto Update

This GitHub repository auto-fetches **Nifty 50** data daily from NSE and plots visual analytics...

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
