import pandas as pd
import matplotlib.pyplot as plt

def previsao_media_movel(df_treino, df_teste):
    # Iniciando um DataFrame vazio para previsão de treino
    previsao_treino_mm = pd.DataFrame(index=df_treino.index)
    previsao_treino_mm['prev'] = df_treino['Adj Close'].rolling(5).mean()

    # Iniciando um DataFrame vazio para previsão de teste
    previsao_teste_mm = pd.DataFrame(index=df_teste.index)
    previsao_teste_mm['prev'] = df_treino['Adj Close'].tail(5).mean()

    return previsao_treino_mm, previsao_teste_mm

def plot_previsao(df_treino, df_teste, previsao_treino_mm, previsao_teste_mm):
    plt.plot(df_treino.index.to_numpy(), df_treino['Adj Close'], '.-', color='tab:grey', label='Dados de treino')
    plt.plot(df_teste.index.to_numpy(), df_teste['Adj Close'], '.-', color='black', label='Dados de teste')
    plt.plot(previsao_treino_mm.index.to_numpy(), previsao_treino_mm['prev'], '--', color='tab:blue', label='Previsão (treino)')
    plt.plot(previsao_teste_mm.index.to_numpy(), previsao_teste_mm['prev'], 'x', color='tab:blue', label='Previsão (teste)', linewidth=2.0)

    plt.title('Previsão: Preço do Dólar')
    plt.xlabel('Data')
    plt.ylabel('Valor (R$)')
    plt.legend(loc='lower left')
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    import 2_preparacao_dados
    df_dolar = 1_dados_obter.obter_dados_moeda("USDBRL=X", "2023-01-01", "2023-07-01")
    df_treino, df_teste = 2_preparacao_dados.preparar_dados(df_dolar, 1)
    previsao_treino_mm, previsao_teste_mm = previsao_media_movel(df_treino, df_teste)
    plot_previsao(df_treino, df_teste, previsao_treino_mm, previsao_teste_mm)
