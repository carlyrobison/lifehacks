import copy
from game_state_model import GameState

class SolveGame:
    def __init__(self, game: GameState):
        self.game_ = copy.deepcopy(game)
    
    def __repr__(self):
        return "game:\n{}\n".format(self.game_.__repr__())

    # def solve(self):
    #     while not self.game_.isSolved():
    #         # Make a move



init_string: str = 'aaaabbbb'
g = GameState(init_string)
print(g)
s = SolveGame(g)
print(s)