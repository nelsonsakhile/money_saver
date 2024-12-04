from app import database as db
import datetime

class Role(db.Model):
  __tablename__ = "roles"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(60), unique=True)

  

class User(db.Model):
  __tablename__ = "employees"
  
  employee_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  surname = db.Column(db.Text, nullable=False)
  
  def __repr__(self):
    return f"Name {self.name}, surname {self.surname}, employee_id {self.employee_id}"

# For Crew members

class TripDetails(db.Model):
  __tablename__ = "trips"
  id = db.Column(db.Integer, primary_key=True)
  location = db.Column(db.Text, nullable=False)
  driver = db.Column(db.Text, nullable=False)
  day_depature = db.Column(db.Text, nullable=False)
  day_return = db.Column(db.Text, nullable=False, default= "Friday")
  date_depature = db.Column(db.DateTime, default=datetime.datetime.utcnow())
  date_return = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())
  def __repr__(self):
    return f"location: {self.location}, \n driver: {self.driver}"
  
# For Dispatch gents/Slaves

