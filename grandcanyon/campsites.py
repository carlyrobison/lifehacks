# Two axes -- river mile (RM) and Nights (N)

from ctypes import Array


class Campsite:
    def __init__(self, name: str, river_mile: float, night: int):
        self.name: str = name
        self.river_mile: float = river_mile
        self.night: int = night

    # Assume self is the first 
    def get_rate(self, other) -> float:
        rm_per_day = (other.river_mile - self.river_mile) / (other.night - self.night)
        return rm_per_day

    def __lt__(self, other) -> bool:
        return self.river_mile < other.river_mile
    
    def __gt__(self, other) -> bool:
        return self.river_mile > other.river_mile

    # For printing
    def __repr__(self):
        return f"Camp {self.name} at RM {self.river_mile} night {self.night}"

class Trip:
    def __init__(self):
        self.camps: Array[Campsite] = []

    def add_camp(self, name: str, rm: float, night: int):
        self.camps.append(Campsite(name, rm, night))

    def print_trip(self):
        self.camps.sort()
        assert(len(self.camps) > 0)
        prev_camp: Campsite = self.camps[0]
        print(prev_camp)
        for camp in self.camps[1:]:
            print("\trate: {:03.2f} miles per day".format(prev_camp.get_rate(camp)))
            print(camp)
            prev_camp = camp

    