import mysql.connector
import authorizer as auth
import json

CATEGORIES_SHOW = 10;

connection_config = {
    'user': 'root',
    'password': '87654321',
    'host': '127.0.0.1',
    'database': 'mts'
}

cnx = mysql.connector.connect(**connection_config)

def buy(id, code):
    if not auth.verify(id, code):
        return json.dumps({''}), 401

def users(id):
    cursor = cnx.cursor()
    query = 'SELECT * FROM users WHERE id = ' + str(id) + ';'
    cursor.execute(query)

    user_row = None
    for element in cursor:
        user_row = element

    cursor.close()

    cursor = cnx.cursor()
    query = 'SELECT timestamp, round_id, count, price, profit FROM transactions WHERE user_id='+str(id) +';'
    print("users(): query:")
    print(query)

    transactions = []

    cursor.execute(query)
    counter = 0
    for elem in cursor:
        if counter >= 10:
            break
        transactions.append({
            'time': str(elem[0]),
            'round_id': elem[1],
            'count': elem[2],
            'price': elem[3],
            'profit': elem[4] 
            })
        ++counter
    cursor.close()
    if user_row is None:
        return json.dumps({
            'error': 'Not found'
            }), 404
    return json.dumps({
        'id': user_row[0],
        'name': user_row[1],
        'surname': user_row[2],
        'balance': user_row[3],
        'transactions' : transactions
    })

def all_categories():
    cursor = cnx.cursor()
    query = 'SELECT * FROM meme_category'
    cursor.execute(query)

    elems = []
    result = []
    
    for elem in cursor:
        elems.append(elem)
        
    cursor.close()
    print(json.dumps(elems))

    for elem in elems:
        print(elem)
            
        c = cnx.cursor()
        q = 'SELECT difference FROM changes WHERE meme_id = ' + str(elem[0]) + ' ORDER BY timestamp DESC;'
        print("all_categories(): query:")
        print(q)
        c.execute(q)
        diffval = c.fetchone()

        if diffval is None:
            diffval = [0]
            
        result.append({
            "id": elem[0],
            "name": elem[1],
            "price": elem[2],
            "popularity": elem[3],
            "diff": diffval[0]
        })
        c.close()
    return json.dumps(result)
    cursor.close()


def categories(name):
    if name == "":
        return all_categories()
    cursor = cnx.cursor()
    print("recv cursor")
    query = ('SELECT * FROM meme_category WHERE name = "' + str(name) + '";')
    cursor.execute(query)
    print("executed query")
    for (id, name, price, pop) in cursor:
        cursor.close()
        cursor = cnx.cursor()

        query = ('SELECT value, DATE_FORMAT(timestamp, "%m-%d-%Y %r") AS date \
         FROM changes \
         WHERE meme_id =' + str(id) + ' \
         ORDER BY timestamp DESC;')

        cursor.execute(query)
        print("executed query 2")

        i = 0
        values = []
        for (val, date) in cursor:
            if i >= CATEGORIES_SHOW:
                break
            values.append({
                "date" : date,
                "value" : val
                });
        cursor.close()

        return json.dumps({
            "id" : id,
            "name" : name,
            "points" : values,
            "price" : price,
            "popularity" : pop
        })

    cursor.close()
    return json.dumps({"error" : "Bad request"}), 400
