import adonthell

class silverhair_start:
	loop = []
	strings = ["Oh!!", "$name, have you found anything yet?  This confinement is intolerable, as you may well understand.", "Mistress! Mistress! $name has come!", "Yes, yes dear, I see him. Please calm yourself. $name, I am relieved to see you. This situation has clearly gone beyond any civil control.", "That is certain, my lady. I am told you are suspected of theft.", "Theft indeed, and theft most grave. This Fingolson may be uncouth, but he bears considerable influence. A theft from him would have dire consequences indeed. But you know I could not have done this thing.", "Of course. Theft is not in you, my Lady, nor is deceipt. But these folk have not my confidence in you. I fear that there is no one who will speak for your honour among them.", "I see. Then it falls to you, $name, as my sole friend in this outpost, to make certain my name is clear of any stain. May I trust you to do this for me?", "Of course, my Lady.  You may trust me to the end of the world.  What little I may do is yours to command.", "What do you know of Fingolson, Lady? I have not met him before.", "Be glad of that, he is an uncouth lout. I should have known better than to deal fairly with such a rough and uncultured beast.", "I thank you for that. Now you must go, lest they find you here and imprison you as well. Free, you are my hope.", "I will try to be worthy of your trust, Lady. I will return once I know more.", "Of course, Lady. I have believed nothing but your innocense since I arrived. You may trust me to act on your behalf.", "I admit, he goaded me to rage earlier, as I am certain the guards have told you by now. But I have done nothing more than voice my anger. You must believe that.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer0, self.answer2, self.answer4, self.answer6, self.answer8, self.answer9, self.answer10, self.answer13, None]

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
		self.set_npc ("Janesta Skywind")
		self.color = adonthell.gamedata_get_character("Janesta Skywind").get_color()
		self.npc.append (0)
		self.cont.append (1)
		self.player.append (-1)
		if 1 == 0:

			self.set_npc ("Imoen Silverhair")
			self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
			self.npc.append (1)
			self.cont.append (-1)
			self.player.append (-1)

	def answer0 (self):
		self.color = adonthell.gamedata_get_character("Janesta Skywind").get_color()
		self.npc.append (2)
		self.cont.append (2)
		self.player.append (-1)

	def answer2 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (4)
		self.cont.append (3)
		self.player.append (-1)

	def answer4 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (4)
		self.player.append (9)
		self.cont.append (6)
		self.player.append (-1)

	def answer9 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (10)
		self.cont.append (7)
		self.player.append (-1)

	def answer10 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (14)
		self.cont.append (-1)
		self.player.append (13)
		self.cont.append (8)
		self.player.append (-1)

	def answer13 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (-1)
		self.player.append (-1)

	def answer12 (self):
		pass

	def answer6 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (7)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (5)
		self.player.append (-1)

	def answer8 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (-1)
		self.player.append (-1)
