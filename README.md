# 📊 NSE Daily Auto Update

Welcome to the **Nifty 50 Auto Update** project!  
This repository automatically fetches daily stock market data from NSE India and visualizes it using interactive financial charts. The project is scheduled to refresh every 1 hour between **9:30 AM to 4:00 PM IST** using **GitHub Actions**.

---

## 📆 Data Coverage

- **From:** 2024-07-01  
- **To:** 2025-07-29  
- 🕒 **Last Updated:** 2025-07-29 15:00:00 (IST)

> *Note: These values are dynamically updated every hour during market hours.*

---

## 📁 Data Source

The raw dataset is sourced from [NSE India](https://www.nseindia.com/) and saved in CSV format for reproducibility and audit trails.

- CSV Location: [`data/nifty.csv`](data/nifty.csv)

---

## 📈 Visualizations

### 🔹 1. Line Chart with SMA (Simple Moving Averages)

This chart shows Nifty 50 closing prices along with two trend lines:
- **SMA-20** (Short-term)
- **SMA-50** (Medium-term)

![Line SMA Chart](outputs/line_with_sma.png)

---

### 🔹 2. Candlestick Chart

Visualizes Open, High, Low, and Close prices per trading day.

![Candlestick Chart](outputs/candlestick.png)

---

### 🔹 3. MACD & RSI Indicator Chart

- **MACD** (Moving Average Convergence Divergence): Momentum trend-following indicator
- **RSI** (Relative Strength Index): Measures overbought/oversold conditions

![MACD RSI Chart](outputs/macd_rsi.png)

---

## ⚙️ Automation Workflow

This project is fully automated using **GitHub Actions**. It runs a workflow defined in `.github/workflows/update.yml` that:

1. Fetches latest Nifty 50 CSV data
2. Recalculates technical indicators (SMA, MACD, RSI)
3. Regenerates plots
4. Updates this `README.md` file with the latest charts and metadata
5. Pushes changes back to GitHub automatically

---

## 🧰 Tech Stack

- Python 3.11
- `pandas`, `plotly`, `ta` (Technical Analysis library)
- GitHub Actions
- NSE data API via CSV scraping

---

## ⭐ Like this Project?

If you found this helpful, please consider ⭐ starring the repo to support ongoing development.

---

**Author:** [Nachiket Dixit](https://github.com/nachidixit)  
**License:** MIT
