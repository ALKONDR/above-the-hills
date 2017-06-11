from datetime import datetime
import mysql.connector.errors
import mysql.connector
import urllib.request
import urllib.error
import urllib.parse
import codecs
import json

BALANCE_ON_START = '0'

connection_config = {
    'user': 'root',
    'password': '87654321',
    'host': '127.0.0.1',
    'database': 'mts'
}

cnx = mysql.connector.connect(**connection_config)

def vk_recv_name(ans):
    try:
        url = 'https://api.vk.com/method/users.get?user_ids=' + ans['user_id'] + '&fields=bdate&v=5.65'
        resp = urllib.request.urlopen(url)
    except urllib.error.HTTPError as error:
        print("Can't get JSON, check user_id")
        return
        
    string = resp.read().decode('utf8')
    answer = json.loads(string)
    if 'response' in answer:
        name = answer['response'][0]['first_name']
        surname = answer['response'][0]['last_name']
        print(name + ' ' + surname)
    else:
        name = ''
        surname = ''
    
    return {
        'name': name,
        'surname': surname
    }

def db_register(code, ans):
	print('db_register() call')
	names = vk_recv_name(ans)
	names = {'name':'Ivan', 'surname':''}

	if names is None:
		print ('db_register(): Cannot receive name from VK')
		return False

	cursor = cnx.cursor()
	query = 'INSERT INTO users (id, name, surname, balance, access_token, secret, token_expires) VALUES ('+str(ans['user_id'])+', "'+names['name']+'", "'+names['surname']+'", '+BALANCE_ON_START+', "'+str(ans['access_token'])+'", "'+code+'", DATE_ADD(NOW(), INTERVAL '+str(ans['expires_in'])+' SECOND));'

	print('db_register(): query is')
	print(query)

	try:
		cursor.execute(query)
		print('db_register(): executed')
		# TODO: Unsuccessful commit?
		cnx.commit()
		cursor.close()
	except mysql.connector.errors.DatabaseError as err:
		print(err.code)
		return False
	print('db_register() ret True')
	return True


def db_usr_update(code, ans):
	print('db_usr_update() call')
	cursor = cnx.cursor()
	query = 'UPDATE users SET access_token = "'+str(ans['access_token'])+'", secret = "'+code+'", token_expires = DATE_ADD(NOW(), INTERVAL '+str(ans['expires_in'])+' SECOND) WHERE id = '+str(ans['user_id'])+';'
	
	print('db_user_update(): Update query is')
	print(query)

	cursor.execute(query)
	# TODO: Unsuccessful execute\commit?
	cnx.commit()
	cursor.close()
	return True


def db_auth_sync(code, ans):
	print("db_auth_sync() call")
	cursor = cnx.cursor()
	print("db_auth_sync(): cursor obtained")

	query = 'SELECT COUNT(*) AS cnt FROM users WHERE id = ' + str(ans['user_id']) + ';'
	print("db_auth_sync(): query:")
	print(query)

	cursor.execute(query)

	row = cursor.fetchone()

	if row is not None:
		cnt = row[0]
		print('db_auth_sync(): count: ' + str(cnt))
	else:
		cnt = 0
		print('db_auth_sync(): row is None then db_register()')

	print('db_auth_sync(): count: ' + str(cnt))

	cursor.close()

	if cnt == 0:
		return db_register(code, ans)
	else:
		return db_usr_update(code, ans)


def authorize(code):
	data = {}
	data['client_id'] = '6069231'
	data['client_secret'] = 'FhCnyYZ6LGtJXkslgiky'
	data['redirect_uri'] = 'membrain.ru'
	data['code'] = code
	url_values = urllib.parse.urlencode(data)
	url = 'https://oauth.vk.com/access_token'
	full_url = url + '?' + url_values

	try:
		print('authorize(): VK URL: ' + full_url)
		resp = urllib.request.urlopen(full_url)
	except urllib.error.HTTPError as error:
		print('authorize(): Could not load ' + url)
		print(error.code)
		return False

	string = resp.read().decode('utf8')
	print('authorize(): Server response..')
	print(string)
	answer = json.loads(string)

	try:
		if answer is not None and answer['access_token'] is not None:
			if db_auth_sync(code, answer):
				if 'user_id' in answer:
					return answer['user_id']
			return None
	except TypeError:
		return None


def verify(code, id=0):
	cursor = cnx.cursor()
	query = "SELECT id, token_expires FROM users WHERE secret = '" + code + "';"

	cursor.execute(query)
	for elem in cursor:
		idx = elem[0]
		exp = elem[1]
		if datetime.now() < exp and (idx == id or id == 0):
			cursor.close()
			return True

	cursor.close()
	return False
