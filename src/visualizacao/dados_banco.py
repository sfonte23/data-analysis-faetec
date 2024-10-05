import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo abreviação (ticker)
bancos_tickers = ["ITUB4.SA", "BBDC4.SA", "SANB11.SA"]

# Obtendo dados
df_bancos = yf.download(bancos_tickers, start="2023-01-01", end="2023-08-01")

# Criando gráfico
df_bancos['Adj Close'].plot(title='Valores de fechamento dos Bancos')
plt.xlabel('Data')
plt.ylabel('Valor (R$)')
plt.show()
