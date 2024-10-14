from campsites import *

t: Trip = Trip()
t.add_camp("Lees Ferry", 0.0, 0)
t.add_camp("Diamond Creek", 225.5, 25)

# Canyoneering day
t.add_camp("Badger Creek", 8.1, 1)
t.add_camp("Badger Creek", 8.1, 2)

# Tatahoysa Wash
t.add_camp("Eminence", 44.5, 6)
t.add_camp("Eminence", 44.5, 7)

# Also Phantom Ranch Swap Day
t.add_camp("Across Pipe Creek", 89.5, 11)
t.add_camp("Across Pipe Creek", 89.5, 12)

t.add_camp("Upper Blacktail", 120.6, 14)

# Cove Canyon
t.add_camp("Upper Cove Canyon", 174.7, 19)
t.add_camp("Upper Cove Canyon", 174.7, 20)

t.print_trip()
