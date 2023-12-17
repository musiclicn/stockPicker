import pandas as pd
import pandas_datareader as pdr
import datetime

# Function to calculate EMA
def calculate_ema(prices, days):
    return prices.ewm(span=days, adjust=False).mean()

# Function to detect EMA crossover in the last N days
def ema_crossover_recent(stock, days=10):
    # Fetch historical data
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=365)  # Adjust as needed
    data = pdr.get_data_yahoo(stock, start, end)

    # Calculate EMAs
    ema_21 = calculate_ema(data['Close'], 21)
    ema_55 = calculate_ema(data['Close'], 55)

    # Detect crossover
    crossover = ema_21 > ema_55

    # Check if crossover happened in the last N days
    recent_crossover = crossover[-days:].any() and not crossover.iloc[-days]
    return recent_crossover

# List of stock symbols
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']  # Add more as needed

# Find stocks with EMA crossover in the last N days
crossover_stocks = [stock for stock in stocks if ema_crossover_recent(stock, 10)]

print("Stocks with 21-day EMA crossing above 55-day EMA in the last 10 days:")
print(crossover_stocks)
