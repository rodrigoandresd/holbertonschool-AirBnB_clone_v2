#!/usr/bin/python3

"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """closes the storage on teardown"""
    storage.close()


@app.route("/states", strict_slashes=False)
def cities_states():
    """Display a HTML page with the states_id"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, flag="state")

@app.route("/states/<id>", strict_slashes=False)
def cities_state_id(id):
    '''Display a HTML page with the states_id'''
    for states in storage.all(State).values():
        if states.id == id:
            return render_template("9-states.html", states=states,
                                   flag="state_id")
    return render_template("9-states.html", states=states, flag="none")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
