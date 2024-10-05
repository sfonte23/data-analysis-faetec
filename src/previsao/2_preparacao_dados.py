import pandas as pd

def preparar_dados(df, periodo):
    df_treino = df.iloc[:-periodo]
    df_teste = df.iloc[-periodo:]
    return df_treino, df_teste

if __name__ == "__main__":
    import 1_dados_obter  # Certifique-se de que o arquivo 1_dados_obter.py está no mesmo diretório
    df_dolar = 1_dados_obter.obter_dados_moeda("USDBRL=X", "2023-01-01", "2023-07-01")
    periodo = 1
    df_treino, df_teste = preparar_dados(df_dolar, periodo)
