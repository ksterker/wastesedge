import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class frostbloom_start (dialogue.base):
	text = [None,\
		_("Hm?  What do you want?"),\
		_("I am a servant of Lady Imoen Silverhair, and I'd like to ask ..."),\
		_("I know who you are, and I do not care what you wish to ask.  Now go away.  The Yeti of my soul must have silence."),\
		_("You again?  I thought I told you to leave me alone."),\
		_("But lady, I must ask you about the theft..."),\
		_("The theft?  You mean your theft of my precious time, when I could be receiving inspiration?  I've lost enough of that already, thank you.  Now be gone, silly servant, you begin to annoy me."),\
		_("But, lady..."),\
		_("Off, I say!  I have no patience for this chatter!"),\
		_("I will go, but I will return to ask my questions.  I must have what you know of my Lady."),\
		_("The half-elf fixes you with a withering gaze.  For a moment, you feel as if you had been skewered.  Her voice is full of sarcasm."),\
		_("I look forward to it with all my heart.  For now, just go away."),\
		_("Back again, eh?  You do hunger for punishment, don't you."),\
		_("I try to be diligent, lady."),\
		_("Well, I must admit that such devotion deserves a reward.  Very well, you may stay for a while.  A short while.  My name is Rhayne Frostbloom.  Take care you remember it."),\
		_("Thank you, lady.  I would ask you about the theft, if I may."),\
		_("For goodness sake, do not bother me with that nonsense.  It's been all anyone speaks about here, and I for one am sick of it."),\
		_("I have seen the lovely Yeti you carved for my mistress.  It is quite impressive."),\
		_("Do you really think so?  I tried to make it worthy of the noble beast, but I always wonder if I have given it enough life."),\
		_("I'm hardly an expert, lady, but to my eye it is excellent."),\
		_("It is important.  The Lady Silverhair is in terrible danger."),\
		_("I know, I know.  And even if she is not hung, the Dwarves will be outraged.  What a foolish noise over such a little thing.  Gems are showy trash.  They cannot comprehend the complex soul of a Yeti."),\
		_("But this is hardly foolish, you must understand that."),\
		_("Frostbloom doesn't appear to hear you.  She stares off into space, occasionally whispering something about Yetis and souls, but you can make little sense of it."),\
		_("It is a masterpiece, my lady.  A true achievement that does credit to its model."),\
		_("Frostbloom eyes you suspiciously for a moment, then smiles."),\
		_("False flattery, eh?  I would wager my next commission you know nothing about the Yeti and their ways, yet would use this praise to loosen my tongue.  Well, have I spoken truth?"),\
		_("No, lady, I honestly appreciate the talent in your piece.  That is, you are honestly talented."),\
		_("My lady, you have a keen eye and a keener wit.  That is precisely why I gave you praise, although you truly do deserve it."),\
		_("Huh! Off with you, I'll not waste time listening to your prattle. If you have a mind to be more honest, come back again.  Otherwise, take your foolishness elsewhere."),\
		_("Very good answer.  I believe you'll do.  Ask of me what you will."),\
		_("Flattery will get you nowhere, so long as you pretend it is nothing more.  I have no time for such idiocy."),\
		_("Ah, the persistent young servant.  Do you wish to ask me something more?"),\
		_("Did anything unusual happen last night?"),\
		_("What do you know of the dwarf, Bjarn?"),\
		_("Do you know anything of the people staying here at Waste's Edge?"),\
		_("Back to try again?  Then tell me whether you offered false flattery!  Then we'll see what you're made of."),\
		_("Unusual?  It was a warm night, which I am told is quite odd for this time of year.  Is that what you had in mind?"),\
		_("Of course not!  Please, my Lady's very life may be in danger!"),\
		_("It is such fun to tease you, do you realize that?  But there was something odd about the night.  There was a sound, which went on for a short time."),\
		_("Has your lady told you any more about the sounds I heard?  I cannot recall anything else of note."),\
		_("A rough little creature.  No trace of creativity in the man at all.  I only noticed him long enough to ignore him, and we were both the better for it."),\
		_("The family who serves the travellers are good folk.  There is a trace of the yeti's spirit in them, deep inside."),\
		_("But the rest are barely forth a speck of dust in the wind.  Dull minds, every one.  Your lady seems the sole exception, I am sorry to say.  But at least the rest leave me in peace."),\
		_("I could not tell you what it was, but I doubt very much these humans would have heard it.  You might ask your fair lady about it, her ears should be keener than mine.  Although she may have been too preoccupied to notice."),\
		_("I may not have an educated taste, but I do know talent when standing in front of me."),\
		_("I must pursue my inspiration, even in this dismal place. Alone, if you please.")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"self.the_npc.get_val (\"talked_to\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"talked_about_yeti\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"talked_about_yeti\") == 1 and self.the_npc.get_val (\"flattered\") == 0\n",\
		"self.the_npc.get_val (\"flattered\") == 2\n",\
		"self.the_npc.get_val (\"flattered\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") != 0\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\" , 1)\nadonthell.gamedata_get_quest(\"demo\").set_val (\"know_frostbloom\" , 1)\n",\
		"self.the_npc.set_val (\"flattered\" , 1)\n",\
		"self.the_npc.set_val (\"flattered\" , 2)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_noise\" , adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") | 2)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (4, 0, 1), (12, 0, 2), (36, 0, 4), (32, 0, 3), )),\
		("Rhayne Frostbloom", 0, ((2, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		("Rhayne Frostbloom", -1, ()),\
		("Rhayne Frostbloom", -1, ((5, 0, -1), )),\
		(None, -1, ((6, 0, -1), )),\
		("Rhayne Frostbloom", -1, ((7, 0, -1), (9, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		("Rhayne Frostbloom", -1, ()),\
		(None, -1, ((10, 0, -1), )),\
		("Narrator", -1, ((11, 0, -1), )),\
		("Rhayne Frostbloom", -1, ()),\
		("Rhayne Frostbloom", -1, ((13, 0, -1), )),\
		(None, -1, ((14, 0, -1), )),\
		("Rhayne Frostbloom", -1, ((15, 0, -1), (17, 0, -1), )),\
		(None, -1, ((16, 0, -1), )),\
		("Rhayne Frostbloom", -1, ((20, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		("Rhayne Frostbloom", -1, ((19, 0, -1), (24, 0, -1), )),\
		(None, -1, ((31, 0, -1), )),\
		(None, -1, ((21, 0, -1), )),\
		("Default", -1, ((22, 0, -1), )),\
		(None, -1, ((23, 0, -1), )),\
		("Narrator", -1, ()),\
		(None, -1, ((25, 0, -1), )),\
		("Narrator", -1, ((26, 0, -1), )),\
		("Default", -1, ((27, 0, -1), (45, 0, -1), (28, 0, -1), )),\
		(None, -1, ((29, 0, -1), )),\
		(None, -1, ((30, 0, -1), )),\
		("Default", 1, ((46, 0, -1), )),\
		("Default", 2, ((33, 0, -1), (34, 0, -1), (35, 0, -1), )),\
		("Default", -1, ()),\
		("Rhayne Frostbloom", -1, ((33, 0, -1), (34, 0, -1), (35, 0, -1), )),\
		(None, -1, ((40, 0, 5), (37, 1, -1), )),\
		(None, -1, ((41, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Rhayne Frostbloom", -1, ((27, 0, -1), (45, 0, -1), (28, 0, -1), )),\
		("Default", 3, ((38, 0, -1), )),\
		(None, -1, ((39, 0, -1), )),\
		("Default", -1, ((44, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ()),\
		("Default", -1, ((43, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ()),\
		(None, -1, ((29, 0, -1), )),\
		("Default", -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
