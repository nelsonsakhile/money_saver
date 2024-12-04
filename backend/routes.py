from flask import render_template, jsonify, request
from models import User, TripDetails

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
    location = request.form.get("location")
    driver = request.form.get("driver")
    day_depature = request.form.get("day_depature")
    day_return = request.form.get("day_return")
    
    trip = TripDetails(
      location = location, 
      driver = driver, 
      day_depature = day_depature,
      day_return = day_return,
      )
      
    database.session.add(trip)
    database.session.commit()
    trips = TripDetails.query.all()
    return str(trip)
    