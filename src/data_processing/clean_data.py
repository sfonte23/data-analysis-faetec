import pandas as pd

def clean_data(df):
    return df.dropna()

if __name__ == "__main__":
    # Exemplo de uso
    df = pd.read_csv('data/raw/sample_data.csv')
    cleaned_df = clean_data(df)
    print(cleaned_df)
