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
        
        # Render the table view template with the data
        return render_template('table.html', table_name=table_name, data=df.to_html(index=False))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
