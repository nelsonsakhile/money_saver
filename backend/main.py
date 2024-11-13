from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
  return None
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)