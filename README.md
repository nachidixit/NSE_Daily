# 📈 NSE Daily Market Dashboard

This project automates fetching, processing, and visualizing daily Nifty 50 data from NSE India using Python and GitHub Actions.

---

## ⚡ Features

- 🔁 Auto-updates every hour between **9:30 AM – 4:00 PM IST**
- 📥 Scrapes latest market data from NSE
- 📊 Generates interactive financial charts:
  - SMA Overlay
  - Candlestick Chart
  - MACD + RSI Chart
- ☁️ GitHub-hosted; no local setup required

---

## 📂 Output Visualizations

The charts are saved as **interactive HTML files** in the [`outputs/`](outputs/) folder:

| Chart Type           | Description                              | Link to View |
|----------------------|------------------------------------------|--------------|
| 📈 Line + SMA Chart  | Closing price with SMA-20 & SMA-50       | [Open](outputs/line_with_sma.html) |
| 📊 Candlestick Chart | OHLC price visualization with wicks      | [Open](outputs/candlestick.html) |
| 🧠 MACD + RSI Chart  | Momentum indicators & overbought zones   | [Open](outputs/macd_rsi.html) |

> 💡 You can download and open these `.html` files locally to view them interactively.

---

## 📁 Data Source

- **Provider:** [NSE India](https://www.nseindia.com/)
- **CSV:** [`data/nifty.csv`](data/nifty.csv)

---

## 🔄 Automation via GitHub Actions

This repo includes a scheduled GitHub Action (`.github/workflows/daily_update.yml`) that:

1. Runs every hour (9:30–16:00 IST)
2. Executes `nse_scraper.py`
3. Updates data and plots in `/outputs`
4. Regenerates `README.md` (optional)

---

## 🚀 Run Locally (Optional)

```bash
git clone https://github.com/nachidixit/NSE_Daily.git
cd NSE_Daily
pip install -r requirements.txt
python nse_scraper.py
