#Dependencies
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# app Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/songs'
db = SQLAlchemy(app)

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    year = db.Column(db.Integer)

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __repr__(self):
        return '<Song %r>' % self.title
#routes
@app.route('/', methods=['GET'])
def index():
    songs = Songs.query.all()
    print(songs)
    return render_template('index.html')

@app.route('/<id>', methods=['GET'])
def mys(id):
    print(id)
    return render_template("mySong.html", id=id)












if __name__ == '__main__':
    app.debug = True
    app.run()
