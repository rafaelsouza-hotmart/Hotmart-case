import pandas as pd
import matplotlib.pyplot as plt
import calendar


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


def countries_top_subs(csv_file_path):
    print("Loading top subscriptions by country...")
    df = pd.read_csv(csv_file_path)

    subscriptions = df[df['purchase_recurrency_number'].notnull()]

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

    niche_products = df.groupby('product_niche')['product_id'].nunique()

    plt.figure(figsize=(12, 6))
    niche_products.sort_values(ascending=False).plot(kind='barh', color='purple')
    plt.title('Number of products by niche')
    plt.xlabel('Niche Type')
    plt.ylabel('Products registered')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def top_niches_sales(csv_file_path):
    print("Loading niches and counting sales...")
    df = pd.read_csv(csv_file_path)

    df = df[df['purchase_parent_id'].isnull()]

    sales_by_niche = df.groupby('product_niche')['purchase_id'].nunique()

    plt.figure(figsize=(12, 6))
    sales_by_niche.sort_values(ascending=False).plot(kind='barh', color='orange')
    plt.title('Sales by Niche')
    plt.xlabel('Number of Sales')
    plt.ylabel('Niche Type')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

#vendas de um produtor (mas apenas cocreator & afiliado)


    #afiliados e cocreators
    #produtos em que os afiliados mais lucram
    # mesma coisa para cocreators    #meses tambem

def top_creators(csv_file_path):
    print("Loading creators...")
    df = pd.read_csv(csv_file_path)

    #filter out affiliates, cocreators & subscriptions
    sales = df[(df['purchase_commission_affiliate'].isnull()) &
               (df['purchase_commission_cocreator'].isnull()) &
               (df['purchase_recurrency_number'].isnull())]


    creator_sales = sales['creator_id'].value_counts().head(10)

    creator_sales = creator_sales.sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    creator_sales.plot(kind='barh', color='red')
    plt.title('Top 10 Creators by Sales')
    plt.xlabel('Number of Sales')
    plt.ylabel('Creator ID')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def year_by_year_total_sales(csv_file_path):
    print("Loading yearly sales data...")
    df = pd.read_csv(csv_file_path)

    df['purchase_release_datetime'] = pd.to_datetime(df['purchase_release_datetime'])

    df = df[df['purchase_recurrency_number'].isnull()]

    df['year'] = df['purchase_release_datetime'].dt.year

    sales_by_year = df.groupby('year')['purchase_id'].count()

    plt.figure(figsize=(12, 6))
    sales_by_year.plot(kind='bar', color='skyblue')
    plt.title('Total Sales by Year (Excluding Recurrences)')
    plt.xlabel('Year')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def year_by_year_total_subs(csv_file_path):
    print("Loading yearly subscription data...")
    df = pd.read_csv(csv_file_path)

    df['purchase_release_datetime'] = pd.to_datetime(df['purchase_release_datetime'])

    df = df[df['purchase_recurrency_number'].notnull()]

    df['year'] = df['purchase_release_datetime'].dt.year

    subs_by_year = df.groupby('year')['purchase_id'].count()

    plt.figure(figsize=(12, 6))
    subs_by_year.plot(kind='bar', color='green')
    plt.title('Total Subscriptions by Year')
    plt.xlabel('Year')
    plt.ylabel('Total Subscriptions')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def month_sales_2023(csv_file_path):
    print("Loading monthly sales...")
    df = pd.read_csv(csv_file_path)

    df['purchase_release_datetime'] = pd.to_datetime(df['purchase_release_datetime'])

    df_2023 = df[df['purchase_release_datetime'].dt.year == 2023]

    df_2023 = df_2023[df_2023['purchase_recurrency_number'].isnull()]

    df_2023['month'] = df_2023['purchase_release_datetime'].dt.month.apply(lambda x: calendar.month_name[x])

    sales_by_month = df_2023.groupby('month')['purchase_id'].count()

    months = list(calendar.month_name)[1:]
    sales_by_month = sales_by_month.reindex(months, fill_value=0)

    plt.figure(figsize=(12, 6))
    sales_by_month.plot(kind='bar', color='green')
    plt.title('Total Sales by Month in 2023 (Excluding Recurrences)')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

def month_subscriptions_2023(csv_file_path):
    print("Loading monthly subscriptions...")
    df = pd.read_csv(csv_file_path)

    df['purchase_release_datetime'] = pd.to_datetime(df['purchase_release_datetime'])

    df_2023 = df[df['purchase_release_datetime'].dt.year == 2023]

    df_2023 = df_2023[df_2023['purchase_recurrency_number'].notnull()]

    df_2023['month'] = df_2023['purchase_release_datetime'].dt.month.apply(lambda x: calendar.month_name[x])

    subscriptions_by_month = df_2023.groupby('month')['purchase_id'].count()

    months = list(calendar.month_name)[1:]
    sales_by_month = subscriptions_by_month.reindex(months, fill_value=0)

    plt.figure(figsize=(12, 6))
    sales_by_month.plot(kind='bar', color='green')
    plt.title('Total Subscriptions by Month in 2023')
    plt.xlabel('Month')
    plt.ylabel('Total Subscriptions')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()