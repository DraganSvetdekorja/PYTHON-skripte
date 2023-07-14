from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        return f"Hello, {name}!"
    
    # Render the HTML template
    return render_template_string('''
        <html>
        <head>
            <title>My Flask App</title>
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
            <script>
                $(document).ready(function() {
                    // Your jQuery code here
                });
            </script>
        </head>
        <body>
            <h1>Welcome to my Flask App!</h1>
            <form method="POST" action="/">
                <input type="text" name="name" placeholder="Enter your name">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run()
