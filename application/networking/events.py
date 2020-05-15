from flask_socketio import emit, join_room

from .. import socketio


@socketio.on("guessed", namespace="/game")
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    # TODO figure out how to get the game name
    game_name = "test"
    join_room(game_name)
    emit("status", {"msg": "User has guessed."}, room=game_name)
