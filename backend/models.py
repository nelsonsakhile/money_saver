from app import database as db



class User(db.Model):
  __tablename__ = "Employees"
  
  employee_id = db.Column(db.Integer, primary_key=True)
  user_role = db.Column(db.Text, nullable=False)
  name = db.Column(db.Text, nullable=False)
  surname = db.Column(db.Text, nullable=False)
  email = db.Column(db.Text, nullable=False)
  password = db.Column(db.Text, nullable=False)
  
  def __repr__(self):
    return f"Name {self.name}"

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

