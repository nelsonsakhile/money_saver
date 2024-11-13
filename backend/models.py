from config import db 


class User(db.Model):
  user_id = 1
  user_role = 1
  name = 1
  surname = 1
  email = 1
  password = 1

# For Crew members

class Depature(db.Model):
  user_id = 1
  date = date
  day = sun-sat

class Return(db.Model):
  user_id = 1
  date = date
  day = day
  time = time
  
class Final_Pay(db.Model):
  id = id
  month = month
  no_days = no_days
  total_pay = total_pay
  
# For Dispatch gents/Slaves

