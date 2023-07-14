import pandas as pd

# Read the Excel file
data = pd.read_excel('CENIKI_B2B_VELEPRODAJA.xls')

# Convert the data to an HTML table
html_table = data.to_html(index=False, classes='table table-striped', border=0)

# Add "sortable" class to the first row's <th> tags
html_table = html_table.replace('<th>', '<th class="sortable">')

# Create a basic HTML file with the table
html_content = f'''
<html>
<head>
    <script src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
    <script>
        $(document).ready(function() {{
            $('#myTable').DataTable();
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
with open('output.html', 'w') as file:
    file.write(html_content)
