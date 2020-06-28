import random
import string
from typing import List, Dict

from application.data.game_tile import GameTile

WORD_COUNT = 25
BLUE_TEAM_TILES = 9
RED_TEAM_TILES = 8


class GameState:
    """
    Class representing the state of a game.
    """

    def __init__(self, game_name: str):
        """
        Generates a new, random game state.
        """
        self.game_name = game_name
        self.game_tiles: Dict[str, GameTile] = dict()

        words = self._generate_words()
        hidden_values = self._generate_hidden_values()
        for i in range(0, WORD_COUNT):
            word = words[i]
            hidden_value = hidden_values[i]
            self.game_tiles[word] = GameTile(word, hidden_value)

        print(self.game_tiles)

    def guess_word(self, guessed_word: str) -> None:
        """
        Updates the game state to reflect the guessed word.

        Args:
            guessed_word: The guessed word
        """
        game_tile = self.game_tiles[guessed_word]
        game_tile.guessed = True

    def get_tiles_json(self) -> List[Dict[str, str]]:
        """
        Returns the current tiles in a list of JSON compatible dictionaries.

        Returns:
            the tiles
        """
        tiles = list()
        for tile in self.game_tiles.values():
            tiles.append(tile.to_json())
        return tiles

    @staticmethod
    def _generate_words() -> List[str]:
        words = []
        for i in range(0, WORD_COUNT):
            word = ""
            for j in range(0, random.randint(3, 8)):
                word += random.choice(string.ascii_uppercase)
            words.append(word)

        return words

    @staticmethod
    def _generate_hidden_values() -> List[int]:
        possible_values = list(range(0, WORD_COUNT))
        hidden_values = [0] * WORD_COUNT

        # Assassin
        index = random.randint(0, len(possible_values) - 1)
        assassin_location = possible_values[index]
        possible_values.pop(index)
        hidden_values[assassin_location] = 3

        # Blue team
        for i in range(0, BLUE_TEAM_TILES):
            index = random.randint(0, len(possible_values) - 1)
            location = possible_values[index]
            possible_values.pop(index)
            hidden_values[location] = 1

        # Red team
        for i in range(0, RED_TEAM_TILES):
            index = random.randint(0, len(possible_values) - 1)
            location = possible_values[index]
            possible_values.pop(index)
            hidden_values[location] = 2

        return hidden_values
