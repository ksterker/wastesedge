import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class fellnir_start (dialogue.base):
	text = [None,\
		_("What do you want from me?  I don't know anything."),\
		_("I am with Lady Silverhair, and I am trying to prove her innocence.  Do you know what happened here?"),\
		_("Fellnir looks suspiciously at you.  He absently jots something down in a notebook and shifts one of his beakers slightly."),\
		_("Ask somebody else.  Anybody.  I just keep to myself and I don't know anything."),\
		_("He turns his attention back to his work, poring over the array of steaming liquids and decanters of unknown origin.  You cannot seem to get his attention again."),\
		_("You've been such a great help sir, I hate to bother you again.  But I seem to have angered the innkeeper's wife, and I need her help.  Have you any advice?"),\
		_("Excuse me? I realize you know nothing of the theft, but you must know the people of this inn well enough. Is there any way the guard could be convinced to allow me into my Lady's room?"),\
		_("Pardon me, good sir?  I hate to trouble you, but do you know this Fingolson well?  I need to enter his room but he will not allow me."),\
		_("I'm still trying to find information that may help my employer.  Are you certain you cannot help?"),\
		_("Do you know anything about strange noises the night of the theft?"),\
		_("I have better things to do than pay attention to what idle people do with their time."),\
		_("Fellnir doesn't even look up at you as you speak.  He mutters a little, \"Take equal parts of vitriol, nitre and sal ammoniac ...\"  Then he speaks more clearly to you."),\
		_("I would have thought elves and their sort would be more creative.  There's more than one way into a room, you know.  Now leave me be."),\
		_("Fellnir picks up a decanter and puts it down, then peers through a length of piping.  He blows into it, then inserts the end into the bottle.  After a while, he turns to you."),\
		_("I wouldn't open my door either to someone as nosy as you.  Try asking someone he likes.  Erek, maybe.  So long as you're not talking to me.  I don't know anything, so I wish you'd stop bothering me."),\
		_("Fellnir pours a blueish liquid into one primarily red, and the resulting mixture turns inexplicably green. He swirls it before his eyes for a moment, then takes a sip. By the look on his face, it doesn't taste very good."),\
		_("Well, of course she's upset.  You got a friend of hers in trouble.  I don't want anything to do with it, you straighten it out with the young guard yourself.  I'm just keeping to myself here."),\
		_("As you finish your question, bubbles begin appearing in a bottle that has no visible flame under it.  It boils for a few moments, until suddenly there is a puff of steam and half the liquid vanishes.  Fellnir is not impressed at this.")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"adonthell.gamedata_get_character(\"Lucia Redwyne\").get_val (\"refuses_key\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"pantry_locked\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_jelom\") == 2 and adonthell.gamedata_get_character(\"Imoen Silverhair\").get_val (\"talked_to\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") != 0 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 0\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, -1), )),\
		("Fellnir Kezular", -1, ((2, 0, 0), (7, 1, 2), (8, 1, 3), (10, 1, 4), (6, 1, 1), (9, 1, -1), )),\
		(None, 0, ((3, 0, -1), )),\
		("Narrator", -1, ((4, 0, -1), )),\
		("Default", -1, ((5, 0, -1), )),\
		("Narrator", -1, ()),\
		(None, -1, ((12, 0, -1), )),\
		(None, -1, ((16, 0, -1), )),\
		(None, -1, ((14, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		("Default", -1, ((5, 0, -1), )),\
		("Narrator", -1, ((17, 0, -1), )),\
		("Default", -1, ((5, 0, -1), )),\
		("Narrator", -1, ((15, 0, -1), )),\
		("Default", -1, ((5, 0, -1), )),\
		("Narrator", -1, ((13, 0, -1), )),\
		("Default", -1, ((5, 0, -1), )),\
		("Narrator", -1, ((11, 0, -1), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
