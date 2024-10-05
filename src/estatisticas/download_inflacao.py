import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# Definindo códigos de inflação
codigo_fred = ['FPCPITOTLZGBRA', 'FPCPITOTLZGRUS', 'FPCPITOTLZGIND', 'FPCPITOTLZGCHN', 'FPCPITOTLZGZAF']

# Definindo data
inicio = datetime.datetime(2000, 1, 1)
fim = datetime.datetime(2021, 1, 1)

# Obtendo dados
df_fred = web.DataReader(codigo_fred, 'fred', inicio, fim)
df_fred.columns = ['Brasil', 'Russia', 'Índia', 'China', 'África do Sul']

# Visualizando resultado
print(df_fred)

# Calculando volatilidade
volatilidade_BRICS = df_fred.std()
print(f'Volatilidade BRICS:\n{volatilidade_BRICS}')

# Criando o gráfico
df_fred.plot()
plt.title('Inflação no BRICS')
plt.xlabel('Data')
plt.ylabel('%')
plt.show()
