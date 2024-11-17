from flask import render_template, request
from models import User

def query_routes(app, database):
  @app.route("/") 
  def index():
    employees = User.query.all()
    return str(employees)