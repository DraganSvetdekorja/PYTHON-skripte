import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('Slike_predprazniki3.xlsx')

# Define the row and value you want to check
row_index = 2  # For example, checking the third row (index starts at 0)
value_to_check = 'AIRLAID-278'  # Replace with the value you're looking for

# Check if the value exists in the specified row
if value_to_check in df.iloc[row_index]:
    print(f"The value '{value_to_check}' is present in row {row_index + 1}.")
else:
    print(f"The value '{value_to_check}' is not found in row {row_index + 1}.")
