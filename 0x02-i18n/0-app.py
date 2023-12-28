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


app = Flask(__name__)


@app.route('/')
def index():
    """
    Route handler for the root ("/") endpoint.

    Returns:
        str: Rendered HTML content from the index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
