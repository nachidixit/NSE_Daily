import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def load_data(file_path='data/nifty.csv'):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  # ✅ Strip spaces from column names
    df['Date'] = pd.to_datetime(df['Date'])  # ✅ Now 'Date' instead of 'Date '
    
    # ✅ Add indicators
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    
    # MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    
    # RSI
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    return df

def plot_line_sma(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_20'], mode='lines', name='SMA 20'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_50'], mode='lines', name='SMA 50'))
    fig.update_layout(title='Close Price with SMA', xaxis_title='Date', yaxis_title='Price')
    fig.write_html('outputs/line_with_sma.html')
    print("Line chart with SMA saved.")

def plot_candlestick(df):
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title='Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
    fig.write_html('outputs/candlestick.html')
    print("Candlestick chart saved.")

def plot_macd_rsi(df):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.1,
                        subplot_titles=('MACD', 'RSI'),
                        row_width=[0.2, 0.7])

    # MACD & Signal Line
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD'], name='MACD', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Signal_Line'], name='Signal Line', line=dict(color='orange')), row=1, col=1)

    # RSI
    fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], name='RSI', line=dict(color='green')), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="red", row=2, col=1)

    fig.update_layout(height=600, title='MACD and RSI Indicators')
    fig.write_html('outputs/macd_rsi.html')
    print("MACD + RSI chart saved.")

if __name__ == "__main__":
    df = load_data()
    plot_line_sma(df)
    plot_candlestick(df)
    plot_macd_rsi(df)
