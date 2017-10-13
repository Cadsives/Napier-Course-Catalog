from main import db

class LocationPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    image = db.Column(db.String())
    image_alt = db.Column(db.String())
    lat = db.Column(db.String())
    lon = db.Column(db.String())

class CoursePage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.Integer)
