# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Coletando dados de setores econômicos (exemplo fictício)
data = {
    'Setor': ['Agronegócio', 'Indústria', 'Serviços', 'Comércio'],
    'Produtividade': [150, 200, 300, 100],
    'Crescimento': [5, 3, 7, 4]
}

df = pd.DataFrame(data)

# Normalizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['Produtividade', 'Crescimento']])

# Aplicando K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(df_scaled)
df['Cluster'] = kmeans.labels_

# Visualizando os resultados
plt.scatter(df['Produtividade'], df['Crescimento'], c=df['Cluster'])
plt.xlabel('Produtividade')
plt.ylabel('Crescimento')
plt.title('Clusters de Setores Econômicos')
plt.show()

# Interpretação dos resultados
print(df)
