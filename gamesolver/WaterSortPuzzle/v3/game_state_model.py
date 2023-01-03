from typing import List, Tuple

VIAL_SIZE = 4
EMPTY_VIALS = 2

class Vial:
    colors_: List[str] = []

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


class GameState:
    vials_: List[Vial] = []

    # Provide vial config with a string of letters
    def __init__(self, init_string: str):
        if (len(init_string) %4 != 0): raise ValueError("Game State Init String must be divisible by {0}".format(VIAL_SIZE))
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
