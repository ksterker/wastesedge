import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class extro (dialogue.base):
	text = [None,\
		_("What is going on here? What are all these people doing in my room? Are you behind this, Half-Elf? I demand an explanation!"),\
		_("Please calm down Master Fingolson. We are here to sort out this business once and for all."),\
		_("Sort this business out? Good ... good! It's about time, I'd say! So ... will that foul Elf finally return my Catseyes? I hear one was found amongst her belongings. And where there is one, the others shouldn't be far."),\
		_("I fear you are mistaken my good Dwarf. Neither were any Catseyes amongst your merchandise, nor am I in possession of your \"precious\" gems."),\
		_("As if an ignorant like you could tell the difference! I ..."),\
		_("Silence! I have enough of your endless quarrel! I assume that $name here has poked around long enough in this pile of crap to produce the thief. He better had! So Half-Elf, go on, do your duty! End this bloody foolery!"),\
		_("Well, it's a fact that Lady Silverhair cannot be the thief."),\
		_("It's obvious that the thief tried to frame Lady Silverhair."),\
		_("I'm sorry, I have no idea as to who the thief might be."),\
		_("There you have it! I daresay it'll be extremely difficult to find a thief other than the Elf over there. Who if not she would have wanted to steal my Catseyes!?"),\
		_("I wonder whether you really want your gems back, or just the Lady Silverhair convicted!"),\
		_("Catseyes? You call those worthless shards of yours Catseyes!?"),\
		_("You doubt my word and expertise? You're truly your mistress' servant! Erek, be so kind and tell our friend here of the stolen gems' nature."),\
		_("Master?"),\
		_("Do as I say!"),\
		_("Very well. I ... - I am not sure about the other gems, but the stone $name has discovered is undoubtedly a Chrysoberyl. However, a Catseye it is not."),\
		_("I'd say this calls for an explanation, don't you think so Master Fingolson?"),\
		_("Erek, this is not the right time for any of your childish pranks! Master Rasgar, you mustn't believe that ..., that impertinent youth!"),\
		_("Deceit! What is deceit compared to the unsound creations our precious stones are turned into, I ask? Foul workings of magic that contradict anything lawful and good! I wonder who's side you're on, Erek?"),\
		_("But you said I was nearly ready for the Rite of Passage, Master! Please return to reason; stop twisting the truth. Have you not taught me that deceit is wrong? Yet you are spreading lies!"),\
		_("Then you took advantage of the theft to discredit my mistress, because you despise the arcane arts?"),\
		_("If your gems are no Catseyes, you have to see that it is unlikely for my mistress to steal them."),\
		_("Foolish Half-Elf! Don't you think I'd know best how unlikely it is for anyone, including your fine mistress, to steal these gems? Were it not for Erek, that betrayer, you'd never know!"),\
		_("So what? I'd gladly go without the stones if only the thief was put to her just punishment. Is this so wrong?"),\
		_("But my mistress has been wrongly accused!"),\
		_("You are obsessed by your aversion to Lady Silverhair!"),\
		_("You understand nothing, Half-Elf! I couldn't care less for your mistress, may she rot in the dungeon! But I do care for the fruits of my peoples work, for the jewels and ores brought forth from the bones of the earth."),\
		_("They are spoilt by the likes of her. Turned into useless trinkets and poisoned with foul enchantments! The thought alone sickens me."),\
		_("If you think like that, why do you sell anything to the Elves at all?"),\
		_("Are you making fun of me? Do you believe I asked for this? I've been chosen for this trade, whether I like it or not. But even the lowest Dwarf has more discipline than you lot together, so I fulfilled my duty without complaint."),\
		_("Until you couldn't bear it any more, am I right?"),\
		_("I doubt that selling mere Chrysoberylls as Catseyes falls under your duty!"),\
		_("What would a Half-Elf know of these matters? You couldn't tell one gem from the other! Erek, you have seen the stones; tell our friend whether they are Catseyes or not!"),\
		_("You call tinkering with the supernatural an art!? It is an insult to any upright Dwarf. But what could I do against it? My people have no use for ornaments or luxuries, but we cannot live of rocks alone. We need to trade."),\
		_("So I couldn't simply refuse selling to those filthy Elves. But if one of their nobles turns out to be a thief, who knows what the elders would decide."),\
		_("You mean the thief expected to escape unnoticed while your mistress would have been held responsible?"),\
		_("That I would imagine."),\
		_("No. I mean the theft's sole purpose was to discredit my mistress."),\
		_("That's a grave accusation, $name! Who would do such a thing, and why, I wonder?"),\
		_("This is ridiculous! My business with the Elf was only known to the both of us. Besides, who amongst the attendees holds any grudge against her?"),\
		_("You do! And you knew of her business."),\
		_("That ... I ... - Master Rasgar, you are not going to believe in this ..., this infamy, are you? Since my arrival at this depraved place I am being continously insulted!"),\
		_("First Silverhair disparages the quality of my stones, only to steal them later on. And as if that wouldn't be enough, that servant of her now tries to pin the crime on me!"),\
		_("Master Fingolson, were it not you who set my Mistress at edge right after her arrival?"),\
		_("But your stones are of poor quality indeed!"),\
		_("You doubt my word and expertise, Half-Elf? Perhaps you have more faith in my apprentice then. Erek, please tell those ignorants how valuable these Catseyes are."),\
		_("Then you confess that the theft was just pretended?"),\
		_("What do you mean?"),\
		_("You feigned the theft, as an act of revenge."),\
		_("Why? It's a fact that she was in need of my gems. And she said herself that I deserved no payment for them. Even without that Catseye appearing in her luggage, this should be proof enough!"),\
		_("But this gem is no Catseye, and therefore worthless to her."),\
		_("You think I did that deliberately?"),\
		_("Yes. And afterwards you offered her worthless gems to enrage her even more!"),\
		_("Rubbish I say! There can be no doubt that the Elf is responsible!"),\
		_("Why do you keep insisting on my mistress' guilt?"),\
		_("Really? Now that is news to me. If you don't mind I would like to know your reasoning, Half-Elf!"),\
		_("Whoever planted that gem in the mistress' chest, it was not her."),\
		_("What makes you so sure about that? And why would a thief other than Lady Silverhair hide something in her luggage?"),\
		_("The gems the Lady is accused of stealing are worthless to her."),\
		_("To conceal his trail, and to direct all suspicion towards Lady Silverhair, of course."),\
		_("What do you mean? Why would my gems be suddenly worthless to her?"),\
		_("My mistress intended to buy Catseyes, but as it turned out, your gems are none."),\
		_("I don't believe this! Lady Silverhair intended to buy my gems, and when she didn't find my conditions to her liking, she simply stole them! There is no other thief!"),\
		_("Lady Silverhair intended to buy Catseyes, not these worthless shards you tried to sell her!")]

	cond = [\
		"self.guess_deceit == 0\n",\
		"self.not_guilty != 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_bjarns_insult\") == 1\n",\
		"self.guess_deceit == 1\n"]

	code = [\
		"self.guess_deceit = 1\n",\
		"self.guess_deceit = 1\n\n",\
		"self.not_guilty = 1\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, -1), )),\
		("Bjarn Fingolson", -1, ((2, 0, -1), )),\
		("Jelom Rasgar", -1, ((3, 0, -1), )),\
		("Bjarn Fingolson", -1, ((4, 0, -1), )),\
		("Imoen Silverhair", -1, ((5, 0, -1), )),\
		("Bjarn Fingolson", -1, ((6, 0, -1), )),\
		("Jelom Rasgar", -1, ((7, 0, -1), (8, 0, -1), (9, 0, -1), )),\
		(None, -1, ((56, 0, -1), )),\
		(None, -1, ((36, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Bjarn Fingolson", -1, ((11, 0, -1), (12, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		("Bjarn Fingolson", -1, ((14, 0, -1), )),\
		("Erek Stonebreaker", -1, ((15, 0, -1), )),\
		("Bjarn Fingolson", -1, ((16, 0, -1), )),\
		("Erek Stonebreaker", -1, ((17, 0, -1), )),\
		("Jelom Rasgar", -1, ((18, 0, -1), )),\
		("Bjarn Fingolson", -1, ((20, 0, -1), )),\
		("Bjarn Fingolson", -1, ((21, 0, 0), (47, 0, 3), (22, 0, -1), )),\
		("Erek Stonebreaker", -1, ((19, 0, -1), )),\
		(None, 0, ((34, 0, -1), )),\
		(None, 1, ((23, 0, -1), )),\
		("Bjarn Fingolson", -1, ((47, 0, 3), )),\
		("Bjarn Fingolson", -1, ((25, 0, 1), (26, 0, -1), )),\
		(None, -1, ((50, 0, -1), )),\
		(None, -1, ((27, 0, -1), )),\
		("Bjarn Fingolson", -1, ((28, 0, -1), )),\
		("Bjarn Fingolson", -1, ((29, 0, -1), (21, 0, 0), )),\
		(None, -1, ((30, 0, -1), )),\
		("Bjarn Fingolson", -1, ((31, 0, -1), (32, 0, -1), )),\
		(None, -1, ((48, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Bjarn Fingolson", -1, ((14, 0, -1), )),\
		("Bjarn Fingolson", -1, ((35, 0, -1), )),\
		("Bjarn Fingolson", -1, ((47, 0, 3), )),\
		("Jelom Rasgar", -1, ((38, 0, -1), (37, 0, -1), )),\
		(None, -1, ((54, 0, -1), )),\
		(None, -1, ((39, 0, -1), )),\
		("Jelom Rasgar", -1, ((40, 0, -1), )),\
		("Bjarn Fingolson", -1, ((41, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Bjarn Fingolson", 0, ((43, 0, -1), )),\
		("Bjarn Fingolson", -1, ((44, 0, 2), (45, 0, -1), )),\
		(None, -1, ((52, 0, -1), )),\
		(None, -1, ((46, 0, -1), )),\
		("Bjarn Fingolson", -1, ((14, 0, -1), )),\
		(None, -1, ()),\
		("Bjarn Fingolson", -1, ((49, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Bjarn Fingolson", -1, ((51, 0, -1), (26, 0, -1), (12, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Bjarn Fingolson", -1, ((53, 0, -1), )),\
		(None, -1, ((46, 0, -1), )),\
		("Bjarn Fingolson", -1, ((55, 0, -1), (11, 0, -1), )),\
		(None, -1, ((50, 0, -1), )),\
		("Bjarn Fingolson", -1, ((59, 0, -1), (57, 0, -1), )),\
		(None, -1, ((58, 0, -1), )),\
		("Jelom Rasgar", -1, ((60, 0, -1), )),\
		(None, -1, ((61, 0, -1), )),\
		(None, -1, ((63, 0, -1), )),\
		("Bjarn Fingolson", -1, ((62, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Bjarn Fingolson", 2, ((64, 0, -1), (11, 0, -1), )),\
		(None, -1, ((33, 0, -1), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n

	def __del__(self):
		self.the_player.set_schedule ("extro")

