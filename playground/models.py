from flask_sqlalchemy import SQLAlchemy
#from app import * might be needed holding off

db = SQLAlchemy()


class Course(db.Model)
    __tablename__ = "courses"

    id = db.Column(db.Integer,primary_key=True)
    course_number = db.Column(db.Integer, nullable = False)
    course_title = = db.Column(db.String, nullable = False)


class RegisterStudent(db.Model)
    __tablename__ = "registeredstudents"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.String, nullable = False)
