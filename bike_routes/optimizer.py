from road_network import *

class Path:
    def __init__(self, start_intersection):
        self.latest_ixn = start_intersection
        self.paths = []
    
    def extend(self, intersection):
        return Path(intersection)

start_num = 17
start_char = 'd'

destination_num = 25
destination_char = 'i'

explored: set[Path] = set()
frontier: list[Intersection] = [Intersections[start_num][start_char]]
found_end: bool = False

# Standard breadth first search solution.
while not found_end:
    to_explore = frontier[0]
    frontier = frontier[1:]
    # explore both further west and further south
    