import adonthell

class tristan_start:
	loop = []
	strings = ["Yes?", "Hello, sir. My name is $name, and I am investigating the theft of Master Fingolson's gems.", "Oh, well met then, $name! I am Tristan Illig, a merchant by trade, and I am currently stuck in this trading post until this theft is cleared up. And you are the man who will do it?", "Well, good sir, I certainly will try. Now, do you mind if I ask you a couple of questions?", "Well, $name, I would like to be of help, but I am afraid that I know nothing that will aid you. Your time would be better spent talking to those who are involved, I would imagine.", "All the same, Master Illig, I would like to ask you a thing or two...", "Look, $name, I already told you! I know nothing, saw nothing, heard nothing. I would be quite pleased if you conducted your investigation effeciently so I can leave this place and rejoin the caravan! Now please, get to the investigating!", "Right then, sorry to bother you, Master Illig.", "Now look here, Tristan! You will cooperate with my investigation if you ever want to leave this place! My mistress is locked in her room, falsely suspected of this crime, and I intend to clear her name!", "Oh, so that is it! You are not really investigating anything, are you? You are just trying to get her freed at any cost! I warn you, Half-Elf, I am losing my patience with you and this whole affair. I am losing money by the minute, while you bumble around, bothering everyone with questions!", "Are you going to answer my questions, or not? It seems that you might have something to hide, what with all this blustering!", "Now you are accusing me, Half-Elf?! I think it is likely that Silverhair is the thief, and that your \"investigation\" will just keep me here longer while you look for anything to get her off!", "Well, if that is the case, I will leave you. But just know that I will be watching you!", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer3, self.answer5, self.answer8, self.answer10, None]

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
		self.color = self.the_npc.get_color()
		self.npc.append (0)
		self.cont.append (-1)
		self.player.append (1)
		self.cont.append (1)
		self.player.append (-1)

	def answer1 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (3)
		self.cont.append (2)
		self.player.append (-1)

	def answer3 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (5)
		self.cont.append (3)
		self.player.append (-1)

	def answer5 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (6)
		self.cont.append (-1)
		self.player.append (7)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (4)
		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (5)
		self.player.append (-1)

	def answer10 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (-1)
		self.player.append (-1)

	def answer12 (self):
		pass

	def answer7 (self):
		pass
