import adonthell

class sarin_start:
	loop = []
	strings = ["What insolence!  $name, do you believe the depths of what they have done to our Lady?  To accuse her of common theft, as if she was a human!  And to lock her away in this tiny, dirty room!  I tell you, I cannot bear it.", "I understand, Sarin, but we must bear this for now.  At least until I have been able to uncover the truth.", "The truth?  The truth is that our Lady is innocent and that, that Dwarf ruffian, he's a liar.", "Perhaps so.  Hopefully, we shall see whether he is.  What do you know of him?", "Very little, I'm happy to say.  I was in the common room downstairs, arranging for dinner, when the Lady came out of the room they were in, as angry as I have ever seen her.  That barbarian must have done something terrible to put her in such a state.", "I gather he is always difficult.  Do you know anything else?  About the other people at the inn, perhaps?", "Nay, not a thing.  An uncouth lot, save for the one.  An artist, I think.  Lady Silverhair had words with her when we arrived, but Janesta and I were too busy to learn her name.", "I'll have to speak to her.  Perhaps she may know something.  Thank you, Sarin.  I'm glad you are here to watch over the Lady during this trouble.", "I wish I could do more, $name.  Good luck to you.", "Her name is Frostbloom.  Not terribly friendly, but the Lady thinks highly of her talents.  She went so far as to buy that figurine on the mantle.", "Is that one of hers?  She is indeed talented.  I may only hope you are as talented in ending this trouble.  Good luck to you, $name.", "He seems to be telling the truth about the theft.  But I cannot believe that our Lady did the deed.  There must be a true thief about.", "I beg you hurry and find him, then.  For every minute you do not, is one minute closer our Lady is to peril.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer3, self.answer5, self.answer7, self.answer9, self.answer11, None]

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
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (0)
		self.cont.append (-1)
		self.player.append (1)
		self.cont.append (1)
		self.player.append (-1)

	def answer1 (self):
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (3)
		self.cont.append (2)
		self.player.append (11)
		self.cont.append (6)
		self.player.append (-1)

	def answer11 (self):
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (12)
		self.cont.append (-1)
		self.player.append (-1)

	def answer3 (self):
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (4)
		self.cont.append (-1)
		self.player.append (5)
		self.cont.append (3)
		self.player.append (-1)

	def answer5 (self):
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (6)
		self.cont.append (-1)
		self.player.append (7)
		self.cont.append (4)
		if adonthell.gamedata_get_quest("demo").get_val ("know_frostbloom") == 1:

			self.player.append (9)
			self.cont.append (5)
		self.player.append (-1)

	def answer9 (self):
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (10)
		self.cont.append (-1)
		self.player.append (-1)

	def answer7 (self):
		self.color = adonthell.gamedata_get_character("Sarin Trailfollower").get_color()
		self.npc.append (8)
		self.cont.append (-1)
		self.player.append (-1)
