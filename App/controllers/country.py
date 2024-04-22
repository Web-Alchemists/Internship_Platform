from App.models import Country
from App.database import db

def create_country(name):
    new_country = Country(name=name)
    db.session.add(new_country)
    db.session.commit()
    return new_country

def get_all_countries():
    countries = Country.query.all()
    return countries