#!/usr/bin/env python3
"""
Flask App with Mocked User Login

This module defines a Flask web application with a mocked user login system.
Users are stored in the 'users' dictionary. The 'login_as' URL parameter is
used to emulate logging in.

Usage:
    Run this script to start the Flask development server.

Routes:
    - /: Displays a welcome message based on the login status.

Dependencies:
    - Flask: The web framework used to create the application.
    - Flask-Babel: Flask extension for internationalization and localization.
    - pytz: Python library for handling time zones.

Author:
    [Ofentse Loeto]
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)


# Mocked user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve user information based on user ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict or None: A dictionary containing user information if found,
                      or None if the user ID is not present in the 'users'
                      dictionary.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Execute before all other functions to set the user in flask.g.

    This function retrieves the 'login_as' URL parameter, emulating the
    user login, and sets the user information in the Flask global object
    (flask.g) for easy access in other parts of the application.
    """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id) if user_id else None


@app.route('/')
def index():
    """
    Route handler for the root ("/") endpoint.

    Returns:
        str: Rendered HTML content from the '5-index.html' template.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
