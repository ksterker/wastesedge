import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class bjarn_start (dialogue.base):
	text = [None,\
		_("You try the door, but find it locked. From within the room you hear a deep voice."),\
		_("At the door to their room, Erek produces a key and unlocks it."),\
		_("Maybe I should not be doing this, but I do want my master to get his stones back."),\
		_("I do not wish to be disturbed right now, so please go away! First I am burgled, and now I can get no peace with all the busybodies running around, making my tragedy their business!"),\
		_("Erek, who is this, and why have you let him in?"),\
		_("This is $name, master, and he is investigating the theft of your gems. He wanted to talk to you, and I thought that maybe he could help."),\
		_("Yes, sir, that is correct. I am here on the behalf of Lady Silverhair, trying to get to the bottom of the disappearance of your stones."),\
		_("I think that \"theft\" is a better word for it than disappearance."),\
		_("Theft, then, if you prefer. Call it what you may, I would like to recover the gems and clear Lady Silverhair's name. Would you mind answering a question or two?"),\
		_("Actually, I would mind. I am sure that you already know what happened, so nothing can be gained from bothering me. I would rather you \"recover\" the gems from your mistress and return them to me!"),\
		_("Sir, please try to be reasonable. Have you even considered the possibility that Lady Silverhair is not the thief?"),\
		_("What, and ignore all the evidence to the contrary? She came here specifically to buy my gems, insulted their quality to weasel out of paying for them, and then stole them when the first opportunity presented itself!"),\
		_("Bjarn looks you up and down with a stern expression on his face; obviously he is not happy with the disturbance."),\
		_("Look, Half-Elf, I told you that I do not want to be bothered!"),\
		_("I'm just wondering whether Erek might have taken the gems."),\
		_("Why did you insult Lady Silverhair upon her arrival? You set her on edge, even before the negotiations started!"),\
		_("Don't you think that Alek Endhelm might be more likely a thief than Lady Silverhair?"),\
		_("You cannot possibly suspect Erek! He is so honest and idealistic that even if he had stolen the gems, he would confess the crime immediately! Do not waste my time with such ridiculous accusations!"),\
		_("But Alek Endhelm leads me to believe that the theft may have been committed before you went to bed."),\
		_("Ha! That sounds just like Alek Endhelm. You are a fool to be taken in by that scoundrel's words. The truth is that I personally packed the gems after Erek went to bed. That is, the theft has been committed later that night."),\
		_("You blame me for your mistress' absence of humour? All I wanted was to liven up the atmosphere before turning to business. I can see nothing wrong with that. Now please stop wasting my time!"),\
		_("Alek Endhelm? That shifty-looking mercenary? He is surely up to no good, but I doubt you can pin the crime on him to clear your mistress."),\
		_("But he was seen snooping around the parlour during negotiations."),\
		_("Well, it is true. He was really interested in my business as soon as I got here! He was snooping around, poking his nose into my affairs. Then he offered me his service as a guard."),\
		_("The roads have been getting more and more dangerous recently, that's for sure. But they would be even more dangerous with the likes of him \"guarding\" me! So I told him, in no uncertain terms, that I didn't like his looks!"),\
		_("What makes you so sure that he is innocent, if you think so poorly of him?"),\
		_("Come on, a clumsy, lumbering human sneaking into my room while I am asleep and stealing my gems! An ogre would be a more likely sneak thief than Alek Endhelm! He couldn't pick a lock if he had the key!"),\
		_("I cannot believe that you have the audacity to ask me questions about this! Please leave!"),\
		_("No, it had to have been one of your kind or a real Elf, that is for sure. Now, I am a busy man, so please stop wasting my time!"),\
		_("And you don't think he stole your gems in an act of revenge?"),\
		_("To me it seems as if Alek was just curious about your gems."),\
		_("And so was your Lady Silverhair! Listen, I don't know why I should be speaking with you, if all you care about is freeing your mistress. If you want to make yourself useful you better go and retrieve my Chrysoberyls."),\
		_("Well, you know Erek best, I guess."),\
		_("Really? According to Erek, you were asleep already when he started packing."),\
		_("Asleep? I? Certainly not! I was just taking a rest, perhaps. Later I put the pouch with the gems into our luggage, from where the thief - your fine mistress - stole it during the night!"),\
		_("I can't believe I am justifying myself in front of the thief's servant! Why am I talking to you at all! You are not doing anything to retrieve my Chrysoberyls. All you care about is freeing your mistress!"),\
		_("You are but wasting my time! Out of my sight you go!"),\
		_("Not even if I've found one of your \"Catseyes\"!"),\
		_("Really? I ... I am impressed. Let me see! And tell me where you found it."),\
		_("In the pantry."),\
		_("In Lady Silverhair's luggage."),\
		_("Ha, I knew it! Who else but Silverhair had reasons and the skills to steal my gems? I'm glad you are finally seeing the truth. Now there can be no more doubt about her guilt. Come, we must inform the guards!"),\
		_("Not so fast! According to Erek, this gem is no Catseye."),\
		_("But Lady Silverhair swears that this is no Catseye."),\
		_("Huh? Erek is young and has much to learn yet, so please excuse his mistake. But this gem is a Chrysoberyl Catseye, no doubt. Now hand it over, so I may take it to Jelom."),\
		_("The thief? Of course she would say that! Even you cannot be that foolish to take her word over mine. I tell you that this gem is a Chrysoberyl Catseye. Now hand it over, so I can take it to Jelom."),\
		_("Don't worry Master Fingolson, I will take care of that myself."),\
		_("I'm sorry, but I won't give this piece of evidence out of my hands."),\
		_("Oh well, it's not as if you could run off with the gem I suppose. You may keep it for now, as long as you see to it that Silverhair gets what she deserves. Now be on your way!"),\
		_("In the pantry? Can't you precise that some more? After all, the place you found the gem might give us a clue about the thief."),\
		_("It was hidden in Lady Silverhair's luggage.")]

	cond = [\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 0 or adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 3\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"ask_packed_gems\") == 1 or adonthell.gamedata_get_quest(\"demo\").get_val (\"ask_packed_gems\") == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_bjarns_insult\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_alek_eavesdrop\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"ask_packed_gems\") == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") > 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") & 2 == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") & 1 == 1\n"]

	code = [\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"bjarn_door_open\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"bjarn_door_open\" , 3)\n",\
		"adonthell.gamedata_get_character(\"Erek Stonebreaker\").do_stuff (\"leave_bjarn\")\nadonthell.gamedata_get_character(\"Erek Stonebreaker\").resume ()\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"ask_packed_gems\" , 3)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"bjarn_lies\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (2, 0, 1), (13, 0, 2), )),\
		("Narrator", 0, ((4, 0, -1), )),\
		("Narrator", 1, ((3, 0, -1), )),\
		("Erek Stonebreaker", -1, ((5, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ((6, 0, -1), )),\
		("Erek Stonebreaker", -1, ((7, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		("Default", -1, ((9, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", 2, ((11, 0, -1), )),\
		(None, -1, ((12, 0, -1), )),\
		("Default", -1, ((28, 0, -1), )),\
		("Narrator", -1, ((14, 0, -1), )),\
		("Default", -1, ((15, 0, 3), (16, 0, 4), (17, 0, 5), (38, 0, 7), )),\
		(None, -1, ((18, 0, -1), )),\
		(None, -1, ((21, 0, -1), )),\
		(None, -1, ((22, 0, -1), )),\
		("Default", -1, ((33, 0, -1), (19, 0, -1), )),\
		(None, -1, ((20, 0, -1), )),\
		("Default", -1, ((34, 0, 6), )),\
		("Default", -1, ()),\
		("Default", -1, ((23, 0, -1), (26, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		("Default", -1, ((25, 0, -1), )),\
		("Default", -1, ((31, 0, -1), (30, 0, -1), )),\
		(None, -1, ((27, 0, -1), )),\
		("Default", -1, ((29, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ()),\
		(None, -1, ((27, 0, -1), )),\
		(None, -1, ((32, 0, -1), )),\
		("Default", -1, ()),\
		(None, -1, ()),\
		(None, -1, ((35, 0, -1), )),\
		("Default", -1, ((36, 0, -1), )),\
		("Default", -1, ((37, 0, -1), )),\
		("Default", 3, ()),\
		(None, -1, ((39, 0, -1), )),\
		("Default", -1, ((40, 0, -1), (41, 0, -1), )),\
		(None, -1, ((50, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((43, 0, 8), (44, 0, 9), )),\
		(None, -1, ((45, 0, -1), )),\
		(None, -1, ((46, 0, -1), )),\
		("Default", -1, ((48, 0, -1), (47, 0, -1), )),\
		("Default", -1, ((48, 0, -1), (47, 0, -1), )),\
		(None, -1, ((49, 0, -1), )),\
		(None, -1, ((49, 0, -1), )),\
		("Default", 4, ()),\
		("Default", -1, ((51, 0, -1), )),\
		(None, -1, ((42, 0, -1), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
