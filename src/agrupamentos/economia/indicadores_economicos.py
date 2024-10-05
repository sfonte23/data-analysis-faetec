# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Coletando dados do Banco Mundial (substitua com seu arquivo ou API)
# Exemplo: Dados fictícios para PIB e Taxa de Desemprego
data = {
    'Pais': ['Brasil', 'Argentina', 'Chile', 'Colômbia', 'Peru'],
    'PIB_per_capita': [9000, 10000, 15000, 12000, 11000],
    'Taxa_de_Desemprego': [12, 9, 7, 10, 8]
}

df = pd.DataFrame(data)

# Visualizando os dados
plt.scatter(df['PIB_per_capita'], df['Taxa_de_Desemprego'])
plt.xlabel('PIB per Capita')
plt.ylabel('Taxa de Desemprego')
plt.title('Distribuição do PIB per Capita e Taxa de Desemprego')
plt.show()

# Normalizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['PIB_per_capita', 'Taxa_de_Desemprego']])

# Aplicando K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(df_scaled)
df['Cluster'] = kmeans.labels_

# Visualizando os resultados
plt.scatter(df['PIB_per_capita'], df['Taxa_de_Desemprego'], c=df['Cluster'])
plt.xlabel('PIB per Capita')
plt.ylabel('Taxa de Desemprego')
plt.title('Clusters de Países')
plt.show()

# Interpretação dos resultados
print(df)
