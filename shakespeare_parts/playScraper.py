# Scrapes a Shakespeare play in MIT txt form and generates a model of the play
# from which we know who speaks with whom
from bs4 import BeautifulSoup

class Play:
	def __init__(self, filename):
		self.filename = filename
		self.scenes = []
		self.characters = []
		self.parsePlayText()

	def parsePlayText(self):
		f = open(self.filename, "r")
		soup = BeautifulSoup(f, 'html.parser')
		# print(soup)
		acts = soup.find_all('h3')
		print([a.text.strip() for a in acts])
		for a in acts:
			# doesn't work :(
			print(a.find('blockquote'))

class Scene:
	def __init__(self, actNum, sceneNum):
		self.act = actNum
		self.scene = sceneNum
		self.characters = []

	def __repr__(self):
		return "Act {0} Scene {1}".format(self.act, self.scene)

	def shortform(self):
		return "{0}.{1}".format(self.act, self.scene)

class Character:
	def __init__(self, name):
		self.name = name
		self.all_names = [name]
		self.scenes = []

	def __repr__(self):
		return self.name + " ({0})".format(", ".join([s.shortform() for s in self.scenes]))






## Testing
p = Play("Coriolanus_Entire_Play.html")
s = Scene(1, 1)
p.scenes = [s, Scene(1, 2)]
c = Character("Lily")
c.scenes = [s, Scene(1, 3)]
p.characters = [c]
print([s for s in p.scenes])
print([c for c in p.characters])


