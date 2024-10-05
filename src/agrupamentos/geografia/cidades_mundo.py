# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Coletando dados de cidades (exemplo fictício)
data = {
    'Cidade': ['Nova Iorque', 'Londres', 'Tóquio', 'São Paulo', 'Paris'],
    'Populacao': [8419600, 8982000, 13929286, 12176866, 2148327],
    'PIB': [1700000, 600000, 2000000, 300000, 700000]  # em bilhões
}

df = pd.DataFrame(data)

# Normalizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['Populacao', 'PIB']])

# Aplicando K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(df_scaled)
df['Cluster'] = kmeans.labels_

# Visualizando os resultados
plt.scatter(df['Populacao'], df['PIB'], c=df['Cluster'])
plt.xlabel('População')
plt.ylabel('PIB')
plt.title('Clusters de Cidades do Mundo')
plt.show()

# Interpretação dos resultados
print(df)
