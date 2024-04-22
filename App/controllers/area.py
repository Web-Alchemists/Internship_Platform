from App.models import Area
from App.database import db

def create_area(name):
    new_area = Area(name=name)
    db.session.add(new_area)
    db.session.commit()
    return new_area

def get_all_areas():
    areas = Area.query.all()
    return areas