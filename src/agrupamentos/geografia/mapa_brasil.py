# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Criando um DataFrame com dados fictícios das regiões do Brasil
data = {
    'Regiao': ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'],
    'PIB_per_capita': [15000, 10000, 20000, 30000, 25000],  # PIB per capita em R$
    'Taxa_de_Alfabetizacao': [85, 80, 95, 98, 93]  # Taxa de alfabetização em porcentagem
}

df = pd.DataFrame(data)

# Visualizando os dados
print(df)

# Normalizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['PIB_per_capita', 'Taxa_de_Alfabetizacao']])

# Aplicando K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df_scaled)
df['Cluster'] = kmeans.labels_

# Visualizando os resultados
plt.figure(figsize=(10, 6))
plt.scatter(df['PIB_per_capita'], df['Taxa_de_Alfabetizacao'], c=df['Cluster'], cmap='viridis', s=100)
plt.xlabel('PIB per Capita (R$)')
plt.ylabel('Taxa de Alfabetização (%)')
plt.title('Agrupamento de Regiões do Brasil')
plt.xticks(rotation=45)
for i in range(df.shape[0]):
    plt.annotate(df['Regiao'][i], (df['PIB_per_capita'][i], df['Taxa_de_Alfabetizacao'][i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.grid()
plt.show()

# Interpretação dos resultados
print(df)
