import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Olha Petryk\'s project.\nAt Jagiellonian University.'

    return app