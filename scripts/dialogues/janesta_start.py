import dialogue
# -- pygettext support
def _(message): return message

class janesta_start (dialogue.base):
	text = [None,\
		_("Oh, $name, we've been so worried for the Mistress.  Can't you do something to set her free?"),\
		_("I will try, Janesta.  But you must be brave.  This is a difficult time for Lady Silverhair, and she needs us all to help her though."),\
		_("I will try.  Thank you, $name."),\
		_("Perhaps.  Do you know anything about this dwarf, Fingolson?"),\
		_("Nothing, I'm afraid.  This is my first time here, and I was brought straight to the Mistress' room to make it ready.  This room is so awful, I cannot see how they expect a High Born to stand it."),\
		_("I see.  Thank you, Janesta.  I'm glad you are here to care for our Lady."),\
		_("Oh, $name.  I pray that this will turn out right.")]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, -1), )),\
		("Janesta Skywind", -1, ((2, 0, -1), (4, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		("Janesta Skywind", -1, ()),\
		(None, -1, ((5, 0, -1), )),\
		("Janesta Skywind", -1, ((6, 0, -1), )),\
		(None, -1, ((7, 0, -1), )),\
		("Default", -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
