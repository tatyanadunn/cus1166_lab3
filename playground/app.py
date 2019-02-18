import sys

from from import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)

@app.route('/')
def index():
    courses = Course.query.all()
    render_template("index.html", courses = courses)

@app.route('/add_course')
def add_course():
    #
    render_template('index.html')

@app.route('/register_student/<int:course_id>', methods=['GET', 'POST'])
def register():
    #pass
    #render_template()


if __name__ == "__main__":
    app.run()
