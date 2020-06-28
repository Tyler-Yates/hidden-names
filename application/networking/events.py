import flask
from flask import current_app
from flask_socketio import emit, join_room

from application import GameManager, GAME_MANAGER_CONFIG_KEY
from .. import socketio


@socketio.on("join")
def joined(message):
    room = message["room"]
    join_room(room)
    session_id = flask.request.sid

    print(f"User {session_id} has joined room {room}")
    game_state = _get_game_manager().get_game_state(room)
    emit("reload", {"game_state": game_state.get_tiles_json()}, to=session_id)


@socketio.on("guess")
def guessed_word(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    # TODO figure out how to get the game name
    print(f"Received guess: {message}")

    room = message["room"]
    guessed_word = message["guess"]

    game_state = _get_game_manager().get_game_state(room)
    game_state.guess_word(guessed_word)

    updated_tile = game_state.game_tiles[guessed_word].to_json()
    emit("reload", {"game_state": [updated_tile]}, room=room)


def _get_game_manager() -> GameManager:
    return current_app.config[GAME_MANAGER_CONFIG_KEY]
