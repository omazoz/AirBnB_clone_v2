#!/usr/bin/python3
""" Flask web application """
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Returns a string at the root route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Returns a string at the /hbnb route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ Returns a string at the /c route with a variable """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """ Returns a string at the /python route with a variable """
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ Returns a string at the /number route with a variable as an int """
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Returns a string at the /number_template route with a variable as an
    int and renders an html template """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Returns a string at the /number_odd_or_even route with a variable as an
    int and renders an html template """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    """runs the application on port 5000"""
    app.run(host="0.0.0.0", port=5000)