from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        # Check if file is selected
        if file.filename == '':
            return render_template('index.html', error='No file selected')

        # Read the file based on the file extension
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return render_template('index.html', error='Invalid file format')

        # Get the table name from the first row
        table_name = df.columns[0]

        covert_to_table = df.to_html(index=False, classes='table table-stripped').style.set_table_attributes('data-toggle="table"')
		#styled = df.style.set_table_attributes('data-toggle="table"')


    # Render the table view template with the data
    # return render_template('table.html', table_name=table_name, data=df.to_html(index=False, classes='table table-stripped'))
		return render_template('table.html', table_name=table_name, data=covert_to_table)


	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
