import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class erek_start (dialogue.base):
	text = [None,\
		_("Before you stands a young Dwarf, with an open face and no sign of the traditional beard. His expression shows his intelligence and a trace of humour as he watches you expectantly."),\
		_("You are Erek Stonebreaker, aren't you?"),\
		_("That I am. Erek Stonebreaker, aspirant to the trading business and Master Fingolson's apprentice. But I seem to not remember you, $fm {madam/sir}."),\
		_("I am $name."),\
		_("I am $name, Lady Silverhair's man. I have some questions."),\
		_("Well met then, $name. Only I fear that you would be better advised to talk to Master Fingolson, if you intend to do business."),\
		_("Forgive me, but I couldn't help but hear you telling {get_right_npc} of your connection with that Silverhair woman."),\
		_("Actually, that isn't the case. I would like to speak to you about Lady Silverhair."),\
		_("Oh ... well, she's the reason why I want to talk to you, if you don't mind."),\
		_("I understand. You have learned of the ... incident, but as I can see, you fail to believe it."),\
		_("Lady Silverhair, hm? There seems to be hardly any other topic since that ... incident. I'm sorry, but I don't think I can satisfy your curiosity."),\
		_("See Erek, I know Lady Silverhair well, and I want to find out what really happened here."),\
		_("You don't understand Erek. I am investigating this matter, and therefore you'd better tell me what you know."),\
		_("Of course. The Lady Silverhair is a wealthy noble; she'd never stoop to theft!"),\
		_("Erek stiffens for a moment, and it seems that he is about to turn you away, but finally he relaxes."),\
		_("You believe Lady Silverhair is innocent then?"),\
		_("Well, what do you believe, Erek?"),\
		_("Master Fingolson says her guilt is proven beyond doubt, and there are indeed facts that support his opinion. But I ... am not sure."),\
		_("She said as much herself.  But that alone is not enough to prove her innocence when you consider what stands against her."),\
		_("I know of nothing that could possibly support such claims. I really would know what has happened!"),\
		_("You suspect somebody else?"),\
		_("This unpleasant fellow must have eavesdropped on us. Not that he had to. A good deal of the conversation must have been audible in the common room as well."),\
		_("Hold on Erek! There was an argument between Fingolson and my mistress?"),\
		_("Very well then. It was yesterday, in the evening, when Lady Silverhair met my Master and me in the parlour next to the common room."),\
		_("Why, Master Fingolson, this is outrageous.  'Tis twice as much as I would spend for stones of a superior quality. Do you believe I have never traded for Chrysoberyls before?"),\
		_("My Lady, these Catseyes are very rare. I doubt that you could aquire anything of that quality for the price I'm willing to grant you."),\
		_("Now Master Fingolson, you call these Catseyes? They are mere Cymophanes. Good gods! I am no Dwarf, but I do know my gems. My offer is 200, for all the good they will be to me as reagents."),\
		_("You call me a liar? As if I couldn't tell a Catseye and a Cymophane apart. Even young Erek here can. 700 and no less. Take it or leave it."),\
		_("Ha! A liar and a thief you are indeed, Master Fingolson. But, I need the stones far more than justice against a Dwarven cheat. 300 is my final offer, and that is more than this rubbish deserves!"),\
		_("Do not try to charm me, Mistress Silverhair. My prize is set. Think about it."),\
		_("You are but making profit off my need. I will think about it, but to be frank, you deserve not a single gold piece!"),\
		_("And with that, she left us alone."),\
		_("Indeed. She intended to buy some rare gems, but it seemed she had underestimated their value. She was quite surprised by my Master's offer:"),\
		_("Wait a moment! What exactly is a \"Catseye\"?"),\
		_("Tell me Erek. Were those gems truly Catseyes?"),\
		_("Well ... yes ... when looked at in a certain way, under the right light. No wonder your mistress mistook them for Cymophanes."),\
		_("Sometimes, a thin narrow band runs across the length of a gem, glowing in the light, see? That gives them the appearance of a cat's eye, hence the name."),\
		_("I see. And Fingolson's stones were truly of such nature?"),\
		_("You refer to the argument she had with your master?"),\
		_("Why yes! She said herself that the master deserves no payment. And the next day, his gems are gone. Who wouldn't deem her guilty after that?"),\
		_("I think Lady Silverhair might have had a reason to utter such words. Perhaps you could recount the conversation she had with your master?"),\
		_("Sure. The three of us sat together in the parlour next to the common room. There wasn't much talk while Lady Silverhair examined the gems. The argument started when she asked for the price, which obviously wasn't to her liking:"),\
		_("I've been told that Fingolson and my mistress had quite an argument."),\
		_("Can I have a word with you, uh... what was the name?"),\
		_("I am Erek Stonebreaker, aspirant to the trading business, at your service $fm{madam/sir}."),\
		_("Erek gives you a welcoming nod as you approach."),\
		_("Ho there, $name. What is it this time?"),\
		_("Could you please repeat what you told me about the argument between your master and Lady Silverhair?"),\
		_("Master Orloth told me of an impolite remark Fingolson made towards Lady Silverhair on her arrival."),\
		_("Erek makes a face as he sees you and raises his finger accusingly."),\
		_("Why haven't you told me that you work for Lady Silverhair!?"),\
		_("Why should I? You figured it out by yourself just the same."),\
		_("I did not know that this was of any importance to you, Erek."),\
		_("But only by chance: I heard you talking to {get_right_npc}! It's simply not right, $name! You are familiar with the prime suspect, but you make me believe that your inquiry is for the best of us all."),\
		_("You ..., you ... didn't know!? It's the truth! Of course it is important to me! You are familiar with the prime suspect, but you deem it unnecessary to tell me!"),\
		_("And you are familiar with the victim. Had I told you, you might have refused your help."),\
		_("Look Erek, I'm sorry that I said nothing about being Lady Silverhair's man. But believe me, I just want to find out the truth, nothing else."),\
		_("The truth! How do you expect to uncover the truth, if you don't carry it within yourself!? Every evil begins with a lie, and as long as you conceal the truth, you are no better than the thief."),\
		_("You should know that to a Dwarf, the truth is a virtue; it is practically carved into his bones. The day a lie parts the lips of a Dwarf is the day the world comes to its end!"),\
		_("I don't understand much of dwarvish philosophy, but if the truth is so important to you, Erek, then I am sorry."),\
		_("I hope you don't think poorly of me now, $name. I didn't mean to insult you. But to say nothing about it would have meant to hide the truth. And by now you should know how I think about that."),\
		_("But no more of this. I don't want to keep you from more important business."),\
		_("That are the thoughts of people living in a world of lies and deceptions. I would have helped you more readily, had you told me the truth right from the beginning."),\
		_("I don't know in what world you are living, Erek, but I doubt that it is the real one."),\
		_("Ha! The Master is right, then. Elves and their likes are no company for an upright Dwarf! All you care for is worthless knowledge and useless trinkets."),\
		_("Is that what Fingolson says?"),\
		_("That are his very words. First I thought he was too extreme in his judgement, but the more I get to see of the world, the more I can see the truth behind his words."),\
		_("Although my feelings tell me that you do not fit into this scheme, $name. Perhaps I spoke too fast."),\
		_("Perhaps you just shouldn't listen to everything Master Fingolson says. How did he become a tradesman anyway, if he despises the people he has to deal with that much?"),\
		_("Usually, the Elders decide what occupation a young Dwarf will practise. They'll take his talents and also their needs into account, but seldom what the individual likes."),\
		_("Master Fingolson is a skilled merchant, but it is easy to see that this is not what he wanted to be."),\
		_("Nothing really. Until later, Erek."),\
		_("I ..., I'm sorry, but that is news to me. It must have happened while I was unpacking our luggage. Although to tell the truth, it does not sound like Master Fingolson at all."),\
		_("He can be tough when it gets down to business, but why would he want to insult Lady Silverhair before? This makes no sense to me."),\
		_("I really cannot say why he would do that, but perhaps I can help you with something else instead?"),\
		_("That was all for now, Erek. Until later."),\
		_("I see. Thank you Erek, you've been most helpful."),\
		_("Is that your opinion, or that of Master Fingolson?"),\
		_("What do you mean? You are not suggesting that my Master tried to deceive Lady Silverhair?"),\
		_("That's not important now. But if the gems were of poor quality, they'd be worthless to her and she'd have no reason to steal them."),\
		_("I am sorry, but I haven't seen them up close, so I have to rely on my Master's word. I would know the difference if I had them in my hand, but that's unlikely."),\
		_("I tried to talk with Master Fingolson, but he would not open the door. Could you have a word with him perhaps?"),\
		_("I fear this is no good idea. He is still very upset about the theft and it is better not to bother him while he is in that mood."),\
		_("I'm sorry, $name. Master Fingolson is not very sociable at best, but right now he wants nobody to disturb him in his misery."),\
		_("Well, in that I case I will leave him alone."),\
		_("I am trying to find his gems and he is not even willing to see me!?"),\
		_("Stubborn Dwarf! But if he is in no hurry to get his gems back, what can I do about it?"),\
		_("I am trying to help here, Erek!"),\
		_("I ... I'll see what I can do. But should you talk with him, you will have to watch your words. I surely won't be able to change his mind a second time."),\
		_("Seemingly reluctant, Erek beckons you to follow him down into the cellar."),\
		_("You surely do. But Master Fingolson made it clear that he wants to be on his own and who am I to disobey his wishes?"),\
		_("Did you pack Master Fingolson's gems that evening, Erek?"),\
		_("Me? What a curious idea! My master wouldn't give them out of his hands. I only packed our clothes and other equipment; after the master went to bed."),\
		_("And the gems were not in your luggage when you packed, right?"),\
		_("What do you mean? No ... they weren't. Of course not!"),\
		_("Thank you Erek."),\
		_("Between you and me $fm{madam/sir}, this mercenary, Alek, was creeping outside the parlour during negotiations. Lady Silverhair nearly bumped into him when she rushed out."),\
		_("Unlikely perhaps, but not impossible. What do you make of this one, Erek?"),\
		_("That ... - it's one of the Master's. It must be. Where did you get that, $name?"),\
		_("I found it in the pantry."),\
		_("It was hidden in Lady Silverhair's luggage."),\
		_("Then your mistress is not as innocent as you thought, no? Let me see the gem, please."),\
		_("Carefully, Erek takes the gem and examines it closely for a while. Suddenly, he tosses it high into the air, a sparkling green star, gleaming in the light of the fire."),\
		_("Once caught again, the young Dwarf shakes his head and starts to smile. Finally, he returns the gem."),\
		_("This is a fine example of a Chrysoberyl. Perfectly suitable for a Lady's ring, were that your Mistress' intention. However, it is no Catseye and as such it is of no use in the workings of magic she had in mind, if I recall correctly."),\
		_("Could you repeat that for Jelom? He would not believe me."),\
		_("Thank you Erek. That's all I need to know."),\
		_("But certainly it was not lying openly on the ground, was it?"),\
		_("No. It was hidden in Lady Silverhair's luggage."),\
		_("Obviously not. Now would you like to see it?"),\
		_("You don't trust me, $name? In that case I'm sorry. Unless I do not know the truth about the gem, I cannot help you."),\
		_("Erek, I'd like to hear your opinion about the gem I have here."),\
		_("Erek tries to keep a straight face, but he fails to hide his grin as you address him."),\
		_("Well, $name, I was almost certain that it wouldn't take long to change your mind. I'm ready for the truth."),\
		_("Judging by your behaviour I thought as much. But don't worry, $name. I also know that the obvious is not necessarily the truth. Now show me that gem."),\
		_("So it be. The gem was hidden in Lady Silverhair's luggage."),\
		_("Jelom will not believe that the gem I have would be worthless to my mistress. But perhaps you could convince him."),\
		_("Of course, $name. Let's go and see him."),\
		_("She intended to buy some rare gems, but it seemed she had underestimated their value. She was quite surprised by my Master's offer:"),\
		_("If you think so. Let's go and see him, then."),\
		_("And those illusions you call magic; they are perversions of anything lawful and good!")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_erek\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"work_4_shair\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_argument\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_argument\") != 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_bjarns_insult\") == 1\n",\
		"self.the_npc.get_val (\"work_4_shair\") == 0 and adonthell.gamedata_get_quest(\"demo\").get_val (\"work_4_shair\") > 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"bjarn_door_open\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"ask_packed_gems\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"have_gem\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"convince_jelom\") == 1\n",\
		"self.the_npc.get_val (\"apologise\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"convince_jelom\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") >= 2\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\", 1)\n",\
		"self.the_npc.set_val (\"insulted\", 1)\n",\
		"self.the_npc.set_val (\"work_4_shair\", 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_alek_eavesdrop\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_low_quality\" , 1)\nadonthell.gamedata_get_quest(\"demo\").set_val (\"know_argument\" , 1)\n",\
		"self.the_npc.set_val (\"work_4_shair\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"bjarn_door_open\" , 2)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"ask_packed_gems\" , 2)\n",\
		"if adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") < 2:\n    adonthell.gamedata_get_quest(\"demo\").set_val (\"gem_worthless\" , adonthell.gamedata_get_quest(\"demo\").get_val (\"gem_worthless\") + 2)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"convince_jelom\" , 2)\n",\
		"self.the_npc.set_val (\"apologise\" , 1)\n",\
		"self.the_npc.set_val (\"apologise\" , 0)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (50, 1, 6), (113, 1, 11), (46, 1, -1), )),\
		("Narrator", 0, ((2, 0, 1), (44, 1, -1), )),\
		(None, -1, ((3, 0, -1), )),\
		("Default", -1, ((4, 0, -1), (5, 0, -1), )),\
		(None, -1, ((6, 0, 2), (7, 1, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", -1, ((8, 0, -1), )),\
		("Default", 1, ((9, 0, -1), )),\
		(None, -1, ((11, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", -1, ((14, 0, -1), (17, 0, -1), )),\
		("Default", -1, ((13, 0, -1), (12, 0, -1), )),\
		(None, -1, ((16, 0, -1), )),\
		(None, 1, ((15, 0, -1), )),\
		(None, -1, ((19, 0, -1), )),\
		("Narrator", -1, ((24, 0, -1), )),\
		("Default", -1, ((14, 0, -1), (17, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		("Default", 2, ((39, 0, 4), (20, 0, -1), (21, 0, -1), )),\
		("Default", 2, ((39, 0, 4), (20, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		(None, -1, ((97, 0, -1), )),\
		("Default", 3, ((23, 0, 3), (43, 1, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		("Default", -1, ((119, 0, -1), )),\
		("Imoen Silverhair", -1, ((26, 0, -1), )),\
		("Bjarn Fingolson", -1, ((27, 0, -1), )),\
		("Imoen Silverhair", 4, ((28, 0, -1), )),\
		("Bjarn Fingolson", -1, ((29, 0, -1), )),\
		("Imoen Silverhair", -1, ((30, 0, -1), )),\
		("Bjarn Fingolson", -1, ((31, 0, -1), )),\
		("Imoen Silverhair", -1, ((32, 0, -1), )),\
		("Default", -1, ((34, 0, -1), (77, 0, -1), (35, 0, -1), )),\
		("Default", -1, ((25, 0, -1), )),\
		(None, -1, ((37, 0, -1), )),\
		(None, -1, ((36, 0, -1), )),\
		("Default", -1, ((77, 0, -1), (78, 0, -1), )),\
		("Default", -1, ((38, 0, -1), (77, 0, -1), )),\
		(None, -1, ((36, 0, -1), )),\
		(None, -1, ((40, 0, -1), )),\
		("Default", -1, ((41, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((25, 0, -1), )),\
		(None, -1, ((33, 0, -1), )),\
		(None, -1, ((45, 0, -1), )),\
		("Default", -1, ((4, 0, -1), (5, 0, -1), )),\
		("Narrator", -1, ((47, 0, -1), )),\
		("Default", -1, ((72, 0, -1), (117, 0, 12), (49, 0, 5), (92, 0, 8), (82, 0, 7), (48, 0, -1), (112, 0, 9), )),\
		(None, -1, ((42, 0, -1), )),\
		(None, -1, ((73, 0, -1), )),\
		("Narrator", 5, ((51, 0, -1), )),\
		("Default", -1, ((52, 0, -1), (53, 0, -1), )),\
		(None, -1, ((54, 0, -1), )),\
		(None, -1, ((55, 0, -1), )),\
		("Default", -1, ((56, 0, -1), )),\
		("Default", -1, ((56, 0, -1), (57, 0, -1), )),\
		(None, -1, ((63, 0, -1), )),\
		(None, -1, ((58, 0, -1), )),\
		("Default", -1, ((59, 0, -1), )),\
		("Default", -1, ((64, 0, -1), (60, 0, -1), )),\
		(None, -1, ((61, 0, -1), )),\
		("Default", -1, ((62, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ((59, 0, -1), )),\
		(None, -1, ((65, 0, -1), )),\
		("Default", -1, ((121, 0, -1), )),\
		(None, -1, ((67, 0, -1), )),\
		("Default", -1, ((68, 0, -1), )),\
		("Default", -1, ((69, 0, -1), )),\
		(None, -1, ((70, 0, -1), )),\
		("Default", -1, ((71, 0, -1), )),\
		("Default", -1, ((62, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((74, 0, -1), )),\
		("Default", -1, ((75, 0, -1), )),\
		("Default", -1, ((82, 0, 7), (48, 0, -1), (76, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ()),\
		(None, -1, ((79, 0, -1), )),\
		("Default", -1, ((80, 0, -1), )),\
		(None, -1, ((81, 0, -1), )),\
		("Default", -1, ((98, 0, 9), (77, 0, -1), )),\
		(None, -1, ((83, 0, -1), )),\
		("Default", -1, ((86, 0, -1), (85, 0, -1), )),\
		("Default", -1, ((88, 0, -1), (87, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((84, 0, -1), )),\
		(None, -1, ((89, 0, -1), )),\
		(None, -1, ((91, 0, -1), )),\
		("Default", -1, ((90, 0, -1), )),\
		("Narrator", 6, ()),\
		("Default", -1, ((85, 0, -1), (87, 0, -1), )),\
		(None, -1, ((93, 0, -1), )),\
		("Default", -1, ((94, 0, -1), )),\
		(None, -1, ((95, 0, -1), )),\
		("Default", 7, ((96, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((22, 0, -1), )),\
		(None, -1, ((99, 0, -1), )),\
		("Default", -1, ((100, 0, -1), (101, 0, -1), )),\
		(None, -1, ((108, 0, -1), )),\
		(None, -1, ((102, 0, -1), )),\
		("Default", -1, ((103, 0, -1), )),\
		("Narrator", -1, ((104, 0, -1), )),\
		("Narrator", -1, ((105, 0, -1), )),\
		("Default", 8, ((107, 0, -1), (106, 0, 10), )),\
		(None, 9, ((118, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((110, 0, -1), (109, 0, -1), )),\
		(None, -1, ((102, 0, -1), )),\
		(None, -1, ((111, 0, -1), )),\
		("Default", 10, ()),\
		(None, -1, ((99, 0, -1), )),\
		("Narrator", 11, ((114, 0, -1), )),\
		("Default", -1, ((116, 0, -1), )),\
		("Default", -1, ((103, 0, -1), )),\
		(None, -1, ((115, 0, -1), )),\
		(None, -1, ((120, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ((25, 0, -1), )),\
		("Default", 9, ()),\
		("Default", -1, ((66, 0, -1), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n

	def __del__(self):
		# -- 'teleport' to Bjarn's room
		if adonthell.gamedata_get_quest("demo").get_val ("bjarn_door_open") == 2:
		    bjarn = adonthell.gamedata_get_character ("Bjarn Fingolson")
		    bjarn.do_stuff ("await_player")
		    bjarn.time_callback_string ("1t", "start_talking")
		
		    erek = adonthell.gamedata_get_character ("Erek Stonebreaker")
		    import events
		    erek.set_val ("goto", erek.submap ())
		    events.switch_submap (self.the_player, 7, 1, 6, 3)
		    events.switch_submap (erek, 7, 2, 7, 0)
		
		# -- Teleport to Jelom
		if adonthell.gamedata_get_quest("demo").get_val ("convince_jelom") == 2:
		    jelom = adonthell.gamedata_get_character ("Jelom Rasgar")
		    jelom.jump_to (9, 2, 3, 1)
		    jelom.time_callback_string ("1t", "start_talking")
		
		    erek = adonthell.gamedata_get_character ("Erek Stonebreaker")
		    erek.set_schedule_active (0)
		    import events
		    events.switch_submap (self.the_player, 9, 1, 3, 3)
		    events.switch_submap (erek, 9, 2, 4, 0)


	# Returns whom the Player told about his connection
	# with Lady Silverhair
	def get_right_npc (self):
	    if adonthell.gamedata_get_quest("demo").get_val ("work_4_shair") & 1 == 1:
	        return _("Master Orloth")
	    elif adonthell.gamedata_get_quest("demo").get_val ("work_4_shair") & 2 == 2:
	        return _("the mercenary")
	    else:
	        return _("Tristan the merchant")
	

