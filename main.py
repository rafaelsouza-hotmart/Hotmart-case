from graphs import product_type_graph

if __name__ == '__main__':
    csv_file_path = '/Users/rafael.souza/Desktop/case dados/drive-download-20240220T202251Z-001/Purchases.csv'

    print("Available graphs")
    print("1 - Product type \n2 - Sale Amount")

    graph_chosen = input("What graph would you like to see: ")

    if graph_chosen == "1":
        product_type_graph(csv_file_path)


