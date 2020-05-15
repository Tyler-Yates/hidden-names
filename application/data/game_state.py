import random
import string
from typing import List


WORD_COUNT = 25


class GameState:
    """
    Class representing the state of a game.
    """

    def __init__(self):
        """
        Generates a new, random game state.
        """
        self.words = self._generate_words()
        self.hidden_values = self._generate_hidden_values()
        self.picked_words = set()

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
        for i in range(0, 5):
            index = random.randint(0, len(possible_values) - 1)
            location = possible_values[index]
            possible_values.pop(index)
            hidden_values[location] = 1

        # Red team
        for i in range(0, 5):
            index = random.randint(0, len(possible_values) - 1)
            location = possible_values[index]
            possible_values.pop(index)
            hidden_values[location] = 2

        return hidden_values
