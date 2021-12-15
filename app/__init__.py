from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

def create_app(config_name):
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app = Flask(__name__)


    app.config.from_object(config_options[config_name])
    return app


bootstrap = Bootstrap()
