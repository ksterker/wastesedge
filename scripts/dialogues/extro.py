import adonthell

class extro:
	loop = []
	strings = ["What is going on here? What are all these people doing in my room? Are you behind this, Half-Elf? I demand an explanation!", "Please calm down Master Fingolson. We are here to sort out this business once and for all.", "Sort this business out? Good ... good! It's about time, I'd say! So ... will that foul Elf finally return my Catseyes? I hear one was found amongst her belongings. And where there is one, the others shouldn't be far.", "I fear you are mistaken my good Dwarf. Neither were any Catseyes amongst your merchandise, nor am I in possession of your \"precious\" gems.", "As if an ignorant like you could tell the difference! I ...", "Silence! I have enough of your endless quarrel! I assume that $name here has poked around long enough in this pile of crap to produce the thief. He better had! So Half-Elf, go on, do your duty! End this bloody foolery!", "Well, it's a fact that Lady Silverhair cannot be the thief.", "It's obvious that the thief tried to frame Lady Silverhair.", "I'm sorry, I have no idea as to who the thief might be.", "There you have it! I daresay it'll be extremely difficult to find a thief other than the Elf over there. Who if not she would have wanted to steal my Catseyes!?", "I wonder whether you really want your gems back, or just the Lady Silverhair convicted!", "Catseyes? You call those worthless shards of yours Catseyes!?", "You doubt my word and expertise? You're truly your mistress' servant! Erek, be so kind and tell our friend here of the stolen gems' nature.", "Master?", "Do as I say!", "Very well. I ... - I am not sure about the other gems, but the stone $name has discovered is undoubtedly a Chrysoberyl. However, a Catseye it is not.", "I'd say this calls for an explanation, don't you think so Master Fingolson?", "Erek, this is not the right time for any of your childish pranks! Master Rasgar, you mustn't believe that ..., that impertinent youth!", "Deceit! What is deceit compared to the unsound creations our precious stones are turned into, I ask? Foul workings of magic that contradict anything lawful and good! I wonder who's side you're on, Erek?", "But you said I was nearly ready for the Rite of Passage, Master! Please return to reason; stop twisting the truth. Have you not taught me that deceit is wrong? Yet you are spreading lies!", "Then you took advantage of the theft to discredit my mistress, because you despise the arcane arts?", "If your gems are no Catseyes, you have to see that it is unlikely for my mistress to steal them.", "Foolish Half-Elf! Don't you think I'd know best how unlikely it is for anyone, including your fine mistress, to steal these gems? Were it not for Erek, that betrayer, you'd never know!", "So what? I'd gladly go without the stones if only the thief was put to her just punishment. Is this so wrong?", "But my mistress has been wrongly accused!", "You are obsessed by your aversion to Lady Silverhair!", "You understand nothing, Half-Elf! I couldn't care less for your mistress, may she rot in the dungeon! But I do care for the fruits of my peoples work, for the jewels and ores brought forth from the bones of the earth.", "They are spoilt by the likes of her. Turned into useless trinkets and poisoned with foul enchantments! The thought alone sickens me.", "If you think like that, why do you sell anything to the Elves at all?", "Are you making fun of me? Do you believe I asked for this? I've been chosen for this trade, whether I like it or not. But even the lowest Dwarf has more discipline than you lot together, so I fulfilled my duty without complaint.", "Until you couldn't bear it any more, am I right?", "I doubt that selling mere Chrysoberylls as Catseyes falls under your duty!", "What would a Half-Elf know of these matters? You couldn't tell one gem from the other! Erek, you have seen the stones; tell our friend whether they are Catseyes or not!", "You call tinkering with the supernatural an art!? It is an insult to any upright Dwarf. But what could I do against it? My people have no use for ornaments or luxuries, but we cannot live of rocks alone. We need to trade.", "So I couldn't simply refuse selling to those filthy Elves. But I could see to it that at least one of them would pay for this perverted \"art\" they practise!", "You mean the thief expected to escape unnoticed while your mistress would have been held responsible?", "That I would imagine.", "No. I mean the theft's sole purpose was to discredit my mistress.", "That's a grave accusation, $name! Who would do such a thing, and why, I wonder?", "This is ridiculous! My business with the Elf was only known to the both of us. Besides, who amongst the attendees holds any grudge against her?", "You do! And you knew of her business.", "That ... I ... - Master Rasgar, you are not going to believe in this ..., this infamy, are you? Since my arrival at this depraved place I am being continously insulted!", "First Silverhair disparages the quality of my stones, only to steal them later on. And as if that wouldn't be enough, that servant of her now tries to pin the crime on me!", "Master Fingolson, were it not you who set my Mistress at edge right after her arrival?", "But your stones are of poor quality indeed!", "You doubt my word and expertise, Half-Elf? Perhaps you have more faith in my apprentice then. Erek, please tell those ignorants how valuable these Catseyes are.", "Then you confess that the theft was just pretended?", "What do you mean?", "You feigned the theft, as an act of revenge.", "Why? It's a fact that she was in need of my gems. And she said herself that I deserved no payment for them. Even without that Catseye appearing in her luggage, this should be proof enough!", "But this gem is no Catseye, and therefore worthless to her.", "You think I did that deliberately?", "Yes. And afterwards you offered her worthless gems to enrage her even more!", "Rubbish I say! There can be no doubt that the Elf is responsible!", "Why do you keep insisting on my mistress' guilt?", "Really? Now that is news to me. If you don't mind I would like to know your reasoning, Half-Elf!", "Whoever planted that gem in the mistress' chest, it was not her.", "I'm not sure I understand. Are you telling us the noise in the stables might have been the thief putting that gem into Silverhair's luggage? Why would he do that?", "The gems the Lady is accused of stealing are worthless to her.", "To conceal his trail, and to direct all suspicion towards Lady Silverhair, of course.", "What do you mean? Why would my gems be suddenly worthless to her?", "My mistress intended to buy Catseyes, but as it turned out, your gems are not.", "I don't believe this! I know of no noise in the stables, but I do know that Silverhair intended to buy my gems. And when she didn't find my conditions to her liking, she simply stole them!", "Lady Silverhair intended to buy Catseyes, not these worthless shards you tried to sell her!", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer0, self.answer1, self.answer2, self.answer3, self.answer4, self.answer6, self.answer7, self.answer8, self.answer10, self.answer11, self.answer12, self.answer13, self.answer14, self.answer15, self.answer16, self.answer17, self.answer19, self.answer20, self.answer21, self.answer24, self.answer25, self.answer26, self.answer28, self.answer30, self.answer31, self.answer32, self.answer33, self.answer36, self.answer37, self.answer38, self.answer40, self.answer41, self.answer43, self.answer44, self.answer45, self.answer48, self.answer50, self.answer52, self.answer54, self.answer56, self.answer58, self.answer59, self.answer61, self.answer63, None]

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
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (0)
		self.cont.append (1)
		self.player.append (-1)

	def answer0 (self):
		self.set_npc ("Jelom Rasgar")
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (1)
		self.cont.append (2)
		self.player.append (-1)

	def answer1 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (2)
		self.cont.append (3)
		self.player.append (-1)

	def answer2 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (3)
		self.cont.append (4)
		self.player.append (-1)

	def answer3 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (4)
		self.cont.append (5)
		self.player.append (-1)

	def answer4 (self):
		self.set_npc ("Jelom Rasgar")
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (6)
		self.player.append (7)
		self.cont.append (7)
		self.player.append (8)
		self.cont.append (8)
		self.player.append (-1)

	def answer8 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (9)
		self.player.append (11)
		self.cont.append (10)
		self.player.append (-1)

	def answer11 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (12)
		self.cont.append (11)
		self.player.append (-1)

	def answer12 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (13)
		self.cont.append (12)
		self.player.append (-1)

	def answer13 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (14)
		self.cont.append (13)
		self.player.append (-1)

	def answer14 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (15)
		self.cont.append (14)
		self.player.append (-1)

	def answer15 (self):
		self.set_npc ("Jelom Rasgar")
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (16)
		self.cont.append (15)
		self.player.append (-1)

	def answer16 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (17)
		self.cont.append (16)
		self.player.append (-1)

	def answer17 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (19)
		self.cont.append (17)
		self.player.append (-1)

	def answer19 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (18)
		self.cont.append (-1)
		self.player.append (21)
		self.cont.append (19)
		if self.guess_deceit == 1:

			self.player.append (46)
			self.cont.append (-1)
		if self.guess_deceit == 0:

			self.player.append (20)
			self.cont.append (18)
		self.player.append (-1)

	def answer20 (self):
		self.guess_deceit = 1

		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (33)
		self.cont.append (27)
		self.player.append (-1)

	def answer33 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (34)
		self.cont.append (-1)
		if self.guess_deceit == 1:

			self.player.append (46)
			self.cont.append (-1)
		self.player.append (-1)

	def answer46 (self):
		pass

	def answer21 (self):
		self.guess_deceit = 1
		

		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (22)
		self.cont.append (-1)
		if self.guess_deceit == 1:

			self.player.append (46)
			self.cont.append (-1)
		self.player.append (-1)

	def answer10 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (23)
		self.cont.append (-1)
		self.player.append (25)
		self.cont.append (21)
		if self.not_guilty != 1:

			self.player.append (24)
			self.cont.append (20)
		self.player.append (-1)

	def answer24 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (49)
		self.cont.append (-1)
		self.player.append (25)
		self.cont.append (21)
		self.player.append (50)
		self.cont.append (37)
		self.player.append (11)
		self.cont.append (10)
		self.player.append (-1)

	def answer50 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (32)
		self.cont.append (26)
		self.player.append (-1)

	def answer32 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (13)
		self.cont.append (12)
		self.player.append (-1)

	def answer25 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (26)
		self.cont.append (22)
		self.player.append (-1)

	def answer26 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (27)
		self.cont.append (-1)
		self.player.append (28)
		self.cont.append (23)
		if self.guess_deceit == 0:

			self.player.append (20)
			self.cont.append (18)
		self.player.append (-1)

	def answer28 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (29)
		self.cont.append (-1)
		self.player.append (30)
		self.cont.append (24)
		self.player.append (31)
		self.cont.append (25)
		self.player.append (-1)

	def answer31 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (32)
		self.cont.append (26)
		self.player.append (-1)

	def answer30 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (47)
		self.cont.append (-1)
		self.player.append (48)
		self.cont.append (36)
		self.player.append (-1)

	def answer48 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (41)
		self.cont.append (32)
		self.guess_deceit = 1

		self.player.append (-1)

	def answer41 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (42)
		self.cont.append (-1)
		self.player.append (44)
		self.cont.append (34)
		if adonthell.gamedata_get_quest("demo").get_val ("know_bjarns_insult") == 1:

			self.player.append (43)
			self.cont.append (33)
		self.player.append (-1)

	def answer43 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (51)
		self.cont.append (-1)
		self.player.append (52)
		self.cont.append (38)
		self.player.append (-1)

	def answer52 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (45)
		self.cont.append (35)
		self.player.append (-1)

	def answer45 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (13)
		self.cont.append (12)
		self.player.append (-1)

	def answer44 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (45)
		self.cont.append (35)
		self.player.append (-1)

	def answer7 (self):
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (35)
		self.cont.append (-1)
		self.player.append (36)
		self.cont.append (28)
		self.player.append (37)
		self.cont.append (29)
		self.player.append (-1)

	def answer37 (self):
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (38)
		self.cont.append (30)
		self.player.append (-1)

	def answer38 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (39)
		self.cont.append (-1)
		self.player.append (40)
		self.cont.append (31)
		self.player.append (-1)

	def answer40 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (41)
		self.cont.append (32)
		self.guess_deceit = 1

		self.player.append (-1)

	def answer36 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (53)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (9)
		self.player.append (54)
		self.cont.append (39)
		self.player.append (-1)

	def answer54 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (49)
		self.cont.append (-1)
		self.player.append (25)
		self.cont.append (21)
		self.player.append (50)
		self.cont.append (37)
		self.player.append (11)
		self.cont.append (10)
		self.player.append (-1)

	def answer6 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (55)
		self.cont.append (-1)
		self.player.append (56)
		self.cont.append (40)
		self.player.append (58)
		self.cont.append (41)
		self.player.append (-1)

	def answer58 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (60)
		self.cont.append (-1)
		self.player.append (61)
		self.cont.append (43)
		self.player.append (-1)

	def answer61 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (32)
		self.cont.append (26)
		self.player.append (-1)

	def answer56 (self):
		self.set_npc ("Jelom Rasgar")
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (57)
		self.cont.append (-1)
		self.player.append (59)
		self.cont.append (42)
		self.player.append (-1)

	def answer59 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (62)
		self.cont.append (-1)
		self.not_guilty = 1

		self.player.append (10)
		self.cont.append (9)
		self.player.append (63)
		self.cont.append (44)
		self.player.append (-1)

	def answer63 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (32)
		self.cont.append (26)
		self.player.append (-1)
