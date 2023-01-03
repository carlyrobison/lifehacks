from typing import List, Tuple

VIAL_SIZE = 4
EMPTY_VIALS = 2

class Vial:
    def __init__(self, init_string: str):
        if len(init_string) != 4: raise ValueError("Game State Init String must be length {0}".format(VIAL_SIZE))
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
        

class GameState:
    # Provide vial config with a string of letters
    def __init__(self, init_string: str):
        if (len(init_string) %4 != 0): raise ValueError("Game State Init String must be divisible by {0}".format(VIAL_SIZE))
        self.vials_ = []
        for i in range(0, int(len(init_string) / 4)):
            vial_string = init_string[i * 4: (i +1) * 4]
            self.vials_.append(Vial(vial_string))
        for i in range(0, EMPTY_VIALS):
            self.vials_.append(Vial('    '))

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

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()
