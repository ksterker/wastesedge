import adonthell

class extro:
	loop = []
	strings = ["What is going on here? What are all these people doing in my room? Are you behind this, Half-Elf? I demand an explanation!", "Please calm down Master Fingolson. We are here to sort out this business once and for all.", "Sort this business out? Good ... good! It's about time, I'd say! So ... will that foul Elf finally return my Catseyes? I hear one was found amongst her belongings. And where there is one, the others shouldn't be far.", "I fear you are mistaken my good Dwarf. Neither were any Catseyes amongst your merchandise, nor am I in posession of your \"precious\" gems.", "As if an ignorant like you could tell the difference! I ...", "Silence! I have enough of your endless quarrel! I assume that $name here has poked around long enough in this pile of crap to produce the thief. He better had! So Half-Elf, go on, do your duty! End this bloody foolery!", "Uh, well, it's a fact that Lady Silverhair cannot be the thief.", "I think the thief tried to frame Lady Silverhair.", "I'm sorry, I have no idea as to who the thief might be.", "There! You all heard it! I daresay it'll be extremely difficult to find a thief other than the Elf over there. Who if not she would have wanted to steal my Catseyes!?", "I wonder whether you really want your gems back, or just the Lady Silverhair convicted!", "Catseyes? You call those worthless shards of yours Catseyes!?", "You doubt my word and expertise? You're truly your mistress' servant! Erek, be so kind and tell our friend here of the stolen gems' nature.", "Master?", "Do as I say!", "Very well. I ... - I will only speak for the stone $name has discovered though. It undoubtedly is a Chrysoberyl. However, a Catseye it is not.", "I'd say this calls for an explanation, don't you think so Master Fingolson?", "Oh deary me! It seems, I was ... mistaken. But even if none of my gems were Catseyes, they'd still remain stolen. So what of it?", "A lie! What is a lie compared to the unsound creations our precious stones are turned into, I ask? Foul workings of magic that contradict anything lawful and good! I wonder who's side you're on, Erek?", "You ... you think it does not matter? But you've wantonly twisted the truth! You have told a lie!", "Then you took advantage of the theft to discredit my mistress, because you despise the arcane arts?", "Master Fingolson, if your gems are no Catseyes, you have to see that it's rather unlikely my mistress has stolen them.", "Foolish Half-Elf! Don't you think I'd know best how unlikely it is for anyone, including your fine mistress, to steal these jewels? And were it not for Erek, that betrayer, you'd never know!", "What are you talking about?", "Are you indicating the gems have not been stolen at all?", "Are you too blind to see? It does not matter any more. The hideous Elf will never get what she deserves now, so what should I care?", "So what? I'd gladly go without the stones if only the thief was put to her just punishment. Is this so wrong?", "But my mistress has been wrongly accused!", "You are obsessed by your aversion to Lady Silverhair!", "You understand nothing, Half-Elf! I couldn't care less for your mistress, may she rot in the dungeon! But I do care for the fruits of my peoples work, for the jewels and ores brought forth from the bones of the earth.", "They are spoilt by the likes of her. Turned into useless trinkets and poisoned with foul enchantments! The thought alone sickens me.", "If you feel like that, why do you sell anything to the Elves at all?", "Are you making fun of me? Do you think I asked for this? I've been chosen for this trade, whether I liked it or not. But even the lowest Dwarf has more discipline than you lot together, so I fulfilled my duty without complaint.", "Until you couldn't bear it any more, am I right?", "I doubt that selling mere Chrysoberylls as Catseyes falls under your duty!", "What would a Half-Elf know of these matters? You couldn't tell one gem from the other! Erek, you have seen the stones; tell our friend whether they are Catseyes or not!", "You call tinkering with the supernatural an art!? It is an insult to any upright Dwarf. But what could I do against it? My people have no use for ornaments or luxuries, but we cannot live of rocks alone. We need to trade.", "It's true: I've seen to it that at least one filthy Elf would pay for this perverted \"art\" they practise.", "So the theft was just pretended?", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer0, self.answer1, self.answer2, self.answer3, self.answer4, self.answer8, self.answer10, self.answer11, self.answer12, self.answer13, self.answer14, self.answer15, self.answer16, self.answer17, self.answer19, self.answer20, self.answer21, self.answer23, self.answer56, self.answer58, self.answer63, self.answer69, self.answer71, self.answer74, None]

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
		self.cont.append (-1)
		self.player.append (7)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (6)
		self.player.append (-1)

	def answer8 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (10)
		self.cont.append (7)
		self.player.append (11)
		self.cont.append (8)
		self.player.append (-1)

	def answer11 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (12)
		self.cont.append (9)
		self.player.append (-1)

	def answer12 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (13)
		self.cont.append (10)
		self.player.append (-1)

	def answer13 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (14)
		self.cont.append (11)
		self.player.append (-1)

	def answer14 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (15)
		self.cont.append (12)
		self.player.append (-1)

	def answer15 (self):
		self.set_npc ("Jelom Rasgar")
		self.color = adonthell.gamedata_get_character("Jelom Rasgar").get_color()
		self.npc.append (16)
		self.cont.append (13)
		self.player.append (-1)

	def answer16 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (17)
		self.cont.append (14)
		self.player.append (-1)

	def answer17 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (19)
		self.cont.append (15)
		self.player.append (-1)

	def answer19 (self):
		self.set_npc ("Bjarn Fingolson")
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (18)
		self.cont.append (-1)
		self.player.append (20)
		self.cont.append (16)
		self.player.append (21)
		self.cont.append (17)
		self.player.append (-1)

	def answer21 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (22)
		self.cont.append (-1)
		self.player.append (23)
		self.cont.append (18)
		self.player.append (24)
		self.cont.append (-1)
		self.player.append (-1)

	def answer24 (self):
		pass

	def answer23 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (-1)

	def answer20 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (36)
		self.cont.append (24)
		self.player.append (-1)

	def answer74 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (37)
		self.cont.append (-1)
		self.player.append (38)
		self.cont.append (-1)
		self.player.append (-1)

	def answer78 (self):
		pass

	def answer10 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (26)
		self.cont.append (-1)
		self.player.append (27)
		self.cont.append (-1)
		self.player.append (28)
		self.cont.append (19)
		self.player.append (-1)

	def answer56 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (29)
		self.cont.append (20)
		self.player.append (-1)

	def answer58 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (20)
		self.cont.append (16)
		self.player.append (31)
		self.cont.append (21)
		self.player.append (-1)

	def answer63 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (32)
		self.cont.append (-1)
		self.player.append (33)
		self.cont.append (-1)
		self.player.append (34)
		self.cont.append (22)
		self.player.append (-1)

	def answer69 (self):
		self.color = adonthell.gamedata_get_character("Bjarn Fingolson").get_color()
		self.npc.append (35)
		self.cont.append (23)
		self.player.append (-1)

	def answer71 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (13)
		self.cont.append (10)
		self.player.append (-1)

	def answer67 (self):
		pass

	def answer54 (self):
		pass

	def answer7 (self):
		pass

	def answer6 (self):
		pass
