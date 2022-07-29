# import mysql.connector
# from mysql.connector import Error
from flask import Flask, request
# from flask_restplus import Api, Resource

app = Flask(__name__)

@app.route('/api/shows', methods=['POST', 'GET'])
def shows():
    if request.method == 'GET':
        return {
            'message' : 'This endpoint should be a list of shows',
            'method' : request.method
        }
    if request.method == 'POST':
        return {
            'message' : 'This endpoint should create a show',
            'method' : request.method,
            'body' : request.json
        }

@app.route('/api/show/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def show(id):
    if request.method == 'GET':
        return {
            'id': id,
            'message': 'This endpoint should return the show {} details'.format(id),
            'method': request.method 
        }
    if request.method == 'PUT':
        return{
            'id':id,
            'message': 'This endpoint should update show {}'.format(id),
            'body': request.json 
        }
    if request.method == "DELETE":
        return {
            'id': id,
            'message': 'This endpoint should delete the show {}'.format(id),
            'method': request.method
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
