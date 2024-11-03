import random
from enum import Enum

# Represents two cross streets
class Intersection:
    def __init__(self, EWstreet: int, NSstreet: str, elevation: int):
        self.numStreet: int = EWstreet
        assert(len(NSstreet) == 1)
        self.charStreet: str = NSstreet
        self.elevation: int = elevation

    def __repr__(self):
        return f"{self.numStreet} & {self.charStreet}"
    
    def __eq__(self, other):
        return self.charStreet == other.charStreet and self.numStreet == other.numStreet
    
    def __hash__(self):
        if self.charStreet == 'a': return 100 + self.numStreet
        if self.charStreet == 'b': return 200 + self.numStreet
        if self.charStreet == 'c': return 300 + self.numStreet
        if self.charStreet == 'd': return 400 + self.numStreet
        if self.charStreet == 'e': return 500 + self.numStreet
        if self.charStreet == 'f': return 600 + self.numStreet
        if self.charStreet == 'g': return 700 + self.numStreet
        if self.charStreet == 'h': return 800 + self.numStreet
        if self.charStreet == 'i': return 900 + self.numStreet

    def getNextNSStreet(self):
        # TODO(carly): Update to python3.10 so this works
        # match self.charStreet:
        #     case 'a':
        #         return 'b'
        if self.charStreet == 'a': return 'b'
        if self.charStreet == 'b': return 'c'
        if self.charStreet == 'c': return 'd'
        if self.charStreet == 'd': return 'e'
        if self.charStreet == 'e': return 'f'
        if self.charStreet == 'f': return 'g'
        if self.charStreet == 'g': return 'h'
        if self.charStreet == 'h': return 'i'
            

# Intersection crossing type, in increasing goodness.
class CrossType(Enum):
    TWO_WAY_UNPROTECTED = 1
    ALL_WAY_STOP = 2
    TWO_WAY_PROTECTED = 3

# Represents a street block between two cross streets
class Block:
    def __init__(self, surface: int, distance: int, crossing: CrossType):
        self.surface_rating = surface  # Sort of a star rating
        self.distance = distance
        self.crossType = crossing  # Crossing out of the block

    def __repr__(self):
        return f"{self.distance} & {self.crossType}"

# Necessary setup of the arrays
EWArray: list[dict[str, Block]] = [] # East west streets are numbered.
NSArray: dict[str, list[Block]] = {} # North south streets are lettered
Intersections: list[dict[str, Intersection]] = []
for i in range(26):
    EWArray.append({})
    Intersections.append({})

# Example road network goes from C & 17th to I & 25th
for c in list('cdefghi'):
    NSArray[c] = []
    for i in range(17, 26):
        EWArray[i][c] = Block(random.randrange(0, 5), random.randrange(50, 150), CrossType.ALL_WAY_STOP)
        NSArray[c].append(Block(random.randrange(0, 5), random.randrange(50, 150), CrossType.ALL_WAY_STOP))
        Intersections[i][c] = Intersection(i, c, random.randrange(1000, 1500))
        # print(c, i)

# print(NSArray)
# print(EWArray)
# print(Intersections)