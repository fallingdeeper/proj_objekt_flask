import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Olha Petryk\'s project.\nAt Jagiellonian University.'

    return app


app = create_app()
