import adonthell

class demo_intro_1:
	loop = []
	strings = ["Your employer, eh? Who might that be?", "The Lady Silverhair, and she must have great need of me, so let me pass!", "Nay, if you are Silverhair's man, then I shall not let you pass. That one is the source of all this mess, and I'll be switched if I let her accomplice in to free her. Be on your way!", "What sort of mess, man? If my Lady is in trouble, I must know!", "I do not know what nonsense you think is going on here. But if my Lady needs me, then I shall come to her aid!", "Don't be foolish! I must see my Lady at once. Open this gate!", "The sort of trouble we have no wish to put up with, that's certain. The Lady is being held for theft, and a grievous theft it was.", "Theft? But that cannot be, the Lady Silverhair is a wealthy noble in her own right. She need not stoop to theft.", "You speak madness, man! There can have been no theft. Allow me in, and I shall prove to you the Lady is innocent.", "But I must! If my Lady is in need of me I cannot simply walk away! Please, I beg you to open the gate so I may aid her.", "That is none of your concern. All you need know is that she is within your walls and will need me close if there is trouble at hand.", "She, eh? Your employer wouldn't be an elven lady named Silverhair, would she?", "Of course she is, you fool! Who else would it be? Are you going to open this gate or not?", "Er, no. No, it is not. In fact, my employer is no lady at all.", "Huh! You won't get in these doors by lying to me. You said your employer was a lady and there's only one in here who'd employ one of your sort.", "Very well then, my employer is Lady Silverhair. What of it?", "Your Lady is the cause of all this mess. And you'll not be coming in here to make it worse.", "That's what you are saying. But fact is, she first argued with the victim over his goods and the other morning they were gone. Now he demands justice and Silverhair is known to need them badly. So what would you say the truth is?", "I cannot tell you the truth unless you let me see for myself.", "You'll have a damned hard time doing that. The lady is guilty and has been seen to be guilty. The truth is that she is the thief and that is all there is to it.", "I tell you again, you shall not come in.", "I tell you, I cannot. My orders...", "I am sick of arguing with you. Are you about to let me in, or will I be forced to take action? And believe me, you would not enjoy it.", "The guard hesitates for a bit, and even from where you stand you can see he is uncertain.", "You'll be in more trouble for not opening that gate than you will for letting me in, I assure you of that. Now do as I say!", "But finally he seems to reach a conclusion, and after carefully scanning the surroundings, he beckons you in.", "Aid her? That is why you can't be allowed in. If you aid her too much, she might escape.", "I promise, please. I am becoming sick with worry. Can you not help me?", "How could she escape from a guarded camp, even if I did help? Now let me in!", "I wish I could, friend. But If I were to open this gate, I would be in terrible trouble.", "I am beginning to lose my patience, man. I don't wish you trouble, but I must be allowed in.", "I tell you I can't.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer1, self.answer3, self.answer4, self.answer5, self.answer7, self.answer8, self.answer9, self.answer10, self.answer12, self.answer13, self.answer15, self.answer18, self.answer22, self.answer23, self.answer24, self.answer27, self.answer28, self.answer30, None]

	def clear (self):
		del self.dialogue

	def get_right_npc (self):
		return "Master Orloth"


	def __getattr__ (self, name):
		return 0

	def run (self, answer):
		self.npc = []
		self.player = []
		self.cont = []
		self.dialogue[answer]()

	def start (self):
		self.color = self.the_npc.get_color()
		self.npc.append (0)
		self.cont.append (-1)
		self.player.append (1)
		self.cont.append (1)
		self.player.append (10)
		self.cont.append (8)
		self.player.append (-1)

	def answer10 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (9)
		self.player.append (13)
		self.cont.append (10)
		self.player.append (-1)

	def answer13 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (14)
		self.cont.append (-1)
		self.player.append (15)
		self.cont.append (11)
		self.player.append (-1)

	def answer15 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (16)
		self.cont.append (-1)
		self.player.append (4)
		self.cont.append (3)
		self.player.append (3)
		self.cont.append (2)
		self.player.append (-1)

	def answer3 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (6)
		self.cont.append (-1)
		self.player.append (7)
		self.cont.append (5)
		self.player.append (8)
		self.cont.append (6)
		self.player.append (-1)

	def answer8 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (19)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (12)
		self.player.append (-1)

	def answer18 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (20)
		self.cont.append (-1)
		self.player.append (9)
		self.cont.append (7)
		self.player.append (-1)

	def answer9 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (-1)
		self.player.append (27)
		self.cont.append (16)
		self.player.append (28)
		self.cont.append (17)
		self.player.append (5)
		self.cont.append (4)
		self.player.append (-1)

	def answer5 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (22)
		self.cont.append (13)
		self.player.append (24)
		self.cont.append (15)
		self.player.append (-1)

	def answer24 (self):
		self.color = 0
		self.npc.append (23)
		self.cont.append (14)
		self.player.append (-1)

	def answer23 (self):
		self.color = 0
		self.npc.append (25)
		self.cont.append (-1)
		self.the_npc.set_dialogue ("dialogues/talan_start")

		self.player.append (-1)

	def answer22 (self):
		self.color = 0
		self.npc.append (23)
		self.cont.append (14)
		self.player.append (-1)

	def answer28 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (29)
		self.cont.append (-1)
		self.player.append (30)
		self.cont.append (18)
		self.player.append (5)
		self.cont.append (4)
		self.player.append (-1)

	def answer30 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (31)
		self.cont.append (-1)
		self.player.append (22)
		self.cont.append (13)
		self.player.append (24)
		self.cont.append (15)
		self.player.append (-1)

	def answer27 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (29)
		self.cont.append (-1)
		self.player.append (30)
		self.cont.append (18)
		self.player.append (5)
		self.cont.append (4)
		self.player.append (-1)

	def answer7 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (18)
		self.cont.append (12)
		self.player.append (-1)

	def answer4 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (26)
		self.cont.append (-1)
		self.player.append (27)
		self.cont.append (16)
		self.player.append (28)
		self.cont.append (17)
		self.player.append (5)
		self.cont.append (4)
		self.player.append (-1)

	def answer12 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (3)
		self.cont.append (2)
		self.player.append (4)
		self.cont.append (3)
		self.player.append (-1)

	def answer1 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (2)
		self.cont.append (-1)
		self.player.append (3)
		self.cont.append (2)
		self.player.append (4)
		self.cont.append (3)
		self.player.append (-1)
