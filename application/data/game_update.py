from typing import List, Dict

from application.data.game_tile import GameTile


class GameUpdate:
    def __init__(self, game_state: 'GameState', tiles: List[GameTile]=None):
        self.blue_team_tiles_remaining = game_state.blue_team_tiles_remaining
        self.red_team_tiles_remaining = game_state.red_team_tiles_remaining
        self.current_team = game_state.current_team

        if tiles:
            self.tiles = tiles
        else:
            self.tiles = game_state.get_tiles_json()

    def to_json(self) -> Dict[str, object]:
        return self.__dict__