import mysql.connector
from mysql.connector import Error


def connect():
    """connect to existing dummy database"""

    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                     database='Shows',
                                     user='fullhouse',
                                     password='my_flask_API')
        if conn.is_connected():
            print('Connected successfully to database')
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
#connect to existing db

    
#reroute from html templates to swagger endpoints
