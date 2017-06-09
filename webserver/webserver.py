from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def send_index():
    return send_static('index.html')

@app.route('/<path:path>')
def send_static(path):
    print(path)
    return send_from_directory(directory='./static/', filename=path)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=80)