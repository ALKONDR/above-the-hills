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

def categories(name):
    cursor = cnx.cursor()
    query = ('SELECT * FROM meme_category WHERE name = "' + str(name) + '";')
    cursor.execute(query)
    for (id, name, price, pop) in cursor:
        cursor.close()
        cursor = cnx.cursor()

        query = ('SELECT value, DATE_FORMAT(timestamp, "%m-%d-%Y %r") AS date \
         FROM changes \
         WHERE meme_id =' + str(id) + ' \
         ORDER BY timestamp DESC;')

        cursor.execute(query)

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
