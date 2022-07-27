from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shows.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #create a table for bands and connect with id by using foreign key
    band_name = db.Column(db.String(200), nullable=False)
    show_venue_address = db.Column(db.String(200), nullable=False)
    show_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.id
    

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/shows')
def shows():
    return render_template('for_users.html')

@app.route('/new-show')
def new_show():
    return render_template('for_bands.html')



if __name__ == '__main__':
    app.run(debug=True)