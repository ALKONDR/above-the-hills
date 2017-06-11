from flask import Flask, send_from_directory
import sqlserver as mysql

app = Flask(__name__)

@app.route('/')
@app.route('/api/')
def send_index():
    return send_static('index.html')

@app.route('/api/categories/<string:name>')
def categories(name):
	return mysql.categories(name)

@app.route('/api/<path:path>')
def send_rest(path):
    return "NotImplemented"

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory(directory='./static/', filename=path)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080)
