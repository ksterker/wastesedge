import adonthell

class bjarn_start:
	loop = []
	strings = ["You try the door, but find it locked. From within the room you hear a deep voice.", "At the door to their room, Erek produces a key and unlocks it.", "Maybe I should not be doing this, but I do want my master to get his stones back.", "I do not wish to be disturbed right now, so please go away! First I am burgled, and now I can get no peace with all the busybodies running around, making my tragedy their business!", "Erek, who is this, and why have you let him in?", "This is $name, master, and he is investigating the theft of your gems. He wanted to talk to you, and I thought that maybe he could help.", "Yes, sir, that is correct. I am here on the behalf of Lady Silverhair, trying to get to the bottom of the disappearance of your stones.", "I think that \"theft\" is a better word for it than disappearance.", "Theft, then, if you prefer. Call it what you may, I would like to recover the gems and clear Lady Silverhair's name. Would you mind answering a question or two?", "Actually, I would mind. I am sure that you already know what happened, so nothing can be gained from bothering me. I would rather you \"recover\" the gems from your mistress and return them to me!", "Sir, please try to be reasonable. Have you even considered the possibility that Lady Silverhair is not the thief?", "What, and ignore all the evidence to the contrary? She came here specifically to buy my gems, insulted their quality to weasel out of paying for them, and then stole them when the first opportunity presented itself!", "Bjarn looks you up and down with a stern expression on his face; obviously he is not happy with the disturbance.", "Look, Half-Elf, I told you that I do not want to be bothered!", "I'm just wondering whether Erek might have taken the gems.", "Why did you insult Lady Silverhair upon her arrival? You set her on edge, even before the negotiations started!", "Don't you think that Alek Endhelm might be more likely a thief than Lady Silverhair?", "You cannot possibly suspect Erek! He is so honest and idealistic that even if he had stolen the gems, he would confess the crime immediately! Do not waste my time with such ridiculous accusations!", "But Alek Endhelm leads me to believe that the theft may have been committed before you went to bed.", "Ha! That sounds just like Alek Endhelm. You are a fool to be taken in by that scoundrel's words. The truth is that I personally packed the gems after Erek went to bed. That is, the theft has been committed later that night.", "You blame me for your mistress' absence of humour? All I wanted was to liven up the atmosphere before turning to business. I can see nothing wrong with that. Now please stop wasting my time!", "Alek Endhelm? That shifty-looking mercenary? He is surely up to no good, but I doubt you can pin the crime on him to clear your mistress.", "But he was seen snooping around the parlour during negotiations.", "Well, it is true. He was really interested in my business as soon as I got here! He was snooping around, poking his nose into my affairs. Then he offered me his service as a guard.", "The roads have been getting more and more dangerous recently, that's for sure. But they would be even more dangerous with the likes of him \"guarding\" me! So I told him, in no uncertain terms, that I didn't like his looks!", "What makes you so sure that he is innocent, if you think so poorly of him?", "Come on, a clumsy, lumbering human sneaking into my room while I am asleep and stealing my gems! An ogre would be a more likely sneak thief than Alek Endhelm! He couldn't pick a lock if he had the key!", "I cannot believe that you have the audacity to ask me questions about this! Please leave!", "No, it had to have been one of your kind or a real Elf, that is for sure. Now, I am a busy man, so please stop wasting my time!", "And you don't think he stole your gems in an act of revenge?", "To me it seems as if Alek was just curious about your gems.", "And so was your Lady Silverhair! Listen, I don't know why I should be speaking with you, if all you care about is freeing your mistress. If you want to make yourself useful you better go and retrieve my Chrysoberyls.", "Well, you know Erek best, I guess.", "Really? According to Erek, you were asleep already when he started packing.", "Asleep? I? Certainly not! I was just taking a rest, perhaps. Later I put the pouch with the gems into our luggage, from where the thief - your fine mistress - stole it during the night!", "I can't believe I am justifying myself in front of the thief's servant! Why am I talking to you at all! You are not doing anything to retrieve my Chrysoberyls. All you care about is freeing your mistress!", "You are but wasting my time! Out of my sight you go!", "Not even if I've found one of your \"Catseyes\"!", "Really? I ... I am impressed. Let me see! And tell me where you found it.", "In the stables.", "In Lady Silverhair's luggage.", "Ha, I knew it! Who else but Silverhair had reasons and the skills to steal my gems? I'm glad you are finally seeing the truth. Now there can be no more doubt about her guilt. Come, we must inform the guards!", "Not so fast! According to Erek, this gem is no Catseye.", "But Lady Silverhair swears that this is no Catseye.", "Huh? You surely won't trust Erek's word over my own? He has much to learn yet. I am an expert, and I tell you that this gem is a Chrysoberyl Catseye. Now hand it over, so I can take it to Jelom.", "The thief? Of course she would say that! Even you cannot be that foolish to take her word over mine. I tell you that this gem is a Chrysoberyl Catseye. Now hand it over, so I can take it to Jelom.", "Don't worry Master Fingolson, I will take care of that myself.", "I'm sorry, but I won't give this pieve of evidence out of my hands.", "Oh well, it's not as if you could run off with the gem I suppose. You may keep it for now, as long as you see to it that Silverhair gets what she deserves. Now be on your way!", "In the stables? Can't you precise that some more? After all, the place you found the gem might give us a clue about the thief.", "It was hidden in Lady Silverhair's luggage.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer0, self.answer1, self.answer2, self.answer4, self.answer6, self.answer8, self.answer10, self.answer11, self.answer12, self.answer14, self.answer15, self.answer16, self.answer18, self.answer22, self.answer23, self.answer25, self.answer26, self.answer29, self.answer30, self.answer33, self.answer34, self.answer35, self.answer37, self.answer39, self.answer40, self.answer42, self.answer43, self.answer46, self.answer47, self.answer102, None]

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
			self.cont.append (9)
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
		self.cont.append (8)
		self.player.append (-1)

	def answer11 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (27)
		self.cont.append (-1)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (13)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") > 0:

			self.player.append (37)
			self.cont.append (23)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1:

			self.player.append (16)
			self.cont.append (12)
		if adonthell.gamedata_get_quest("demo").get_val ("know_bjarns_insult") == 1:

			self.player.append (15)
			self.cont.append (11)
		if adonthell.gamedata_get_quest("demo").get_val ("ask_packed_gems") == 1 or adonthell.gamedata_get_quest("demo").get_val ("ask_packed_gems") == 2:

			self.player.append (14)
			self.cont.append (10)
		self.player.append (-1)

	def answer14 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (13)
		self.player.append (32)
		self.cont.append (-1)
		self.player.append (-1)

	def answer32 (self):
		pass

	def answer18 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (19)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("ask_packed_gems") == 2:

			self.player.append (33)
			self.cont.append (20)
		self.player.append (-1)

	def answer33 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (34)
		self.cont.append (21)
		self.player.append (-1)

	def answer34 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (35)
		self.cont.append (22)
		self.player.append (-1)

	def answer35 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (36)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("ask_packed_gems" , 3)

		self.player.append (-1)

	def answer15 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (22)
		self.cont.append (14)
		self.player.append (25)
		self.cont.append (16)
		self.player.append (-1)

	def answer25 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (17)
		self.player.append (-1)

	def answer26 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (28)
		self.cont.append (-1)
		self.player.append (-1)

	def answer22 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (23)
		self.cont.append (15)
		self.player.append (-1)

	def answer23 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (24)
		self.cont.append (-1)
		self.player.append (29)
		self.cont.append (18)
		self.player.append (30)
		self.cont.append (19)
		self.player.append (-1)

	def answer30 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (31)
		self.cont.append (-1)
		self.player.append (-1)

	def answer29 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (17)
		self.player.append (-1)

	def answer37 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (38)
		self.cont.append (-1)
		self.player.append (39)
		self.cont.append (24)
		self.player.append (40)
		self.cont.append (25)
		self.player.append (-1)

	def answer40 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (41)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 1 == 1:

			self.player.append (43)
			self.cont.append (27)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 2 == 2:

			self.player.append (42)
			self.cont.append (26)
		self.player.append (-1)

	def answer42 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (44)
		self.cont.append (-1)
		self.player.append (46)
		self.cont.append (28)
		self.player.append (47)
		self.cont.append (29)
		self.player.append (-1)

	def answer47 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (48)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("bjarn_lies" , 1)

		self.player.append (-1)

	def answer46 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (48)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("bjarn_lies" , 1)

		self.player.append (-1)

	def answer43 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (45)
		self.cont.append (-1)
		self.player.append (46)
		self.cont.append (28)
		self.player.append (47)
		self.cont.append (29)
		self.player.append (-1)

	def answer39 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (49)
		self.cont.append (-1)
		self.player.append (50)
		self.cont.append (30)
		self.player.append (-1)

	def answer102 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (41)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 1 == 1:

			self.player.append (43)
			self.cont.append (27)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 2 == 2:

			self.player.append (42)
			self.cont.append (26)
		self.player.append (-1)
