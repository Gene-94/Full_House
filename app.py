import mysql.connector
from mysql.connector import Error
from flask import Flask
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(app = flask_app)

name_space = app.namespace('api', description='Full House Api')

@name_space.route('/')
class MainClass(Resource):
    def get(self):
        return {
            "status" : "Got new data"
        }
    def post(self):
        return {
            "status" : "Posted new data"
        }


# try:
#     db = mysql.connector.connect(host='localhost',
#                                     database='Shows',
#                                     user='fullhouse',
#                                     password='my_flask_API')
#     if db.is_connected():
#         print('Connected successfully to database')
# except Error as e:
#     print(e)

# cur = db.cursor()
# query = 'select name, id from artists'
# cur.execute(query)
# for (name, id) in cur:
#     print("artist name: {}\nartist id: {}").format(name, id)

# if db is not None and db.is_connected():
#     db.close()    
#connect to existing db

    
#reroute from html templates to swagger endpoints
