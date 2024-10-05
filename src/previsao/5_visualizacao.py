import matplotlib.pyplot as plt

def plotar_resultados(df_treino, df_teste, previsao_treino_mm, previsao_teste_mm, previsoes_treino_prophet, previsoes_teste_prophet):
    # Gráficos para média móvel
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(df_treino.index, df_treino['Adj Close'], label='Treino')
    plt.plot(df_teste.index, df_teste['Adj Close'], label='Teste')
    plt.plot(previsao_treino_mm.index, previsao_treino_mm['prev'], label='MM Treino')
    plt.plot(previsao_teste_mm.index, previsao_teste_mm['prev'], label='MM Teste')
    plt.title('Previsão: Média Móvel')
    plt.legend()

    # Gráficos para Prophet
    plt.subplot(1, 2, 2)
    plt.plot(df_treino['ds'], df_treino['y'], label='Treino')
    plt.plot(df_teste['ds'], df_teste['y'], label='Teste')
    plt.plot(df_treino['ds'], previsoes_treino['yhat'], label='Prophet Treino')
    plt.plot(df_teste['ds'], previsoes_teste['yhat'], label='Prophet Teste')
    plt.fill_between(df_teste['ds'], previsoes_teste['yhat_lower'], previsoes_teste['yhat_upper'], alpha=0.2)
    plt.title('Previsão: Prophet')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import 3_previsao_media_movel
    import 4_previsao_prophet

    # Aqui você pode combinar os resultados e chamá-los
