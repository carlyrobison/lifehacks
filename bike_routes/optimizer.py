from road_network import *

class Path:
    def __init__(self, intersection: Intersection):
        self.latest_ixn: Intersection = intersection
        self.ixns: list = []

    def __repr__(self):
        return " -> ".join([str(self.latest_ixn)] + [str(p) for p in self.ixns])
    
    def extend(self, intersection):
        new_path = Path(intersection)
        new_path.ixns.append(self.latest_ixn)
        new_path.ixns += self.ixns
        return new_path
    
    def printStats(self):
        # Initialize stats
        elevGain: int = 0
        elevLoss: int = 0
        distance: int = 0
        crossingStats: dict[CrossType, int] = {
            CrossType.TWO_WAY_UNPROTECTED: 0,
            CrossType.ALL_WAY_STOP: 0,
            CrossType.TWO_WAY_PROTECTED: 0,
        }
        surfaceRatings: list[int] = []

        ixn: Intersection = self.latest_ixn
        for i in self.ixns:
            # Get elev gain/loss from the two intersections
            if ixn.elevation > i.elevation:
                elevGain += (ixn.elevation - i.elevation)
            else:
                elevLoss += (ixn.elevation - i.elevation)

            # Get all other stats from the block
            block = Blocks[(i, ixn)]
            distance += block.distance
            crossingStats[block.crossType] += 1
            surfaceRatings.append(block.surface_rating)

            # Set up for the next iteration
            ixn = i
        
        print("Route: " + str(self))
        print("+" + str(elevGain) + ", " + str(elevLoss))
        print("Min surface rating: " + str(min(surfaceRatings)))
        print("Distance: " + str(distance))
        print(crossingStats)


startIntersection = Intersection(17, 'd')
destination = Intersection(25, 'i')

explored: dict[Intersection, list[Path]] = {}
frontier: list[Path] = [Path(Intersections[startIntersection])]
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
            frontier.append(next.extend(Intersections[Intersection(to_explore.numStreet, getNextNSStreet(to_explore.charStreet))]))

        if to_explore.numStreet < destination.numStreet:
            # explore further south
            frontier.append(next.extend(Intersections[Intersection(to_explore.numStreet + 1, to_explore.charStreet)]))

        frontier = frontier[1:]

print("Search concluded")
# TODO: sort by minimum elev gained
for p in explored[destination]:
    p.printStats()
