import matplotlib.pyplot as plt

def visualize_data(df):
    df.plot()
    plt.show()

if __name__ == "__main__":
    # Exemplo de uso
    df = pd.read_csv('data/processed/cleaned_data.csv')
    visualize_data(df)
