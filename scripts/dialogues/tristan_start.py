import adonthell

class tristan_start:
	loop = []
	strings = ["Yes?", "Hello, sir. My name is $name, and I am investigating the theft of Master Fingolson's gems.", "Well met then, $name! I am Tristan Illig, a merchant by trade, and currently stuck here at the Redwyne Inn until this business is cleared up. So may I suggest to continue your investigation.", "Well, good sir, I certainly will try. Now, do you mind if I ask you a couple of questions?", "Well, $name, I would like to be of help, but I am afraid that I know nothing that will aid you. Your time would be better spent talking to those who are involved, I would imagine.", "All the same I would like to ask you a thing or two ...", "Look, $name, I already told you! I know nothing, saw nothing, heard nothing. I would be quite pleased if you conducted your investigation efficiently so I can leave this place.", "Right then, sorry to bother you, Master Illig.", "Oh, so that is it! You are working for Silverhair! You are not really investigating anything then, are you? You are just trying to get her freed at any cost!", "Are you going to answer my questions, or not? It seems that you might have something to hide, what with all this blustering!", "Now you are accusing me, Half-Elf?! I think it is likely that Silverhair is the thief, and that your \"investigation\" will just keep me here longer while you look for anything to get her off!", "Well, if that is the case, I will leave you. But just know that I will be watching you!", "The small man before you wears a cold expression. Judging by his garments he is sort of a merchant, and a rather successful one, as it seems.", "Hello, sir. My name is $name and I wonder whether you can tell me anything about that theft.", "That is what I am doing, Master Illig. I'd like to ask you a few questions.", "And who says you are not amongst those?", "You cannot seriously consider that? Use your eyes, man! Do I look like a thief to you?", "There's a caravan with Saffron waiting for me, worth ten times the money that Dwarf claims to have lost. And if I cannot reach it in time ... I'll be ruined! Ruined!", "Nobody will buy any Saffron if those cutpurses from Elminscourt arrive with their cheap Achiote or Safflor before I have completed my business in Cirdanth.", "Who says you aren't broke already?", "Do you perhaps think my mistress is in need of stealing? Yet she is accused!", "You cannot seriously believe I would endanger my business for a few worthless pebbles!", "I warn you, Half-Elf, I am losing my patience with you and this whole affair. I am losing money by the hour, while you bumble around, bothering everyone with questions!", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer5, self.answer6, self.answer8, self.answer9, self.answer12, self.answer25, self.answer28, self.answer30, self.answer31, self.answer34, self.answer37, None]

	def clear (self):
		del self.dialogue

	def __getattr__ (self, name):
		return 0

	def run (self, answer):
		self.npc = []
		self.player = []
		self.cont = []
		self.dialogue[answer]()

	def start (self):
		self.color = 0
		self.npc.append (12)
		self.cont.append (6)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (0)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_argument") == 1:

			self.player.append (1)
			self.cont.append (1)
		else:

			self.player.append (13)
			self.cont.append (-1)
		self.player.append (-1)

	def answer23 (self):
		pass

	def answer1 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (3)
		self.cont.append (-1)
		self.player.append (14)
		self.cont.append (7)
		self.player.append (-1)

	def answer25 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (5)
		self.cont.append (2)
		self.player.append (15)
		self.cont.append (8)
		self.player.append (-1)

	def answer28 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (16)
		self.cont.append (9)
		self.player.append (-1)

	def answer30 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (10)
		self.player.append (-1)

	def answer31 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (18)
		self.cont.append (11)
		self.player.append (-1)

	def answer34 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (7)
		self.cont.append (-1)
		self.player.append (20)
		self.cont.append (12)
		self.player.append (19)
		self.cont.append (-1)
		self.player.append (-1)

	def answer36 (self):
		pass

	def answer37 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (8)
		self.cont.append (4)
		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (22)
		self.cont.append (-1)
		self.player.append (9)
		self.cont.append (5)
		self.player.append (-1)

	def answer9 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (10)
		self.cont.append (-1)
		self.player.append (11)
		self.cont.append (-1)
		self.player.append (-1)

	def answer11 (self):
		pass

	def answer7 (self):
		pass

	def answer5 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (6)
		self.cont.append (3)
		self.player.append (-1)

	def answer6 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (10)
		self.player.append (-1)

	def answer3 (self):
		pass
