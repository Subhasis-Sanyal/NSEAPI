from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import yfinance as yf
import requests

app = FastAPI()
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
})

@app.get("/price/{symbol}", response_class=PlainTextResponse)
def get_stock_price(symbol: str):
    try:
        ticker = yf.Ticker(f"{symbol.upper()}.NS", session=session)        
        current_data = ticker.history(period="1d")        
        if current_data.empty:
            return "0"
        return str(round(current_data.iloc[-1]['Close'], 2))
    except Exception as e:
        return f"Error: {str(e)}"
