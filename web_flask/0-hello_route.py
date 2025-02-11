#!/usr/bin/python3
# This script initializes a Flask web application with a route that returns "Hello HBNB!" when accessed.

from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define route with strict_slashes=False
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    This function handles the route "/". It returns the string 'Hello HBNB!' when accessed.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    """
    This block starts the Flask web application. It listens on all available IP addresses (0.0.0.0)
    and uses port 5000. The application runs in debug mode to provide detailed error logs.
    """
    app.run(host="0.0.0.0", port=5000, debug=True)
