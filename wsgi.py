import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import *

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

def create_all_companies():
    create_company("CompanyA", None, "compamyamail@mail", "555-4545")
    create_company("CompanyB", "compnanya.com", "companybmail@mail", "705-2230")
    create_company("CompanyC", None, "companycmail@mail", "876-4649")
    create_company("CompanyD", "company.com", "compamydmail@mail", "141-4112")

def create_all_countries():
    create_country("Anguilla")
    create_country("Antigua & Barbuda")
    create_country("Bahamas")
    create_country("Barbados")
    create_country("Antigua & Barbuda")
    create_country("Belize")
    create_country("British Virgin Islands")
    create_country("Cayman Islands")
    create_country("Dominica")
    create_country("Grenada")
    create_country("Jamaica")
    create_country("Montserrat")
    create_country("St. Kitts & Nevis")
    create_country("St. Lucia")
    create_country("St. Vincent & the Grenadines")
    create_country("Trinidad & Tobago")
    create_country("Turks & Caicos")

def create_all_areas():
    create_area("Engineering")
    create_area("Food & Agriculture")
    create_area("Humanities & Education")
    create_area("Law")
    create_area("Medical Sciences")
    create_area("Science & Technology")
    create_area("Social Sciences")
    create_area("Sport")

def create_all_disciplines():
    create_discipline("Civil Engineering", 1)
    create_discipline("Mechanical Engineering", 1)
    create_discipline("Electircal Engineering", 1)
    create_discipline("Chemical Engineering", 1)
    create_discipline("Geomatics Engineering & Land Management", 1)
    create_discipline("Nutrition", 2)
    create_discipline("Agriculture", 2)
    create_discipline("Geography", 2)
    create_discipline("Climate", 2)
    create_discipline("Visual Arts", 3)
    create_discipline("Theatre", 3)
    create_discipline("Dance", 3)
    create_discipline("Music", 3)
    create_discipline("Film", 3)
    create_discipline("History", 3)
    create_discipline("Language", 3)
    create_discipline("Linguistics", 3)
    create_discipline("Education", 3)
    create_discipline("Culture", 3)
    create_discipline("Communication", 3)
    create_discipline("Film", 3)
    create_discipline("Law", 4)
    create_discipline("Nursing", 5)
    create_discipline("Pharmacy", 5)
    create_discipline("Dentistry", 5)
    create_discipline("Veterinary", 5)
    create_discipline("Optomoetry", 5)
    create_discipline("Psychiatry", 5)
    create_discipline("Data Science", 6)
    create_discipline("Database Administration", 6)
    create_discipline("Information Security", 6)
    create_discipline("Web Development", 6)
    create_discipline("Software Engineering", 6)
    create_discipline("Networking", 6)
    create_discipline("Mathematics", 6)
    create_discipline("Statistics", 6)
    create_discipline("Electronics", 6)
    create_discipline("Physics", 6)
    create_discipline("Chemistry", 6)
    create_discipline("Biology", 6)
    create_discipline("Environmental Science", 6)
    create_discipline("Accounting", 7)
    create_discipline("Finance", 7)
    create_discipline("Marketing", 7)
    create_discipline("Management", 7)
    create_discipline("Psychology", 7)
    create_discipline("Socilogy", 7)
    create_discipline("Politics", 7)


def create_all_courses():
    pass

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_all_countries()
    create_all_areas()
    create_all_disciplines()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)