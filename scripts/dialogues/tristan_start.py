import adonthell

class tristan_start:
	loop = []
	strings = ["Yes?", "Hello, sir. My name is $name, and I am investigating the theft of Master Fingolson's gems.", "Well met then, $name! I am Tristan Illig, a merchant by trade, and currently stuck here at the Redwyne Inn until this business is cleared up. So may I ask you to continue your investigation?", "Well, $name, I would like to be of help, but I am afraid that I know nothing that will aid you. Your time would be better spent talking to those who are involved, I would imagine.", "All the same I would like to ask you a thing or two ...", "Listen, $name, I already told you! I know nothing, saw nothing, heard nothing. I would be quite pleased if you conducted your investigation efficiently so I can finally leave this place.", "Right then, sorry to bother you, Master Illig.", "Oh, now I understand! You are working for Silverhair! You are not really investigating anything then, are you? You are just trying to get her freed at any cost!", "Could it be that you have something to hide, what with all this blustering?", "You have the nerve to accuse me, Half-Elf?! I don't have to take this. Go! Go before I lose my temper!", "The small man before you wears a cold expression. Judging by his garments he is sort of a merchant, and a rather successful one by the looks of it.", "Greetings sir, I am $name. I wonder whether you know anything about that theft.", "That is what I am doing, Master Illig. I have a few questions for you.", "And who says you are not amongst those?", "What? You cannot seriously consider that! Use your eyes, man! Do I look like a thief to you?", "There is a caravan with Saffron waiting for me, worth ten times the money that Dwarf claims to have lost. And if I cannot reach it in time ... I'll be ruined! Ruined!", "Nobody will buy any Saffron if those cutpurses from Elminscourt arrive with their cheap Achiote or Safflor before I have completed my business in Cirdanth.", "Who says you aren't broke already?", "Do you perhaps think my mistress is in need of stealing? Yet she is accused!", "Now leave me alone, please. I assure you that I know nothing about the theft, let alone have any part in it. Or do you think I would endanger my whole business for a few worthless pebbles?", "I warn you, Half-Elf, I am losing my patience with you and this whole affair. I am losing money by the hour, while you bumble around, bothering everyone with questions!", "My name is Tristan Illig and I'm a merchant by trade, no thieftaker. All I know is that they are making a big fuss about a few worthless gems stolen from that Dwarf, Fingolson.", "Who is \"they\"?", "Above all Fingolson himself. He seems to consider the theft a personal affront. And not to forget that excuse for a guard; Jelom by name I believe. He is responsible for locking us all in here.", "All right, all right! I'll leave you alone. But I shall be watching you!", "Tristan looks irritated as you approach him again.", "And it's not as if they would still be looking for the thief. As it turned out, it's been that Elf, Lady Silverhair. But so far they failed in retrieving the gems from her.", "As my mistress did certainly not steal them, they'll have a hard time in doing so I guess.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer4, self.answer5, self.answer7, self.answer8, self.answer10, self.answer11, self.answer12, self.answer13, self.answer14, self.answer15, self.answer16, self.answer17, self.answer18, self.answer22, self.answer23, self.answer53, self.answer59, None]

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
		if self.the_npc.get_val ("talked_to") == 1:

			self.color = 0
			self.npc.append (25)
			self.cont.append (17)
			self.player.append (-1)
		else:

			self.color = 0
			self.npc.append (10)
			self.cont.append (6)
			self.the_npc.set_val ("talked_to" , 1)

			self.player.append (-1)

	def answer10 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (0)
		self.cont.append (-1)
		if adonthell.gamedata_get_quest("demo").get_val ("know_argument") == 1:

			self.player.append (1)
			self.cont.append (1)
		else:

			self.player.append (11)
			self.cont.append (7)
		self.player.append (-1)

	def answer11 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (22)
		self.cont.append (15)
		self.player.append (6)
		self.cont.append (-1)
		self.player.append (-1)

	def answer6 (self):
		pass

	def answer22 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (23)
		self.cont.append (16)
		self.player.append (-1)

	def answer23 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (-1)
		self.player.append (27)
		self.cont.append (18)
		self.player.append (-1)

	def answer59 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (7)
		self.cont.append (4)
		self.player.append (-1)

	def answer7 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (5)
		self.player.append (24)
		self.cont.append (-1)
		self.player.append (-1)

	def answer51 (self):
		pass

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (24)
		self.cont.append (-1)
		self.player.append (-1)

	def answer1 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (8)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (4)
		self.cont.append (2)
		self.player.append (13)
		self.cont.append (9)
		self.player.append (-1)

	def answer13 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (14)
		self.cont.append (10)
		self.player.append (-1)

	def answer14 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (11)
		self.player.append (-1)

	def answer15 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (16)
		self.cont.append (12)
		self.player.append (-1)

	def answer16 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (19)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (14)
		self.player.append (17)
		self.cont.append (13)
		self.player.append (-1)

	def answer17 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (9)
		self.cont.append (-1)
		self.player.append (24)
		self.cont.append (-1)
		self.player.append (-1)

	def answer18 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (7)
		self.cont.append (4)
		self.player.append (-1)

	def answer4 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (5)
		self.cont.append (3)
		self.player.append (-1)

	def answer5 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (15)
		self.cont.append (11)
		self.player.append (-1)

	def answer53 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (5)
		self.cont.append (3)
		self.player.append (-1)
