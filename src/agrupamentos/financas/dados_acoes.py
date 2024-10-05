# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import yfinance as yf

# Coletando dados de ações usando a API do Yahoo Finance (exemplo fictício)
# Substitua os códigos das ações conforme necessário
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    data.append({
        'Ticker': ticker,
        'Retorno': hist['Close'].pct_change().mean(),
        'Volume': hist['Volume'].mean()
    })

df = pd.DataFrame(data)

# Normalizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['Retorno', 'Volume']])

# Aplicando K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(df_scaled)
df['Cluster'] = kmeans.labels_

# Visualizando os resultados
plt.scatter(df['Retorno'], df['Volume'], c=df['Cluster'])
plt.xlabel('Retorno Médio')
plt.ylabel('Volume Médio')
plt.title('Clusters de Ações no Mercado')
plt.show()

# Interpretação dos resultados
print(df)
