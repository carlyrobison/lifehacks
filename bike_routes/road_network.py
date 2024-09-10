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
        return str(self.numStreet) + " & " + self.charStreet

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
        self.crossType = crossing

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
        print(c, i)
