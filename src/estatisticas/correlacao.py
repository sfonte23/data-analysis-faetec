import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo abreviação (ticker)
ticker = ["BRL=X", "CAD=X", "CHF=X", "GBPUSD=X"]

# Obtendo dados
df_cambio = yf.download(ticker, start="2023-01-01", end="2023-04-01", progress=False)

# Matriz de correlação
correlacao = df_cambio.corr()
print(f'Matriz de correlação:\n{correlacao}')

# Criando o gráfico
pd.plotting.scatter_matrix(df_cambio)
plt.show()
