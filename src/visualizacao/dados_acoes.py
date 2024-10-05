import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo abreviação (ticker)
acao_ticker = ["PETR4.SA"]  # Petrobras

# Obtendo dados
df_acao = yf.download(acao_ticker, start="2023-01-01", end="2023-08-01")

# Criando gráfico
df_acao['Adj Close'].plot(title='Valores de fechamento da PETR4.SA')
plt.xlabel('Data')
plt.ylabel('Valor (R$)')
plt.show()
