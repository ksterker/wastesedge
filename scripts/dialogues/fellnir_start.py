import adonthell

class fellnir_start:
	loop = []
	strings = ["What do you want from me?  I don't know anything.", "I am with Lady Silverhair, and I am trying to prove her innocense.  Do you know what happened here?", "Fellnir looks suspiciously at you.  He absently jots something down in a notebook and shifts one of his beakers slightly.", "Ask somebody else.  Anybody.  I just keep to myself and I don't know anything.", "He turns his attention back to his work, poring over the array of steaming liquids and decanters of unknown origin.  You cannot seem to get his attention again.", "You've been such a great help sir, I hate to bother you again.  But I seem to have angered the innkeeper's wife, and I need her help.  Have you any advice?", "Excuse me? I realize you know nothing of the theft, but you must know the people of this inn well enough. Is there any way the guard could be convinced to allow me into my Lady's room?", "Pardon me, good sir?  I hate to trouble you, but do you know this Fingolson well?  I need to enter his room but he will not allow me.", "I'm still trying to find information that may help my employer.  Are you certain you cannot help?", "Do you know anything about strange noises the night of the theft?", "I have better things to do than pay attention to what idle people do with their time.", "Fellnir doesn't even look up at you as you speak.  He mutters a little, \"Take equal parts of vitriol, nitre and sal ammoniac ...\"  Then he speaks more clearly to you.", "I would have thought elves and their sort would be more creative.  There's more than one way into a room, you know.  Now leave me be.", "Fellnir picks up a decanter and puts it down, then peers through a length of piping.  He blows into it, then inserts the end into the bottle.  After a while, he turns to you.", "I wouldn't open my door either to someone as nosy as you.  Try asking someone he likes.  Erek, maybe.  So long as you're not talking to me.  I don't know anything, so I wish you'd stop bothering me.", "Fellnir pours a blueish liquid into one primarily red, and the resulting mixture turns inexplicably green. He swirls it before his eyes for a moment, then takes a sip. By the look on his face, it doesn't taste very good.", "Well, of course she's upset.  You got a friend of hers in trouble.  I don't want anything to do with it, you straighten it out with the young guard yourself.  I'm just keeping to myself here.", "As you finish your question, bubbles begin appearing in a bottle that has no visible flame under it.  It boils for a few moments, until suddenly there is a puff of steam and half the liquid vanishes.  Fellnir is not impressed at this.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer2, self.answer3, self.answer5, self.answer6, self.answer7, self.answer8, self.answer9, self.answer10, self.answer11, self.answer12, self.answer13, self.answer14, self.answer15, self.answer16, self.answer17, None]

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
		self.set_npc ("Fellnir Kezular")
		self.color = adonthell.gamedata_get_character("Fellnir Kezular").get_color()
		self.npc.append (0)
		self.cont.append (-1)
		if self.the_npc.get_val ("talked_to") == 0:

			self.player.append (1)
			self.cont.append (1)
		elif adonthell.gamedata_get_quest("demo").get_val ("know_jelom") == 2 and adonthell.gamedata_get_character("Imoen Silverhair").get_val ("talked_to") == 0:

			self.player.append (6)
			self.cont.append (5)
		elif adonthell.gamedata_get_quest("demo").get_val ("told_on_talan") == 1:

			self.player.append (5)
			self.cont.append (4)
		elif adonthell.gamedata_get_quest("demo").get_val ("know_noise") != 0 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 0:

			self.player.append (9)
			self.cont.append (8)
		elif adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 1:

			self.player.append (7)
			self.cont.append (6)
		else:

			self.player.append (8)
			self.cont.append (7)
		self.player.append (-1)

	def answer8 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = 0
		self.npc.append (2)
		self.cont.append (2)
		self.player.append (-1)

	def answer2 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (3)
		self.player.append (-1)

	def answer3 (self):
		self.color = 0
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (-1)

	def answer7 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = 0
		self.npc.append (13)
		self.cont.append (12)
		self.player.append (-1)

	def answer13 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (14)
		self.cont.append (13)
		self.player.append (-1)

	def answer14 (self):
		self.color = 0
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (-1)

	def answer9 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = 0
		self.npc.append (17)
		self.cont.append (16)
		self.player.append (-1)

	def answer17 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (10)
		self.cont.append (9)
		self.player.append (-1)

	def answer10 (self):
		self.color = 0
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (-1)

	def answer5 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = 0
		self.npc.append (11)
		self.cont.append (10)
		self.player.append (-1)

	def answer11 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (16)
		self.cont.append (15)
		self.player.append (-1)

	def answer16 (self):
		self.color = 0
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (-1)

	def answer6 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = 0
		self.npc.append (15)
		self.cont.append (14)
		self.player.append (-1)

	def answer15 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (12)
		self.cont.append (11)
		self.player.append (-1)

	def answer12 (self):
		self.color = 0
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (-1)

	def answer1 (self):
		self.the_npc.set_val ("talked_to" , 1)

		self.set_npc (self.the_npc.get_id())
		self.color = 0
		self.npc.append (2)
		self.cont.append (2)
		self.player.append (-1)
