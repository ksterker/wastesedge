import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class alek_start (dialogue.base):
	text = [None,\
		_("And who do we have here? A damn freak Half-Elf I say!"),\
		_("That's $name, you ass! I'm working for Lady Silverhair."),\
		_("For Lady Silverhair, eh? Now that scares the shit out of me, Half-Elf. Go and bother somebody else!"),\
		_("I'll be damned if that's not our freakish Half-Elf! Still pokin' your nose in other peoples business?"),\
		_("Listen! Need we really go through all this crap again?"),\
		_("You're getting on my nerves, Half-Elf. Go ahead then, ask your stupid questions."),\
		_("I don't like you either, friend. But unfortunately, I need to talk to you."),\
		_("You? Tell me, what would one of your sort want from Alek Endhelm?"),\
		_("I need some questions answered, concerning the theft."),\
		_("I'm just wondering what someone like you is doing at Waste's Edge."),\
		_("That's none of your business Half-Elf. Don't waste my time, will ya!?"),\
		_("So it's none of my business if valuables disappear around here and my mistress is held responsible?"),\
		_("I don't like the implication. It's not wise going around, calling other people thieves."),\
		_("So far, I've called you nothing. But if you don't help me with a few answers, I might change my mind."),\
		_("I daresay being caught eavesdropping on the victim just before his gems are stolen is unwise as well."),\
		_("Who told you? The little gritsucker? He'll say what his master tells him to say, haven't you noticed?"),\
		_("Come on, don't make a face like that, Half-Elf. Of course I was there. I was on my way to see what all the shouting was about. Looked like my skills might have been needed."),\
		_("Not so quick! Who do you think you are, walking around pestering other people?"),\
		_("If you must know, I'm working for Lady Silverhair."),\
		_("I'm here to get to the bottom of the matter. So if you don't want to share Silverhair's fate, you had better answer my questions."),\
		_("To hell with you, Half-Elf. What do you want to know?"),\
		_("Next moment, the door's burstin' open and your lovely mistress rushes past ... - I don't think you could call that eavesdropping."),\
		_("Leave the thinking to me and simply answer my questions, will you?"),\
		_("What is your business here, then?"),\
		_("If you don't believe me, why don't you ask Fingolson himself? Oh, I forgot. He doesn't want to talk with people of your kind, does he? Well, I cannot blame him for that."),\
		_("What on earth has my business to do with the theft? You're just wasting my time with your bloody questions."),\
		_("I fear you do not understand, Half-Elf. If you keep asking for irrelevant details you'll accomplish nothing. But I might know a thing or two, were you only asking the right questions."),\
		_("Listen, man. I am not interested into your gossip."),\
		_("So what questions should I ask, in your opinion?"),\
		_("I don't see how *that* could get me any further."),\
		_("Just tryin' to help. But a smartass like you doesn't need any help, do you?"),\
		_("Even if I was, I bet you could never prove it, Half-Elf. You wouldn't recognise a clue if someone pushed your pretty nose into it."),\
		_("I certainly don't need yours. For all I know, you may well be the thief."),\
		_("Now do you have any dumb questions left, or can I go back to my drink?"),\
		_("Simply answering my questions would be help enough!"),\
		_("If you say so. Then go on, ask what you want, even if it's not getting you anywhere."),\
		_("Who's wasting whose time here? The sooner you answer my questions, the sooner I leave you to yourself. Even you should understand this!"),\
		_("Not before I get some answers out of you. You don't have something to hide, do you?"),\
		_("So what is your business here, then?"),\
		_("If it makes you happy; I made camp here on my way back from Limebruck where I had an ... appointment, which is absolutely none of your concern. I'm just an innocent traveller caught in this bloody mess."),\
		_("Master Orloth says your chamber is below ground, next to the Dwarf's. So did you hear anything unusual in the night of the theft?"),\
		_("No I didn't. But perhaps there wasn't anything unusual to hear that night."),\
		_("What do you mean?"),\
		_("You're a slow thinker, eh Half-Elf!? Hasn't it occurred to you that the theft might've already been committed by the time Fingolson went to bed?"),\
		_("Don't make me laugh. That's the most ridiculous thing I ever heard."),\
		_("Do you have any proof of this?"),\
		_("That's impossible. Fingolson had the gems on him during the negotiations. And afterwards, either he or Erek were down in their room."),\
		_("Well, that would rule out quite a few possible thieves, wouldn't it?"),\
		_("You want to tell me that Erek has taken the gems?"),\
		_("You don't believe me? Perhaps you should ask Erek who has packed them then!"),\
		_("I don't. But since you are so good in finding stuff out, this shouldn't be a problem for you!"),\
		_("If you don't like what you hear from me, why don't you look for different company, Half-Elf?"),\
		_("So? Was that of any help? I shouldn't think so. A waste of time it was!"),\
		_("For what would they have needed your skills?"),\
		_("What were you doing outside the parlour during negotiations? Trying to spy on Master Fingolson?"),\
		_("Perhaps it's just me, but I'd ask myself why the ... thief hasn't left Waste's Edge."),\
		_("The muscular fellow in front of you has the air of a troublemaker about him. Scars all over his body are evidence of his readiness to use the sword he is carrying. He eyes you with undisguised distaste as you approach."),\
		_("Well, why hasn't he?"),\
		_("Good question, isn't it! Now if I were you, Half-Elf, I'd be off to a quiet corner and made some use of what brain I had."),\
		_("Perhaps you are right. Any further conversation would be useless anyway. So I'll leave you ... for now!"),\
		_("Very funny! Should I ever need a fool, I'll send for you."),\
		_("Why should I \"spy\" on a conversation that could be heard up to Erinsford. Nah, I was about to look whether my skills might be needed."),\
		_("You disappoint me, Half-Elf. The poor Dwarfs were practically attacked by that furious woman. How should I know she wasn't about to turn them into toads or something?"),\
		_("Don't tell me you thought Fingolson would enrol you as his guard?"),\
		_("He wasn't very enthusiastic about you, am I right?"),\
		_("So what? You think I stole his gems because he didn't accept my offer?"),\
		_("Well, that's it! I have enough of your useless blather. But I shall be watching you!"),\
		_("I think you wouldn't need any reason at all. However, until I find a clue as to your guilt, I'll have to leave you to yourself."),\
		_("Endhelm puts a threatening grin on his face as he sees you walking towards him."),\
		_("Actually, there is nothing you could possibly tell me.")]

	cond = [\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_alek_eavesdrop\")\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_aleks_room\") == 1\n",\
		"not self.eavesdrop and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_alek_eavesdrop\")\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 3\n",\
		"self.the_npc.get_val (\"talked_to\") != 0\n"]

	code = [\
		"work = adonthell.gamedata_get_quest(\"demo\").get_val (\"work_4_shair\")\nwork = work | 2\nadonthell.gamedata_get_quest(\"demo\").set_val (\"work_4_shair\" , work)\n",\
		"self.eavesdrop = 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"ask_packed_gems\" , 1)\n",\
		"self.the_npc.set_val (\"talked_to\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((69, 0, 4), (57, 1, -1), )),\
		("Default", -1, ((2, 0, -1), (7, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		("Default", 0, ((38, 0, -1), )),\
		("Default", -1, ((5, 0, -1), )),\
		(None, -1, ((6, 0, -1), )),\
		("Default", -1, ((70, 0, -1), (24, 0, -1), (41, 0, 1), (55, 0, 2), )),\
		(None, -1, ((8, 0, -1), )),\
		("Default", -1, ((9, 0, -1), (10, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		(None, -1, ((11, 0, -1), )),\
		("Default", -1, ((12, 0, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		("Default", -1, ((14, 0, -1), (15, 0, 0), )),\
		(None, -1, ((21, 0, -1), )),\
		(None, 1, ((16, 0, -1), )),\
		("Default", -1, ((17, 0, -1), )),\
		("Default", -1, ((22, 0, -1), )),\
		("Default", -1, ((20, 0, -1), (19, 0, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		(None, -1, ((21, 0, -1), )),\
		("Default", -1, ((24, 0, -1), (41, 0, 1), (55, 0, 2), )),\
		("Default", -1, ((23, 0, -1), (54, 0, -1), )),\
		(None, -1, ((21, 0, -1), )),\
		(None, -1, ((26, 0, -1), )),\
		("Default", -1, ((67, 0, -1), (65, 0, 3), )),\
		("Default", -1, ((37, 0, -1), )),\
		("Default", -1, ((29, 0, -1), (28, 0, -1), )),\
		(None, -1, ((31, 0, -1), )),\
		(None, -1, ((56, 0, -1), )),\
		(None, -1, ((31, 0, -1), )),\
		("Default", -1, ((33, 0, -1), (35, 0, -1), )),\
		("Default", -1, ((34, 0, -1), )),\
		(None, -1, ((32, 0, -1), )),\
		("Default", -1, ((39, 0, -1), (41, 0, 1), (55, 0, 2), )),\
		(None, -1, ((36, 0, -1), )),\
		("Default", -1, ((39, 0, -1), (41, 0, 1), (55, 0, 2), )),\
		(None, -1, ((27, 0, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		(None, -1, ((40, 0, -1), )),\
		("Default", -1, ((53, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((43, 0, -1), )),\
		(None, -1, ((44, 0, -1), )),\
		("Default", -1, ((45, 0, -1), (46, 0, -1), (47, 0, -1), )),\
		(None, -1, ((52, 0, -1), )),\
		(None, -1, ((51, 0, -1), )),\
		(None, -1, ((48, 0, -1), )),\
		("Default", -1, ((49, 0, -1), )),\
		(None, -1, ((50, 0, -1), )),\
		("Default", 2, ((45, 0, -1), (46, 0, -1), )),\
		("Default", -1, ((67, 0, -1), )),\
		("Default", -1, ((60, 0, -1), )),\
		("Default", -1, ((67, 0, -1), )),\
		(None, -1, ((63, 0, -1), )),\
		(None, -1, ((62, 0, -1), )),\
		("Default", -1, ((58, 0, -1), (30, 0, -1), )),\
		("Narrator", 3, ((1, 0, -1), )),\
		(None, -1, ((59, 0, -1), )),\
		("Default", -1, ((60, 0, -1), (61, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((31, 0, -1), )),\
		("Default", -1, ((54, 0, -1), )),\
		("Default", -1, ((45, 0, -1), (64, 0, -1), )),\
		(None, -1, ((25, 0, -1), )),\
		(None, -1, ((66, 0, -1), )),\
		("Default", -1, ((68, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ()),\
		("Narrator", -1, ((4, 0, -1), )),\
		(None, -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
