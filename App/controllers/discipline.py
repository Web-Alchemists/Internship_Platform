from App.models import Discipline
from App.database import db

def create_discipline(name, area):
    new_discipline = Discipline(name=name, area=area)
    db.session.add(new_discipline)
    db.session.commit()
    return new_discipline

def get_all_disciplines():
    disciplines = Discipline.query.all()
    return disciplines