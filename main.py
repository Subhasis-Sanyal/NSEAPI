import requests
import re
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/price/{symbol}", response_class=PlainTextResponse)
def get_stock_price(symbol: str):
    clean_symbol = symbol.upper()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }
    try:
        groww_url = f"https://groww.in/v1/api/stocks_data/v1/tr_live_prices/exchange/NSE/segment/CASH/{clean_symbol}"
        groww_resp = requests.get(groww_url, headers=headers, timeout=5)
        if groww_resp.status_code == 200:
            data = groww_resp.json()
            if "ltp" in data:  # ltp = Last Traded Price
                return str(data["ltp"])
    except:
        pass

    try:
        gf_url = f"https://www.google.com/finance/quote/{clean_symbol}:NSE"
        gf_resp = requests.get(gf_url, headers=headers, timeout=5)
        match = re.search(r'class="YMlKec fxKbKc"[^>]*>₹([0-9,.]+)<', gf_resp.text)
        if match:
            price_str = match.group(1).replace(",", "")
            return str(float(price_str))

        match = re.search(r'data-last-price="([0-9.]+)"', gf_resp.text)
        if match:
             return str(float(match.group(1)))
             
        return "0"
    except Exception as e:
        return f"Error: {str(e)}"
