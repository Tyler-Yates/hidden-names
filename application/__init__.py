from flask import Flask
from flask_socketio import SocketIO

from application.data.game_manager import GameManager

GAME_MANAGER_CONFIG_KEY = "game_manager"

socketio = SocketIO()


def create_flask_app() -> Flask:
    # Create the flask app
    app = Flask(__name__)

    # Create a DAO and add it to the flask app config for access by the blueprints
    app.config[GAME_MANAGER_CONFIG_KEY] = GameManager()

    from .networking import main as main_blueprint

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)

    return app
