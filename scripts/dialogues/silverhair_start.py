import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class silverhair_start (dialogue.base):
	text = [None,\
		_("Oh!!"),\
		_("$name, have you found anything yet?  This confinement is intolerable, as you may well understand."),\
		_("Mistress!  Mistress!  $name has come!"),\
		_("Yes, yes dear, I see him.  Please calm yourself.  $name, I am relieved to see you.  This situation has clearly gone beyond any civil control."),\
		_("That is certain, my lady.  I am told you are suspected of theft."),\
		_("Theft indeed, and theft most grave. This Fingolson may be uncouth, but he bears considerable influence. A theft from him would have dire consequences indeed. But you know I could not have done this thing."),\
		_("Of course.  Theft is not in you, my Lady, nor is deceit.  But these folk have not my confidence in you.  I fear that there is no one who will speak for your honour among them."),\
		_("I see.  Then it falls to you, $name, as my sole friend in this outpost, to make certain my name is clear of any stain.  May I trust you to do this for me?"),\
		_("Of course, my Lady.  You may trust me to the end of the world.  What little I may do is yours to command."),\
		_("What do you know of Fingolson, Lady?  I have not met him before."),\
		_("Be glad of that, he is an uncouth lout at best. I should have known better than to deal fairly with such a rough and uncultured beast."),\
		_("I thank you for that.  Now you must go, lest they find you here and imprison you as well.  Free, you are my hope."),\
		_("I will try to be worthy of your trust, Lady.  I will return once I know more."),\
		_("Of course, Lady. I have believed nothing but your innocence since I arrived. You may trust me to act on your behalf."),\
		_("I understand, Lady.  Please be patient."),\
		_("I have little choice.  Do you have news?  Or questions?"),\
		_("News?  I must disappoint you, Lady.  I have none.  I simply wished to know if there was anything you need."),\
		_("You must go.  The human at the door may not hear as well as you or I, but he hears well enough.  Leave before he discovers you."),\
		_("I am curious, Lady.  What of that figurine there?  I do not recall it."),\
		_("The Yeti?  I bought that upon arriving here.  From a young lady of your breed, it was."),\
		_("The artist, then?  I must speak more with her.  I had not known you had been together."),\
		_("She is a very intelligent woman, and regards the Yeti highly.  Do not take her lightly."),\
		_("$name!  Thank the Powers!"),\
		_("I have spoken with the artist, Frostbloom. She mentioned that she had heard some strange sounds in the night, when the theft must have taken place. Did you hear anything?"),\
		_("Lady, could you tell me more about the argument you had with the Dwarf?  It may be helpful."),\
		_("It is kind of you to ask.  Indeed my possessions, other than what you see, have been taken from me.  They are kept in the pantry below."),\
		_("Do you wish me to retrieve them for you, Lady?"),\
		_("No, that would not be wise.  I have an item I need, but to fetch it now would be to invite trouble.  Better we wait."),\
		_("Very well, Lady.  I am yours to command."),\
		_("So I gathered.  I will do my best, Lady."),\
		_("In the night...? Yes.  Yes, I do recall a sound in the night.  How could I have forgotten such a thing?"),\
		_("This may be important to your freedom.  What are you able to tell me of it?"),\
		_("Little, I'm afraid.  I know it was a voice, of that I am certain.  But whose voice I was not able to tell, nor what was said."),\
		_("Then it must have been someone about after the theft.  Perhaps the thief itself.  Do you remember anything else?"),\
		_("Are you certain you cannot recall the voice?  It would be helpful to the extreme if we could match a name to it."),\
		_("She thinks for a moment, her eyes distant."),\
		_("No, I am sorry.  The nature of the voice is a mystery to me still."),\
		_("Very little, I'm afraid.  Only that it seemed to come from a distance.  Past the wall, perhaps.  In the direction of the stables."),\
		_("The lady looks anxiously at the door."),\
		_("Argument?  An insult, it was.  That foul creature had the audacity to accuse me of ignorance!"),\
		_("Ignorance?  But you are highly educated, Lady.  Anyone could see that."),\
		_("Not this beast.  He attempted to sell inferior gems to me, pretending that they were of a high grade.  As if I was nothing more than a child who could not tell one stone from another."),\
		_("You know it is my intent to enchant these stones.  Else why would I trek this far?  Awful stones like his would shatter in an instant."),\
		_("Yes, that's true.  When we set out, you told me of your intent."),\
		_("That rough animal! He went so far as to claim that I not only did not know the value of the stone, but that I hardly knew one gem from another! If I could have destroyed the filth on the spot, I certainly would have!"),\
		_("Silverhair's eyes flash with remembered anger, but a scuffing sound by the door distracts her and her anger drains as suddenly as it rose."),\
		_("My Lady, I am glad to see you.  You will be free soon, I know it."),\
		_("I would ask a boon from you, now that it is safe.  I have personal articles that I need, but are kept with our packs.  I'm sure you know which articles I mean."),\
		_("Of course, Lady.  That would be the least I could do after what you have endured.  Rest assured, I will be back shortly."),\
		_("$name, you have come back so soon?  But where are the articles I asked for?"),\
		_("I have yet to retrieve them, Lady."),\
		_("Then please do so at once.  I have been without them for too long."),\
		_("Very well, Lady."),\
		_("Returned already?  But what is this?"),\
		_("A stone I found in the cellar, among your chests.  I hate to think such a thing, but is this one of the jewels that the Dwarf has lost?"),\
		_("You show the jewel to Lady Silverhair, who frowns upon seeing it.  She inspects it more closely, but carefully avoids touching it.  She straightens then, a puzzled look on her features."),\
		_("You say this was found among my goods?  But this is not a stone of mine, and neither is it the stone I was shown before.  I have never seen this before."),\
		_("But is this not one of the Catseyes he claims to have lost?"),\
		_("It cannot be. For this is no Catseye at all, and in fact is hardly worth a fraction of the other stones."),\
		_("I do not understand this at all."),\
		_("I admit he goaded me to rage earlier, to my shame. But I have done nothing more than voice my anger. You must believe that."),\
		_("And where are the packs kept, Lady?"),\
		_("You will find them below, in the pantry.")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"silverhair_free\") != 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"talked_about_yeti\") == 0 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_frostbloom\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"get_item\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") & 2 == 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_argument\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"have_gem\") == 1\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"talked_about_yeti\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"get_item\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_noise\" , adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") | 1 )\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"gem_worthless\" , adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") | 1)\n\n\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (2, 1, 1), (23, 1, 3), (54, 1, 6), (50, 1, -1), )),\
		("Janesta Skywind", 0, ((3, 0, -1), )),\
		("Imoen Silverhair", -1, ((15, 0, -1), )),\
		(None, -1, ((4, 0, -1), )),\
		("Imoen Silverhair", -1, ((5, 0, -1), )),\
		(None, -1, ((6, 0, -1), )),\
		("Imoen Silverhair", -1, ((10, 0, -1), (7, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		("Imoen Silverhair", -1, ((9, 0, -1), )),\
		(None, -1, ((12, 0, -1), )),\
		(None, -1, ((11, 0, -1), )),\
		("Imoen Silverhair", -1, ((61, 0, -1), )),\
		("Imoen Silverhair", -1, ((13, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((12, 0, -1), )),\
		(None, -1, ((16, 0, -1), )),\
		("Imoen Silverhair", -1, ((17, 0, -1), (19, 0, 2), (24, 0, 4), (25, 0, 5), )),\
		(None, -1, ((26, 0, -1), )),\
		("Imoen Silverhair", -1, ()),\
		(None, 1, ((20, 0, -1), )),\
		("Imoen Silverhair", -1, ((21, 0, -1), )),\
		(None, -1, ((22, 0, -1), )),\
		("Default", -1, ((30, 0, -1), )),\
		("Imoen Silverhair", 2, ((47, 0, -1), )),\
		(None, 3, ((31, 0, -1), )),\
		(None, -1, ((40, 0, -1), )),\
		("Imoen Silverhair", -1, ((27, 0, -1), )),\
		(None, -1, ((28, 0, -1), )),\
		("Default", -1, ((29, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		("Default", -1, ((32, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Default", -1, ((34, 0, -1), (35, 0, -1), )),\
		(None, -1, ((38, 0, -1), )),\
		(None, -1, ((36, 0, -1), )),\
		("Narrator", -1, ((37, 0, -1), )),\
		("Default", -1, ((34, 0, -1), )),\
		("Default", -1, ((39, 0, -1), )),\
		("Narrator", -1, ((18, 0, -1), )),\
		("Imoen Silverhair", -1, ((41, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((43, 0, -1), )),\
		("Default", -1, ((44, 0, -1), )),\
		(None, -1, ((45, 0, -1), )),\
		("Default", -1, ((46, 0, -1), )),\
		("Narrator", -1, ((18, 0, -1), )),\
		(None, -1, ((48, 0, -1), )),\
		("Imoen Silverhair", -1, ((49, 0, -1), (62, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((51, 0, -1), )),\
		(None, -1, ((52, 0, -1), )),\
		("Default", -1, ((53, 0, -1), )),\
		(None, -1, ()),\
		("Default", 4, ((55, 0, -1), )),\
		(None, -1, ((56, 0, -1), )),\
		("Narrator", -1, ((57, 0, -1), )),\
		("Default", -1, ((58, 0, -1), )),\
		(None, -1, ((59, 0, -1), )),\
		("Default", -1, ((60, 0, -1), )),\
		("Default", -1, ()),\
		("Imoen Silverhair", -1, ((14, 0, -1), )),\
		(None, -1, ((63, 0, -1), )),\
		("Imoen Silverhair", -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
