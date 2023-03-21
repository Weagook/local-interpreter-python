from flask import Flask, render_template, url_for, request
import requests
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', filename=url_for('static', filename='style.css'), script=url_for('static', filename='app.js'))

@app.route("/api/compile-code/", methods=['POST'])
def compile_code():
    if request.method == 'POST':
        params = request.json
        with open('test_file.py', 'w', encoding='utf-8') as file:
            file.write(params['code'])
        os.system('python test_file.py > output.txt')
        with open('output.txt', 'r') as file:
            return file.read()
    return 'Error'

if __name__ == "__main__":
    app.run(debug=True)