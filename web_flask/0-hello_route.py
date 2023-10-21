#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and a view function

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == "__main__":
    """runs the application on port 5000"""
    app.run(host="0.0.0.0", port=5000)