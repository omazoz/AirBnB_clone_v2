#!/usr/bin/python3
"""Import Module"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    # start function
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # start function
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # start function
    s = text.replace('_', ' ')
    return 'C ' + s


@app.route('/python', strict_slashes=False)
def python(text='is_cool'):
    # start function
    s = text.replace('_', ' ')
    return 'Python ' + s


@app.route('/python/<text>', strict_slashes=False)
def python1(text='is_cool'):
    # start function
    s = text.replace('_', ' ')
    return 'Python ' + s


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # start function
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # start function
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    # start function
    s = "odd"
    if n % 2 == 0:
        s = "even"
    return render_template("6-number_odd_or_even.html", num=n, res=s)


@app.route('/states_list', strict_slashes=False)
def states_list(n):
    # start function
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", state_list=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    # start function
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    # start function
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port='5000')
