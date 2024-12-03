from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

database = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"
  database.init_app(app)
  from routes import query_routes
  query_routes(app, database)
  migrate = Migrate(app, database)
  return app