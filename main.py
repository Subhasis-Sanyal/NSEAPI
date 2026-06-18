import requests
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()
API_KEY = "iPeKJCDdwxRKF69EKfKoL1EI24kP4mYK"

@app.get("/price/{symbol}", response_class=PlainTextResponse)
def get_stock_price(symbol: str):
    try:
        ticker_symbol = f"{symbol.upper()}.NS"
        url = f"https://financialmodelingprep.com/stable/quote?symbol={ticker_symbol}&apikey={API_KEY}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0 and 'price' in data[0]:
                price = data[0].get('price')
                if price is not None:
                    return str(round(price, 2))
            
        return "0"
    except Exception as e:
        return f"Error: {str(e)}"
