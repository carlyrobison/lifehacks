from typing import List, Tuple

VIAL_SIZE = 4
EMPTY_VIALS = 2

class Vial:
    def __init__(self, init_string: str):
        if len(init_string) != VIAL_SIZE: raise ValueError("Game State Init String must be length {0}".format(VIAL_SIZE))
        self.colors_ = [char for char in init_string]

    def __repr__(self) -> str:
        return ''.join(self.colors_)

    def isSolved(self) -> bool:
        # TODO optimization: skip checking first one for speedup of 25%
        for color in self.colors_:
            if color != self.colors_[0]:
                return False
        return True
    
    def canFillWith(self) -> Tuple[int, str]:
        if self.colors_[-1] != ' ':
            return (0, ' ')
        for i in range(1, VIAL_SIZE):
            if self.colors_[(-1 * i) - 1] != ' ':
                return (i, self.colors_[(-1 * i) - 1])
        return (4, '*')

    def topLayer(self) -> Tuple[int, str]:
        i = VIAL_SIZE
        topLayerChar: str = '*'
        layerSize: int = 0
        while (i > 0):
            if layerSize > 0:
                if self.colors_[i-1] == topLayerChar:
                    layerSize += 1
                    i -= 1
                    continue
                else:
                    return (layerSize, topLayerChar)

            if self.colors_[i - 1] != ' ':
                topLayerChar = self.colors_[i - 1]
                layerSize = 1
            i -= 1
        return (layerSize, topLayerChar)
    
    def addColor(self, color: str) -> None:
        # use canFillWith to determine location to add color
        fillableSpace = self.canFillWith()
        if (fillableSpace[1] != '*') and (fillableSpace[1] != color): raise ValueError("Invalid color {0} for vial {1}".format(color, self))
        if fillableSpace[0] == 0: raise ValueError("Vial {0} does not have any space".format(self))
        if len(color) != 1: raise ValueError("Invalid color {}".format(color))
        self.colors_[VIAL_SIZE-fillableSpace[0]] = color
    
    def removeColor(self) -> None:
        fillableSpace = self.canFillWith()
        if fillableSpace[0] == VIAL_SIZE: raise ValueError("Vial {0} is already empty".format(self))
        self.colors_[VIAL_SIZE-fillableSpace[0] - 1] = ' '

    # Hypothesis: metric always decreases as we make progress towards the solution
    # Metric is "How many colors are 'trapped' by the wrong color?"
    # This metric isn't quite monotonic?
    def metricValue(self) -> int:
        metric: int = 0
        current_color: str = self.colors_[0]
        for i in range(1, VIAL_SIZE):
            if (self.colors_[i] != ' '):
                if (self.colors_[i] != current_color):
                    metric -= 1
                else:
                    metric += 1
            current_color = self.colors_[i]
        return metric
    
    def isEmpty(self) -> bool:
        for i in range(VIAL_SIZE):
            if self.colors_[i] != ' ':
                return False
        return True
        
class GameState:
    # Provide vial config with a string of letters
    def __init__(self, init_string: str):
        self.vials_ = []
        for vial_string in init_string.split(' '):
            self.vials_.append(Vial(vial_string))
        for i in range(0, EMPTY_VIALS):
            self.vials_.append(Vial('    '))

        # Finally, check that this is solvable, i.e. that each color present has VIAL_SIZE blocks.
        color_map = {}
        for vial in self.vials_:
            for color in vial.colors_:
                if color in color_map:  # TODO: probably a nice way to do this with enumerable
                    color_map[color] += 1
                else:
                    color_map[color] = 1
        for color, qty in color_map.items():
            if color != ' ' and qty != VIAL_SIZE:
                raise ValueError('Invalid number {1} of color blocks {0}, needs to be {2}'.format(color, qty, VIAL_SIZE))

    def __repr__(self) -> str:
        return '\n'.join([vial.__repr__() for vial in self.vials_])

    def isSolved(self) -> bool:
        for vial in self.vials_:
            if not vial.isSolved():
                return False
        return True

    def canMoveInto_(self, layer: Tuple[int, str], gap: Tuple[int, str]) -> bool:
        if gap[0] == 0: return False  # Gap has to be > 0
        if layer[0] == 0: return False  # Must have something to fill with
        if gap[1] == '*':
            return True  # Anything can fill this
        return gap[1] == layer[1]  # Only returns true if they are compatible colors

    # Use vial indices as input. Move A into B
    def isValidMove(self, move: Tuple[int, int]) -> bool:
        if move[0] >= len(self.vials_): raise IndexError("Vial does not exist at index {}".format(move[0]))
        if move[1] >= len(self.vials_): raise IndexError("Vial does not exist at index {}".format(move[1]))
        if move[0] == move[1]: return False  # cannot move vial into itself
        fromVialLayer = self.vials_[move[0]].topLayer()
        toVialFillWith = self.vials_[move[1]].canFillWith()
        return self.canMoveInto_(fromVialLayer, toVialFillWith)

    # Makes the given move.
    def makeMove(self, move: Tuple[int, int]) -> None:
        if not self.isValidMove(move): raise ValueError("Invalid move")
        fromVial = self.vials_[move[0]]
        toVial = self.vials_[move[1]]
        fromVialLayer = self.vials_[move[0]].topLayer()
        while self.isValidMove(move):  # Fill as much of the vial as possible
            fromVial.removeColor()
            toVial.addColor(fromVialLayer[1])

    def metricValue(self) -> int:
        metric: int = sum([vial.metricValue() for vial in self.vials_])
        return metric

    def __eq__(self, other):
        return set([vial.__repr__() for vial in self.vials_]) == set([vial.__repr__() for vial in other.vials_])
