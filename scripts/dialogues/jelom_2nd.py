import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class jelom_2nd (dialogue.base):
	text = [None,\
		_("Back again, Half-Elf? Have you learned anything of importance from your mistress?"),\
		_("Nothing you'd be interested in, Jelom."),\
		_("It seems that Fingolson's gems are worthless to her."),\
		_("Really? I imagine you have some sort of proof for this, then?"),\
		_("I have this Chrysoberyl. Apparently it is no Catseye, so why should Lady Silverhair have stolen it?"),\
		_("You mean this is one of the stolen gems? How in hell did you come across that? And where are the others?"),\
		_("I don't know where the others are, but this one was hidden in Lady Silverhair's luggage."),\
		_("Slow down! Didn't you just claim that your mistress had no use for the gems? And now you're telling me that you found that one amongst her stuff. That makes no sense!"),\
		_("Unless the ... \"real\" thief wanted to direct all suspicion to your mistress. Ha! Nice idea, Half-elf. But why should I believe that your gem really belongs to Fingolson?"),\
		_("Oh no! You are Silverhair's loyal servant. And as long as there is no other suspect I cannot possibly trust in anything you say. Now take your gem and leave me alone!"),\
		_("Lady Silverhair said so."),\
		_("Oh! *The Lady Silverhair said so.* I assure you Half-Elf, the Lady Silverhair said quite a lot when we put her under arrest, and it wasn't very lady-like. Come back once you have something more substantial!"),\
		_("I'm just repeating Erek Stonebreaker's words."),\
		_("Now I'm surprised. What makes him believe all of a sudden that his Master is selling crap? That doesn't sound at all like the Erek I know."),\
		_("I showed him one of Fingolson's gems I found."),\
		_("What? One of the stolen gems? Tell me Half-Elf, where have you found that?"),\
		_("It was hidden in Lady Silverhair's luggage."),\
		_("If you don't believe me, go ask him yourself!"),\
		_("And leave my post? Unlike Talan I do know my duty. Now go and don't bother me again before you can't prove your words."),\
		_("That's not important. The important thing is that this gem is of poor quality. See?"),\
		_("Well, to me it looks valuable enough. Of course I am no expert in these matters, and I doubt that you are."),\
		_("Not you again, Half-Elf? Are you still trying to make me believe that your Mistress has no use for the gems?"),\
		_("I'd be just wasting my breath on you!"),\
		_("What's going on now? What are you doing here, Erek Stonebreaker?"),\
		_("I'm here on behalf of $name, master Rasgar. I can testify that his gem belongs to my Master, and that it is of insufficient quality to be of any use for the Lady Silverhair."),\
		_("I should have known it! Believe me Erek, these Half-Elves are  talking you into things you will regret later on. Is it not so, Half-Elf?"),\
		_("Listen Jelom, I am getting sick of you. What is it you want?"),\
		_("I want to be sure, that's all. I told you that I don't trust you in this matter. And you Erek, you might think that you know the truth, but perhaps it's just what your friend here made you believe."),\
		_("If this gem really belongs to Master Fingolson, why don't I hear what he has to say about it?"),\
		_("You think that I deceived Erek?"),\
		_("I wouldn't be surprised. And I find it more than suspicious that I heard nothing from the gem's owner yet. If it really belongs to Master Fingolson, he should be able to give reliable information."),\
		_("Uh, I haven't asked him yet."),\
		_("Perhaps you should do that then, Half-Elf. I'll be waiting here."),\
		_("Well, Master Fingolson is pretending that this gem is a valuable Catseye, despite the fact that it isn't."),\
		_("Is that true, Erek?"),\
		_("$name's gem is definitely no Catseye, master Rasgar. I hate to admit, but Master Fingolson appears to be ... lying!"),\
		_("Now I understand nothing at all. Listen you both, I have enough of this! We are going to see this Dwarf. And Lady Silverhair is coming with us. I want to hear what she has to say to all of this."),\
		_("It's about time you return, Half-Elf! Tell me, what does Master Fingolson say about this gem of yours?"),\
		_("Nothing. He refused to talk with me!"),\
		_("Ha, that's laughable. You want to solve this matter, and don't even manage to speak to Master Fingolson!? Out of my sight, and don't even think about coming back before you haven't talked to the Dwarf!")]

	cond = [\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"convince_jelom\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") > 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"have_gem\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") & 1 == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") & 2 == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"convince_jelom\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"convince_jelom\") == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_lies\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") < 3\n"]

	code = [\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"convince_jelom\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"convince_jelom\" , 3)\n",\
		"# make all dudes go down to Bjarn\nadonthell.gamedata_get_quest(\"demo\").set_val (\"the_end\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (22, 1, 5), (24, 1, 6), (38, 1, -1), )),\
		("Default", -1, ((2, 0, -1), (3, 0, 1), )),\
		(None, -1, ()),\
		(None, -1, ((4, 0, -1), )),\
		("Default", -1, ((11, 0, 3), (13, 0, 4), (5, 0, 2), )),\
		(None, -1, ((6, 0, -1), )),\
		("Default", -1, ((7, 0, -1), (20, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		("Default", -1, ((9, 0, -1), )),\
		("Default", -1, ((10, 0, -1), )),\
		("Default", 0, ()),\
		(None, -1, ((12, 0, -1), )),\
		("Default", -1, ()),\
		(None, -1, ((14, 0, -1), )),\
		("Default", -1, ((18, 0, -1), (15, 0, -1), )),\
		(None, -1, ((16, 0, -1), )),\
		("Default", -1, ((17, 0, -1), (20, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		(None, -1, ((19, 0, -1), )),\
		("Default", 0, ()),\
		(None, -1, ((21, 0, -1), )),\
		("Default", -1, ((10, 0, -1), )),\
		("Default", -1, ((13, 0, 4), (5, 0, 2), (23, 0, -1), )),\
		(None, -1, ()),\
		("Default", 1, ((25, 0, -1), )),\
		("Erek Stonebreaker", -1, ((26, 0, -1), )),\
		("Default", -1, ((27, 0, -1), (30, 0, -1), )),\
		(None, -1, ((28, 0, -1), )),\
		("Default", -1, ((29, 0, -1), )),\
		("Default", -1, ((34, 0, 7), (32, 0, -1), )),\
		(None, -1, ((31, 0, -1), )),\
		("Default", -1, ((34, 0, 7), (32, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Default", -1, ()),\
		(None, -1, ((35, 0, -1), )),\
		("Default", -1, ((36, 0, -1), )),\
		("Erek Stonebreaker", -1, ((37, 0, -1), )),\
		("Default", 2, ()),\
		("Default", -1, ((39, 0, 8), (34, 0, 7), )),\
		(None, -1, ((40, 0, -1), )),\
		("Default", -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n

	def __del__(self):
		if adonthell.gamedata_get_quest("demo").get_val ("the_end") == 1:
		    bjarn = adonthell.gamedata_get_character("Bjarn Fingolson")
		    bjarn.do_stuff ("await_player")
		
		    # make all dudes go down to Bjarn
		    shair = adonthell.gamedata_get_character("Imoen Silverhair")
		    shair.set_schedule ("to_cellar")
		    shair.time_callback_string ("2t", "walk")
		
		    jelom = adonthell.gamedata_get_character("Jelom Rasgar")
		    jelom.set_schedule ("to_cellar")
		    jelom.time_callback_string ("1t", "walk")
				
		    player = adonthell.gamedata_player ()
		    player.set_schedule ("to_cellar")
		    player.time_callback_string ("2t", "walk")
				
		    erek = adonthell.gamedata_get_character("Erek Stonebreaker")
		    erek.resume ()
		    erek.set_schedule ("to_cellar")
		    erek.time_callback_string ("3t", "walk")
				
		    fnir = adonthell.gamedata_get_character("Fellnir Kezular")
		    fnir.set_schedule ("to_cellar")
		    fnir.time_callback_string ("4t", "walk")
				
		    illig = adonthell.gamedata_get_character("Tristan Illig")
		    illig.set_schedule ("to_cellar")
		    illig.time_callback_string ("7t", "walk")
		

