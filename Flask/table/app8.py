from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
picture_folder = "Slike"  # Update with the actual path to your picture folder

@app.route('/', methods=['GET', 'POST'])
def index():

	table_data = [
		{'sifra': 'apple', 'img_url':'images/apple.jpg', 'price':4},
		{'sifra': 'orange', 'img_url':'images/orange.jpeg', 'price':5},
		{'sifra': 'pear', 'img_url':'images/pear.jpeg', 'price':6},
	]



    # if request.method == 'POST':
        # # Get the uploaded file
        # file = request.files['file']
        
        # # Check if file is selected
        # if file.filename == '':
            # return render_template('index.html', error='No file selected')
        
        # # Read the file based on the file extension
        # if file.filename.endswith('.csv'):
            # df = pd.read_csv(file)
        # elif file.filename.endswith(('.xls', '.xlsx')):
            # df = pd.read_excel(file)
        # else:
            # return render_template('index.html', error='Invalid file format')
        
        # # Get the table name from the first row
        #table_name = "ldkdld"
		
		

        
        # # Check if the 'Image' column exists
        # if 'sifra' in df.columns:
            # # Add the picture path to the 'Image' column values
            # df['Image'] = df['Image'].apply(lambda x: os.path.join(picture_folder, x) if pd.notnull(x) else 'sssss')
        
        # Render the table view template with the data
        #return render_template('table_3.html', table_name=table_name, table_data=df.to_html(index=False))
	return render_template('table_3.html', table_data=table_data)    
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
