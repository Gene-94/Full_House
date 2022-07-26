from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALVHEMY_DATAASE_URI'] = 'sqlite:///shows.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

@app.route('/index')
@app.route('/')
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