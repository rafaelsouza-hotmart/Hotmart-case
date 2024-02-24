import pandas as pd

csv_file_path = '/Users/rafael.souza/Desktop/case dados/drive-download-20240220T202251Z-001/Purchases.csv'
df = pd.read_csv(csv_file_path)
query_result2 = df['product_format'].head(10)

if __name__ == '__main__':
    print(query_result2)


