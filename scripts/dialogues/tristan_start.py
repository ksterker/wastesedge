import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class tristan_start (dialogue.base):
	text = [None,\
		_("Yes?"),\
		_("Hello, sir. My name is $name, and I am investigating the theft of Master Fingolson's gems."),\
		_("Well met then, $name! I am Tristan Illig, a merchant by trade, and currently stuck here at the Redwyne Inn until this business is cleared up. So may I ask you to continue your investigation?"),\
		_("Well, $name, I would like to be of help, but I am afraid that I know nothing that will aid you. Your time would be better spent talking to those who are involved, I would imagine."),\
		_("All the same I would like to ask you a thing or two ..."),\
		_("Listen, $name, I already told you! I know nothing, saw nothing, heard nothing. I would be quite pleased if you conducted your investigation efficiently so I can finally leave this place."),\
		_("Right then, sorry to bother you, Master Illig."),\
		_("Oh, now I understand! You are working for Silverhair! You are not really investigating anything then, are you? You are just trying to get her freed at any cost!"),\
		_("Could it be that you have something to hide, what with all this blustering?"),\
		_("You have the nerve to accuse me, Half-Elf?! I don't have to take this. Go! Go before I lose my temper!"),\
		_("The small man before you wears a cold expression. Judging by his garments he is sort of a merchant, and a rather successful one by the looks of it."),\
		_("Greetings sir, I am $name. I wonder whether you know anything about that theft."),\
		_("That is what I am doing, Master Illig. I have a few questions for you."),\
		_("And who says you are not amongst those?"),\
		_("What? You cannot seriously consider that! Use your eyes, man! Do I look like a thief to you?"),\
		_("There is a caravan with Saffron waiting for me, worth ten times the money that Dwarf claims to have lost. And if I cannot reach it in time ... I'll be ruined! Ruined!"),\
		_("Nobody will buy any Saffron if those cutpurses from Elminscourt arrive with their cheap Achiote or Safflor before I have completed my business in Cirdanth."),\
		_("Who says you aren't broke already?"),\
		_("Do you perhaps think my mistress is in need of stealing? Yet she is accused!"),\
		_("Now leave me alone, please. I assure you that I know nothing about the theft, let alone have any part in it. Or do you think I would endanger my whole business for a few worthless pebbles?"),\
		_("I warn you, Half-Elf, I am losing my patience with you and this whole affair. I am losing money by the hour, while you bumble around, bothering everyone with questions!"),\
		_("My name is Tristan Illig and I'm a merchant by trade, no thieftaker. All I know is that they are making a big fuss about a few worthless gems stolen from that Dwarf, Fingolson."),\
		_("Who is \"they\"?"),\
		_("Above all Fingolson himself. He seems to consider the theft a personal affront. And not to forget that excuse for a guard; Jelom by name I believe. He is responsible for locking us all in here."),\
		_("All right, all right! I'll leave you alone. But I shall be watching you!"),\
		_("Tristan looks irritated as you approach him again."),\
		_("And it's not as if they would still be looking for the thief. As it turned out, it's been that Elf, Lady Silverhair. But so far they failed in retrieving the gems from her."),\
		_("As my mistress did certainly not steal them, they'll have a hard time in doing so I guess.")]

	cond = [\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_argument\") == 1\n",\
		"self.the_npc.get_val (\"talked_to\") == 1\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((26, 0, 1), (11, 1, -1), )),\
		("Default", -1, ((2, 0, 0), (12, 1, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		("Default", -1, ((13, 0, -1), (7, 0, -1), )),\
		("Default", -1, ((5, 0, -1), (14, 0, -1), )),\
		(None, -1, ((6, 0, -1), )),\
		("Default", -1, ((16, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((21, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", -1, ((25, 0, -1), )),\
		("Narrator", 0, ((1, 0, -1), )),\
		(None, -1, ((22, 0, -1), )),\
		(None, -1, ((4, 0, -1), )),\
		(None, -1, ((15, 0, -1), )),\
		("Default", -1, ((16, 0, -1), )),\
		("Default", -1, ((17, 0, -1), )),\
		("Default", -1, ((20, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		("Default", -1, ((19, 0, -1), (7, 0, -1), (18, 0, -1), )),\
		("Default", -1, ((25, 0, -1), (9, 0, -1), )),\
		("Default", -1, ((7, 0, -1), (23, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		("Default", -1, ((27, 0, -1), )),\
		(None, -1, ()),\
		("Narrator", -1, ((6, 0, -1), )),\
		("Default", -1, ((28, 0, -1), )),\
		(None, -1, ((8, 0, -1), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
