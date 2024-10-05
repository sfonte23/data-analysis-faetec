import pandas as pd

# Dados fictícios
dados = pd.Series([8, 6, 5, 7, 3, 2])

# Calculando a média manualmente
media = dados.sum() / len(dados)
print(f'Média: {media}')

# Calculando a média usando pandas
print(f'Média com Pandas: {dados.mean()}')
