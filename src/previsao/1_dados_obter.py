import yfinance as yf
import pandas as pd

def obter_dados_moeda(ticker, inicio, fim):
    df = yf.download(ticker, start=inicio, end=fim, progress=False)
    return df

if __name__ == "__main__":
    df_dolar = obter_dados_moeda("USDBRL=X", "2023-01-01", "2023-07-01")
    print(df_dolar)
