import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class oliver_start (dialogue.base):
	text = [None,\
		_("As he notices you, the boy stops whatever he's been doing. With a cheerful grin on his face, he turns towards you."),\
		_("Hello sir! Welcome to Waste's Edge."),\
		_("Oh! I am Oliver, sir. I help Mum and Dad with the Inn. Looking after the stables and such."),\
		_("Why yes! Would you belive that we have an actual Elven Lady staying at the Inn?"),\
		_("Really? An Elven Lady?"),\
		_("Yes, sir. Lady Silverbeard. From Cirdanth. And her two servants! She frightened me a bit, but now she's locked up in her room."),\
		_("And who would you be?"),\
		_("You can surely tell me something about Waste's Edge, then."),\
		_("Did something unusual happen here lately, Oliver?"),\
		_("Have you heard about the theft, sir? Everybody speaks about it."),\
		_("Then I don't want to keep you off your work any longer."),\
		_("Are there other guests too?"),\
		_("Yes, but they are just ordinary people. Merchants and such."),\
		_("What can you tell me about that?"),\
		_("Can you imagine, sir? The Elven Lady robbed Master Fingolson in his sleep. And none of the adults noticed anything."),\
		_("Why would anyone want to lock her up?"),\
		_("Then you better tell me about the Elven Lady, Oliver."),\
		_("Well, thank you for the information. Until later."),\
		_("Who is Master Fingolson?"),\
		_("But you heard something that night?"),\
		_("Just another Dwarf from Uzdun'kal. He sells jewels and such. We get a lot of them here, but none of them got robbed so far."),\
		_("Speaking of that, you say you noticed something that night?"),\
		_("Yeah. Someone must have been in the stables. But when I went and had a look, they were gone."),\
		_("I see. Thank you for your help, Oliver. Until later."),\
		_("Oliver looks pleased as he sees you nearing."),\
		_("Uh, hello again sir. Do you have more questions?"),\
		_("Can you tell me something about Waste's Edge, Oliver?"),\
		_("What do you know about the theft?"),\
		_("Oliver leads you to a room on the first floor."),\
		_("I hope you like it, sir. All the other rooms are occupied."),\
		_("You have a lot of guests here at the moment, then?"),\
		_("Don't worry Oliver. This one is fine."),\
		_("Yes sir. And with that theft, nobody can leave."),\
		_("Nobody can leave?"),\
		_("No. As long as Master Fingolson's jewels are not found, the guards don't allow it."),\
		_("I see. Thank you Oliver. Until later.")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"adonthell.gamedata_get_character (\"Oliver Redwyne\").submap () == 12\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_olivers_noise\" , 1)\n",\
		"self.the_npc.set_val (\"talked_to\" , 1)\nself.the_npc.set_val (\"goto_barn\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((29, 0, 1), (1, 1, 0), (25, 1, -1), )),\
		("Narrator", 0, ((2, 0, -1), )),\
		("Default", -1, ((7, 0, -1), )),\
		("Default", -1, ((11, 0, -1), (8, 0, -1), (9, 0, -1), )),\
		("Default", -1, ((12, 0, -1), (5, 0, -1), )),\
		(None, -1, ((6, 0, -1), )),\
		("Default", -1, ((16, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		(None, -1, ((4, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", -1, ((14, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((13, 0, -1), )),\
		("Default", -1, ((18, 0, -1), (17, 0, -1), )),\
		(None, -1, ((15, 0, -1), )),\
		("Default", -1, ((19, 0, -1), (20, 0, -1), )),\
		(None, -1, ((15, 0, -1), )),\
		(None, -1, ((6, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((21, 0, -1), )),\
		(None, -1, ((23, 0, -1), )),\
		("Default", -1, ((22, 0, -1), )),\
		(None, -1, ((23, 0, -1), )),\
		("Default", 1, ((24, 0, -1), )),\
		(None, -1, ()),\
		("Narrator", -1, ((26, 0, -1), )),\
		("Default", -1, ((27, 0, -1), (28, 0, -1), )),\
		(None, -1, ((4, 0, -1), )),\
		(None, -1, ((15, 0, -1), )),\
		("Narrator", 2, ((30, 0, -1), )),\
		("Default", -1, ((31, 0, -1), (32, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((28, 0, -1), (34, 0, -1), )),\
		(None, -1, ((35, 0, -1), )),\
		("Default", -1, ((36, 0, -1), )),\
		(None, -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n

	def __del__(self):
		if self.the_npc.get_val ("goto_barn") == 1:
		    adonthell.gamedata_get_character("Oliver Redwyne").do_stuff ("goto_barn")

