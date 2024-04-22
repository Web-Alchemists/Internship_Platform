from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import *

from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return {'id': self.id, 'username': self.username}

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    email = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(8), nullable=False)
    residence = db.Column(db.String(100), nullable=False)
    transcript = db.Column(db.String(100), db.ForeignKey('transcript.id'))
    letter = db.Column(db.String(1000), nullable=False)
    projects = db.Relationship('InternshipMatch', backref='student', lazy=True)

    def __init__(self, student_id, first_name, last_name, email, contact, residence, transcript, letter, projects):
        self.username = username
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.residence = residence
        self.transcript = transcript
        self.letter = letter
        self.projects = projects

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'passowrd': self.password,
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'contact': self.contact,
            'residence': self.residence,
            'transcript': self.transcript,
            'letter': self.letter,
            'projects': [project.get_json() for project in self.projects]
        }

    def viewTranscript(self):
        return self.transcript.get_json()

    def updateTranscrpit(self, updated_details):
        for key, value in updated_details.items():
            setattr(self.transcript, key, value)
        db.session.commit()

class Representative(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    company = db.Relationship('CompanyRep', backref='representative', lazy=True)

    def __init__(self, user_id, first_name, last_name, contact, company):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.company = company

    def get_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'contact': self.contact,
            'company': self.company
        }

    def submitProject(self, project_id):
        self.submitted_projects.append(project_id)
        db.session.commit()

    def viewProjects(self):
        return self.submitted_projects.get_json()

    def updateProject(self, project_id, updated_details):
        project = Project.query.get(project_id)
        for key, value in updated_details.items():
            setattr(project, key, value)
        db.session.commit()

    def removeProject(self, project_id):
        project = Project.query.get(project_id)
        db.session.delete(project)
        db.session.commit()

class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email

    def get_json(self):
        return {
            'id': self.id,
            'user-d': selft.user_id,
            'email': self.email
        }
  
    def viewAllCompanies(self):
        companies = Company.query.all()
        return companies

    def viewCompanyProjects(self, company_id):
        projects = Project.query.filter_by(company_id=company_id).all()
        return projects

    def viewAllStudents(self):
        students = Student.query.all()
        return students

    def viewStudentProjects(self, student_id):
        projects = Project.query.filter_by(student_id=student_id).all()
        return projects

    def viewAllProjects(self):
        projects = Project.query.all()
        return projects

    def viewProjectShortlist(self, project_id):
        shortlist = Project.query.filter_by(id=project_id).all()
        return shortlist

    def addToShortlist(self, project_id, student_id):
        project = Project.query.get(project_id)
        project.shortlist.append(student_id)
        db.session.commit()
        return project.shortlist

    def removeFromShortlist(self, project_id, student_id):
        project = Project.query.get(project_id)
        project.shortlist.remove(student_id)
        db.session.commit()
        return project.shortlist

class Company(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  country = db.Column(db.String(100), nullable=False)
  website = db.Column(db.String(100), nullable=True)
  email = db.Column(db.String(120), nullable=False)
  contact = db.Column(db.String(100), nullable=False)
  representatives = db.Relationship('CompanyRep', backref='company', lazy=True)

  def __init__(self, name, country, website, email, contact):
    self.name = name
    self.country = country
    self.website = website
    self.email = email
    self.contact = contact

  def get_json(self):
    return {
      'id': self.id,
      'company_id': self.company_id,
      'name': self.name,
      'country': self.country,
      'website': self.website,
      'email': self.email,
      'contact': self.contact,
      'representatives': [representative.get_json() for representative in self.representatives]
    }

class CompanyRep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    representative_id = db.Column(db.Integer, db.ForeignKey('representative.id'))

class Course(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(50), nullable=False)
  title = db.Column(db.String(100), nullable=False)

  def __init__ (self, code, title):
    self.code = code
    self.title = title

class Transcript(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  year = db.Column(db.Integer, nullable=False)
  major = db.Column(db.String(100), nullable=False)
  major2 = db.Column(db.String(100))
  minor = db.Column(db.String(100))
  minor2 = db.Column(db.String(100))
  courses = db.relationship('TranscriptCourses', backref='transcript', lazy=True)
  gpa = db.Column(db.Float, nullable=False)

  def __init__(self, year, major, major2, minor, minor2, courses, gpa):
    self.year = year
    self.major = major
    self.major2 = major2
    self.minor = minor
    self.minor2 = minor2
    self.courses = courses
    self.gpa = gpa

  def get_json(self):
    return {
      'id': self.id,
      'year': self.year,
      'major': self.major,
      'major2': self.major2,
      'minor': self.minor,
      'minor2': self.minor2,
      'courses': [course.get_json() for course in self.courses],
      'gpa': self.gpa
    }

class TranscriptCourses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transcript_id = db.Column(db.Integer, db.ForeignKey('transcript.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Project(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  representative_id = db.Column(db.Integer, db.ForeignKey('representative.id'))
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(300), nullable=False)
  capacity = db.Column(db.Integer, nullable=False)
  contact = db.Column(db.String(8), nullable=False)
  format = db.Column(db.String(100), nullable=False)
  duration = db.Column(db.Integer, nullable=False)
  shorlist = db.Relationship('InternshipMatch', backref='project', lazy=True)

  def __init__(self, representative_id, company_id, name, description, capacity, format, duration, shorlist):
    self.representative_id = representative_id
    self.company_id = company_id
    self.name = name
    self.description = description
    self.capacit = capacity
    self.format = format
    self.duration = duration
    self.shorlist = shorlist

  def get_json(self):
    return {
      'id': self.id,
      'representative_id': self.representative_id,
      'company_id': self.company_id,
      'name': self.name,
      'description': self.description,
      'capacity': self.capacity,
      'format': self.format,
      'duration': self.duration,
      'shorlist': [student.get_json() for student in self.shorlist]
    }

class Requirement(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  summary = db.Column(db.String(300), nullable=False)
  disciplines = db.Relationship('RequirementDisciplines', backref='requirement', lazy=True)
  year = db.Column(db.Integer, nullable=False)
  residence = db.Column(db.String(100), nullable=False)

  def __init__(self, summary, disciplines, year, residence):
    self.summary = summary
    self.disciplines = disciplines
    self.year = year
    self.residence = residence

  def get_json(self):
    return {
      'id': self.id,
      'summary': self.summary,
      'disciplines': [discipline.get_json() for discipline in self.disciplines],
      'year': self.year,
      'residence': self.residence
    }

class Discipline(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  area = db.Column(db.String(100), db.ForeignKey('area.id'))

  def __init__(self, name, area):
    self.name = name
    self.area = area

class RequirementDisciplines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requirement_id = db.Column(db.Integer, db.ForeignKey('requirement.id'))
    discipline_id = db.Column(db.Integer, db.ForeignKey('discipline.id'))

class Programme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(100), db.ForeignKey('area.id'))

class Area(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)

  def __init__(self, name):
    self.name = name

  def get_json(self):
    return {
      'id': self.id,
      'name': self.name
    }

class InternshipMatch(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

  def __init__(self, student_id, project_id):
    self.student_id = student_id
    self.project_id = project_id

class Country(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__ (self, name):
        self.name = name
    
    def get_json(self):
        return {
        'id': self.id,
        'name': self.name
        }