from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import yfinance as yf

app = FastAPI()

@app.get("/price/{symbol}", response_class=PlainTextResponse)
def get_stock_price(symbol: str):
    try:
        ticker = yf.Ticker(f"{symbol.upper()}.NS")
        
        current_data = ticker.history(period="1d")        
        if current_data.empty:
            return "0"

        return str(round(current_data.iloc[-1]['Close'], 2))
    except Exception as e:
        return f"Error: {str(e)}"
