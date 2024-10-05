import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definindo abreviação (ticker)
ticker = ["BBAS3.SA", "BBDC4.SA", "ITUB4.SA"]

# Obtendo dados
df_acao = yf.download(ticker, start="2014-01-01", end="2023-04-01", progress=False)
df_acao = df_acao.iloc[:, [0, 1, 2]]
df_acao.columns = ticker

# Calculando a média móvel de 5 períodos
media_movel = pd.DataFrame()
media_movel['BBAS3.SA_MM'] = df_acao['BBAS3.SA'].rolling(5).mean()
media_movel['BBDC4.SA_MM'] = df_acao['BBDC4.SA'].rolling(5).mean()
media_movel['ITUB4.SA_MM'] = df_acao['ITUB4.SA'].rolling(5).mean()

# Criando o gráfico
df_acao.plot()
plt.title('Valores de fechamento: 2014/T1 a 2023/T1')
plt.xlabel('Data')
plt.ylabel('Valor (R$)')

# Adicionando as médias móveis
for col in media_movel.columns:
    plt.plot(media_movel.index, media_movel[col], linestyle='dashed')

plt.show()

# Recuperando o último valor e previsão
previsao_mm = df_acao['BBAS3.SA'].tail(5).mean()
print(f'BBAS3.SA | Previsão para o próximo dia útil: R${round(previsao_mm, 2)}')
