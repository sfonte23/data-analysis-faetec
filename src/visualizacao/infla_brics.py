import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

# Definindo códigos para inflação
codigo_fred = ['FPCPITOTLZGBRA', 'FPCPITOTLZGRUS', 'FPCPITOTLZGIND', 'FPCPITOTLZGCHN', 'FPCPITOTLZGZAF']
inicio = datetime.datetime(2017, 1, 1)
fim = datetime.datetime(2021, 1, 1)

# Obtendo dados
df_fred = web.DataReader(codigo_fred, 'fred', inicio, fim)

# Criando gráfico
df_fred.plot.bar(rot=0, edgecolor='black', grid=False)
plt.title('Inflação (BRICS)')
plt.xlabel('Ano')
plt.ylabel('Percentual (%)')
plt.show()
