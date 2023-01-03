import copy
from itertools import product
from game_state_model import GameState

class SolveGame:
    def __init__(self, game: GameState):
        self.game_ = copy.deepcopy(game)
        self.explored_gamestates = {hash(self.game_)}
    
    def __repr__(self):
        return "game:\n{0}\nexplored gamestates:{1}".format(self.game_.__repr__(), self.explored_gamestates)

    def solve(self):
        numVials = len(self.game_.vials_)
        while not self.game_.isSolved():
            print('----------------')
            print(self.game_)
            # Find the first valid move
            validMoveMade = False
            for i, j in product(range(numVials), range(numVials)):
                if self.game_.isValidMove((i, j)):
                    print("Moving vial {0} into vial {1}".format(i, j))
                    self.game_.makeMove((i, j))
                    validMoveMade = True
                    break
            if not validMoveMade:
                print('No valid moves, but game not solved :(')
                break

init_string: str = 'aabbbbaa'
g = GameState(init_string)
print(g)
s = SolveGame(g)
s.solve()