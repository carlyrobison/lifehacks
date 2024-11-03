from road_network import *

class Path:
    def __init__(self, start_intersection):
        self.latest_ixn = start_intersection
        self.paths = []
    
    def extend(self, intersection):
        return Path(intersection)

startIntersection = Intersection(17, 'd', 0)
destination = Intersection(25, 'i', 0)

explored: set[Path] = set()
frontier: list[Intersection] = [Intersections[startIntersection.numStreet][startIntersection.charStreet]]
should_stop: bool = False

# Standard breadth first search solution.
while not should_stop:
    to_explore = frontier[0]

    # check if we found the end
    if to_explore == destination:
        should_stop = True
    elif len(frontier) == 0:
        should_stop = True
    else: 
        # Add the Intersection path so far
        
        if to_explore.charStreet < destination.charStreet:
            # go further west
            frontier.append(Intersections[to_explore.numStreet][to_explore.getNextNSStreet()])

        if to_explore.numStreet < destination.numStreet:
            # explore further south
            frontier.append(Intersections[to_explore.numStreet + 1][to_explore.charStreet])

        frontier = frontier[1:]

print("Search concluded")

