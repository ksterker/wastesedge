import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class jelom_start (dialogue.base):
	text = [None,\
		_("Halt there! No-one is allowed into the prisoner's room!"),\
		_("Stop right there, Half-Elf! You know that you are not allowed in there!"),\
		_("No-one is allowed into the prisoner's room, so please leave this hallway!"),\
		_("You again, Half-Elf? What do you want this time?"),\
		_("Ah, you must be Jelom. Talan told me that I could find you here."),\
		_("And just who are you to prevent me from entering, sir?"),\
		_("Nice to see you again, Jelom. Look, I have some more questions regarding the theft."),\
		_("Look, Jelom, I found out something that will cast some serious doubt on Lady Silverhair having committed the theft!"),\
		_("My name is Jelom, and I am the chief of the guard at Waste's Edge! Who the hell are you?"),\
		_("Who are you, and why were you looking for me?"),\
		_("My name is $name. I'm investigating the theft and I have a few questions for you."),\
		_("And what might those questions be, Half-Elf?"),\
		_("I doubt that, but since I won't get any peace from your pestering until you tell me, go ahead."),\
		_("You trust in the overactive imagination of some little kid? I know from Talan that everything was quiet during the night.  And I take the word of my own guard over Oliver's!"),\
		_("Talan did not hear anything that night, because he was not at his post."),\
		_("What do you mean? Why wasn't he at his post?"),\
		_("He sneaked away to take a nap."),\
		_("He wandered off to practise singing, of all things!"),\
		_("A nap? I knew it! I had suspected that he caught some shuteye on duty from time to time, but have never caught him at it! He is in big trouble, this time!"),\
		_("Singing? What, does the fool want to be a bard now? He is in big trouble now!"),\
		_("But regardless of that, how do you know that it was not Silverhair herself who went to the stables and caused the noise? After stealing Master Fingolson's gems!"),\
		_("Erek actually packed the gems, according to Alek. Do you think he could be mixed up in this?"),\
		_("Alek Endhelm was eavesdropping outside the room during the negotiations, according to Erek. Do you think he could be mixed up in this?"),\
		_("Erek? Come on, don't be stupid. You are a more likely thief than Erek, and you weren't even here! It is just like Alek to tell you things like that!"),\
		_("Why do you say that?"),\
		_("Don't get excited, half-elf. Alek looks like scum, and probably is, being a mercenary, but there is no reason to suspect him of the theft. In fact, I hear that he offered his services to Bjarn as a guard."),\
		_("You don't think that is a little suspicious?"),\
		_("Look, Half-Elf, I am getting pretty damn tired of you and your questions. This investigation has nothing to do with you, so why don't you keep your nose out of it? Now get the hell out of here!"),\
		_("Can you tell me what happened on the night of the theft?"),\
		_("No, I can't. Talan was on guard duty. Go bother him."),\
		_("You won't tell me anything about your own investigation, then?"),\
		_("I am Lady Silverhair's clerk. I demand to see her immediately!"),\
		_("It does not matter who you are. None may leave this room and none may enter. 'Tis as simple as that."),\
		_("Who's order is this?"),\
		_("What harm could it do if I spoke to my mistress?"),\
		_("Mine! As long as Silverhair does not give in and hands out Master Fingolson's gems she's staying where she is. On her own!"),\
		_("I assure you, Lady Silverhair is innocent."),\
		_("Really? Too bad then, that all the facts I know prove the opposite."),\
		_("Now get lost!"),\
		_("How should I know!? But I'm not taking any risk."),\
		_("The stableboy, Oliver, heard a noise in the stables, well after everyone had gone to sleep."),\
		_("But that noise might have been caused by the real thief!"),\
		_("I say this is crap. You'll need better arguments then mere fantasies of a child to convince me. Now don't hold me off my duty!"),\
		_("Did you know that Talan left his post during the night of the theft?"),\
		_("Her servants could certainly confirm that she did not leave the room that night."),\
		_("Ha! They'd do everything to please their mistress. I wouldn't trust in any of their words."),\
		_("Well, everybody knows that Elves can move with absolute silence."),\
		_("Hm ... yes, that's a fact. You are right, Half-Elf. Something strange is going on."),\
		_("Maybe you should go in and see if your mistress can shed some light on the whole affair. However, until we find a new suspect, I'll be keeping an eye on her."),\
		_("What!? Are you telling me the kid was right after all? I don't believe it! Can't I even trust my own men any more!? Tell me, what was he doing?"),\
		_("You investigate the theft? You don't look at all like the officer I sent Bregon for. What makes you believe you could meddle in my affairs?"),\
		_("My mistress has been wrongly accused, and I intend to clear her name."),\
		_("Listen, Half-Elf! The theft and any investigations are business of the guard and none of yours! But by the looks of it, the only way to keep your nose out would be to lock you up."),\
		_("So I won't prevent you from pestering the folk at the Inn. But should you find out anything, you report to me, you understand! Now, what is it you want from me?")]

	cond = [\
		"self.the_player.get_val (\"at_silverhairs_door\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_jelom\") != 2\n",\
		"self.the_player.get_val (\"at_silverhairs_door\") == 1\n",\
		"self.the_player.get_val (\"at_silverhairs_door\") != 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_jelom\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_jelom\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_olivers_noise\") == 1 and self.the_npc.get_val (\"not_convinced\") == 0 and self.the_npc.get_val (\"allows_meddling\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"ask_packed_gems\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_alek_eavesdrop\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 2 and self.the_npc.get_val (\"not_convinced\") == 1\n",\
		"self.the_npc.get_val (\"allows_meddling\") == 0\n"]

	code = [\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"told_on_talan\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_jelom\" , 2)\n",\
		"self.the_npc.set_val (\"not_convinced\" , 1     )\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"silverhair_free\" , 1)\nself.the_npc.set_dialogue (\"dialogues.jelom_2nd\")\n",\
		"self.the_npc.set_val (\"allows_meddling\" , 1)\nadonthell.gamedata_get_quest(\"demo\").set_val (\"know_jelom\" , 2)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (3, 1, 2), (2, 1, 1), (4, 1, -1), )),\
		("Default", -1, ((6, 0, 3), (5, 1, -1), )),\
		("Default", -1, ((32, 0, -1), (8, 0, 4), (44, 1, 9), (7, 1, -1), )),\
		("Default", -1, ((6, 0, 3), (5, 1, -1), )),\
		("Default", -1, ((8, 0, 4), (44, 1, 9), (7, 1, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		(None, -1, ((9, 0, -1), )),\
		(None, -1, ((53, 0, 10), (12, 1, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		("Default", -1, ((32, 0, -1), (11, 0, -1), )),\
		("Default", -1, ((32, 0, -1), (11, 0, -1), )),\
		(None, -1, ((51, 0, -1), )),\
		("Default", -1, ((23, 0, 7), (22, 0, 6), (44, 1, 9), (29, 0, 8), )),\
		("Default", -1, ((41, 0, -1), )),\
		("Default", -1, ((15, 0, 5), (42, 0, -1), )),\
		(None, -1, ((16, 0, -1), )),\
		("Default", -1, ((17, 0, -1), (18, 0, -1), )),\
		(None, -1, ((19, 0, -1), )),\
		(None, 0, ((20, 0, -1), )),\
		("Default", -1, ((21, 0, -1), )),\
		("Default", -1, ((21, 0, -1), )),\
		("Default", -1, ((45, 0, -1), (47, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		(None, -1, ((26, 0, -1), )),\
		("Default", -1, ((25, 0, -1), )),\
		(None, -1, ((26, 0, -1), )),\
		("Default", -1, ((27, 0, -1), )),\
		(None, -1, ((28, 0, -1), )),\
		("Default", -1, ()),\
		(None, -1, ((30, 0, -1), )),\
		("Default", -1, ((31, 0, -1), )),\
		(None, -1, ((28, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Default", -1, ((34, 0, -1), (35, 0, -1), )),\
		(None, -1, ((36, 0, -1), )),\
		(None, -1, ((40, 0, -1), )),\
		("Default", -1, ((37, 0, -1), (35, 0, -1), )),\
		(None, -1, ((38, 0, -1), )),\
		("Default", -1, ((39, 0, -1), )),\
		("Default", 1, ()),\
		("Default", -1, ((39, 0, -1), )),\
		(None, -1, ((14, 0, -1), )),\
		(None, -1, ((43, 0, -1), )),\
		("Default", 2, ()),\
		(None, -1, ((50, 0, -1), )),\
		(None, -1, ((46, 0, -1), )),\
		("Default", -1, ((47, 0, -1), )),\
		(None, -1, ((48, 0, -1), )),\
		("Default", -1, ((49, 0, -1), )),\
		("Default", 3, ()),\
		("Default", -1, ((17, 0, -1), (18, 0, -1), )),\
		("Default", -1, ((52, 0, -1), )),\
		(None, -1, ((53, 0, 10), )),\
		("Default", 4, ((54, 0, -1), )),\
		("Default", -1, ((23, 0, 7), (22, 0, 6), (29, 0, 8), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
