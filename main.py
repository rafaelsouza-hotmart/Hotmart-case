import pandas as pd
import matplotlib.pyplot as plt


csv_file_path = '/Users/rafael.souza/Desktop/case dados/drive-download-20240220T202251Z-001/Purchases.csv'
df = pd.read_csv(csv_file_path)
query_result2 = df['product_format'].head(10)
count = df['product_format'].value_counts()

plt.figure(figsize=(10, 6))
count.plot(kind='bar', color='skyblue')
plt.title('Contagem de cada tipo de formato de produto')
plt.xlabel('Formato do Produto')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

tipo_grafico = input("Qual tipo de gráfico você gostaria de criar? (barras/novo): ")


if __name__ == '__main__':
    # print(query_result2)
    print(count)
    plt.show()


