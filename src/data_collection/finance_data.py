import yfinance as yf

def get_stock_data(tickers, start_date, end_date):
    df = yf.download(tickers, start=start_date, end=end_date)
    return df

if __name__ == "__main__":
    stock_data = get_stock_data(["PETR4.SA", "ITUB4.SA"], "2023-01-01", "2023-08-01")
    print(stock_data)
