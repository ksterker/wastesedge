import adonthell

class jelom_start:
	loop = []
	strings = ["Halt there! No-one is allowed into the prisoner's room!", "Stop right there, half-elf! You know that you are not allowed in there!", "No-one is allowed into the prisoner's room, so please leave this hallway!", "You again, half-elf? What do you want this time?", "Ah, you must be Jelom. Talan told me that I could find you here.", "And just who are you to prevent me from entering, sir?", "Nice to see you again, Jelom. Look, I have some more questions for you.", "Look, Jelom, I found out something that will cast some serious doubt on Lady Silverhair having committed the theft!", "My name is Jelom, and I am the chief of the guard at Waste's Edge! Who the hell are you?", "Who are you, and why were you looking for me?", "My name is $name. I'm investigating the theft and I have a few questions for you.", "And what might those questions be, half-elf?", "I doubt that, but since I won't get any peace from your pestering until you tell me, go ahead.", "You trust in the overactive imagination of some little kid? I know from Talan that everything was quiet during the night.  And I take the word of my own guard over Oliver's!", "Talan did not hear anything that night, because he was not at his post.", "What do you mean? Why wasn't he at his post?", "He sneaked away to take a nap.", "He wandered off to practise singing, of all things!", "A nap? I knew it! I had suspected that he caught some shuteye on duty from time to time, but have never caught him at it! He is in big trouble, this time!", "Singing? What, does the fool want to be a bard now? He is in big trouble now!", "But regardless of that, how do you know that it was not Silverhair herself who went to the stables and caused the noise? After stealing Master Fingolsons gems!", "Erek actually packed the gems, according to Alek. Do you think he could be mixed up in this?", "Alek Endhelm was eavesdropping outside the room during the negotiations, according to Erek. Do you think he could be mixed up in this?", "Erek? Come on, don't be stupid. You are a more likely thief than Erek, and you weren't even here! It is just like Alek to tell you things like that!", "Why do you say that?", "Don't get excited, half-elf. Alek looks like scum, and probably is, being a mercenary, but there is no reason to suspect him of the theft. In fact, I hear that he offered his services to Bjarn as a guard.", "You don't think that is a little suspicious?", "Look, half-elf, I am getting pretty damn tired of you and your questions. This investigation has nothing to do with you, so why don't you keep your nose out of it? Now get the hell out of here!", "Can you tell me what happened on the night of the theft?", "No, I can't. Talan was on guard duty. Go bother him.", "You won't tell me anything about your own investigation, then?", "I am Lady Silverhair's clerk. I demand to see her immediately!", "It does not matter who you are. None may leave this room and none may enter. 'Tis as simple as that.", "Who's order is this?", "What harm could it do if I spoke to my mistress?", "Mine! As long as Silverhair does not give in and hands out Master Fingolson's gems she's staying where she is. On her own!", "I assure you, Lady Silverhair is innocent.", "Really? Too bad then, that all the facts I know prove the opposite.", "Now get lost!", "How should I know!? But I'm not taking any risk.", "The stableboy, Oliver, heard a noise in the stables, well after both Bjarn and Lady Silverhair had gone to their rooms.", "But that noise might have been caused by the real thief!", "I say this is crap. You'll need better arguments then mere fantasies of a child to convince me. Now don't hold me off my duty!", "Did you know that Talan left his post during the night of the theft?", "Her servants could certainly confirm that she did not leave the room that night.", "Ha! They'd do everything to please their mistress. I wouldn't trust in any of their words.", "Well, everybody knows that Elves can move absolutly silent.", "Hm ... yes, that's a fact. You are right, Half-Elf. Something strange is going on.", "Maybe you should go in and see if your mistress can shed some light on the whole affair. However, until we find a new suspect, I'll be keeping an eye on her.", "What!? Are you telling me the kid was right after all? I don't believe it! Can't I even trust my own men any more!? Tell me, what was he doing?", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer4, self.answer5, self.answer6, self.answer7, self.answer10, self.answer14, self.answer16, self.answer17, self.answer18, self.answer19, self.answer21, self.answer22, self.answer24, self.answer26, self.answer28, self.answer30, self.answer31, self.answer33, self.answer34, self.answer36, self.answer37, self.answer39, self.answer40, self.answer41, self.answer43, self.answer44, self.answer46, self.answer47, None]

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
		if self.the_player.get_val ("at_silverhairs_door") == 1 and adonthell.gamedata_get_quest("demo").get_val ("know_jelom") != 2:
		

			self.color = self.the_npc.get_color()
			self.npc.append (0)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("know_jelom") == 1:

				self.player.append (4)
				self.cont.append (1)
			else:

				self.player.append (5)
				self.cont.append (2)
			self.player.append (-1)
		elif self.the_player.get_val ("at_silverhairs_door") == 1:

			self.color = self.the_npc.get_color()
			self.npc.append (1)
			self.cont.append (-1)
			self.player.append (31)
			self.cont.append (17)
			if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 2 and self.the_npc.get_val ("not_convinced") == 1:

				self.player.append (43)
				self.cont.append (25)
			if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") == 1 and self.the_npc.get_val ("not_convinced") == 0:

				self.player.append (7)
				self.cont.append (4)
			if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") != 2:

				self.player.append (6)
				self.cont.append (3)
			self.player.append (-1)
		elif self.the_player.get_val ("at_silverhairs_door") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_jelom") != 2:

			self.color = self.the_npc.get_color()
			self.npc.append (2)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("know_jelom") == 1:

				self.player.append (4)
				self.cont.append (1)
			else:

				self.player.append (5)
				self.cont.append (2)
			self.player.append (-1)
		else:
		

			self.color = self.the_npc.get_color()
			self.npc.append (3)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 2 and self.the_npc.get_val ("not_convinced") == 1:

				self.player.append (43)
				self.cont.append (25)
			if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") != 2:

				self.player.append (6)
				self.cont.append (3)
			if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") == 1 and self.the_npc.get_val ("not_convinced") == 0:

				self.player.append (7)
				self.cont.append (4)
			self.player.append (-1)

	def answer6 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (11)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 2 and self.the_npc.get_val ("not_convinced") == 1:

			self.player.append (43)
			self.cont.append (25)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1 and adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") != 2:

			self.player.append (22)
			self.cont.append (12)
		if adonthell.gamedata_get_quest("demo").get_val ("ask_packed_gems") == 1 and adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") != 2:

			self.player.append (21)
			self.cont.append (11)
		if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") == 1 and self.the_npc.get_val ("not_convinced") == 0:

			self.player.append (7)
			self.cont.append (4)
		else:

			self.player.append (28)
			self.cont.append (15)
		self.player.append (-1)

	def answer28 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (29)
		self.cont.append (-1)
		self.player.append (30)
		self.cont.append (16)
		self.player.append (-1)

	def answer30 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (27)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("know_jelom" , 2)

		self.player.append (-1)

	def answer21 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (23)
		self.cont.append (-1)
		self.player.append (24)
		self.cont.append (13)
		self.player.append (-1)

	def answer24 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (26)
		self.cont.append (14)
		self.player.append (-1)

	def answer26 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (27)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("know_jelom" , 2)

		self.player.append (-1)

	def answer22 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (26)
		self.cont.append (14)
		self.player.append (-1)

	def answer7 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (12)
		self.cont.append (-1)
		self.player.append (40)
		self.cont.append (23)
		self.player.append (-1)

	def answer40 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (13)
		self.cont.append (-1)
		self.player.append (41)
		self.cont.append (24)
		if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 2:

			self.player.append (14)
			self.cont.append (6)
		self.player.append (-1)

	def answer14 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (-1)
		self.player.append (16)
		self.cont.append (7)
		self.player.append (17)
		self.cont.append (8)
		self.player.append (-1)

	def answer17 (self):
		adonthell.gamedata_get_quest("demo").set_val ("told_on_talan" , 1)

		self.color = self.the_npc.get_color()
		self.npc.append (19)
		self.cont.append (10)
		self.player.append (-1)

	def answer19 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (44)
		self.cont.append (26)
		self.player.append (46)
		self.cont.append (27)
		self.player.append (-1)

	def answer46 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (47)
		self.cont.append (28)
		self.player.append (-1)

	def answer47 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (48)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("silverhair_free" , 1)

		self.player.append (-1)

	def answer44 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (45)
		self.cont.append (-1)
		self.player.append (46)
		self.cont.append (27)
		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (18)
		self.cont.append (9)
		self.player.append (-1)

	def answer18 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (44)
		self.cont.append (26)
		self.player.append (46)
		self.cont.append (27)
		self.player.append (-1)

	def answer41 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (42)
		self.cont.append (-1)
		self.the_npc.set_val ("not_convinced" , 1     )

		self.player.append (-1)

	def answer43 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (49)
		self.cont.append (-1)
		self.player.append (16)
		self.cont.append (7)
		self.player.append (17)
		self.cont.append (8)
		self.player.append (-1)

	def answer31 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (32)
		self.cont.append (-1)
		self.player.append (33)
		self.cont.append (18)
		self.player.append (34)
		self.cont.append (19)
		self.player.append (-1)

	def answer34 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (39)
		self.cont.append (22)
		self.player.append (-1)

	def answer39 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (38)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("know_jelom" , 2)

		self.player.append (-1)

	def answer33 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (35)
		self.cont.append (-1)
		self.player.append (34)
		self.cont.append (19)
		self.player.append (36)
		self.cont.append (20)
		self.player.append (-1)

	def answer36 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (37)
		self.cont.append (21)
		self.player.append (-1)

	def answer37 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (38)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("know_jelom" , 2)

		self.player.append (-1)

	def answer5 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (8)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (5)
		self.player.append (31)
		self.cont.append (17)
		self.player.append (-1)

	def answer10 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (11)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 2 and self.the_npc.get_val ("not_convinced") == 1:

			self.player.append (43)
			self.cont.append (25)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1 and adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") != 2:

			self.player.append (22)
			self.cont.append (12)
		if adonthell.gamedata_get_quest("demo").get_val ("ask_packed_gems") == 1 and adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1 and adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") != 2:

			self.player.append (21)
			self.cont.append (11)
		if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") == 1 and self.the_npc.get_val ("not_convinced") == 0:

			self.player.append (7)
			self.cont.append (4)
		else:

			self.player.append (28)
			self.cont.append (15)
		self.player.append (-1)

	def answer4 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (5)
		self.player.append (-1)
