#!/usr/bin/env python3
"""
0-app.py - Basic Flask App

This module defines a basic Flask web application with a
single route ("/") and an index.html template.

Usage:
    Run this script to start the Flask development server.

Routes:
    - /: Renders the index.html template with the title
         "Welcome to Holberton" and the header "Hello world".

Dependencies:
    - Flask: The web framework used to create the application.

Author:
    Ofentse Loeto
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app with Flask-Babel extension.

    This class defines configuration parameters for internationalization
    (i18n) using Flask-Babel in a Flask web application.

    Attributes:
        LANGUAGES (list): List of supported languages for translation.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.

    Example Usage:
        app = Flask(__name__)
        app.config.from_object(Config)
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language for the user.

    This function is decorated with babel.localeselector and is used to
    determine the user's preferred language based on the Accept-Language header
    in the request.

    Returns:
        str: The best-matching language code from the supported languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Route handler for the root ("/") endpoint.

    Returns:
        str: Rendered HTML content from the index.html template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
