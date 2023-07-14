from flask import Flask, render_template, request, send_file
import pandas as pd
import openpyxl
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(filename)

            #df = pd.read_csv(filename)  # For CSV files
            df = pd.read_excel(filename)  # For Excel files

            image_urls = df['image_url_column'].tolist()

            return render_template('index.html', data=df.to_html(index=False))

    return render_template('upload.html')

@app.route('/table')
def show_table():
    data = get_data()
    image_urls = get_image_urls()

    data['image_url_column'] = image_urls

    return render_template('table.html', data=data.to_html(index=False))

@app.route('/export', methods=['POST'])
def export_table():
    data = get_data()
    image_urls = get_image_urls()

    data['image_url_column'] = image_urls

    excel_writer = pd.ExcelWriter('exported_table.xlsx', engine='openpyxl')

    data.to_excel(excel_writer, index=False)

    for i, image_url in enumerate(image_urls):
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image_path = f'image_{i}.png'
        image.save(image_path)
        worksheet = excel_writer.sheets['Sheet1']
        worksheet.column_dimensions[f'H{i+2}'].width = 20
        img = openpyxl.drawing.image.Image(image_path)
        img.width = 80
        img.height = 80
        worksheet.add_image(img, f'H{i+2}')

    excel_writer.save()
    excel_writer.close()

    return send_file('exported_table.xlsx', as_attachment=True)

def get_data():
    # Implement logic to retrieve the data
    return data

def get_image_urls():
    # Implement logic to retrieve the image URLs
    return image_urls

if __name__ == '__main__':
    app.run()
