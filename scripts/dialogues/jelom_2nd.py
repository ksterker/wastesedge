import adonthell

class jelom_2nd:
	loop = []
	strings = ["Back again, Half-Elf? Have you learned anything of importance from your mistress?", "Nothing you'd be interested in, Jelom.", "It seems that Fingolson's gems are worthless to her.", "Really? I imagine you have some sort of proof for this, then?", "I have this Chrysoberyl. Apparently it is no Catseye, so why should Lady Silverhair have stolen it?", "You mean this is one of the stolen gems? How in hell did you come across that? And where are the others?", "I don't know where the others are, but this one was hidden in Lady Silverhair's luggage.", "Slow down! Didn't you just claim that your mistress had no use for the gems? And now you're telling me that you found that one amongst her stuff. That makes no sense!", "Unless the ... \"real\" thief wanted to direct all suspicion to your mistress. Ha! Nice idea, Half-elf. But why should I believe that your gem really belongs to Fingolson?", "Oh no! You are Silverhair's loyal servant. And as long as there is no other suspect I cannot possibly trust in anything you say. Now take your gem and leave me alone!", "Lady Silverhair said so.", "Oh! *The Lady Silverhair said so.* I assure you Half-Elf, the Lady Silverhair said quite a lot when we put her under arrest, and it wasn't very lady-like. Come back once you have something more substantial!", "I'm just repeating Erek Stonebreaker's words.", "Now I'm surprised. What makes him believe all of a sudden that his Master is selling crap? That doesn't sound at all like the Erek I know.", "I showed him one of Fingolson's gems I found.", "What? One of the stolen gems? Tell me Half-Elf, where have you found that?", "It was hidden in Lady Silverhair's luggage.", "If you don't believe me, go ask him yourself!", "And leave my post? Unlike Talan I do know my duty. Now go and don't bother me again before you can't prove your words.", "That's not important. The important thing is that this gem is of poor quality. See?", "Well, to me it looks valuable enough. Of course I am no expert in these matters, and I doubt that you are.", "Not you again, Half-Elf? Are you still trying to make me believe that your Mistress has no use for the gems?", "I'd be just wasting my breath on you!", "What's going on now? What are you doing here, Erek Stonebreaker?", "I'm here on behalf of $name, master Rasgar. I can testify that his gem belongs to my Master, and that it is of insufficient quality to be of any use for the Lady Silverhair.", "I should have known it! Believe me Erek, these Half-Elves are  talking you into things you will regret later on. Is it not so, Half-Elf?", "Listen Jelom, I am getting sick of you. What is it you want?", "I want to be sure, that's all. I told you that I don't trust you in this matter. And you Erek, you might think that you know the truth, but perhaps it's just what your friend here made you believe.", "If this gem really belongs to Master Fingolson, why don't I hear what he has to say about it?", "You think that I deceived Erek?", "I wouldn't be surprised. And I find it more than suspicious that I heard nothing from the gem's owner yet. If it really belongs to Master Fingolson, he should be able to give reliable information.", "Uh, I haven't asked him yet.", "Perhaps you should do that then, Half-Elf. I'll be waiting here.", "Well, Master Fingolson is pretending that this gem is a valuable Catseye, despite the fact that it isn't.", "Is that true, Erek?", "$name's gem is definitely no Catseye, master Rasgar. I hate to admit, but Master Fingolson appears to be ... lying!", "Now I understand nothing at all. Listen you both, I have enough of this! We are going to see this Dwarf. And Lady Silverhair is coming with us. I want to hear what she has to say to all of this.", "It's about time you return, Half-Elf! Tell me, what does Master Fingolson say about this gem of yours?", "Nothing. He refused to talk with me!", "Ha, that's laughable. You want to solve this matter, and don't even manage to speak to Master Fingolson!? Out of my sight, and don't even think about coming back before you haven't talked to the Dwarf!", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer2, self.answer4, self.answer6, self.answer7, self.answer8, self.answer10, self.answer12, self.answer14, self.answer16, self.answer17, self.answer19, self.answer20, self.answer23, self.answer24, self.answer26, self.answer27, self.answer29, self.answer31, self.answer33, self.answer34, self.answer35, self.answer38, None]

	def clear (self):
		del self.dialogue

	def __del__(self):
	    if adonthell.gamedata_get_quest("demo").get_val ("the_end") == 1:
	        # make all dudes go down to Bjarn
	        shair = adonthell.gamedata_get_character("Imoen Silverhair")
	        shair.set_schedule ("to_cellar")
	        shair.set_val ("delay", 5)
	
	        jelom = adonthell.gamedata_get_character("Jelom Rasgar")
	        jelom.set_val ("delay", 20)
	        jelom.set_schedule ("to_cellar")
			
	        player = adonthell.gamedata_player ()
	        player.set_val ("delay", 35)
	        player.set_schedule ("to_cellar")
			
	        erek = adonthell.gamedata_get_character("Erek Stonebreaker")
	        erek.set_schedule_active (1)
	        erek.set_schedule ("to_cellar")
	        erek.set_val ("delay", 45)
			
	        fnir = adonthell.gamedata_get_character("Fellnir Kezular")
	        fnir.set_schedule ("to_cellar")
	        fnir.set_val ("delay", 130)
			
	        illig = adonthell.gamedata_get_character("Tristan Illig")
	        illig.set_schedule ("to_cellar")
	        illig.set_val ("delay", 300)
	


	def __getattr__ (self, name):
		return 0

	def run (self, answer):
		self.npc = []
		self.player = []
		self.cont = []
		self.dialogue[answer]()

	def start (self):
		if adonthell.gamedata_get_quest("demo").get_val ("convince_jelom") == 0:

			self.color = self.the_npc.get_color()
			self.npc.append (0)
			self.cont.append (-1)
			self.player.append (1)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") > 0:

				self.player.append (2)
				self.cont.append (1)
			self.player.append (-1)
		elif adonthell.gamedata_get_quest("demo").get_val ("convince_jelom") == 1:

			self.color = self.the_npc.get_color()
			self.npc.append (21)
			self.cont.append (-1)
			self.player.append (22)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("have_gem") == 1:

				self.player.append (4)
				self.cont.append (2)
			if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 2 == 2:

				self.player.append (12)
				self.cont.append (7)
			self.player.append (-1)
		elif adonthell.gamedata_get_quest("demo").get_val ("convince_jelom") == 2:

			self.color = self.the_npc.get_color()
			self.npc.append (23)
			self.cont.append (13)
			adonthell.gamedata_get_quest("demo").set_val ("convince_jelom" , 3)

			self.player.append (-1)
		else:

			self.color = self.the_npc.get_color()
			self.npc.append (37)
			self.cont.append (-1)
			if adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") < 3:

				self.player.append (38)
				self.cont.append (22)
			if adonthell.gamedata_get_quest("demo").get_val ("bjarn_lies") == 1:

				self.player.append (33)
				self.cont.append (19)
			self.player.append (-1)

	def answer33 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (34)
		self.cont.append (20)
		self.player.append (-1)

	def answer34 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (35)
		self.cont.append (21)
		self.player.append (-1)

	def answer35 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (36)
		self.cont.append (-1)
		# make all dudes go down to Bjarn
		adonthell.gamedata_get_quest("demo").set_val ("the_end" , 1)

		self.player.append (-1)

	def answer38 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (39)
		self.cont.append (-1)
		self.player.append (-1)

	def answer23 (self):
		self.set_npc ("Erek Stonebreaker")
		self.color = adonthell.gamedata_get_character("Erek Stonebreaker").get_color()
		self.npc.append (24)
		self.cont.append (14)
		self.player.append (-1)

	def answer24 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = self.the_npc.get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (26)
		self.cont.append (15)
		self.player.append (29)
		self.cont.append (17)
		self.player.append (-1)

	def answer29 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (31)
		self.cont.append (18)
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_lies") == 1:

			self.player.append (33)
			self.cont.append (19)
		self.player.append (-1)

	def answer31 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (32)
		self.cont.append (-1)
		self.player.append (-1)

	def answer26 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (27)
		self.cont.append (16)
		self.player.append (-1)

	def answer27 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (28)
		self.cont.append (-1)
		self.player.append (31)
		self.cont.append (18)
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_lies") == 1:

			self.player.append (33)
			self.cont.append (19)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (13)
		self.cont.append (-1)
		self.player.append (14)
		self.cont.append (8)
		self.player.append (17)
		self.cont.append (10)
		self.player.append (-1)

	def answer17 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (18)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("convince_jelom" , 1)

		self.player.append (-1)

	def answer14 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (-1)
		self.player.append (16)
		self.cont.append (9)
		self.player.append (19)
		self.cont.append (11)
		self.player.append (-1)

	def answer19 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (12)
		self.player.append (-1)

	def answer20 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("convince_jelom" , 1)

		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (7)
		self.cont.append (4)
		self.player.append (-1)

	def answer7 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (8)
		self.cont.append (5)
		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		adonthell.gamedata_get_quest("demo").set_val ("convince_jelom" , 1)

		self.player.append (-1)

	def answer4 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (3)
		self.player.append (19)
		self.cont.append (11)
		self.player.append (-1)

	def answer6 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (7)
		self.cont.append (4)
		self.player.append (-1)

	def answer22 (self):
		pass

	def answer2 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 2 == 2:

			self.player.append (12)
			self.cont.append (7)
		if adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") & 1 == 1:

			self.player.append (10)
			self.cont.append (6)
		if adonthell.gamedata_get_quest("demo").get_val ("have_gem") == 1:

			self.player.append (4)
			self.cont.append (2)
		self.player.append (-1)

	def answer10 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (-1)

	def answer1 (self):
		pass
