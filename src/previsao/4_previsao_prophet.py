from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

def ajustar_prophet(df):
    df = df.reset_index()
    df = df[['Date', 'Adj Close']]
    df.columns = ['ds', 'y']
    return df

def prever_prophet(df_treino, df_teste):
    modelo = Prophet()
    modelo.fit(df_treino)

    previsoes_treino = modelo.predict(df_treino)
    previsoes_teste = modelo.predict(df_teste)

    return previsoes_treino, previsoes_teste

def plot_prophet(df_treino, df_teste, previsoes_treino, previsoes_teste):
    plt.plot(df_treino['ds'], df_treino['y'], '.-', color='tab:grey', label='Dados de treino')
    plt.plot(df_teste['ds'], df_teste['y'], '.-', color='black', label='Dados de teste')
    plt.plot(df_treino['ds'], previsoes_treino['yhat'], '--', color='tab:blue', label='Previsão (treino)')
    plt.plot(df_teste['ds'], previsoes_teste['yhat'], color='tab:blue', label='Previsão (teste)', linewidth=2.0)

    plt.fill_between(df_teste['ds'], previsoes_teste['yhat_lower'], previsoes_teste['yhat_upper'],
                     color='tab:blue', alpha=0.25, label='Incerteza')

    plt.title('Previsão: Preço do Dólar com Prophet')
    plt.xlabel('Data')
    plt.ylabel('Valor (R$)')
    plt.legend(loc='lower left')
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    import 2_preparacao_dados
    df_dolar = 1_dados_obter.obter_dados_moeda("USDBRL=X", "2023-01-01", "2023-07-01")
    df_treino, df_teste = 2_preparacao_dados.preparar_dados(df_dolar, 30)
    df_treino_prophet = ajustar_prophet(df_treino)
    df_teste_prophet = ajustar_prophet(df_teste)
    previsoes_treino, previsoes_teste = prever_prophet(df_treino_prophet, df_teste_prophet)
    plot_prophet(df_treino_prophet, df_teste_prophet, previsoes_treino, previsoes_teste)
