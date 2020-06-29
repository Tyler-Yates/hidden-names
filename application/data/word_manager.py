import os
import random

FILE_LOCATION = os.path.dirname(os.path.realpath(__file__))


class WordManager:
    def __init__(self):
        self.words = []
        with open(f"{FILE_LOCATION}/../static/words.txt", mode='r') as word_file:
            for line in word_file:
                line = line.strip().upper()
                self.words.append(line)

        print(f"Loaded {len(self.words)} words.")

    def get_random_word(self) -> str:
        return random.choice(self.words)
