from flask import Flask, send_from_directory
import sqlserver as mysql
import authorizer as auth
from flask import request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/api/')
def send_index():
    return send_static('index.html')

@app.route('/api/users/<int:user_id>')
def users(user_id):
	return mysql.users(user_id)

@app.route('/api/categories/')
def all_categories():
	print('all_categories')
	return mysql.all_categories()

@app.route('/api/categories/<string:name>')
def categories(name):
	print('categories: ' + name)
	return mysql.categories(name)

@app.route('/api/login/')
def login():
	code = request.args.get('code')
	ident = auth.authorize(code)
	if ident is not None:
		return json.dumps({
			'code': code,
			'id': ident,
			'status': 'OK'
			})
	else:
		return json.dumps({
			'status' : 'Unauthorized'
			}), 401

#@app.route('/api/user/buy/<int:user_id>')
#def buy(user_id):
#	request.args.get('code')
#	return mysql.buy(user_id, code)

@app.route('/api/<path:path>')
def send_rest(path):
    return "NotImplemented"

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory(directory='./static/', filename=path)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080, threaded=True)
