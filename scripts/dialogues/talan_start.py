import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class talan_start (dialogue.base):
	text = [None,\
		_("Oh, hullo again, $name."),\
		_("Listen, I really am sorry about that fuss at the gate. I hope you will not hold it against me."),\
		_("Please do not mention it again. I assure you that I hold no grudge against you."),\
		_("Oh... that. Yes, how may I help you?"),\
		_("Hello, Talan. Look, I have a couple more questions about the theft."),\
		_("In the morning, of course, I heard that Master Fingolson's gems had been stolen and that Lady Silverhair was suspected of the theft."),\
		_("So you did not see or hear anything out of place that night?"),\
		_("No... no, not at all."),\
		_("If you do not have any more questions ..."),\
		_("No, thank you, I have a lot of work to do. You have been most helpful."),\
		_("I hear that Alek Endhelm was very interested in Fingolsons business. Have you noticed him doing anything suspicious?"),\
		_("Oh, he's a nasty sort, he is, sir. But other than being a busybody, I haven't noticed him doing anything that would lead me to believe that he is the thief."),\
		_("Now, if you don't have any more questions..."),\
		_("I wish you had not lied to me about the night of the theft."),\
		_("Wh... what do you mean?"),\
		_("You were not, as you told me, manning your post the whole night."),\
		_("Now you look here! I was, and I do not appreciate you calling me a liar."),\
		_("Oh. So you do know ... ?"),\
		_("Yes I do. And I believe you left your post that night, did you not, Talan?"),\
		_("Yes, I did. But please do not tell Jelom, sir! He will have my hide for sure if he finds out! Please, I beg you!"),\
		_("No, you missed it. Because you were off singing, weren't you?"),\
		_("I'm afraid I was. Oh what terrible mistake! I am so sorry, $name. I did not know about the noise! It is my fault that Lady Silverhair is being held in her room!"),\
		_("Calm down, Talan. Now I can prove that something strange happened that night at least."),\
		_("And why was Lady Silverhair accused?"),\
		_("Well, the most obvious reason is of course that she was interested in the gems, and made a trip here just to buy them."),\
		_("But she felt the quality of the gems was too low, and she is hardly pressed for money, so why would she turn around and steal the gems?"),\
		_("Well, according to Jelom, what better way to throw suspicion off yourself then to claim that the stones are of low quality?"),\
		_("Ah, Jelom said that, did he? What else did he say?"),\
		_("Who is Jelom? Your superiour?"),\
		_("He is the other guard here. He is not exactly my superiour, but he is older than me and has been here much longer, so he is kind of in charge."),\
		_("He found her behaviour suspicious. I mean, she is all high and mighty, acting above the rest of us, and she obviously doesn't like dwarves ..."),\
		_("Wait! Why does everybody believe that she has an aversion to dwarves?"),\
		_("Well, the way I heard the story, Bjarn made a point of insulting the entire elven race, loudly and publicly, upon her arrival!"),\
		_("Well, as I heard it told, she had quite an argument with Master Fingolson in which she insulted the quality of his gems and then the dwarven race!"),\
		_("Well, Master Fingolson can be, um ... blunt, I guess, at times, but ..."),\
		_("Wasn't the argument rather Fingolson's fault, then?"),\
		_("Well, I... ah, perhaps..."),\
		_("Maybe you should speak to Jelom. He knows more about the theft and his reasons for suspecting her than I do..."),\
		_("Well, you've talked to Jelom. You know what he thinks..."),\
		_("And so I shall. Where is he?"),\
		_("Yes. I do know what he thinks. That, however, does not help me too much."),\
		_("He is guarding the hallway leading to Lady Silverhair's room."),\
		_("Well, I shall go and talk to him, then. Thank you and good day."),\
		_("Ah, $name, hello."),\
		_("Hi there, Talan. Look, I am sorry that ..."),\
		_("No, you did what you had to do, and it was only right that I got in trouble for leaving my post. And I owe you a big favour for covering for me!"),\
		_("No, I understand. It was because of me shirking my duty that I did not see what happened that night. You had no choice, and I do not hold a grudge against you for doing your duty."),\
		_("All the same, I am still sorry for getting you into trouble with Jelom. Thank you for understanding."),\
		_("No, it was the least I could do. Do not worry about the favour."),\
		_("I don't know if there is any coincidence, but this visit of Master Fingolson is very unusual. You see, he is quite a regular here. He comes every other month or so, and usually stays for a week before going back."),\
		_("Usually he shows up a few days before the client, just to relax, I guess. Until about a year ago, he would spend this time in the common room, drinking ale and talking with Erek, his apprentice."),\
		_("About a year ago, things changed. When he came, he came alone. He still showed up a couple of days ahead of the client, but he no longer visited the common room much. He just stayed down in his room."),\
		_("But at this most recent visit, Bjarn got here the morning of Lady Silverhair's arrival, which was a little strange. What's more, he brought Erek again, although I thought he had finished his apprenticeship and moved on long ago."),\
		_("I see ... that is strange. Thanks for telling me, Talan!"),\
		_("Couldn't it be that you missed what there was to see or hear?"),\
		_("You think this argument is enough to prove Lady Silverhair's guilt?"),\
		_("I ... I don't know."),\
		_("And you say Lady Silverhair was accused because she \"obviously doesn't like dwarves\"!?"),\
		_("True, but practically anyone at the Inn could have thrown an eye on the stones."),\
		_("According to Jelom there is no doubt that Lady Silverhair is the thief."),\
		_("I'm anxious to hear his reasoning, then."),\
		_("I should think so Talan, considering the discomfort you caused my mistress."),\
		_("What has happened cannot be undone, I fear. But perhaps there is a little detail that might help to clear the Lady's reputation."),\
		_("I've been told about a noise that night, but you say you heard nothing."),\
		_("Should I rather call you a bard then?"),\
		_("A ... noise? What noise?"),\
		_("The noise of someone singing, Talan."),\
		_("According to Oliver, somebody must have been in the stables that night."),\
		_("Well, I did not notice anything, $name. That's the truth!"),\
		_("It had better be, my friend.."),\
		_("If I want to prove Lady Silverhair's innocence, I have little other choice, I fear."),\
		_("I, I understand. I am very sorry, $name ..."),\
		_("Sure, but there is not much to tell. I was out here, making my rounds, walking around the yard like every other night."),\
		_("Thank you sir. By the way, I am Talan."),\
		_("I am $name, and I'd like to learn a little more about the theft."),\
		_("Why was the Lady Silverhair accused?"),\
		_("Are you sure you haven't noticed anything out of place that night?"),\
		_("But Lady Frostbloom told me about a noise she heard."),\
		_("Frostbloom? Then it must have been a Yeti, I suppose."),\
		_("But seriously, I did not notice anything. I'm sorry, $name.")]

	loop = [8, 9]

	cond = [\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"silverhair_free\") != 1\n",\
		"self.the_npc.get_val (\"apologised\") != 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_alek_eavesdrop\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 1 and self.the_npc.get_val (\"heard_nothing\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_low_quality\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_jelom\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_bjarns_insult\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"told_on_talan\") < 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"know_olivers_noise\") != 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_olivers_noise\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_talan_singing\") != 2\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") & 2 == 2\n"]

	code = [\
		"self.the_npc.set_val (\"apologised\" , 1)\n",\
		"self.the_npc.set_val (\"heard_nothing\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_talan_singing\" , 2)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_jelom\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"told_on_talan\" , 2)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((2, 0, 1), (1, 1, 0), (44, 1, -1), )),\
		("Default", -1, ((14, 0, 3), (5, 1, -1), )),\
		("Default", 0, ((3, 0, -1), )),\
		(None, -1, ((74, 0, -1), )),\
		("Default", -1, ((76, 0, -1), (77, 0, 11), (11, 0, 2), )),\
		(None, -1, ((4, 0, -1), )),\
		("Default", -1, ((24, 0, -1), (7, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		("Default", 1, ((9, 0, -1), )),\
		("Default", -1, ((24, 0, -1), (78, 0, 12), (10, 0, -1), (55, 0, 9), (11, 0, 2), (68, 0, 10), )),\
		(None, -1, ()),\
		(None, -1, ((12, 0, -1), )),\
		("Default", -1, ((13, 0, -1), )),\
		("Default", -1, ((76, 0, -1), (10, 0, -1), (77, 0, 11), )),\
		(None, -1, ((15, 0, -1), )),\
		("Default", -1, ((64, 0, -1), (16, 0, -1), )),\
		(None, -1, ((17, 0, -1), )),\
		("Default", -1, ((64, 0, -1), (65, 0, -1), )),\
		("Default", -1, ((19, 0, -1), )),\
		(None, -1, ((20, 0, -1), )),\
		("Default", -1, ((71, 0, -1), )),\
		(None, -1, ((22, 0, -1), )),\
		("Default", 2, ((23, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((25, 0, -1), )),\
		("Default", -1, ((59, 0, -1), (26, 0, 5), )),\
		(None, -1, ((27, 0, -1), )),\
		("Default", -1, ((29, 0, 6), (28, 1, -1), )),\
		(None, -1, ((31, 0, -1), )),\
		(None, -1, ((30, 0, -1), )),\
		("Default", 3, ((31, 0, -1), )),\
		("Default", -1, ((32, 0, -1), )),\
		(None, -1, ((34, 0, -1), )),\
		(None, -1, ((35, 0, -1), )),\
		("Default", -1, ((33, 0, 7), (56, 0, -1), )),\
		("Default", -1, ((36, 0, -1), (58, 0, -1), )),\
		(None, -1, ((57, 0, -1), )),\
		("Default", -1, ((38, 0, 6), (39, 1, -1), )),\
		("Default", -1, ((40, 0, -1), (43, 0, -1), )),\
		("Default", -1, ((41, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((43, 0, -1), )),\
		(None, -1, ()),\
		("Default", -1, ((45, 0, -1), )),\
		(None, -1, ((46, 0, 8), (47, 1, -1), )),\
		("Default", -1, ((62, 0, -1), (49, 0, -1), )),\
		("Default", 4, ((48, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ()),\
		("Default", -1, ((51, 0, -1), )),\
		("Default", -1, ((52, 0, -1), )),\
		("Default", -1, ((53, 0, -1), )),\
		("Default", -1, ((54, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((15, 0, -1), )),\
		(None, -1, ((37, 0, -1), )),\
		("Default", -1, ((38, 0, 6), (39, 1, -1), )),\
		(None, -1, ((37, 0, -1), )),\
		(None, -1, ((60, 0, -1), )),\
		("Default", -1, ((29, 0, 6), (61, 1, -1), )),\
		(None, -1, ((31, 0, -1), )),\
		(None, -1, ((63, 0, -1), )),\
		("Default", -1, ((50, 0, -1), )),\
		(None, -1, ((66, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		("Default", -1, ((68, 0, 10), (67, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		(None, -1, ((69, 0, -1), )),\
		("Default", -1, ((21, 0, 4), (70, 1, -1), )),\
		(None, -1, ()),\
		(None, -1, ((72, 0, -1), )),\
		("Default", 2, ()),\
		("Default", -1, ((6, 0, -1), )),\
		("Default", -1, ((75, 0, -1), )),\
		(None, -1, ((73, 0, -1), )),\
		(None, -1, ((25, 0, -1), )),\
		(None, -1, ((8, 0, -1), )),\
		(None, -1, ((79, 0, -1), )),\
		("Default", -1, ((80, 0, -1), )),\
		("Default", -1, ((21, 0, 4), ))]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n
