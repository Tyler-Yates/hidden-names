from flask_socketio import emit

from .. import socketio


@socketio.on("guess")
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    # TODO figure out how to get the game name
    print(f"Received guess: {message}")
    # emit("status", {"msg": "User has guessed."}, room=game_name)
