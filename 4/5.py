import pandas as pd

# Read the CSV file
data = pd.read_csv('your_file.csv')

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
