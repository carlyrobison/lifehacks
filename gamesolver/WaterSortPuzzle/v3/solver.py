import copy
from itertools import product
from typing import List
from game_state_model import GameState

MAX_MOVES = 50

# TODO optimize with hashing
def solve(game: GameState, explored_gamestates : List[GameState] = []) -> bool:
    # Base case 1: Solved!
    if game.isSolved():
        print('Solved! Printing in reverse order....')
        print('------------')
        print(game)
        return True
    
    # Base case 2: Loops :(
    if game in explored_gamestates:
        # print('Found a loop')
        return False  # Unsolvable
    
    explored_gamestates.append(game)

    numVials = len(game.vials_)
    for i, j in product(range(numVials), range(numVials)):
        if game.isValidMove((i, j)):      
            newgame = copy.deepcopy(game)
            newgame.makeMove((i, j))
            if solve(newgame, explored_gamestates):  # This returning True means there is a valid solve path.
                print('------------')
                print("{2} Moved vial {0} into vial {1}".format(i, j, len(explored_gamestates)* '\t'))
                print(game)
                return True
    
    explored_gamestates.pop()
    # Base case 3: No valid moves, or all moves end in failure
    # print('No winning moves :(')
    return False

init_string: str = 'aabbbbaa'
g = GameState(init_string)
print(g)
assert(solve(g))

# TODO: Fix move selection so it doesn't move the green back and forth
init_string: str = 'otbwlagpwtlvvaaykgrltproboprlwgvbvybwogakykprkyt'
g = GameState(init_string)
print(g)
assert(solve(g))