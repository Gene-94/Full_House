from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from flask_restplus import Api, Resource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fullhouse:my_flask_API@localhost/Shows'

db = SQLAlchemy(app)

class event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True )
    venue_id = db.Column(db.Integer, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class bands(db.Model):
    band_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True )
    created_date = db.Column(db.DateTime, nullable=False)
    music_genre = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<Name %r>' % self.name




@app.route('/api/shows', methods=['POST', 'GET'])
def shows():
    if request.method == 'GET':
        cur.execute("SELECT name, event_date FROM event")
        return {
            'event name' : name,
            'event date' : event_date
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




if __name__ == '__main__':
    app.run()



    

