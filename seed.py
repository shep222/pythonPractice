from models import Songs
from app import db

song = Songs('Cant stop', 'Red Hot Chili Peppers', 2000)

db.session.add(song)
db.session.commit()
