import adonthell

class talan_start:
	loop = []
	strings = ["Oh, hullo again, $name.", "Listen, I really am sorry about that fuss at the gate. I hope you will not hold it against me.", "Please, my good man, do not mention it again. I assure you that I hold no grudge against you. Now, if we may go on to the business at hand?", "Oh... that. Yes, how may I help you?", "Hello, Talan. Look, I have a couple questions about the theft.", "Well, can you tell me what happened on the night of the theft?", "In the morning, of course, I heard that Master Fingolson's gems had been stolen and that Lady Silverhair was suspected of the theft.", "So you did not see or hear anything out of place that night?", "No... no, not at all.", "If you do not have any more questions ...", "No, thank you, I have a lot of work to do. You have been most helpful.", "Well, Alek Endhelm was acting very interested in what Bjarn was doing. Have you noticed him doing anything suspicious?", "Oh, he's a nasty sort, he is, sir. But other than being a busybody, I haven't noticed him doing anything that would lead me to believe that he is the thief.", "Now, if you don't have any more questions...", "I wish you had not lied to me about the night of the theft.", "Wh... what do you mean?", "You were not, as you told me, manning your post the whole night.", "Now you look here! I was, and I do not appreciate you calling me a liar.", "Oh. So you do know ... ?", "Yes I do. And I believe you left your post that night, did you not, Talan?", "Yes, I did. But please do not tell Jelom, sir! He will have my hide for sure if he finds out! Please, I beg you!", "No, you missed it. Because you were off singing, weren't you?", "I'm afraid I was. Oh what terrible mistake! I am so sorry, $name. I did not know about the noise! It is my fault that Lady Silverhair is being held in her room!", "Calm down, Talan. Now I can prove that something strange happened that night at least.", "And why was Lady Silverhair accused?", "Well, the most obvious reason is of course that she was interested in the gems, and made a trip here just to buy them.", "But she felt the quality of the gems was too low, and she is hardly pressed for money, so why would she turn around and steal the gems?", "Well, according to Jelom, what better way to throw suspicion off yourself then to claim that the stones are of low quality?", "Ah, Jelom said that, did he? What else did he say?", "Who is Jelom? Your boss?", "He is the other guard here. He is not exactly my boss, but he is older than me and has been here much longer, so he is kind of in charge.", "He found her behaviour suspicious. I mean, she is all high and mighty, acting above the rest of us, and she obviously doesn't like dwarves ...", "Wait! Why does everybody believe that she has an aversion to dwarves?", "Well, the way I heard the story, Bjarn made a point of insulting the entire elven race, loudly and publicly, upon her arrival!", "Well, as I heard it told, she had quite an argument with Master Fingolson in which she insulted the quality of his gems and then the dwarven race!", "Well, Master Fingolson can be, um ... blunt, I guess, at times, but ...", "Wasn't the argument rather Fingolson's fault, then?", "Well, I... ah, perhaps...", "Maybe you should speak to Jelom. He knows more about the theft and his reasons for suspecting her than I do...", "Well, you've talked to Jelom. You know what he thinks...", "And so I shall. Where is he?", "Yes. I do know what he thinks. That, however, does not help me too much.", "He is guarding the hallway leading to Lady Silverhair's room.", "Well, I shall go and talk to him, then. Thank you and good day.", "Ah, $name, hello.", "Hi there, Talan. Look, I...", "No, you did what you had to do, and it was only right that I got in trouble for leaving my post. And I owe you a big favour for covering for me!", "No, I understand. It was because of me shirking my duty that I did not see what happened that night. You had no choice, and I do not hold a grudge against you for doing your duty.", "All the same, I am still sorry for getting you into trouble with Jelom. Thank you for understanding.", "No, it was the least I could do. Do not worry about the favour.", "I don't know if there is any coincidence, but this visit of Master Fingolson is very unusual. You see, he is quite a regular here. He comes every other month or so, and usually stays for a week before going back.", "Usually he shows up a few days before the client, just to relax, I guess. Until about a year ago, he would spend this time in the common room, drinking ale and talking with Erek, his apprentice.", "About a year ago, things changed. When he came, he came alone. He still showed up a couple of days ahead of the client, but he no longer visited the common room much. He just stayed down in his room.", "But at this most recent visit, Bjarn got here the morning of Lady Silverhair's arrival, which was a little strange. What's more, he brought Erek again, although I thought he had finished his apprenticeship and moved on long ago.", "I see ... that is strange. Thanks for telling me, Talan!", "Couldn't it be that you missed what there was to see or hear?", "You think this argument is enough to prove Lady Silverhair's guilt?", "I ... I don't know.", "And you say Lady Silverhair was accused because she \"obviously doesn't like dwarves\"!?", "True, but practically anyone at the Inn could have thrown an eye on the stones.", "According to Jelom there is no doubt that Lady Silverhair is the thief.", "I'm anxious to hear his reasoning, then.", "I should think so Talan, considering the discomfort you caused my mistress.", "What has happened cannot be undone, I fear. But perhaps there is a little detail that might help to clear the Lady's reputation.", "I've been told about a noise that night, but you say you heard nothing.", "Should I rather call you a bard then?", "A ... noise? What noise?", "The noise of someone singing, Talan.", "According to Oliver, somebody must have been in the stables that night.", "Well, I did not notice anything, $name. That's the truth!", "It had better be, my friend..", "If I want to prove Lady Silverhair's innocence, I have little other choice, I fear.", "I, I understand. I am very sorry, $name ...", "Sure, but there is not much to tell. I was out here, making my rounds, walking around the yard like every other night.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer2, self.answer4, self.answer5, self.answer7, self.answer8, self.answer11, self.answer12, self.answer14, self.answer16, self.answer19, self.answer21, self.answer24, self.answer26, self.answer28, self.answer29, self.answer30, self.answer32, self.answer33, self.answer36, self.answer37, self.answer40, self.answer45, self.answer50, self.answer51, self.answer52, self.answer55, self.answer56, self.answer57, self.answer58, self.answer59, self.answer61, self.answer62, self.answer63, self.answer64, self.answer65, self.answer67, self.answer68, self.answer71, self.answer73, None]

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
		if self.the_npc.get_val( "apologised" ) != 1:

			self.color = self.the_npc.get_color()
			self.npc.append (1)
			self.cont.append (-1)
			self.the_npc.set_val( "apologised", 1 );

			self.player.append (2)
			self.cont.append (1)
			self.player.append (-1)
		elif adonthell.gamedata_get_quest("demo").get_val ("silverhair_free") != 1:

			self.color = self.the_npc.get_color()
			self.npc.append (0)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 1 and self.the_npc.get_val ("heard_nothing") == 1:

				self.player.append (14)
				self.cont.append (8)
			else:

				self.player.append (4)
				self.cont.append (2)
			self.player.append (-1)
		else:

			self.color = self.the_npc.get_color()
			self.npc.append (44)
			self.cont.append (-1)
			self.player.append (45)
			self.cont.append (22)
			self.player.append (-1)

	def answer45 (self):
		if adonthell.gamedata_get_quest("demo").get_val ("told_on_talan") != 1:

			self.color = self.the_npc.get_color()
			self.npc.append (46)
			self.cont.append (-1)
			self.player.append (49)
			self.cont.append (-1)
			self.player.append (62)
			self.cont.append (32)
			self.player.append (-1)
		else:

			self.color = self.the_npc.get_color()
			self.npc.append (47)
			self.cont.append (-1)
			self.player.append (48)
			self.cont.append (-1)
			self.player.append (-1)

	def answer48 (self):
		pass

	def answer62 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (63)
		self.cont.append (33)
		self.player.append (-1)

	def answer63 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (50)
		self.cont.append (23)
		self.player.append (-1)

	def answer50 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (51)
		self.cont.append (24)
		self.player.append (-1)

	def answer51 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (52)
		self.cont.append (25)
		self.player.append (-1)

	def answer52 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (53)
		self.cont.append (-1)
		self.player.append (54)
		self.cont.append (-1)
		self.player.append (-1)

	def answer54 (self):
		pass

	def answer49 (self):
		pass

	def answer4 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (5)
		self.cont.append (3)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1:

			self.player.append (11)
			self.cont.append (6)
		self.player.append (-1)

	def answer11 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (12)
		self.cont.append (7)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (13)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (-1)
		self.player.append (5)
		self.cont.append (3)
		self.player.append (-1)

	def answer10 (self):
		pass

	def answer5 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (73)
		self.cont.append (39)
		self.player.append (-1)

	def answer73 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (6)
		self.cont.append (-1)
		self.player.append (7)
		self.cont.append (4)
		self.player.append (24)
		self.cont.append (12)
		self.player.append (-1)

	def answer24 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (59)
		self.cont.append (30)
		if adonthell.gamedata_get_quest("demo").get_val ("know_low_quality") == 1:

			self.player.append (26)
			self.cont.append (13)
		self.player.append (-1)

	def answer26 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (27)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_jelom") != 2:
		

			self.player.append (29)
			self.cont.append (15)
		else:

			self.player.append (28)
			self.cont.append (14)
		self.player.append (-1)

	def answer28 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (31)
		self.cont.append (-1)
		self.player.append (32)
		self.cont.append (17)
		self.player.append (-1)

	def answer32 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (34)
		self.cont.append (-1)
		self.player.append (56)
		self.cont.append (27)
		if adonthell.gamedata_get_quest("demo").get_val ("know_bjarns_insult") == 1:

			self.player.append (33)
			self.cont.append (18)
		self.player.append (-1)

	def answer33 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (35)
		self.cont.append (-1)
		self.player.append (58)
		self.cont.append (29)
		self.player.append (36)
		self.cont.append (19)
		self.player.append (-1)

	def answer36 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (57)
		self.cont.append (28)
		self.player.append (-1)

	def answer57 (self):
		if adonthell.gamedata_get_quest("demo").get_val ("know_jelom") != 2:

			self.color = self.the_npc.get_color()
			self.npc.append (38)
			self.cont.append (-1)
			self.player.append (40)
			self.cont.append (21)
			self.player.append (43)
			self.cont.append (-1)
			self.player.append (-1)
		else:

			self.color = self.the_npc.get_color()
			self.npc.append (39)
			self.cont.append (-1)
			self.player.append (41)
			self.cont.append (-1)
			self.player.append (-1)

	def answer41 (self):
		pass

	def answer43 (self):
		pass

	def answer40 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (42)
		self.cont.append (-1)
		self.player.append (43)
		self.cont.append (-1)
		self.player.append (-1)

	def answer58 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (37)
		self.cont.append (20)
		self.player.append (-1)

	def answer37 (self):
		if adonthell.gamedata_get_quest("demo").get_val ("know_jelom") != 2:

			self.color = self.the_npc.get_color()
			self.npc.append (38)
			self.cont.append (-1)
			self.player.append (40)
			self.cont.append (21)
			self.player.append (43)
			self.cont.append (-1)
			self.player.append (-1)
		else:

			self.color = self.the_npc.get_color()
			self.npc.append (39)
			self.cont.append (-1)
			self.player.append (41)
			self.cont.append (-1)
			self.player.append (-1)

	def answer56 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (37)
		self.cont.append (20)
		self.player.append (-1)

	def answer29 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (16)
		adonthell.gamedata_get_quest("demo").set_val ("know_jelom" , 1)

		self.player.append (-1)

	def answer30 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (31)
		self.cont.append (-1)
		self.player.append (32)
		self.cont.append (17)
		self.player.append (-1)

	def answer59 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (60)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_jelom") != 2:
		

			self.player.append (29)
			self.cont.append (15)
		else:

			self.player.append (61)
			self.cont.append (31)
		self.player.append (-1)

	def answer61 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (31)
		self.cont.append (-1)
		self.player.append (32)
		self.cont.append (17)
		self.player.append (-1)

	def answer7 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (8)
		self.cont.append (5)
		self.the_npc.set_val ("heard_nothing" , 1)

		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (-1)
		self.player.append (24)
		self.cont.append (12)
		if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") == 1:

			self.player.append (68)
			self.cont.append (37)
		if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 1 and adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") != 1:

			self.player.append (55)
			self.cont.append (26)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1:

			self.player.append (11)
			self.cont.append (6)
		self.player.append (-1)

	def answer55 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (-1)
		self.player.append (16)
		self.cont.append (9)
		self.player.append (64)
		self.cont.append (34)
		self.player.append (-1)

	def answer64 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (66)
		self.cont.append (-1)
		self.player.append (67)
		self.cont.append (36)
		if adonthell.gamedata_get_quest("demo").get_val ("know_olivers_noise") == 1:

			self.player.append (68)
			self.cont.append (37)
		self.player.append (-1)

	def answer67 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (18)
		self.cont.append (-1)
		self.player.append (19)
		self.cont.append (10)
		self.player.append (-1)

	def answer19 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (71)
		self.cont.append (38)
		self.player.append (-1)

	def answer71 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (72)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("know_talan_singing" , 2)

		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (65)
		self.cont.append (35)
		self.player.append (64)
		self.cont.append (34)
		self.player.append (-1)

	def answer65 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (18)
		self.cont.append (-1)
		self.player.append (19)
		self.cont.append (10)
		self.player.append (-1)

	def answer68 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (69)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_talan_singing") == 1:

			self.player.append (21)
			self.cont.append (11)
		else:

			self.player.append (70)
			self.cont.append (-1)
		self.player.append (-1)

	def answer70 (self):
		pass

	def answer21 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (22)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (-1)
		self.player.append (-1)

	def answer23 (self):
		adonthell.gamedata_get_quest("demo").set_val ("know_talan_singing" , 2)
		

		pass

	def answer14 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (-1)
		self.player.append (16)
		self.cont.append (9)
		self.player.append (64)
		self.cont.append (34)
		self.player.append (-1)

	def answer2 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (5)
		self.cont.append (3)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop") == 1:

			self.player.append (11)
			self.cont.append (6)
		self.player.append (-1)
