import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class sarin_start (dialogue.base):
	text = [None,\
		_("What insolence! $name, do you believe the depths of what they have done to our Lady? To accuse her of common theft, as if she was a human! And to lock her away in this tiny, dirty room! I tell you, I cannot bear it."),\
		_("I understand, Sarin, but we must bear this for now. At least until I have been able to uncover the truth."),\
		_("The truth? The truth is that our Lady is innocent and that, that Dwarf ruffian, he's a liar."),\
		_("Perhaps so. Hopefully, we shall see whether he is. What do you know of him?"),\
		_("Very little, I'm happy to say. I was in the common room downstairs, arranging for dinner, when the Lady came out of the room they were in, as angry as I have ever seen her."),\
		_("I gather he is always difficult. Do you know anything else? About the other people at the inn, perhaps?"),\
		_("Nay, not a thing. An uncouth lot, save for the one. An artist, I think. Lady Silverhair had words with her when we arrived, but Janesta and I were too busy to learn her name."),\
		_("I'll have to speak to her. Perhaps she may know something. Thank you, Sarin. I'm glad you are here to watch over the Lady during this trouble."),\
		_("I wish I could do more, $name. Good luck to you."),\
		_("Her name is Frostbloom. Not terribly friendly, but the Lady thinks highly of her talents. She went so far as to buy that figurine on the mantle."),\
		_("Is that one of hers? She is indeed talented. I may only hope you are as talented in ending this trouble. Good luck to you, $name."),\
		_("He seems to be telling the truth about the theft. But I cannot believe that our Lady did the deed. There must be a true thief about."),\
		_("I beg you hurry and find him, then. For every minute you do not, is one minute closer our Lady is to peril."),\
		_("That barbarian must have done something terrible to put her in such a state.")]

	cond = [\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"talked_about_yeti\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") >= 3\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, -1), )),\
		("Sarin Trailfollower", -1, ((2, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		("Sarin Trailfollower", -1, ((4, 0, -1), (12, 0, 1), )),\
		(None, -1, ((5, 0, -1), )),\
		("Sarin Trailfollower", -1, ((14, 0, -1), )),\
		(None, -1, ((7, 0, -1), )),\
		("Sarin Trailfollower", -1, ((10, 0, 0), (8, 0, -1), )),\
		(None, -1, ((9, 0, -1), )),\
		("Sarin Trailfollower", -1, ()),\
		(None, -1, ((11, 0, -1), )),\
		("Sarin Trailfollower", -1, ()),\
		(None, -1, ((13, 0, -1), )),\
		("Sarin Trailfollower", -1, ()),\
		("Sarin Trailfollower", -1, ((6, 0, -1), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
