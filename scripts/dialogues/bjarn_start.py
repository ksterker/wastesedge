import adonthell

class bjarn_start:
	loop = []
	strings = ["You try the door, but find it locked. From within the room you hear a deep voice.", "At the door to their room, Erek produces a key and unlocks it.", "Maybe I should not be doing this, but I do want my master to get his stones back.", "I do not wish to be disturbed right now, so please go away! First I am burglarised, and now I can get no peace with all the busybodies running around, making my tragedy their business!", "Erek, who is this, and why have you let him in?", "This is $name, master, and he is investigating the theft of your gems. He wanted to talk to you, and I thought that maybe he could help.", "Yes, sir, that is correct. I am here on the behalf of Lady Silverhair, trying to get to the bottom of the disappearance of your stones.", "I think that \"theft\" is a better word for it than disappearance.", "Theft, then, if you prefer. Call it what you may, I would like to recover the gems and clear Lady Silverhair's name. Would you mind answering a question or two?", "Actually, I would mind. I am sure that you already know what happened, so nothing can be gained from bothering me. I would rather you \"recover\" the gems from your mistress and return them to me!", "Sir, please try to be reasonable. Have you even considered the possibility that Lady Silverhair is not the thief?", "What, and ignore all the evidence to the contrary? She came here specifically to buy my gems, insulted their quality to weasel out of paying for them, and then stole them when the first opportunity presented itself! I cannot believe that you have the audacity to ask me questions about this! Please leave!", "You knock on Bjarn's door. After a moment, he swings it open, obviously not happy with the disturbance.", "Look, Half-Elf, I told you that I do not want to be bothered!", "I have an important question for you. How long has Erek been working for you?", "I am sorry, but some things have come to light since we last talked. It seems that you made some insulting remarks about elves to Lady Silverhair probably apon her arrival. That is probably what set her on edge, even before the negotiations started!", "I am sorry, but I need to know something. How well do you know Alek?", "You cannot possibly suspect Erek! He is so honest and idealistic that even if he had stolen the gems, he would confess the crime immediately! Do not waste my time with such ridiculous accusations!", "This is important! Alek has assured me that he heard nothing on the night of the theft, and this leads me to believe that the theft may have been committed before you went to bed. I understand that Erek packed the gems away that night?", "Oh, Alek told you. Now that is rich!", "What makes you say that?", "I may have made some harmless remarks, yes. What does that prove? Now please stop wasting my time!", "Alek Endhelm? That shifty-looking mercenary? Not at all, until two days ago.", "What happened two days ago?", "Looking at the guy, I could tell that he was up to no good! He was really interested in my business as soon as I got here, that is for sure! He was snooping around, poking his nose into my affairs.", "And what happened?", "He offered his services to me as a guard! It is true that the roads have been getting more and more dangerous recently, but I think they would be even more dangerous with the likes of him \"guarding\" me! So I told him, in no uncertain terms, that I didn't like his looks and didn't want him snooping around my room anymore!", "He was snooping around your room?", "Yeah, trying to hear something interesting, I guess. But I don't think you can pin the crime on him to clear your mistress!", "What makes you so sure that he is innocent, if you think so poorly of him?", "Come on, a clumsy, lumbering human sneaking into my room while I am asleep and stealing my gems! An ogre would be a more likely sneak thief than Alek Endhelm! He couldn't pick a lock if he had the key! It had to have been one of your kind or a real elf, that is for sure. Now, I am a busy man, so please stop wasting my time!", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer0, self.answer1, self.answer2, self.answer4, self.answer6, self.answer8, self.answer10, self.answer12, self.answer14, self.answer15, self.answer16, self.answer18, self.answer20, self.answer23, self.answer25, self.answer27, self.answer29, None]

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
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 3:

			self.color = 0
			self.npc.append (12)
			self.cont.append (8)
			self.player.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 2:

			self.color = 0
			self.npc.append (1)
			self.cont.append (2)
			adonthell.gamedata_get_quest("demo").set_val ("bjarn_door_open" , 3)

			self.player.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 0 or adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 1:

			self.color = 0
			self.npc.append (0)
			self.cont.append (1)
			adonthell.gamedata_get_quest("demo").set_val ("bjarn_door_open" , 1)

			self.player.append (-1)

	def answer0 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (-1)

	def answer1 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (2)
		self.cont.append (3)
		self.player.append (-1)

	def answer2 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (4)
		self.cont.append (4)
		self.player.append (-1)

	def answer4 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (5)
		self.player.append (-1)

	def answer6 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (7)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (6)
		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		adonthell.gamedata_get_character("Erek Stonebreaker").set_val ("leave_bjarn" , 1)
		adonthell.gamedata_get_character("Erek Stonebreaker").set_schedule_active (1)

		self.player.append (10)
		self.cont.append (7)
		self.player.append (-1)

	def answer10 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (13)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1:

			self.player.append (16)
			self.cont.append (11)
		if adonthell.gamedata_get_quest("demo").get_val ("know_bjarns_insult") == 1:

			self.player.append (15)
			self.cont.append (10)
		if adonthell.gamedata_get_quest("demo").get_val ("ask_packed_gems") == 1:

			self.player.append (14)
			self.cont.append (9)
		self.player.append (-1)

	def answer14 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (12)
		self.player.append (-1)

	def answer18 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (19)
		self.cont.append (-1)
		self.player.append (20)
		self.cont.append (13)
		self.player.append (-1)

	def answer20 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (24)
		self.cont.append (-1)
		self.player.append (25)
		self.cont.append (15)
		self.player.append (-1)

	def answer25 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (-1)
		self.player.append (27)
		self.cont.append (16)
		self.player.append (-1)

	def answer27 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (28)
		self.cont.append (-1)
		self.player.append (29)
		self.cont.append (17)
		self.player.append (-1)

	def answer29 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (-1)

	def answer15 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (22)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (14)
		self.player.append (-1)

	def answer23 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (24)
		self.cont.append (-1)
		self.player.append (25)
		self.cont.append (15)
		self.player.append (-1)
