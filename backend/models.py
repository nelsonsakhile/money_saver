from config import db 


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_role = db.Column(db.String(80), unique=True, nullable=False)
  name = db.Column(db.String(80), unique=True, nullable=False)
  surname = db.Column(db.String(120), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=True, nullable=False)
  
  def to_json(self):
    return {
      "userRole": self.user_role,
      "name": self.name,
      "surname": self.surname,
      "email": self.email,
      "password": self.password
    }

# For Crew members

class Depature(db.Model):
  id = db.Column(db.Integer, primary_key=True)
 # date = date
#  day = sun-sat

class Return(db.Model):
  id = db.Column(db.Integer, primary_key=True)
 # date = date
 # day = day
 # time = time
  
  
# For Dispatch gents/Slaves

