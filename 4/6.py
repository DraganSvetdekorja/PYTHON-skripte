import pandas as pd
import os
import xlrd
# Read the Excel file
#data = pd.read_excel('CENIKI_B2B_VELEPRODAJA.xls')

#wb = xlrd.open_workbook('CENIKI_B2B_VELEPRODAJA.xls', logfile=open(devnull, 'w'))
#data = pd.read_excel(data, engine='xlrd')

wb = xlrd.open_workbook('CENIKI_B2B_VELEPRODAJA.xls', logfile=open(os.devnull, 'w'))
data = pd.read_excel(wb, dtype=str, usecols=None, skiprows=0, engine='xlrd')

# Convert the data to an HTML table
html_table = data.to_html(index=False)

# Create a basic HTML file with the table
html_content = f'''
<html>
<head>
    <script src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready(function() {{
            $('#myTable').DataTable();
        }});
    </script>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
</head>
<body>
    <table id="myTable">
        {html_table}
    </table>
</body>
</html>
'''

# Save the HTML content to a file
with open('output.html', 'w') as file:
    file.write(html_content)
