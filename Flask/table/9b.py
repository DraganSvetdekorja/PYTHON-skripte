import pandas as pd

def get_products(file_path):
    # Read the file using pandas
    #df = pd.read_csv(file_path)  # For CSV files
    df = pd.read_excel(file_path)  # For Excel files

    # Calculate products for each column
    column_products = df.prod()

    # Calculate products for each row
    row_products = df.prod(axis=1)

    # Print the output
    print("Column Products:")
    print(column_products)
    print("\nRow Products:")
    print(row_products)

# Specify the file path here
file_path = "Slike_predprazniki4.xlsx"  # Replace with the actual file path

# Call the function to get products
get_products(file_path)
