from flask import flask
from flask_sqlachemy import SQLAlchemy
from flask_cors import CORS

app = FLASK(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqllite://mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)