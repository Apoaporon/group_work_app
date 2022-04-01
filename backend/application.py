# application.py
from flask import Flask


def create_app(app_name='FLASK-VUE'):
    app = Flask(app_name,
                static_folder="./dist/static",
                template_folder="./dist")
    app.config.from_object('backend.config.BaseConfig')

    return app
