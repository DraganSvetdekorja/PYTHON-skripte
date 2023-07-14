import pandas as pd

def read_products_from_csv(file_path):
    try:
        df = pd.read_csv(file_path)  # Read CSV file
        products = df["Product"].tolist()  # Get the 'Product' column as a list
        return products
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def read_products_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)  # Read Excel file
        products = df["sifra"].tolist()  # Get the 'Product' column as a list
        return products
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

# # Example usage
# file_path = "products.csv"  # Replace with your CSV file path
# products = read_products_from_csv(file_path)
# if products:
    # print(products)

file_path = "Slike_predprazniki4.xlsx"  # Replace with your Excel file path
products = read_products_from_excel(file_path)
if products:
    print(products)
