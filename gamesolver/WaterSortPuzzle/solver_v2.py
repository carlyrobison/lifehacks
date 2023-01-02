VIAL_SIZE = 4

class ColorBit:
	def __init__(self, color, size):
		if size > VIAL_SIZE:
			raise Error("ColorBit larger than maximum vial size")
		self.color = color
		self.size = size

	def __repr__(self):
		return self.color * self.size

	def get_color(self):
		return self.color

	def get_size(self):
		return self.size

	def add_volume(self, qty):
		assert(self.size + qty <= VIAL_SIZE)
		self.size += qty

	def empty():
		return self.get_size() == 0

class Vial:
	def __init__(self, colorBits):
		self.colorBits = colorBits

	def peek_top(self):
		return self.colorBits[-1].get_color()

	def vial_fillage(self):
		return sum([c.get_size() for c in self.colorBits])

	def empty_space(self):
		return VIAL_SIZE - self.vial_fillage()

	def can_add_color(self, colorBit):
		if (not self.peek_top() or self.peek_top().get_color() == colorBit.get_color()):
			return self.empty_space()
		return 0  # cannot add color

	# append what we can and return the rest
	# do NOT check if we can do this
	# assume colorBit.size() <= VIAL_SIZE
	def append_colorBit(self, colorBit):
		if self.empty_space() == 0:
			raise Error("Trying to pour into a vial which doesn't have space")
		if not self.can_add_color(colorBit):  # "zero is falsey"
			raise Error("Cannot add the specified ColorBit")
		if self.empty_space() == VIAL_SIZE:  # Empty vial case
			self.colorBits.append(colorBit)
		else:
			amt_to_pour = min(self.empty_space(), colorBit.get_size())
			self.peek_top().add_volume(amt_to_pour)
			self.colorBit.add_volume(0 - amt_to_pour)  # may remove all the color from colorBit

	def __repr__(self):
		vialDisplayString = "["
		for c in self.colorBits:
			vialDisplayString += str(c)
		vialDisplayString += " " * self.empty_space()
		vialDisplayString += "]"
		return vialDisplayString

	# pour this vial into the other vial
	def pour_into(self, otherVial):
		pourable = otherVial.can_add_color(self.peek_top())
		if pourable > 0:
			otherVial.append_colorBit(self.peek_top())
			# if the top colorBit is empty after this, pop it
			if self.peek_top().empty():
				self.colorBits.pop()

v = Vial([ColorBit('a', 1), ColorBit('b', 1), ColorBit('c', 1)])
v2 = Vial([ColorBit('c', 1)])

print(v)
print(v2)
print(v.peek_top())
print(v.can_add_color(ColorBit('c', 1)))
v2.pour_into(v)
print(v)
print(v2)

