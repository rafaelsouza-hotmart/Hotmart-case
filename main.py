import pandas as pd
import matplotlib.pyplot as plt

print("Available graphs")
print("1 - Product type \n2 - Sale Amount")
tipo_grafico = input("What graph would you like to see: ")

csv_file_path = '/Users/rafael.souza/Desktop/case dados/drive-download-20240220T202251Z-001/Purchases.csv'
df = pd.read_csv(csv_file_path)
query_result2 = df['product_format'].head(10)
count = df['product_format'].value_counts()

plt.figure(figsize=(10, 6))
count.plot(kind='bar', color='orange')
plt.title('Contagem de cada tipo de formato de produto')
plt.xlabel('Formato do Produto')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


# if __name__ == '__main__':
    # print(query_result2)
    # print(count)
    # plt.show()


