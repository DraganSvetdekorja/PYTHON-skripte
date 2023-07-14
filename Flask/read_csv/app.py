import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'xls', 'xlsx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def read_product_data(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.csv':
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    return df


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            df = read_product_data(file_path)
            return render_template('index.html', products=df.to_dict('records'))

    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
