from graphs import product_type_graph, find_parent_purchases, countries_top_sales, countries_top_subs, \
    most_used_recurrences, top_payment_methods, top_niches

if __name__ == '__main__':
    csv_file_path = '/Users/rafael.souza/Desktop/case dados/drive-download-20240220T202251Z-001/Purchases.csv'

    while True:
        print("Available graphs")
        print("1 - Product type \n2 - Countries with the most sales"
              "\n3 - Countries with the most subscriptions"
              "\n4 - Most used recurrences"
              "\n5 - Most used  payment methods"
              "\n6 - Top niches"
              "\n0 - Exit")

        graph_chosen = input("What graph would you like to see: ")

        if graph_chosen == "0":
            break

        if graph_chosen == "1":
            product_type_graph(csv_file_path)
        elif graph_chosen == "2":
            countries_top_sales(csv_file_path)
        elif graph_chosen == "3":
            countries_top_subs(csv_file_path)
        elif graph_chosen == "4":
            most_used_recurrences(csv_file_path)
        elif graph_chosen == "5":
            top_payment_methods(csv_file_path)
        elif graph_chosen == "6":
            top_niches(csv_file_path)
        else:
            print("Invalid option.")


