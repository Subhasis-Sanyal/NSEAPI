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

        return round(current_data.iloc[-1]['Close'], 2)
    except Exception as e:
        return "0"
        

    try:
        ticker = yf.Ticker(f"{symbol.upper()}.NS")
        current_data = ticker.history(period="1d")
        
        
        # Return only the closing price as a number
        return round(current_data.iloc[-1]['Close'], 2)
        
    except:
        return None

# Example usage
if __name__ == "__main__":
    price = get_stock_price("RELIANCE")
    print(price)  # Output: 2456.75 (just the number