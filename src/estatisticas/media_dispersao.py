import pandas as pd

# Dados fictícios
dados = pd.Series([8, 6, 5, 7, 3, 2])

# Calculando a variância
print(f'Variância: {dados.var()}')

# Calculando o desvio-padrão
print(f'Desvio-padrão: {dados.std()}')
