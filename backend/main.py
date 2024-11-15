from flask import Flask
from flask import request, jsonify
from models import User


app = Flask(__name__)

@app.route('/', methods= ["GET"])
def index():
  users = User.query_all()
  json_users = list(map(lambda i: i.to_json, users))
  return jsonify({"users": json_users})
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)