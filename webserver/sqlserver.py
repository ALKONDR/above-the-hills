import mysql.connector
import json

CATEGORIES_SHOW = 10;

connection_config = {
    'user': 'root',
    'password': '87654321',
    'host': '127.0.0.1',
    'database': 'mts'
}

cnx = mysql.connector.connect(**connection_config)

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
