import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class lucia_start (dialogue.base):
	text = [None,\
		_("There is little doubt that this busy-looking woman is the unchallenged mistress of the Redwyne household. As she spots you, a look of resignation flashes across her face."),\
		_("You young people never learn to keep out of my kitchen, do you?"),\
		_("Sorry madam, I did not mean to trespass, but I need to talk to you."),\
		_("I have no time for this, woman! I have some questions for you."),\
		_("What questions? Don't you see I'm busy? Who's going to put the food on the table, if I'm going to chat with you? Now out of my sight with you!"),\
		_("My apologies. Must have been the wrong door ..."),\
		_("Calm down, please. This is important. I'm investigating the theft."),\
		_("It's always the same. I can never do my work without interruptions. But you won't hear me complaining. So what is it you want?"),\
		_("I am $name, Lady Silverhair's clerk. I'm investigating the theft."),\
		_("The Elven Lady you say? Then you must be from Cirdanth, ain't you?"),\
		_("Yes I am from Cirdanth."),\
		_("Listen madam ..."),\
		_("Ah, the city. What would I give to live there! But no, Orloth had to buy the Inn from his scoundrel brother. The deal of his life he said!"),\
		_("Do you? Oh what an awful thing to happen! But I'm not surprised. Out here, in the middle of nowhere, something like this was bound to happen one day."),\
		_("I told Orloth. \"If you're going to buy this inn, you'll end up with trouble\", I said. But would he listen to me?"),\
		_("Sorry to interrupt, but did you notice anything odd during the night of the theft?"),\
		_("Something unusual? How should I? We're sleeping under the roof, whereas poor Master Fingolson has his room downstairs, in the cellar. Just as his kind likes it the most."),\
		_("He is such a regular and welcome guest, and of all people he gets robbed in our house. What a shame!"),\
		_("So you know Fingolson?"),\
		_("The Dwarf, madam! Do you know him?"),\
		_("In Cirdanth that wouldn't have happened. And even if it had, there would be proper guards to track the thief down. But whom do I tell? Surely, you are from Cirdanth, ain't you?"),\
		_("What about the guards here?"),\
		_("He stays here quite often, and has done that for many years. I wouldn't say that I know him well, though. He behaves quite retained and formal, but he is a pleasant character. Not like the other types we get here usually."),\
		_("Oh, you mean Jelom and Talan. They are good men, no doubt. Their task is to keep the peace, and usually they are well up to it."),\
		_("My name is $name. I am investigating the theft."),\
		_("You should have said so! It is about time that something is going to happen. I tell you, in Cirdanth, everything would have been solved by now."),\
		_("But here, in the middle of nowhere, they hold an Elven Lady responsible and nobody seems interested in finding poor Master Fingolson's gems."),\
		_("I am Lady Silverhair's clerk, madam, and I'm going to find the real thief, if you'd only let me ask you some questions!"),\
		_("Then you are from Cirdanth? What would I give to live there! But no! Orloth had to buy the Inn from his scoundrel brother. As if it'd bring him anything but trouble."),\
		_("True, Waste's Edge is quite a remote place, but ..."),\
		_("Could we perhaps return to more pressing matters?"),\
		_("Just take a look at that mercenary. What a dreadful man! You wouldn't find people like him in the city!"),\
		_("What about the guards you have here?"),\
		_("Oh forgive me. Orloth always says I'm talking too much, but actually, he never keeps his mouth shut. He always denies when I tell him, but I'm sure you have noticed yourself."),\
		_("Now don't keep me off my work. Ask what you want to know and then out with you!"),\
		_("Yes, madam. Did you notice anything unusual during the night of the theft?"),\
		_("Remote!? The edge of the world couldn't be more remote! Mind you, I'm not complaining. It's just..."),\
		_("All these filthy types we get here. Like that Endhelm fellow. I don't think you'd meet people like him in Cirdanth."),\
		_("What about him? Do you think he is involved into the theft?"),\
		_("Oh, forgive me. I am sure you have more important things on your mind than listening to the sorrows of a woman."),\
		_("But perhaps you should ask Talan, as he was on duty that night. If somebody noticed something, then it was him."),\
		_("You said Master Fingolson is a regular guest. What can you tell me about him?"),\
		_("I was wondering whether you noticed anything unusual during the night of the theft."),\
		_("How should I know? But he does look suspicious to me. More than any others of our guests."),\
		_("Can you tell me a little more about them?"),\
		_("Well, you were very ... helpful, madam. But if you'll excuse me now, I've got a thief to catch."),\
		_("I am afraid there is only little I know about him. He is so retained and formal, a calm and pleasant character. But he stays here regularly."),\
		_("Which is no surprise; much of the trade with the mines of Uzdun'kal is done here, and Master Fingolson is one of the few tradesmen the Dwarfs have."),\
		_("I didn't know that much trade with the Dwarfs runs through Waste's Edge."),\
		_("Lunch can wait, but if you don't help with my investigation, the thief might get away!"),\
		_("You are looking for the thief!? My apologies then, sir. It is about time that somebody takes an interest into this unlucky incident."),\
		_("Can you imagine they suspect the fair Lady Silverhair!? And bad types like that dreadful Endhelm are walking around unnoticed."),\
		_("I say, in a city like Cirdanth the true thief would have been tracked down by now. But out here, in the middle of nowhere, law and order are just hollow phrases."),\
		_("Rest assured that I will find out the truth, madam. But to do so I need to know whether you noticed anything unusual during the night of the theft."),\
		_("I fear I haven't. See, our rooms are under the roof, while Master Fingolson sleeps below ground, like his kind is used to. Any noise hearable in our chamber would have woken up the whole house."),\
		_("But as far as I know, none of our guests noticed anything suspicious. It is really a shame, theft beneath our roof. And of all people, the good Master Fingolson is the victim."),\
		_("So you know the Dwarf well?"),\
		_("I hardly get out of the kitchen during the day. Best you talk to my husband. He usually knows more about people than they know themselves."),\
		_("But a situation like this exceeds their abilities. Not that I'd blame them. Convicting this thief is no job for simple people. I hope you understand, sir."),\
		_("We're days from the next settlement out here. Were it not for all the trade passing through we couldn't even buy the most basic things we need for our living."),\
		_("Although without the trade, Waste's Edge wouldn't even exist and we might run an Inn in Cirdanth instead. But as long as the mines of Uzdun'kal are there, there is little chance to get Orloth away from here."),\
		_("Well, upwards from here the river gets treacherous, therefore most boats go no further. The way remaining is covered by caravans. So everything that comes along the river runs past our gates."),\
		_("There is also an ancient road that leads north towards Elgilad and the human cities. A lot of spice comes along that way, from Elminscourt and beyond."),\
		_("But enough chatting. This food won't prepare itself, and you still have a thief to catch."),\
		_("Just don't blame him, if he hasn't, sir. He is a good lad and I don't want any harm coming to him."),\
		_("Don't worry, madam. I won't trouble the guards more than they deserve."),\
		_("I'll take you at your word, $name sir. But if you'll excuse me now. I have to prepare the food, and you still have your thief to catch."),\
		_("What about your son? Oliver said he heard something that night."),\
		_("That boy! If I ever catch him outside when he should be sleeping in his bedroom ... . And if that's not enough, he starts spreading rumours."),\
		_("You don't believe him?"),\
		_("Don't get me wrong. Oliver tells no lies. He'd better not! But he has an overactive imagination, so I would be careful with his \"observations\". Trust me, sir."),\
		_("Talan practising what?"),\
		_("I shouldn't have mentioned this at all! Telling on other people is not right. But if it helps to clear your mistress' guilt, I cannot keep it secret. But you mustn't tell anybody, do you understand!?"),\
		_("You have my word, Lucia. Now what is it?"),\
		_("He is singing. Talan sometimes leaves his post to practice his voice where nobody hears him. That's nothing bad, but he'd be more than embarrassed if you tell it around. And I fear Jelom won't take it very well."),\
		_("And he'd be right! Singing might not be bad, but leaving ones post during duty is! I think I'll have to have a serious word with Talan. If you'll excuse me, madam."),\
		_("I ... I cannot tell. I have said more than I should have already."),\
		_("I can't promise anything before I don't know what you are talking about."),\
		_("I want no harm done to Talan, see. He is a good lad, and he deserves better than ending like Jelom. Don't destroy the chance to make something out of his life."),\
		_("I don't want anybody harm, but I will do what I must to find the thief."),\
		_("Please Lucia. If it has anything to do with the theft, I need to know! Don't you want the real thief caught?"),\
		_("And that is the only reason why I'll tell you about Talan. But you'd better not disappoint me!"),\
		_("What if it wasn't!? If that guard would do his duty instead of wandering off for a singsong at nights, we'd know for sure."),\
		_("Please sir, don't be too harsh with Talan. He is a good lad at heart, and I wouldn't like any harm coming to him."),\
		_("I know that {who_heard_noise} heard a noise outside the inn during that night."),\
		_("Outside the inn you say? I don't know anything about this, but I suspect that was rather Talan practising than the thief."),\
		_("Lucia seems busy as usual, but this time she actually smiles as she turns to you."),\
		_("Come back to hold me off my work again, did you?"),\
		_("I'm afraid so. I'd like you to repeat what you've heard the night of the theft."),\
		_("I already told you everything I know, but if you insist."),\
		_("As I said, we're sleeping under the roof, whereas poor Master Fingolson has his room down below ground. So if he hasn't heard anything, how should i?"),\
		_("Lucia does not even bother to look up from her work as you approach her."),\
		_("Excuse me Lucia, I have ..."),\
		_("Don't even think of asking me for anything. The way you let Talan down, even though you gave your word not to, makes me sick."),\
		_("I'm sorry, but I had no other choice."),\
		_("I don't want to hear your lame excuses. You have broken your word and that is all that counts."),\
		_("With these words she turns her back on you and continues with her work."),\
		_("I am afraid so. I was wondering whether you noticed something unusual during the night of the theft?"),\
		_("But {who_heard_noise} heard something outside the inn as well."),\
		_("What mercenary?"),\
		_("His name is Endhelm, I believe. You must have noticed him in the common room: he carries a sword and swears a lot. I'm sick of his likes, but out here we are getting to see plenty of them."),\
		_("Could he be involved into the theft?"),\
		_("Besides, few Dwarves go further than Waste's Edge, so if you want to buy from them directly, this is the best place to meet."),\
		_("I need to fetch something for my mistress, but the pantry is locked."),\
		_("Then you have spoken to your Lady? I was afraid that Jelom wouldn't allow you to see her. Even I was refused entry when I brought her some breakfast this morning! Can you imagine that?"),\
		_("The key, Mrs. Redwyne ..."),\
		_("What? Ah ... the key. Sorry, $name. I only hope it is not too uncomfortable for your mistress, being locked into that small chamber and all that."),\
		_("Lucia rambles on some more, but finally she reaches into her apron and hands you the key to the storeroom."),\
		_("Excuse me Lucia, I have to fetch something for Lady Silverhair from the pantry, and ..."),\
		_("... and now you want my key!? You have nerves! Do you think I'd forget how you let Talan down, despite the word you've given me?"),\
		_("Please Lucia, I need the key."),\
		_("Spare me your false friendliness. You tricked me once with your charm, but a second time I won't fall for it!"),\
		_("And what about my mistress?"),\
		_("I pity the poor woman; held for theft and stuck with a sycophant like you."),\
		_("Just give me that key and I won't bother you again!"),\
		_("And I'm not taking that tone either! You have used my confidence and must suffer the consequences."),\
		_("Look, Lucia, I spoke with Talan and he understands what I had to do."),\
		_("He's not in terrible trouble then? Seems you are in luck, $name. I wouldn't have forgiven you if you brought any harm upon the lad."),\
		_("May I have the key then?"),\
		_("Without any further words, Lucia reaches into her apron and hands you the key to the storeroom.")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"self.talked_about_fingolson == 1\n",\
		"self.asked_about_theft == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_olivers_noise\") == 1 and self.asked_about_noise == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 0\n",\
		"self.the_npc.get_val (\"know_shairs_clerk\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") != 0 and self.asked_about_noise == 1\n",\
		"self.the_npc.get_val (\"talked_about_theft\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"told_on_talan\") == 1 or adonthell.gamedata_get_quest(\"demo\").get_val (\"told_on_talan\") == 2\n",\
		"self.the_npc.get_val (\"talked_about_theft\") != 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") != 0\n",\
		"adonthell.gamedata_get_character(\"Alek Endhelm\").get_val (\"talked_to\") == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"get_item\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"pantry_locked\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"soothe_lucia\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"told_on_talan\") == 2\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\", 1)\n",\
		"self.the_npc.set_val (\"know_shairs_clerk\", 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"complain_about_wastesedge\" , 1)\n",\
		"self.talked_about_fingolson = 1\nself.asked_about_noise = 1\nself.the_npc.set_val (\"talked_about_theft\", 1)\n",\
		"self.asked_about_theft = 1\n",\
		"self.talked_about_fingolson = 1\n",\
		"self.asked_about_noise = 1\nself.the_npc.set_val (\"talked_about_theft\", 1) \n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_talan_singing\" , 1)\n",\
		"self.talked_about_fingolson = 1\nself.asked_about_noise = 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"pantry_locked\" , 2)\n",\
		"self.the_npc.set_val (\"refuses_key\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"soothe_lucia\" , 0)\nadonthell.gamedata_get_quest(\"demo\").set_val (\"told_on_talan\" , 3)\nadonthell.gamedata_get_quest(\"demo\").set_val (\"pantry_locked\" , 2)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (92, 1, 8), (87, 1, -1), )),\
		("Narrator", -1, ((2, 0, -1), )),\
		("Default", -1, ((3, 0, -1), (4, 0, -1), (6, 0, -1), )),\
		(None, 0, ((8, 0, -1), )),\
		(None, 0, ((5, 0, -1), )),\
		("Default", -1, ((7, 0, -1), (50, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((26, 0, -1), )),\
		("Default", -1, ((9, 0, -1), (25, 0, -1), )),\
		(None, 1, ((14, 0, -1), (10, 0, -1), )),\
		("Default", -1, ((12, 0, -1), (11, 0, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		("Default", 2, ((30, 0, -1), (31, 0, -1), )),\
		("Default", -1, ((15, 0, -1), )),\
		("Default", 2, ((16, 0, -1), )),\
		(None, -1, ((17, 0, -1), )),\
		("Default", 3, ((41, 0, -1), (18, 0, 1), )),\
		("Default", -1, ((85, 0, 6), (68, 0, 3), (19, 0, -1), )),\
		(None, -1, ((23, 0, -1), (21, 0, -1), )),\
		(None, -1, ((23, 0, -1), )),\
		("Default", 4, ((20, 0, -1), (22, 0, -1), (11, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		("Default", -1, ((32, 0, -1), )),\
		("Default", -1, ((59, 0, -1), )),\
		(None, -1, ((26, 0, -1), )),\
		("Default", -1, ((27, 0, -1), )),\
		("Default", 5, ((28, 0, -1), (33, 0, -1), )),\
		(None, 1, ((18, 0, 1), (29, 0, -1), (34, 0, -1), )),\
		("Default", 2, ((30, 0, -1), (31, 0, -1), )),\
		(None, -1, ((37, 0, -1), )),\
		(None, -1, ((40, 0, -1), )),\
		("Default", -1, ((100, 0, 11), (39, 0, -1), )),\
		(None, -1, ((24, 0, -1), )),\
		("Default", -1, ((35, 0, -1), )),\
		("Default", -1, ((36, 0, -1), )),\
		(None, -1, ((17, 0, -1), )),\
		("Default", -1, ((38, 0, -1), (60, 0, -1), )),\
		("Default", -1, ((39, 0, -1), )),\
		(None, -1, ((44, 0, -1), )),\
		("Default", -1, ((42, 0, 2), (43, 1, -1), )),\
		("Default", -1, ((65, 0, -1), )),\
		(None, -1, ((47, 0, -1), )),\
		(None, -1, ((55, 0, -1), )),\
		("Default", -1, ((45, 0, -1), (46, 0, -1), )),\
		(None, -1, ((58, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((48, 0, -1), )),\
		("Default", -1, ((46, 0, -1), (49, 0, -1), )),\
		(None, -1, ((62, 0, -1), )),\
		(None, -1, ((51, 0, -1), )),\
		("Default", -1, ((52, 0, -1), (53, 0, -1), )),\
		("Default", -1, ((39, 0, -1), (28, 0, -1), )),\
		("Default", -1, ((33, 0, -1), (54, 0, -1), )),\
		(None, -1, ((55, 0, -1), )),\
		("Default", 6, ((56, 0, -1), )),\
		("Default", -1, ((85, 0, 6), (68, 0, 3), (57, 0, -1), )),\
		(None, -1, ((23, 0, -1), )),\
		("Default", -1, ((64, 0, -1), )),\
		("Default", -1, ((66, 0, -1), )),\
		("Default", -1, ((61, 0, -1), )),\
		("Default", -1, ((46, 0, -1), (49, 0, -1), )),\
		("Default", -1, ((103, 0, -1), )),\
		("Default", -1, ((64, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ((66, 0, -1), (85, 0, 6), (68, 0, 3), )),\
		(None, -1, ((67, 0, -1), )),\
		("Default", -1, ()),\
		(None, -1, ((69, 0, -1), )),\
		("Default", -1, ((99, 0, 10), (70, 0, -1), )),\
		(None, -1, ((71, 0, -1), )),\
		("Default", -1, ()),\
		(None, -1, ((73, 0, 5), (77, 1, -1), )),\
		("Default", -1, ((74, 0, -1), (78, 0, -1), )),\
		(None, -1, ((75, 0, -1), )),\
		("Default", 7, ((76, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((81, 0, -1), )),\
		(None, -1, ((79, 0, -1), )),\
		("Default", -1, ((74, 0, -1), (80, 0, -1), )),\
		(None, -1, ((82, 0, -1), )),\
		(None, -1, ((79, 0, -1), )),\
		("Default", -1, ((75, 0, -1), )),\
		(None, -1, ((84, 0, -1), )),\
		("Default", -1, ((66, 0, -1), )),\
		(None, -1, ((86, 0, -1), )),\
		("Default", -1, ((72, 0, 4), (83, 1, -1), )),\
		("Narrator", -1, ((88, 0, -1), )),\
		("Default", -1, ((104, 0, 12), (89, 0, 7), (98, 0, 9), )),\
		(None, -1, ((90, 0, -1), )),\
		("Default", -1, ((91, 0, -1), )),\
		("Default", 8, ((41, 0, -1), (18, 0, 1), )),\
		("Narrator", -1, ((117, 0, 13), (109, 1, 12), (93, 1, -1), )),\
		(None, -1, ((94, 0, -1), )),\
		("Default", -1, ((95, 0, -1), )),\
		(None, -1, ((96, 0, -1), )),\
		("Default", -1, ((97, 0, -1), )),\
		("Narrator", -1, ()),\
		(None, -1, ((17, 0, -1), )),\
		(None, -1, ((86, 0, -1), )),\
		(None, -1, ((101, 0, -1), )),\
		("Default", -1, ((102, 0, -1), )),\
		(None, -1, ((44, 0, -1), )),\
		("Default", -1, ((63, 0, -1), )),\
		(None, 9, ((105, 0, -1), )),\
		("Default", -1, ((106, 0, -1), )),\
		(None, -1, ((107, 0, -1), )),\
		("Default", -1, ((108, 0, -1), )),\
		("Narrator", -1, ()),\
		(None, -1, ((110, 0, -1), )),\
		("Default", 10, ((95, 0, -1), (111, 0, -1), )),\
		(None, -1, ((112, 0, -1), )),\
		("Default", -1, ((113, 0, -1), (115, 0, -1), )),\
		(None, -1, ((114, 0, -1), )),\
		("Default", -1, ((97, 0, -1), )),\
		(None, -1, ((116, 0, -1), )),\
		("Default", -1, ((97, 0, -1), )),\
		(None, -1, ((118, 0, -1), )),\
		("Default", -1, ((119, 0, -1), )),\
		(None, 11, ((120, 0, -1), )),\
		("Narrator", -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n

	def who_heard_noise (self):
	    n = adonthell.gamedata_get_quest("demo").get_val ("know_noise")
	    if n == 1:
	        return _("Lady Silverhair has")
	    elif n == 2:
	        return _("Lady Frostbloom has")
	    else:
	        return _("both Lady Silverhair and Lady Frostbloom have")

