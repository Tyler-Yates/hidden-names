from flask import Flask

from application.data.custom_json_encoder import CustomJsonEncoder
from application.data.dao import ApplicationDao
from application.routes.api_routes import API_BLUEPRINT
from application.routes.html_routes import HTML_BLUEPRINT

# Key to use when accessing flask app config
DATABASE_CONFIG_KEY = "DB"


def create_flask_app() -> Flask:
    # Create the flask app
    app = Flask(__name__)

    # Set custom JSON encoder to handle MongoDB ObjectID
    app.json_encoder = CustomJsonEncoder

    # Create a DAO and add it to the flask app config for access by the blueprints
    app.config[DATABASE_CONFIG_KEY] = ApplicationDao()

    # Register blueprints to add routes to the app
    app.register_blueprint(API_BLUEPRINT)
    app.register_blueprint(HTML_BLUEPRINT)

    return app
