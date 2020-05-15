import random
import string
from typing import Optional

from application.data.game_state import GameState


class GameManager:
    """
    Manages all the games.
    """

    def __init__(self):
        self.games = {}

    def create_game(self) -> str:
        """
        Creates a new game state and returns the game name.

        Returns:
            the game name
        """
        game_name = self._create_game_name()
        while game_name in self.games:
            game_name = self._create_game_name()

        self.games[game_name] = GameState()

        return game_name

    def get_game_state(self, game_name: str) -> Optional[GameState]:
        """
        Returns the game state for the given game name if one exists.
        Args:
            game_name: the game name

        Returns:
            the game state if one exists
        """
        return self.games.get(game_name, None)

    @staticmethod
    def _create_game_name() -> str:
        game_name = ""
        for i in range(0, 4):
            game_name += random.choice(string.ascii_uppercase)
        return game_name

    def _expire_game(self):
        # TODO we should expire games so that they don't live in memory forever.
        pass
