import mysql.connector
from mysql.connector import Error


try:
    db = mysql.connector.connect(host='localhost',
                                    database='Shows',
                                    user='fullhouse',
                                    password='my_flask_API')
    if db.is_connected():
        print('Connected successfully to database')
except Error as e:
    print(e)

cur = db.cursor()
query = 'select name, id from artists'
cur.execute(query)
for (name, id) in cur:
    print("artist name: {}\nartist id: {}").format(name, id)

if db is not None and db.is_connected():
    db.close()    
#connect to existing db

    
#reroute from html templates to swagger endpoints
