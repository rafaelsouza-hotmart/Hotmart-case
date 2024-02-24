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

def find_parent_purchases(csv_file_path):
    df = pd.read_csv(csv_file_path)

    filtered_df = df[df['purchase_parent_id'] == "97-124-26-127-125-126-112-28-116"]

    filtered_df = filtered_df[['purchase_parent_id', 'purchase_installment_number']]

    return filtered_df

def countries_top_sales(csv_file_path):
    print("Loading top sales by country...")
    df = pd.read_csv(csv_file_path)

    #sales
    original_sales = df[df['purchase_parent_id'].isnull()]

    #countries
    country_count = original_sales['user_buyer_country'].value_counts()

    plt.figure(figsize=(12, 6))
    country_count.plot(kind='bar', color='skyblue')
    plt.title('Number of Sales by Country (Original Purchases)')
    plt.xlabel('Country')
    plt.ylabel('Number of Sales')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()


#TODO o count desse carinha não está certo
def countries_top_subs(csv_file_path):
    print("Loading top subscriptions by country...")
    df = pd.read_csv(csv_file_path)

    # subs
    subscriptions = df[df['purchase_parent_id'].notnull()]

    # countries
    country_count = subscriptions['user_buyer_country'].value_counts()

    plt.figure(figsize=(12, 6))
    country_count.plot(kind='bar', color='skyblue')
    plt.title('Number of Subscriptions by Country (Original Purchases)')
    plt.xlabel('Country')
    plt.ylabel('Number of Subscriptions')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def most_used_recurrences(csv_file_path):
    print("Loading recurrences...")
    df = pd.read_csv(csv_file_path)

    recurrence_counts = df['purchase_recurrency_type'].value_counts(dropna=False)

    plt.figure(figsize=(8, 8))
    recurrence_counts.plot(kind='pie', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'],
                           autopct='%1.1f%%')
    plt.title('Recurrency Analysis')
    plt.ylabel('')  # Remove the y-label
    plt.tight_layout()

    plt.show()

def top_payment_methods(csv_file_path):
    print("Loading most used payment methods...")
    df = pd.read_csv(csv_file_path)

    payment_methods = df['purchase_payment_method'].value_counts()

    plt.figure(figsize=(12, 6))
    payment_methods.plot(kind='bar', color='purple')
    plt.title('Top Payment Methods Analysis')
    plt.xlabel('Payment Methods Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def top_niches(csv_file_path):
    print("Loading niches...")
    df = pd.read_csv(csv_file_path)

    niches = df['product_niche'].value_counts()

    plt.figure(figsize=(12, 6))
    niches.plot(kind='barh', color='purple')
    plt.title('Niche Analysis')
    plt.xlabel('Niche Type')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()