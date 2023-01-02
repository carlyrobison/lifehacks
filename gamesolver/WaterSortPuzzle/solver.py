'''
Setup, if you haven't played this game before.
There's a number of vials of different color liquids, always 4 blocks tall.
You also get 2 empty vials.
You need to sort the blocks of liquid, Tower of Hanoi style, until each vial
contains 4 blocks of the same color, and you again have 2 empty vials.

a b       ->      a b
b a _ _   ->  _ _ a b

You can only put like colors on top of each other.
  b    ->    b a             b
a b a  ->  _ b a   NOT   a b a
You can also put any color in a blank vial.

And contiguous colors fill as much as they can.
a         a
a a  -> a a 
b a     b a

I'm pretty sure you can prove this problem's solvability with 2 vials, but it's been
a while since that algorithms proofs class. Something something there always exists a
move that decreases some metric.
'''

class State:
	def __init__(self, arr):
		# Array's rows are the vials
		self.vials = arr.copy()  # inefficient, sue me

	def __repr__(self):
		# Display vials vertically like in the game.
		return "\n".join([" ".join([v[i] for v in self.vials]) for i in range(len(self.vials[0]))])

	def is_solved(self):
		for v in self.vials:
			for b in v:
				if b != v[0]:
					return False
		return True

	# List of allowed moves in form (old vial, new vial)
	def allowed_moves(self):
		moves = []
		for f in range(len(self.vials)):
			for t in range(len(self.vials)):
				if f != t and self.can_move(f, t):
					# print('Can move!')
					moves.append((f, t))
		return moves

	def can_move(self, vial_from, vial_to):
		receiving_vial = self.topmost_color(vial_to)
		sending_vial = self.topmost_color(vial_from)
		# print('Evaluating ({}, {}), top colors {} and {}'.format(vial_from, vial_to, sending_vial, receiving_vial))
		if sending_vial == ' ':
			return False  # can't send zero color
		if self.vials[vial_to][0] != ' ':
			return False  # can't overflow vials
		if sending_vial == receiving_vial or receiving_vial == ' ':
			return True
		return False

	def topmost_color(self, vial):
		for b in self.vials[vial]:
			if b > ' ':  # the power of lexicographic comparisons!
				return b
		return ' '

	# Returns a copy of the State
	def duplicate_state(self):
		return State(self.vials)

	# Moves come in a tuple of (from_vial, to_vial)
	def make_move(self, move):
		vial_from = move[0]
		vial_to = move[1]
		color = self.topmost_color(vial_from)
		self.vials[vial_to][0] != ' '
		# move the top color to the other vial
		# while the other vial is not overflowing
		# while ()
		# while sending_vial == receiving_vial or receiving_vial == ' ':

class Puzzle:
	def __init__(self, level_num, start_state):
		self.start = State([c for c in start_state.split('\n')])
		self.level = level_num
		self.moves = []  # FIFO queue, optimize later

	def __repr__(self):
		return "Level {} with start state \n{}\n".format(self.level, self.start)

	# def solve_puzzle(self):
	# 	# breadth first search, so we don't get stuck in a cycle
	# 	moves = 0
	# 	frontier = []
	# 	for m in self.start.allowed_moves:


# Presolved puzzle
p = Puzzle(0, 'aa\nbb\n  \n  ')
print(p)
assert(p.start.is_solved())
print(p.start.allowed_moves())

# Harder puzzle
p = Puzzle(0, 'ab\nca\n c\n b')
print(p)
assert(not p.start.is_solved())
print(p.start.allowed_moves())
