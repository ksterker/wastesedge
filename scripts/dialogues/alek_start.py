import adonthell

class alek_start:
	loop = []
	strings = ["And who do we have here? A damn freak Half-Elf I say!", "That's $name, you ass! I'm working for Lady Silverhair.", "For Lady Silverhair, eh? Now that scares the shit out of me, Half-Elf. Go and bother somebody else!", "I'll be damned if that's not our freakish Half-Elf! Still pokin' your nose in other peoples business?", "Listen! Need we really go through all this crap again?", "You're getting on my nerves, Half-Elf. Go ahead then, ask your stupid questions.", "I don't like you either, friend. But unfortunately, I need to talk to you.", "You? Tell me, what would one of your sort want from Alek Endhelm?", "I need some questions answered, concerning the theft.", "I'm just wondering what someone like you is doing at Waste's Edge.", "That's none of your business Half-Elf. Don't waste my time, will ya!?", "So it's none of my business if valuables disappear around here and my mistress is held responsible?", "I don't like the implication. It's not wise going around, calling other people thieves.", "So far, I've called you nothing. But if you don't help me with a few answers, I might change my mind.", "I daresay being caught eavesdropping on the victim just before his gems are stolen is unwise as well.", "Who told you? The little gritsucker? He'll say what his master tells him to say, haven't you noticed?", "Come on, don't make a face like that, Half-Elf. Of course I was there. I was on my way to see what all the shouting was about. Looked like my skills might have been needed.", "Not so quick! Who do you think you are, walking around pestering other people?", "If you must know, I'm working for Lady Silverhair.", "I'm here to get to the bottom of the matter. So if you don't want to share Silverhair's fate, you had better answer my questions.", "To hell with you, Half-Elf. What do you want to know?", "Next moment, the door's burstin' open and your lovely mistress rushes past ... - I don't think you could call that eavesdropping.", "Leave the thinking to me and simply answer my questions, will you?", "What is your business here, then?", "If you don't believe me, why don't you ask Fingolson himself? Oh, I forgot. He doesn't want to talk with people of your kind, does he? Well, I cannot blame him for that.", "What on earth has my business to do with the theft? You're just wasting my time with your bloody questions.", "I fear you do not understand, Half-Elf. If you keep asking for irrelevant details you'll accomplish nothing. But I might know a thing or two, were you only asking the right questions.", "Listen, man. I am not interested into your gossip.", "So what questions should I ask, in your opinion?", "I don't see how *that* could get me any further.", "Just tryin' to help. But a smartass like you doesn't need any help, do you?", "Even if I was, I bet you could never prove it, Half-Elf. You wouldn't recognise a clue if someone pushed your pretty nose into it.", "I certainly don't need yours. For all I know, you may well be the thief.", "Now do you have any dumb questions left, or can I go back to my drink?", "Simply answering my questions would be help enough!", "If you say so. Then go on, ask what you want, even if it's not getting you anywhere.", "Who's wasting whose time here? The sooner you answer my questions, the sooner I leave you to yourself. Even you should understand this!", "Not before I get some answers out of you. You don't have something to hide, do you?", "So what is your business here, then?", "If it makes you happy; I made camp here on my way back from Limebruck where I had an ... appointment, which is absolutely none of your concern. I'm just an innocent traveller caught in this bloody mess.", "Master Orloth says your chamber is below ground, next to the Dwarf's. So did you hear anything unusual in the night of the theft?", "No I didn't. But perhaps there wasn't anything unusual to hear that night.", "What do you mean?", "You're a slow thinker, eh Half-Elf!? Hasn't it occurred to you that the theft might've already been committed by the time Fingolson went to bed?", "Don't make me laugh. That's the most ridiculous thing I ever heard.", "Do you have any proof of this?", "That's impossible. Fingolson had the gems on him during the negotiations. And afterwards, either he or Erek were down in their room.", "Well, that would rule out quite a few possible thieves, wouldn't it?", "You want to tell me that Erek has taken the gems?", "You don't believe me? Perhaps you should ask Erek who has packed them then!", "I don't. But since you are so good in finding stuff out, this shouldn't be a problem for you!", "If you don't like what you hear from me, why don't you look for different company, Half-Elf?", "So? Was that of any help? I shouldn't think so. A waste of time it was!", "For what would they have needed your skills?", "What were you doing outside the parlour during negotiations? Trying to spy on Master Fingolson?", "Perhaps it's just me, but I'd ask myself why the ... thief hasn't left Waste's Edge.", "The muscular fellow in front of you has the air of a troublemaker about him. Scars all over his body are evidence of his readiness to use the sword he is carrying. He eyes you with undisguised distaste as you approach.", "Well, why hasn't he?", "Good question, isn't it! Now if I were you, Half-Elf, I'd be off to a quiet corner and made some use of what brain I had.", "Perhaps you are right. Any further conversation would be useless anyway. So I'll leave you ... for now!", "Very funny! Should I ever need a fool, I'll send for you.", "Why should I \"spy\" on a conversation that could be heard up to Erinsford. Nah, I was about to look whether my skills might be needed.", "You disappoint me, Half-Elf. The poor Dwarfs were practically attacked by that furious woman. How should I know she wasn't about to turn them into toads or something?", "Don't tell me you thought Fingolson would enrol you as his guard?", "He wasn't very enthusiastic about you, am I right?", "So what? You think I stole his gems because he didn't accept my offer?", "Well, that's it! I have enough of your useless blather. But I shall be watching you!", "I think you wouldn't need any reason at all. However, until I find a clue as to your guilt, I'll have to leave you to yourself.", "Endhelm puts a threatening grin on his face as he sees you walking towards him.", "Actually, there is nothing you could possibly tell me.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer4, self.answer6, self.answer8, self.answer9, self.answer11, self.answer13, self.answer14, self.answer15, self.answer16, self.answer18, self.answer19, self.answer22, self.answer23, self.answer27, self.answer28, self.answer29, self.answer31, self.answer32, self.answer34, self.answer36, self.answer37, self.answer38, self.answer39, self.answer40, self.answer42, self.answer44, self.answer45, self.answer46, self.answer48, self.answer53, self.answer54, self.answer56, self.answer57, self.answer60, self.answer63, self.answer64, self.answer68, None]

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
		if self.the_npc.get_val ("talked_to") == 0:

			self.color = 0
			self.npc.append (56)
			self.cont.append (33)
			self.the_npc.set_val ("talked_to" , 1)

			self.player.append (-1)
		else:

			self.color = 0
			self.npc.append (68)
			self.cont.append (38)
			self.player.append (-1)

	def answer68 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (4)
		self.cont.append (2)
		self.player.append (-1)

	def answer4 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (69)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (14)
		if not self.eavesdrop and adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (54)
			self.cont.append (32)
		if adonthell.gamedata_get_quest("demo").get_val ("know_aleks_room") == 1:

			self.player.append (40)
			self.cont.append (25)
		self.player.append (-1)

	def answer40 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (41)
		self.cont.append (-1)
		self.player.append (42)
		self.cont.append (26)
		self.player.append (-1)

	def answer42 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (43)
		self.cont.append (-1)
		self.player.append (44)
		self.cont.append (27)
		self.player.append (45)
		self.cont.append (28)
		self.player.append (46)
		self.cont.append (29)
		self.player.append (-1)

	def answer46 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (47)
		self.cont.append (-1)
		self.player.append (48)
		self.cont.append (30)
		self.player.append (-1)

	def answer48 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (49)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("ask_packed_gems" , 1)

		self.player.append (44)
		self.cont.append (27)
		self.player.append (45)
		self.cont.append (28)
		self.player.append (-1)

	def answer45 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (50)
		self.cont.append (-1)
		self.player.append (66)
		self.cont.append (-1)
		self.player.append (-1)

	def answer66 (self):
		pass

	def answer44 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (51)
		self.cont.append (-1)
		self.player.append (59)
		self.cont.append (-1)
		self.player.append (-1)

	def answer59 (self):
		pass

	def answer54 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (61)
		self.cont.append (-1)
		self.player.append (53)
		self.cont.append (31)
		self.player.append (-1)

	def answer53 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (62)
		self.cont.append (-1)
		self.player.append (63)
		self.cont.append (36)
		self.player.append (44)
		self.cont.append (27)
		self.player.append (-1)

	def answer63 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (24)
		self.cont.append (-1)
		self.player.append (66)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 3:

			self.player.append (64)
			self.cont.append (37)
		self.player.append (-1)

	def answer64 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (65)
		self.cont.append (-1)
		self.player.append (67)
		self.cont.append (-1)
		self.player.append (-1)

	def answer67 (self):
		pass

	def answer23 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (36)
		self.cont.append (21)
		self.player.append (-1)

	def answer36 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (-1)
		self.player.append (27)
		self.cont.append (15)
		self.player.append (28)
		self.cont.append (16)
		self.loop.append (28)
		self.player.append (-1)

	def answer28 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (55)
		self.cont.append (-1)
		self.player.append (29)
		self.cont.append (17)
		self.player.append (57)
		self.cont.append (34)
		self.player.append (-1)

	def answer57 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (58)
		self.cont.append (-1)
		self.player.append (59)
		self.cont.append (-1)
		self.player.append (60)
		self.cont.append (35)
		self.player.append (-1)

	def answer60 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (32)
		self.cont.append (19)
		self.player.append (34)
		self.cont.append (20)
		self.player.append (-1)

	def answer34 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (35)
		self.cont.append (-1)
		self.player.append (38)
		self.cont.append (23)
		if not self.eavesdrop and adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (54)
			self.cont.append (32)
		if adonthell.gamedata_get_quest("demo").get_val ("know_aleks_room") == 1:

			self.player.append (40)
			self.cont.append (25)
		self.player.append (-1)

	def answer38 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (39)
		self.cont.append (24)
		self.player.append (-1)

	def answer39 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (52)
		self.cont.append (-1)
		self.player.append (66)
		self.cont.append (-1)
		self.player.append (-1)

	def answer32 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (31)
		self.cont.append (18)
		self.player.append (-1)

	def answer31 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (33)
		self.cont.append (-1)
		self.player.append (38)
		self.cont.append (23)
		if not self.eavesdrop and adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (54)
			self.cont.append (32)
		if adonthell.gamedata_get_quest("demo").get_val ("know_aleks_room") == 1:

			self.player.append (40)
			self.cont.append (25)
		self.player.append (-1)

	def answer29 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (32)
		self.cont.append (19)
		self.player.append (34)
		self.cont.append (20)
		self.player.append (-1)

	def answer27 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (32)
		self.cont.append (19)
		self.player.append (34)
		self.cont.append (20)
		self.player.append (-1)

	def answer69 (self):
		pass

	def answer56 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (0)
		self.cont.append (-1)
		self.player.append (1)
		self.cont.append (1)
		self.player.append (6)
		self.cont.append (3)
		self.player.append (-1)

	def answer6 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (7)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (4)
		self.player.append (9)
		self.cont.append (5)
		self.player.append (-1)

	def answer9 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (10)
		self.cont.append (-1)
		self.player.append (11)
		self.cont.append (6)
		self.player.append (-1)

	def answer11 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (12)
		self.cont.append (-1)
		self.player.append (13)
		self.cont.append (7)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (14)
			self.cont.append (8)
		self.player.append (-1)

	def answer14 (self):
		self.eavesdrop = 1

		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (9)
		self.player.append (-1)

	def answer15 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (16)
		self.cont.append (10)
		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (22)
		self.cont.append (13)
		self.player.append (53)
		self.cont.append (31)
		self.player.append (-1)

	def answer22 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (14)
		if not self.eavesdrop and adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (54)
			self.cont.append (32)
		if adonthell.gamedata_get_quest("demo").get_val ("know_aleks_room") == 1:

			self.player.append (40)
			self.cont.append (25)
		self.player.append (-1)

	def answer13 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (14)
		if not self.eavesdrop and adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (54)
			self.cont.append (32)
		if adonthell.gamedata_get_quest("demo").get_val ("know_aleks_room") == 1:

			self.player.append (40)
			self.cont.append (25)
		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (11)
		self.player.append (19)
		self.cont.append (12)
		self.player.append (-1)

	def answer19 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (14)
		if not self.eavesdrop and adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (54)
			self.cont.append (32)
		if adonthell.gamedata_get_quest("demo").get_val ("know_aleks_room") == 1:

			self.player.append (40)
			self.cont.append (25)
		self.player.append (-1)

	def answer18 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		work = adonthell.gamedata_get_quest("demo").get_val ("work_4_shair")
		work = work | 2
		adonthell.gamedata_get_quest("demo").set_val ("work_4_shair" , work)

		self.player.append (37)
		self.cont.append (22)
		self.player.append (-1)

	def answer37 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (12)
		self.cont.append (-1)
		self.player.append (13)
		self.cont.append (7)
		if adonthell.gamedata_get_quest("demo").get_val ("know_alek_eavesdrop"):

			self.player.append (14)
			self.cont.append (8)
		self.player.append (-1)

	def answer1 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		work = adonthell.gamedata_get_quest("demo").get_val ("work_4_shair")
		work = work | 2
		adonthell.gamedata_get_quest("demo").set_val ("work_4_shair" , work)

		self.player.append (37)
		self.cont.append (22)
		self.player.append (-1)
