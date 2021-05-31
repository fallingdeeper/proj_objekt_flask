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


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=80)
