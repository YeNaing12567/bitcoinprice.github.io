import requests
import talib

def fetch_crypto_data():
    # Crypto data ကို API မှ fetch လုပ်သည်
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1'
    response = requests.get(url)
    data = response.json()
    return data

def analyze_data(prices):
    # TA-Lib ကို သုံးပြီး data ကို analysis လုပ်သည်
    close_prices = [price['close'] for price in prices]
    pattern = talib.CDLHAMMER(close_prices)
    return pattern
