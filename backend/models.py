from app import database as db

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
    return f"Name {self.name}, \n surname {self.surname}, \n employee_id {self.employee_id}"

# For Crew members

#class Depature(db.Model):
  #id = db.Column(db.Integer, primary_key=True)
 # date = date
#  day = sun-sat

#class Return(db.Model):
 # id = db.Column(db.Integer, primary_key=True)
 # date = date
 # day = day
 # time = time
  
  
# For Dispatch gents/Slaves

