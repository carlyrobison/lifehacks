from road_network import *

class Path:
    def __init__(self, intersection: Intersection):
        self.latest_ixn: Intersection = intersection
        self.paths: list = []

    def __repr__(self):
        return " -> ".join([str(self.latest_ixn)] + [str(p) for p in self.paths])
    
    def extend(self, intersection):
        new_path = Path(intersection)
        new_path.paths = self.paths + [self.latest_ixn]
        return Path(intersection)

startIntersection = Intersection(17, 'd', 0)
destination = Intersection(25, 'i', 0)

explored: dict[Intersection, list[Path]] = {}
frontier: list[Path] = [Path(Intersections[startIntersection.numStreet][startIntersection.charStreet])]
should_stop: bool = False

# Standard breadth first search solution.
while not should_stop:
    if len(frontier) == 0:
        should_stop = True
    else: 
        next = frontier[0]
        to_explore = next.latest_ixn
        # Add the Intersection path so far
        if to_explore in explored:
            explored[to_explore].append(next)
        else:
            explored[to_explore] = [next]

        if to_explore.charStreet < destination.charStreet:
            # go further west
            frontier.append(next.extend(Intersections[to_explore.numStreet][to_explore.getNextNSStreet()]))

        if to_explore.numStreet < destination.numStreet:
            # explore further south
            frontier.append(next.extend(Intersections[to_explore.numStreet + 1][to_explore.charStreet]))

        frontier = frontier[1:]

print("Search concluded")
for p in explored[destination]:
    print(p)
