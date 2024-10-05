# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Coletando dados de fundos de investimento (exemplo fictício)
data = {
    'Fundo': ['Fundo A', 'Fundo B', 'Fundo C', 'Fundo D'],
    'Retorno': [0.08, 0.10, 0.06, 0.12],  # Retorno anual
    'Risco': [0.15, 0.20, 0.10, 0.25]    # Desvio padrão dos retornos
}

df = pd.DataFrame(data)

# Normalizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['Retorno', 'Risco']])

# Aplicando K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(df_scaled)
df['Cluster'] = kmeans.labels_

# Visualizando os resultados
plt.scatter(df['Retorno'], df['Risco'], c=df['Cluster'])
plt.xlabel('Retorno Anual')
plt.ylabel('Risco (Desvio Padrão)')
plt.title('Clusters de Fundos de Investimento')
plt.show()

# Interpretação dos resultados
print(df)
