from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form['data']
    # Implement your data processing logic here
    # ...

    return 'Data processing complete'

if __name__ == '__main__':
    app.run(port=8080)