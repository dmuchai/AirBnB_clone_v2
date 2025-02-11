#!/usr/bin/python3
# a script that initializes a Flask web application
from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define route with strict_slashes=False
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    # Start the web application on 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
