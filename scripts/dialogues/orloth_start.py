import dialogue
import adonthell

# -- pygettext support
def _(message): return message

class orloth_start (dialogue.base):
	text = [None,\
		_("This appears to be the Innkeeper and owner of the place. He seems lost in thought and it looks as if he hasn't slept much lately. His worried face brightens up as you approach though, and his voice is warm and friendly:"),\
		_("Welcome to Waste's Edge, traveller. Here you shall find the pleasures of a hot meal and bath if you desire. And safe and comfortable lodging."),\
		_("But excuse me sir, I talk and talk and haven't even introduced myself. Orloth's the name, sir. Orloth Redwyne, I'm the landlord here at Waste's Edge. Just speak your wishes and I'll see to it."),\
		_("What are those troubles you talked about. The guard said something about a theft, but it made not much sense."),\
		_("'Tis a shame, really. You'd think you were in danger on the road, with all those bandits about. But no, right here, despite the guards, a mans belongings aren't safe from filthy thieves."),\
		_("And do you know what bothers me the most? It's no obvious bad types doing this, but people like you and me, if I may say so. An elvish Lady even! Where to will this lead, I ask!"),\
		_("Hold on! That Talan told me the same nonsense. But I know the Lady Silverhair and to suspect her of all is simply absurd."),\
		_("Do not worry, Master Redwyne. I believe things would turn out quite different if only someone would commence a proper investigation."),\
		_("I couldn't agree more, sir. But who could possibly do that? Don't get me wrong, Talan is a good lad, and Jelom is surely doing his duty, but they are clearly overtaxed with the situation. And it will be days before a senior officer arrives."),\
		_("Of course. Well, you may have met Lady Frostbloom in the yard already. She's an artist with a fancy to yetis. She says the wilderness and the nearby mountains inspire her, so she's a regular visitor."),\
		_("My apologies, sir. To tell the truth, when they first accused her I could hardly believe it myself. But the evidence is too strong to put aside."),\
		_("Do not worry, Master Redwyne. I will unmask the culprit. Then you'll see that it isn't the Lady Silverhair."),\
		_("That may be as it will. I for one will be glad if only this business gets sorted out, either way. So I shall do my best to support your efforts."),\
		_("Still she's a nice person if you get to know her better, unlike the rough fellow over there. Alek Endhelm, a mercenary from the north. That's all I know about him, but I would say where he goes, trouble follows afoot."),\
		_("But what can I do about it? He's paying for his room, although he insisted on a cheap one down the cellar. And as long as he's behaving, I can but keep an eye on him. You should beware of him as well, if I may advice you, sir."),\
		_("No worries. I've dealt with his likes before. So who else is here, then?"),\
		_("Thank you Master Redwyne. I think I have heard enough of this."),\
		_("There is Master Fingolson of course, and young Erek, his apprentice. They mostly keep to themselves, as Fingolson does not approve of non-dwarvish company."),\
		_("So you haven't heard about that, yet? On Lady Silverhair's arrival, the Dwarf made some remark about her. A jest about Elves or somesuch. I don't remember the words, as it's been a busy afternoon with the inn crowded like that."),\
		_("There was the lot I've already mentioned plus Tristan Illig and, not to forget, that nosy Fellnir Kezular, asking me questions about everyone else. I really hadn't much time to follow the conversations."),\
		_("Please tell me more about the last two."),\
		_("Certainly. Tristan Illig, a merchant from Cirdanth sits over there. He was waiting at the inn to meet his caravan. But when it moved by in the morning, he wasn't allowed to join it."),\
		_("And finally there is Fellnir Kezular, a healer of some sorts. He's trading in medicine and gossip, as it seems. From what I've heard, he must have had a confrontation with the mercenary. Now he hardly leaves his room."),\
		_("I hope I've given you an idea of the people at Waste's Edge. A colourful crowd for sure, but if you'd ask me to point out the thief, I couldn't. I'll support your efforts as good as I can, though."),\
		_("She certainly wouldn't like a Dwarf to make fun of her."),\
		_("I guess it's partly Fingolson's fault. When Lady Silverhair arrived he made some remark about her, a harmless jest about Elves, if I recall. But it seems she didn't take well to this kind of humour."),\
		_("I still wonder why he became a tradesman, what with that aversion to other people. However, he is as honourable as a Dwarf can be. That's why I'm still a bit surprised about his behaviour towards Lady Silverhair."),\
		_("And Lady Silverhair has practically admitted that she was in need of the gems. I imagine that she was pretty desperate and so one thing led to the other."),\
		_("Ah. See, that is where the trouble starts. Lady Silverhair wouldn't have it, that her room be searched. I would be glad to believe in her innocence, but you have to agree that this is highly suspicious."),\
		_("And you should have heard with what she threatened the first person to touch her luggage. She made quite an impression on the poor guards, and who is to argue with an elvish noble?"),\
		_("Not now. You have given me plenty to think about already, Master Redwyne."),\
		_("Ah, any news about the thief, $name?"),\
		_("I am $name, Lady Silverhair's clerk."),\
		_("$name, from Cirdanth."),\
		_("I wish you luck with your inquiries then, uh ... I didn't catch your name, sir?"),\
		_("Well then, $name, now we've got to find you a room. We're practically full up to the roof. What room remains is small, but comfortable, you'll see."),\
		_("The landlord calls for Oliver, the boy you met outside, and shortly afterwards he enters the common room to show the way to your chamber."),\
		_("That's Lucia, all right. Did she go on about Lenhart again? He's my elder brother. Inherited the business from our father, although he never really liked it out here. So he asked me to buy the Inn."),\
		_("See, I was a carter's apprentice in Erinsford back then, and the prospect of taking over at Waste's Edge instead was very appealing. Lucia and I had just married, and the dowry would have nearly paid for the Inn."),\
		_("But I am forgetting myself. Lucia's right when she says I'd talk too much. Not that she is much better in that respect. Excuse my rambling, $name.. There must be other things you want to know."),\
		_("I'm making progress, but I still need more information."),\
		_("Well, I'll do my best to be of some help. Just ask your questions."),\
		_("I don't mean to pry, but I couldn't help to notice your wife's dislike of Waste's Edge."),\
		_("I'd like to hear about the theft again, Master Redwyne."),\
		_("Sure. Where shall I begin?"),\
		_("I'd like to know what happened before the theft."),\
		_("Could you tell me something about your guests?"),\
		_("I see. Can I help you with something else then?"),\
		_("Please start with Lady Silverhair's arrival."),\
		_("I'd like to hear the bit about the argument again."),\
		_("How was the theft discovered again, Master Redwyne?"),\
		_("She came shortly before lunchhour, so a number of guests were gathered in the common room. Silverhair took place next to the Dwarfs and Fingolson leaned over to talk to her."),\
		_("As I have said already, I don't know what he said. But that Alek fellow burst out laughing, so it must have been a jest of some sort. Whatever it was, Lady Silverhair didn't enjoy it."),\
		_("The more I think about it, the less the outcome surprises me. I have never noticed Dwarves and Elves getting along any worse than other people here, but in the case of Fingolson and Silverhair, the cliche seems to fit."),\
		_("But it's too late to think about this. The theft already happened and talking won't convict the thief. So ... where was I?"),\
		_("The argument between the two."),\
		_("How was the theft discovered?"),\
		_("I think you were finished."),\
		_("Ah, the argument; let's see. Master Fingolson and Lady Silverhair sat together in the parlour to discuss their business in private. I don't know what they talked first but it didn't take long before we heard them shouting."),\
		_("Suddenly the door burst open and Silverhair swept out of the room. She vanished upstairs without another word and nobody felt like bothering her at that moment, I tell you!"),\
		_("Shortly afterwards the Dwarves appeared. Fingolson headed straight for his room, but that nosy Kezular threw himself at Erek. They didn't talk long though, as Fingolson returned and sent the apprentice to pack their luggage."),\
		_("Fingolson did not keep his voice down, so everyone could hear that he would leave with the first light of dawn, \"without selling to the greedy Elf\", as he said."),\
		_("Then he turned to us others, let out a rant about Elves and their unseemly manners and marched off down the stairs."),\
		_("I have never seen Master Fingolson so enraged and emotional. He was practically fuming with anger. Whatever the argument was about, it must have hurt him deeply."),\
		_("And what about the theft? How was that discovered, then?"),\
		_("Thank you Master Redwyne, that's all I wanted to hear."),\
		_("That was in the morning. As I told you, Fingolson was going to leave early. As he told us, he and Erek were going through their luggage to see whether everything was well packed up, and there they found the gems gone."),\
		_("Perhaps you better speak with Fingolson or Erek yourself, since I can only tell what I heard of them. But it seems that somebody sneaked into their room during the night and took them away."),\
		_("However, once the guards were fetched and everyone gathered in the common room, it turned out that nobody had noticed anything, and nobody had left Waste's Edge either."),\
		_("That was creepy, I tell you. To know that the thief was amongst us at that moment. But I had never thought that it would be the Lady Silverhair!"),\
		_("Why was the Lady Silverhair accused of the theft?"),\
		_("And that argument was the sole reason to accuse Lady Silverhair of the theft?"),\
		_("What made the guards think that she committed the theft?"),\
		_("But first of all we had to convince my beloved wife. And that, as you might imagine, was no easy task. I'm still a bit puzzled how my brother did it, but in the end she gave in to him."),\
		_("She likes running the Inn, no doubt. But her dream is to move business to Cirdanth, to civilisation as she says. Not that she would find nothing to complain about in the city. Otherwise she wouldn't be the Lucia I love."),\
		_("Isn't that obvious? She had an interest into these gems, and, as it turned out, didn't like Master Fingolson's offer. She didn't like Master Fingolson either."),\
		_("Of course she denied stealing the gems and declared it below her dignity. But she didn't allow the guards to search her room, and why would she do that if she had nothing to hide?"),\
		_("Of course not. The main reason was that she wanted those gems, but, as it turned out, she didn't want to pay Fingolson's price. And she admitted that she didn't like him. So she had a motive."),\
		_("To be honest, everybody could be the thief. That's why nobody may leave until the gems are retrieved. But all the evidence is against Lady Silverhair."),\
		_("Very well. Is there something else you wish to know then, $name?"),\
		_("That's all for now, Master Redwyne. I don't want to keep you off your work any longer."),\
		_("I fear there aren't. I'm still at the beginning of my investigations."),\
		_("Since you know her, sir, would you mind talking some sense into her? It'd be much easier for all parties if she would finally confess."),\
		_("Certainly not! I don't know what is going on, but I assure you that Lady Silverhair has no part in it."),\
		_("No offence meant sir, but I fear it will take more than your word to clear her Ladyship from suspicion."),\
		_("Well, actually I'd be glad to lend a hand."),\
		_("I'll speak with her, but I doubt that Lady Silverhair will confess to a crime she hasn't committed."),\
		_("Really? Now that's a relief to hear. The sooner everything returns to normal, the better I say! So I for one shall help you as good as I can."),\
		_("Thank you, Master Redwyne. I will come back to you when I need some help."),\
		_("First of all I'd like to know what exactly happened."),\
		_("Could you tell me something about your guests then?"),\
		_("All right. So lets see: you know about Lady Silverhair's business here?"),\
		_("Yes I do."),\
		_("No, not yet."),\
		_("She had an appointment with Bjarn Fingolson, a merchant from Uzdun'Kal. She wanted to buy some gems off the Dwarf. I guess they were pretty important to her if she came all the way from Cirdanth herself."),\
		_("Well, the evening of her arrival, she and Master Fingolson sat together in the little parlour next to the common room to complete the bargain. But it wasn't long when we heard them arguing."),\
		_("I cannot tell what happened before the shouting started. Perhaps you can learn more from Fingolson's apprentice, Erek, who was in there with them."),\
		_("However, all of us could hear that Lady Silverhair did not approve of Master Fingolson's offer."),\
		_("And because of that argument, Lady Silverhair was blamed after the gems had been stolen?"),\
		_("It wasn't the argument alone. She and the Dwarf did not get along very well from the beginning. And there were other reasons of course."),\
		_("They didn't get along well, you say? How come?"),\
		_("Tell me about the other reasons."),\
		_("But the gems were not found on her, right?"),\
		_("Well, it was unfortunate at least and has probably influenced the negotiations. She enraged Fingolson so much that he swore to leave early next morning without selling to her."),\
		_("Isn't that a bit far-fetched? Practically anyone could have stolen the gems, couldn't they?"),\
		_("Well, for one, the theft must have happened during the night as Master Fingolson assured us. And who if not an Elf could sneak into a room without two people inside noticing?"),\
		_("Then nobody has left the inn. Any of the others could have been long gone in the morning, but for someone known to the victim, this wouldn't be an option."),\
		_("And finally, after she had been accused, she could have easily proved that she did not hide the gems. Instead she allowed nobody even to enter her room."),\
		_("That turned out to be a bit of a dilemma though. As long as the gems are not found, there is uncertainty about her guilt. So to prevent the thief from smuggling them outside, nobody must leave the Inn."),\
		_("Lady Silverhair has been confined to her room, and Bregon of the guard has been sent to fetch a senior officer from the garrison at Erinsford to take over the investigations."),\
		_("The landlord calls for someone named Oliver, and soon after, a small boy enters the common room to show you to your chamber."),\
		_("In that case I'll better hurry and make sure that his presence won't be necessary. Thank you Master Redwyne."),\
		_("Now I see a lot clearer. But I would know a little more about the people here."),\
		_("Sorry, but I don't follow you, Master Redwyne."),\
		_("An impolite Dwarf isn't the most pressing problem right now. So please go on."),\
		_("I'd like to know what exactly happened."),\
		_("She is probably the only person around not bothered by the theft. She's never paying much attention to anything but her work."),\
		_("Although, I fear latter is no longer granted for sure. You've chosen troublesome times for your visit, as you have probably noticed."),\
		_("Well, it's certain that it isn't the Lady Silverhair. But I need to learn more."),\
		_("It's something she can't forgive, although I am not sure whom she blames more: herself or Lenhart."),\
		_("You look troubled, $name. Can I help you with something?"),\
		_("You don't have a spare key to the storeroom, by any chance?"),\
		_("I need to fetch something from the pantry for my mistress, but the door is locked."),\
		_("Sorry, I can't help you there. Lucia keeps the key; you'll have to ask her."),\
		_("Why that? Has Lucia mislaid hers? That doesn't sound like her at all."),\
		_("That is the problem, I fear. She's annoyed and refuses to hand it out."),\
		_("No, she is annoyed and won't give it to me."),\
		_("Ah! That's Lucia. I should have warned you not to anger her, $name. Now there is little you can do, I fear. There is no spare key, and it'll take a while before her anger wears off."),\
		_("Could you not try to calm her, Master Orloth?"),\
		_("Me? I want to sleep in my bed tonight, thank you! I'm not going to meddle. That you have upset her is bad enough already."),\
		_("Is there nothing I can do?"),\
		_("You upset her!? Oh what terrible mistake! Once enraged, it takes a while before her anger wears off. I don't think that you'll be getting that key anytime soon."),\
		_("Well, I don't know what you did to anger my dear Lucia, and I don't wanna know, but unless you don't set things right, she'll be giving you a hard time."),\
		_("No, the only way to calm her is to set things right.")]

	cond = [\
		"self.the_npc.get_val (\"talked_to\") == 0\n",\
		"self.the_npc.get_val (\"told_about_shair\") == 0\n",\
		"self.first_run == 1\n",\
		"adonthell.gamedata_get_character(\"Oliver Redwyne\").get_val (\"talked_to\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_noise\") != 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"complain_about_wastesedge\") == 1\n",\
		"self.the_npc.get_val (\"explain_events\") == 1 and self.first_run != 1\n",\
		"self.the_npc.get_val (\"explain_events\") == 0\n",\
		"self.introduce_guests == 0\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"know_bjarns_insult\") == 0\n",\
		"self.the_npc.get_val (\"explain_events\") == 0 and self.first_run == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"silverhair_free\") == 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").get_val (\"get_item\") == 1 and adonthell.gamedata_get_quest(\"demo\").get_val (\"pantry_locked\") == 1\n",\
		"adonthell.gamedata_get_character(\"Lucia Redwyne\").get_val (\"refuses_key\") == 1\n"]

	code = [\
		"self.the_npc.set_val (\"talked_to\" , 1)\nself.first_run = 1\n",\
		"self.the_npc.set_val (\"told_about_shair\", 1)\nmyvar = adonthell.gamedata_get_quest(\"demo\").get_val (\"work_4_shair\")\nmyvar = myvar | 1\nadonthell.gamedata_get_quest(\"demo\").set_val (\"work_4_shair\" , myvar)\n",\
		"self.introduce_guests = 1\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_aleks_room\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_erek\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_bjarns_insult\" , 1)\n",\
		"self.the_npc.set_val (\"told_about_shair\", 1)\n\nmyvar = adonthell.gamedata_get_quest(\"demo\").get_val (\"work_4_shair\")\nmyvar = myvar | 1\nadonthell.gamedata_get_quest(\"demo\").set_val (\"work_4_shair\" , myvar)\n\n",\
		"adonthell.gamedata_get_character(\"Oliver Redwyne\").set_val (\"goto_players_room\" , 1)\n",\
		"self.the_npc.set_val (\"explain_events\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"know_argument\" , 1)\n",\
		"adonthell.gamedata_get_quest(\"demo\").set_val (\"soothe_lucia\" , 1)\n"]

	# -- (speaker, code, ((text, operation, condition), ...))
	dlg = [\
		(None, -1, ((1, 0, 0), (121, 1, 12), (32, 1, -1), )),\
		("Narrator", 0, ((2, 0, -1), )),\
		("Default", -1, ((118, 0, -1), )),\
		("Default", -1, ((4, 0, -1), )),\
		(None, -1, ((5, 0, -1), )),\
		("Default", -1, ((6, 0, -1), )),\
		("Default", -1, ((7, 0, -1), (8, 0, -1), )),\
		(None, 1, ((11, 0, -1), )),\
		(None, -1, ((9, 0, -1), )),\
		("Default", -1, ((86, 0, -1), )),\
		("Default", 2, ((117, 0, -1), )),\
		("Default", -1, ((83, 0, -1), )),\
		(None, -1, ((13, 0, -1), )),\
		("Default", -1, ((89, 0, -1), (90, 0, -1), (91, 0, -1), )),\
		("Default", -1, ((15, 0, -1), )),\
		("Default", 3, ((17, 0, -1), (16, 0, -1), )),\
		(None, -1, ((18, 0, -1), )),\
		(None, -1, ((48, 0, -1), )),\
		("Default", 4, ((27, 0, -1), )),\
		("Default", -1, ((20, 0, -1), )),\
		("Default", -1, ((17, 0, -1), (21, 0, -1), )),\
		(None, -1, ((22, 0, -1), )),\
		("Default", -1, ((23, 0, -1), )),\
		("Default", -1, ((24, 0, -1), )),\
		("Default", -1, ((89, 0, -1), (116, 0, 10), (44, 0, 6), )),\
		(None, -1, ((104, 0, -1), )),\
		("Default", 5, ((25, 0, -1), )),\
		("Default", -1, ((17, 0, -1), (114, 0, 9), (115, 0, -1), )),\
		("Default", -1, ((105, 0, -1), (103, 0, -1), )),\
		("Default", -1, ((30, 0, -1), )),\
		("Default", -1, ((109, 0, -1), )),\
		(None, -1, ((35, 0, 2), )),\
		("Default", -1, ((119, 0, 11), (41, 1, 4), (82, 1, -1), )),\
		(None, 6, ((36, 0, -1), )),\
		(None, -1, ((36, 0, -1), )),\
		("Default", -1, ((33, 0, 1), (34, 0, -1), )),\
		("Default", 7, ((37, 0, 3), (111, 1, -1), )),\
		("Narrator", -1, ()),\
		("Default", -1, ((39, 0, -1), )),\
		("Default", -1, ((74, 0, -1), )),\
		("Default", -1, ((47, 0, 8), (44, 0, 6), (46, 0, 7), (81, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((47, 0, 8), (44, 0, 6), (46, 0, 7), (43, 0, 5), )),\
		(None, -1, ((38, 0, -1), )),\
		(None, -1, ((45, 0, -1), )),\
		("Default", -1, ((49, 0, -1), (50, 0, -1), (51, 0, -1), (71, 0, -1), )),\
		(None, -1, ((92, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", -1, ((31, 0, -1), (116, 0, 10), (47, 0, 8), (44, 0, 6), )),\
		(None, -1, ((52, 0, -1), )),\
		(None, -1, ((59, 0, -1), )),\
		(None, -1, ((67, 0, -1), )),\
		("Default", -1, ((53, 0, -1), )),\
		("Default", -1, ((54, 0, -1), )),\
		("Default", -1, ((55, 0, -1), )),\
		("Default", -1, ((56, 0, -1), (58, 0, -1), (57, 0, -1), )),\
		(None, -1, ((59, 0, -1), )),\
		(None, -1, ((67, 0, -1), )),\
		(None, -1, ((80, 0, -1), )),\
		("Default", -1, ((60, 0, -1), )),\
		("Default", -1, ((61, 0, -1), )),\
		("Default", -1, ((62, 0, -1), )),\
		("Default", -1, ((63, 0, -1), )),\
		("Default", -1, ((64, 0, -1), )),\
		("Default", -1, ((65, 0, -1), (72, 0, -1), (66, 0, -1), )),\
		(None, -1, ((67, 0, -1), )),\
		(None, -1, ((80, 0, -1), )),\
		("Default", -1, ((68, 0, -1), )),\
		("Default", -1, ((69, 0, -1), )),\
		("Default", -1, ((70, 0, -1), )),\
		("Default", -1, ((73, 0, -1), (66, 0, -1), )),\
		(None, -1, ((76, 0, -1), )),\
		(None, -1, ((78, 0, -1), )),\
		(None, -1, ((76, 0, -1), )),\
		("Default", -1, ((120, 0, -1), )),\
		("Default", -1, ((40, 0, -1), )),\
		("Default", -1, ((77, 0, -1), )),\
		("Default", -1, ((79, 0, -1), )),\
		("Default", -1, ((77, 0, -1), )),\
		("Default", -1, ((66, 0, -1), )),\
		("Default", -1, ((47, 0, 8), (43, 0, 5), (81, 0, -1), )),\
		(None, -1, ()),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((84, 0, -1), (87, 0, -1), )),\
		(None, -1, ((85, 0, -1), )),\
		("Default", -1, ((12, 0, -1), )),\
		(None, -1, ((88, 0, -1), )),\
		(None, -1, ((85, 0, -1), )),\
		("Default", -1, ((89, 0, -1), (90, 0, -1), (91, 0, -1), )),\
		(None, -1, ((35, 0, 2), )),\
		(None, -1, ((92, 0, -1), )),\
		(None, -1, ((10, 0, -1), )),\
		("Default", 8, ((93, 0, -1), (94, 0, -1), )),\
		(None, -1, ((96, 0, -1), )),\
		(None, -1, ((95, 0, -1), )),\
		("Default", -1, ((96, 0, -1), )),\
		("Default", -1, ((97, 0, -1), )),\
		("Default", 9, ((98, 0, -1), )),\
		("Default", -1, ((99, 0, -1), )),\
		(None, -1, ((100, 0, -1), )),\
		("Default", -1, ((101, 0, -1), (102, 0, -1), (103, 0, -1), )),\
		(None, -1, ((26, 0, -1), )),\
		(None, -1, ((106, 0, -1), )),\
		(None, -1, ((29, 0, -1), )),\
		("Default", -1, ((28, 0, -1), )),\
		(None, -1, ((106, 0, -1), )),\
		("Default", -1, ((107, 0, -1), )),\
		("Default", -1, ((108, 0, -1), )),\
		("Default", -1, ((30, 0, -1), )),\
		("Default", -1, ((110, 0, -1), )),\
		("Default", -1, ((112, 0, -1), (113, 0, 8), )),\
		("Narrator", -1, ()),\
		(None, -1, ((35, 0, 2), )),\
		(None, -1, ((10, 0, -1), )),\
		(None, 5, ((19, 0, -1), )),\
		(None, -1, ((22, 0, -1), )),\
		(None, -1, ((92, 0, -1), )),\
		("Default", -1, ((14, 0, -1), )),\
		("Default", -1, ((3, 0, -1), )),\
		(None, -1, ((42, 0, -1), )),\
		("Default", -1, ((75, 0, -1), )),\
		("Default", -1, ((122, 0, 13), (123, 0, -1), )),\
		(None, -1, ((125, 0, -1), )),\
		(None, -1, ((124, 0, -1), )),\
		("Default", -1, ((126, 0, 13), )),\
		("Default", -1, ((127, 0, -1), )),\
		(None, -1, ((132, 0, -1), )),\
		(None, -1, ((128, 0, -1), )),\
		("Default", -1, ((131, 0, -1), (129, 0, -1), )),\
		(None, 10, ((130, 0, -1), )),\
		("Default", -1, ((134, 0, -1), )),\
		(None, 10, ((133, 0, -1), )),\
		("Default", -1, ((131, 0, -1), (129, 0, -1), )),\
		("Default", -1, ()),\
		("Default", -1, ())]


	def __init__(self, p, n):
		self.namespace = globals ()
		self.the_player = p
		self.the_npc = n

	def __del__(self):
		oliver = adonthell.gamedata_get_character ("Oliver Redwyne")
		if oliver.get_val ("goto_players_room") == 2:
		    import events
		    events.switch_submap (self.the_player, 12, 5, 3, 1)
		    oliver.set_offset (0, 0)
		    oliver.set_val ("goto_players_room", 3)
		    oliver.set_val ("todo", 0)
		    events.switch_submap (oliver, 12, 5, 4, 0)
		


	def thief (self):
	    if self.the_npc.get_val ("told_about_shair") == 1:
	        return _("responsible to their")
	    else:
	        return _("thief to her")
	
	def your (self):
	    if self.the_npc.get_val ("told_about_shair") == 1:
	        return _("your ")
	    else:
	        return ""
	

