import pandas as pd

def calculate_sma(data, window=20):
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

def calculate_macd(data, fast=12, slow=26, signal=9):
    exp1 = data['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = data['Close'].ewm(span=slow, adjust=False).mean()
    data['MACD'] = exp1 - exp2
    data['Signal_Line'] = data['MACD'].ewm(span=signal, adjust=False).mean()
    return data

def add_all_indicators(file_path='data/nifty_1yr_data_clean.csv'):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    
    data = calculate_sma(data)
    data = calculate_rsi(data)
    data = calculate_macd(data)
    
    data.to_csv(file_path, index=False)
    print("Indicators calculated and saved successfully.")

if __name__ == "__main__":
    add_all_indicators()
