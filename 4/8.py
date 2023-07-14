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
html_table = data.to_html(index=False, classes='table table-striped', border=0)

# Create a basic HTML file with the table
html_content = f'''
<html>
<head>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.min.css">
    <script>
        $(document).ready(function() {{
            $('#myTable').DataTable({{
                "order": [[0, "asc"]],
                "search": {{
                    "smart": true
                }}
            }});
        }});
    </script>
</head>
<body>
    <table id="myTable" class="display">
        <thead>
            <tr>
                {"".join(f"<th>{col}</th>" for col in data.columns)}
            </tr>
        </thead>
        <tbody>
            {"".join(f"<tr>{"".join(f'<td>{str(cell)}</td>' for cell in row)}</tr>" for _, row in data.iterrows())}
        </tbody>
    </table>
</body>
</html>
'''

# Save the HTML content to a file
with open('output3.html', 'w') as file:
    file.write(html_content)