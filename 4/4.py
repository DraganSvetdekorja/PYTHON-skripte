import pandas as pd

# Read the CSV file
data = pd.read_csv('your_file.csv')

# Convert the data to an HTML table
html_table = data.to_html(index=False, classes='table', na_rep='')

# Add sorting and filtering functionality to the table
html = '''
<html>
<head>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.min.js"></script>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.min.css">
    <script>
        $(document).ready(function() {
            // Initialize the DataTable
            var table = $('#myTable').DataTable();

            // Add column filtering
            $('#myTable tfoot th').each(function() {
                var title = $(this).text();
                $(this).html('<input type="text" placeholder="Search ' + title + '" />');
            });

            // Apply column filtering
            table.columns().every(function() {
                var that = this;

                $('input', this.footer()).on('keyup change', function() {
                    if (that.search() !== this.value) {
                        that.search(this.value).draw();
                    }
                });
            });
        });
    </script>
</head>
<body>
    <table id="myTable" class="display">
        <thead>
            <tr>'''

# Add column headers to the HTML table
for column in data.columns:
    html += f'<th>{column}</th>'

html += '''
            </tr>
        </thead>
        <tfoot>
            <tr>'''

# Add footer for column filtering
for _ in data.columns:
    html += '<th></th>'

html += '''
            </tr>
        </tfoot>
        <tbody>'''

# Add table data to the HTML table
for _, row in data.iterrows():
    html += '<tr>'
    for value in row:
        html += f'<td>{value}</td>'
    html += '</tr>'

html += '''
        </tbody>
    </table>
</body>
</html>'''

# Write the HTML table to a file
with open('output.html', 'w') as file:
    file.write(html)
