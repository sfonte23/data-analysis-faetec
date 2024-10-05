# Importando bibliotecas necessárias
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Criando um DataFrame com coordenadas fictícias das capitais
data = {
    'Regiao': ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'],
    'Latitude': [-3.71722, -5.42801, -15.60161, -23.5505, -29.16867],
    'Longitude': [-60.5775, -37.40199, -56.09679, -46.63333, -51.93324]
}

df = pd.DataFrame(data)

# Convertendo para GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

# Visualizando o mapa
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(10, 10))
gdf.plot(ax=ax, color='red')

plt.title('Capitais do Brasil')
plt.show()

# Aplicando K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(gdf[['Latitude', 'Longitude']])
gdf['Cluster'] = kmeans.labels_

# Visualizando os resultados no mapa
ax = world.plot(figsize=(10, 10))
gdf.plot(column='Cluster', ax=ax, legend=True)

plt.title('Clusters de Regiões do Brasil')
plt.show()
