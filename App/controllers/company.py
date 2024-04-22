from App.models import Company
from App.database import db

def create_company(name, country, website, email, contact):
    new_company = Company(name=name, country=country, website=website, email=email, contact=contact)
    db.session.add(new_company)
    db.session.commit()
    return new_company

def get_all_companies():
    companies = Country.query.all()
    return companies