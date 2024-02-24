import pandas as pd
import matplotlib.pyplot as plt


def product_type_graph(csv_file_path):
    df = pd.read_csv(csv_file_path)

    count = df['product_format'].value_counts()

    plt.figure(figsize=(10, 6))
    count.plot(kind='bar', color='orange')
    plt.title('Contagem de cada tipo de formato de produto')
    plt.xlabel('Formato do Produto')
    plt.ylabel('Contagem')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()