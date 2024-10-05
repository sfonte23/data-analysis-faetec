import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo abreviação (ticker)
ticker = ["BRL=X", "CAD=X", "CHF=X", "GBPUSD=X"]

# Obtendo dados
df_cambio = yf.download(ticker, start="2023-01-01", end="2023-04-01", progress=False)

# Renomeando colunas
df_cambio.columns = ["BRL", "CAD", "CHF", "GBP"]

# Calculando volatilidade: Desvio-padrão
volatilidade = df_cambio.std()
print(f'Volatilidade:\n{volatilidade}')

# Criando o gráfico
df_cambio.plot()
plt.title('Câmbio')
plt.xlabel('Data')
plt.ylabel('Valor (moeda corrente)')
plt.show()
