from flask import render_template, request
from models import User

def query_routes(app, database):
  @app.route("/") 
  def index():
    employees = User.query.all()
    return str(employees)
  
  @app.route("/", methods=["POST"])
  def create_user():
    name = request.form.get("name")
    surname = request.form.get("surname")
    user = User(name=name, surname=surname)
    database.session.add(user)
    database.session.commit()
    employees = User.query.all()
    return str(employees)
    
  @app.route("/add_trip", methods = ["POST"])
  def trip_details():
    pass