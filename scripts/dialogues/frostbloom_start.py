import adonthell

class frostbloom_start:
	loop = []
	strings = ["Hm?  What do you want?", "I am a servant of Lady Imoen Silverhair, and I'd like to ask ...", "I know who you are, and I do not care what you wish to ask.  Now go away.  The Yeti of my soul must have silence.", "You again?  I thought I told you to leave me alone.", "But lady, I must ask you about the theft...", "The theft?  You mean your theft of my precious time, when I could be receiving inspiration?  I've lost enought of that already, thank you.  Now be gone, silly servant, you begin to annoy me.", "But, lady...", "Off, I say!  I have no patience for this chatter!", "I will go, but I will return to ask my questions.  I must have what you know of my Lady.", "The half-elf fixes you with a withering gaze.  For a moment, you feel as if you had been skewered.  Her voice is full of sarcasm.", "I look forward to it with all my heart.  For now, just go away.", "Back again, eh?  You do hunger for punishment, don't you.", "I try to be diligent, lady.", "Well, I must admit that such devotion deserves a reward.  Very well, you may stay for a while.  A short while.  My name is Rhayne Frostbloom.  Take care you remember it.", "Thank you, lady.  I would ask you about the theft, if I may.", "For goodness sake, do not bother me with that nonsense.  It's been all anyone speaks about here, and I for one am sick of it.", "I have seen the lovely Yeti you carved for my mistress.  It is quite impressive.", "Do you really think so?  I tried to make it worthy of the noble beast, but I always wonder if I have given it enough life.", "I'm hardly an exprert, lady, but to my eye it is excellent.", "It is important.  The Lady Silverhair is in terrible danger.", "I know, I know.  And even if she is not hung, the Dwarves will be outraged.  What a foolish noise over such a little thing.  Gems are showy trash.  They cannot comprehend the complex soul of a Yeti.", "But this is hardly foolish, you must understand that.", "Frostbloom doesn't appear to hear you.  She stares off into space, occasionally whispering something about Yetis and souls, but you can make little sense of it.", "It is a masterpiece, my lady.  A true achievement that does credit to its model.", "Frostbloom eyes you suspiciously for a moment, then smiles.", "False flattery, eh?  I would wager my next commission you know nothing about the Yeti and their ways, yet would use this praise to loosen my tongue.  Well, have I spoken truth?", "No, lady, I honestly appreciate the talent in your piece.  That is, you are honestly talented.", "My lady, you have a keen eye and a keener wit.  That is precisely why I gave you praise, although you truly do deserve it.", "Huh!  Off with you, I'll not waste time listening to your prattle.  If you have a mind to be more honest, come back again.  Otherwise, take your foolishness elsewhere.  I must pursue my inspiration, even in this dismal place.  Alone, if you please.", "Very good answer.  I believe you'll do.  Ask of me what you will.", "Flattery will get you nowhere, so long as you pretend it is nothing more.  I have no time for such idiocy.", "Ah, the persistant young servant.  Do you wish to ask me something more?", "Did anything unusual happen last night?", "What do you know of the dwarf, Bjarn?", "Do you know anything of the people staying here at Waste's Edge?", "Back to try again?  Then tell me whether you offered false flattery!  Then we'll see what you're made of.", "Unusual?  It was a warm night, which I am told is quite odd for this time of year.  Is that what you had in mind?", "Of course not!  Please, my Lady's very life may be in danger!", "It is such fun to tease you, do you realize that?  But there was something odd about the night.  There was a sound, which went on for a short time.", "Has your lady told you any more about the sounds I heard?  I cannot recall anything else of note.", "A rough little creature.  No trace of creativity in the man at all.  I only noticed him long enough to ignore him, and we were both the better for it.", "The family who serves the travellers are good folk.  There is a trace of the yeti's spirit in them, deep inside.", "But the rest are barely forth a speck of dust in the wind.  Dull minds, every one.  Your lady seems the sole exception, I am sorry to say.  But at least the rest leave me in peace.", "I could not tell you what it was, but I doubt very much these humans would have heard it.  You might ask your fair lady about it, her ears should be keener than mine.  Although she may have been too preoccupied to notice.", "I may not have an educated taste, but I do know talent when standing in front of me.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer4, self.answer6, self.answer8, self.answer9, self.answer12, self.answer14, self.answer16, self.answer18, self.answer19, self.answer21, self.answer23, self.answer24, self.answer26, self.answer27, self.answer32, self.answer33, self.answer34, self.answer37, self.answer38, self.answer41, self.answer44, None]

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
		if self.the_npc.get_val ("flattered") == 1:

			self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
			self.npc.append (35)
			self.cont.append (-1)
			self.player.append (26)
			self.cont.append (14)
			self.player.append (27)
			self.cont.append (15)
			self.player.append (44)
			self.cont.append (22)
			self.player.append (-1)
		if self.the_npc.get_val ("flattered") == 2:

			self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
			self.npc.append (31)
			self.cont.append (-1)
			self.player.append (32)
			self.cont.append (16)
			self.player.append (33)
			self.cont.append (17)
			self.player.append (34)
			self.cont.append (18)
			self.player.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("talked_about_yeti") == 1 and self.the_npc.get_val ("flattered") == 0:

			self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
			self.npc.append (11)
			self.cont.append (-1)
			self.player.append (12)
			self.cont.append (6)
			self.player.append (-1)
		if self.the_npc.get_val ("talked_to") == 1 and adonthell.gamedata_get_quest("demo").get_val ("talked_about_yeti") == 0:

			self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
			self.npc.append (3)
			self.cont.append (-1)
			self.player.append (4)
			self.cont.append (2)
			self.player.append (-1)
		if self.the_npc.get_val ("talked_to") == 0:

			self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
			self.npc.append (0)
			self.cont.append (-1)
			self.the_npc.set_val ("talked_to" , 1)

			self.player.append (1)
			self.cont.append (1)
			self.player.append (-1)

	def answer1 (self):
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (-1)

	def answer4 (self):
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (3)
		self.player.append (8)
		self.cont.append (4)
		self.player.append (-1)

	def answer8 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = 0
		self.npc.append (9)
		self.cont.append (5)
		self.player.append (-1)

	def answer9 (self):
		self.set_npc ("Rhayne Frostbloom")
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (10)
		self.cont.append (-1)
		self.player.append (-1)

	def answer6 (self):
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (7)
		self.cont.append (-1)
		self.player.append (-1)

	def answer12 (self):
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (13)
		self.cont.append (-1)
		self.player.append (14)
		self.cont.append (7)
		self.player.append (16)
		self.cont.append (8)
		self.player.append (-1)

	def answer16 (self):
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (9)
		self.player.append (23)
		self.cont.append (12)
		self.player.append (-1)

	def answer23 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = 0
		self.npc.append (24)
		self.cont.append (13)
		self.player.append (-1)

	def answer24 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (26)
		self.cont.append (14)
		self.player.append (27)
		self.cont.append (15)
		self.player.append (44)
		self.cont.append (22)
		self.player.append (-1)

	def answer18 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (-1)

	def answer14 (self):
		self.color = adonthell.gamedata_get_character("Rhayne Frostbloom").get_color()
		self.npc.append (15)
		self.cont.append (-1)
		self.player.append (19)
		self.cont.append (10)
		self.player.append (-1)

	def answer19 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (21)
		self.cont.append (11)
		self.player.append (-1)

	def answer21 (self):
		self.color = 0
		self.npc.append (22)
		self.cont.append (-1)
		self.player.append (-1)

	def answer34 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (41)
		self.cont.append (21)
		self.player.append (-1)

	def answer41 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (42)
		self.cont.append (-1)
		self.player.append (-1)

	def answer33 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (40)
		self.cont.append (-1)
		self.player.append (-1)

	def answer32 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (36)
		self.cont.append (-1)
		self.player.append (37)
		self.cont.append (19)
		self.player.append (-1)
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (39)
		self.cont.append (-1)
		self.player.append (-1)

	def answer37 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (38)
		self.cont.append (20)
		self.player.append (-1)

	def answer38 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (43)
		self.cont.append (-1)
		self.player.append (-1)

	def answer44 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (28)
		self.cont.append (-1)
		self.the_npc.set_val ("flattered" , 1)

		self.player.append (-1)

	def answer27 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (29)
		self.cont.append (-1)
		self.the_npc.set_val ("flattered" , 2)

		self.player.append (32)
		self.cont.append (16)
		self.player.append (33)
		self.cont.append (17)
		self.player.append (34)
		self.cont.append (18)
		self.player.append (-1)

	def answer26 (self):
		self.set_npc (self.the_npc.get_name())
		self.color = self.the_npc.get_color()
		self.npc.append (28)
		self.cont.append (-1)
		self.the_npc.set_val ("flattered" , 1)

		self.player.append (-1)
