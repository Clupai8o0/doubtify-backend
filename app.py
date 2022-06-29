# Importing dependencies
from flask import Flask

# Creating flask app
app = Flask(__name__)

# Creating a default route
@app.route("/")
def home():
  return "Hello World"

# Running the project
app.run(port=5000)