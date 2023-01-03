import copy
from game_state_model import GameState

class SolveGame:
    def __init__(self, game: GameState):
        self.initial_game_ = copy.deepcopy(game)
    
    def __repr__(self):
        return "Initial game:\n{}\n".format(self.initial_game_.__repr__())





init_string: str = 'aaaabbbb'
g = GameState(init_string)
print(g)
s = SolveGame(g)
print(s)