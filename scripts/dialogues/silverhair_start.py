import adonthell

class silverhair_start:
	loop = []
	strings = ["Oh!!", "$name, have you found anything yet?  This confinement is intolerable, as you may well understand.", "Mistress!  Mistress!  $name has come!", "Yes, yes dear, I see him.  Please calm yourself.  $name, I am relieved to see you.  This situation has clearly gone beyond any civil control.", "That is certain, my lady.  I am told you are suspected of theft.", "Theft indeed, and theft most grave. This Fingolson may be uncouth, but he bears considerable influence. A theft from him would have dire consequences indeed. But you know I could not have done this thing.", "Of course.  Theft is not in you, my Lady, nor is deceipt.  But these folk have not my confidence in you.  I fear that there is no one who will speak for your honour among them.", "I see.  Then it falls to you, $name, as my sole friend in this outpost, to make certain my name is clear of any stain.  May I trust you to do this for me?", "Of course, my Lady.  You may trust me to the end of the world.  What little I may do is yours to command.", "What do you know of Fingolson, Lady?  I have not met him before.", "Be glad of that, he is an uncouth lout at best. I should have known better than to deal fairly with such a rough and uncultured beast.", "I thank you for that.  Now you must go, lest they find you here and imprison you as well.  Free, you are my hope.", "I will try to be worthy of your trust, Lady.  I will return once I know more.", "Of course, Lady.  I have believed nothing but your innocense since I arrived.  You may trust me to act on your behalf.", "I understand, Lady.  Please be patient.", "I have little choice.  Do you have news?  Or questions?", "News?  I must disappoint you, Lady.  I have none.  I simply wished to know if there was anything you need.", "You must go.  The human at the door may not hear as well as you or I, but he hears well enough.  Leave before he discovers you.", "I am curious, Lady.  What of that figurine there?  I do not recall it.", "The Yeti?  I bought that upon arriving here.  From a young lady of your breed, it was.", "The artist, then?  I must speak more with her.  I had not known you had been together.", "She is a very intelligent woman, and regards the Yeti highly.  Do not take her lightly.", "$name!  Thank the Powers!", "I have spoken with the artist, Frostbloom. She mentioned that she had heard some strange sounds in the night, when the theft must have taken place. Did you hear anything?", "Lady, could you tell me more about the argument you had with the Dwarf?  It may be helpful.", "It is kind of you to ask.  Indeed my possessions, other than what you see, have been taken from me.  They are kept in the pantry below.", "Do you wish me to retrieve them for you, Lady?", "No, that would not be wise.  I have an item I need, but to fetch it now would be to invite trouble.  Better we wait.", "Very well, Lady.  I am yours to command.", "So I gathered.  I will do my best, Lady.", "In the night...? Yes.  Yes, I do recall a sound in the night.  How could I have forgotten such a thing?", "This may be important to your freedom.  What are you able to tell me of it?", "Little, I'm afraid.  I know it was a voice, of that I am certain.  But whose voice I was not able to tell, nor what was said.", "Then it must have been someone about after the theft.  Perhaps the thief itself.  Do you remember anything else?", "Are you certain you cannot recall the voice?  It would be helpful to the extreme if we could match a name to it.", "She thinks for a moment, here eyes distant.", "No, I am sorry.  The nature of the voice is a mystery to me still.", "Very little, I'm afraid.  Only that it seemed to come from a distance.  Past the wall, perhaps.  In the direction of the stables.", "The lady looks anxiously at the door.", "Argument?  An insult, it was.  That foul creature had the audacity to accuse me of ignorance!", "Ignorance?  But you are highly educated, Lady.  Anyone could see that.", "Not this beast.  He attempted to sell inferior gems to me, pretending that they were of a high grade.  As if I was nothing more than a child who could not tell one stone from another.", "You know it is my intent to enchant these stones.  Else why would I trek this far?  Awful stones like his would shatter in an instant.", "Yes, that's true.  When we set out, you told me of your intent.", "That rough animal! He went so far as to claim that I not only did not know the value of the stone, but that I hardly knew one gem from another! If I could have destroyed the filth on the spot, I certainly would have!", "Silverhair's eyes flash with remembered anger, but a scuffing sound by the door distracts her and her anger drains as suddenly as it rose.", "My Lady, I am glad to see you.  You will be free soon, I know it.", "I would ask a boon from you, now that it is safe.  I have personal articles that I need, but are kept with our packs.  I'm sure you know which articles I mean.", "Of course, Lady.  That would be the least I could do after what you have endured.  Rest assured, I will be back shortly.", "$name, you have come back so soon?  But where are the articles I asked for?", "I have yet to retrieve them, Lady.", "Then please do so at once.  I have been without them for too long.", "Very well, Lady.", "Returned already?  But what is this?", "A stone I found in the cellar, among your chests.  I hate to think such a thing, but is this one of the jewels that the Dwarf has lost?", "You show the jewel to Lady Silverhair, who frowns upon seeing it.  She inspects it more closely, but carefully avoids touching it.  She straightens then, a puzzled look on her features.", "You say this was found among my goods?  But this is not a stone of mine, and neither is it the stone I was shown before.  I have never seen this before.", "But is this not one of the Catseyes he claims to have lost?", "It cannot be. For this is no Catseye at all, and in fact is hardly worth a fraction of the other stones.", "I do not understand this at all.", "I admit he goaded me to rage earlier, to my shame. But I have done nothing more than voice my anger. You must believe that.", "And where are the packs kept, Lady?", "You will find them below, in the pantry.", ""]

	def set_name (self, new_name):
		pass

	def set_npc (self, new_npc):
		pass

	def set_portrait (self, new_portrait):
		pass

	def __init__(self, p, n):
		self.the_player = p
		self.the_npc = n

		self.dialogue = [self.start, self.answer2, self.answer4, self.answer6, self.answer8, self.answer9, self.answer10, self.answer13, self.answer14, self.answer16, self.answer18, self.answer20, self.answer23, self.answer24, self.answer26, self.answer28, self.answer29, self.answer31, self.answer33, self.answer34, self.answer35, self.answer37, self.answer38, self.answer40, self.answer41, self.answer43, self.answer44, self.answer45, self.answer46, self.answer50, self.answer54, self.answer55, self.answer57, self.answer58, self.answer61, None]

	def clear (self):
		del self.dialogue

	def __getattr__ (self, name):
		return 0

	def run (self, answer):
		self.npc = []
		self.player = []
		self.cont = []
		self.dialogue[answer]()

	def start (self):
		if self.the_npc.get_val ("talked_to") == 0:

			self.set_npc ("Janesta Skywind")
			self.color = adonthell.gamedata_get_character("Janesta Skywind").get_color()
			self.npc.append (0)
			self.cont.append (-1)
			self.the_npc.set_val ("talked_to" , 1)

			self.player.append (2)
			self.cont.append (1)
			self.player.append (-1)
		elif adonthell.gamedata_get_quest("demo").get_val ("silverhair_free") != 1:

			self.set_npc ("Imoen Silverhair")
			self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
			self.npc.append (1)
			self.cont.append (-1)
			self.player.append (14)
			self.cont.append (8)
			self.player.append (-1)
		elif adonthell.gamedata_get_quest("demo").get_val ("get_item") == 0:

			self.set_npc ("Imoen Silverhair")
			self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
			self.npc.append (22)
			self.cont.append (-1)
			adonthell.gamedata_get_quest("demo").set_val ("get_item" , 1)

			self.player.append (46)
			self.cont.append (28)
			self.player.append (-1)
		elif adonthell.gamedata_get_quest("demo").get_val ("have_gem") == 1:

			self.color = self.the_npc.get_color()
			self.npc.append (53)
			self.cont.append (-1)
			adonthell.gamedata_get_quest("demo").set_val ("gem_worthless" , adonthell.gamedata_get_quest("demo").get_val ("gem_worthless") | 1)
			
			

			self.player.append (54)
			self.cont.append (30)
			self.player.append (-1)
		else:

			self.color = self.the_npc.get_color()
			self.npc.append (49)
			self.cont.append (-1)
			self.player.append (50)
			self.cont.append (29)
			self.player.append (-1)

	def answer50 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (51)
		self.cont.append (-1)
		self.player.append (52)
		self.cont.append (-1)
		self.player.append (-1)

	def answer52 (self):
		pass

	def answer54 (self):
		self.color = 0
		self.npc.append (55)
		self.cont.append (31)
		self.player.append (-1)

	def answer55 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (56)
		self.cont.append (-1)
		self.player.append (57)
		self.cont.append (32)
		self.player.append (-1)

	def answer57 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (58)
		self.cont.append (33)
		self.player.append (-1)

	def answer58 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (59)
		self.cont.append (-1)
		self.player.append (-1)

	def answer46 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (47)
		self.cont.append (-1)
		self.player.append (61)
		self.cont.append (34)
		self.player.append (48)
		self.cont.append (-1)
		self.player.append (-1)

	def answer48 (self):
		pass

	def answer61 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (62)
		self.cont.append (-1)
		self.player.append (-1)

	def answer14 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (15)
		self.cont.append (-1)
		self.player.append (16)
		self.cont.append (9)
		if adonthell.gamedata_get_quest("demo").get_val ("know_argument") == 1:

			self.player.append (24)
			self.cont.append (13)
		if adonthell.gamedata_get_quest("demo").get_val ("know_noise") & 2 == 2:

			self.player.append (23)
			self.cont.append (12)
		if adonthell.gamedata_get_quest("demo").get_val ("talked_about_yeti") == 0 and adonthell.gamedata_get_quest("demo").get_val ("know_frostbloom") == 1:

			self.player.append (18)
			self.cont.append (10)
		self.player.append (-1)

	def answer18 (self):
		adonthell.gamedata_get_quest("demo").set_val ("talked_about_yeti" , 1)

		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (19)
		self.cont.append (-1)
		self.player.append (20)
		self.cont.append (11)
		self.player.append (-1)

	def answer20 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = self.the_npc.get_color()
		self.npc.append (21)
		self.cont.append (-1)
		self.player.append (29)
		self.cont.append (16)
		self.player.append (-1)

	def answer29 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (-1)

	def answer23 (self):
		adonthell.gamedata_get_quest("demo").set_val ("know_noise" , adonthell.gamedata_get_quest("demo").get_val ("know_noise") | 1 )

		self.set_npc (self.the_npc.get_id())
		self.color = self.the_npc.get_color()
		self.npc.append (30)
		self.cont.append (-1)
		self.player.append (31)
		self.cont.append (17)
		self.player.append (-1)

	def answer31 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (32)
		self.cont.append (-1)
		self.player.append (33)
		self.cont.append (18)
		self.player.append (34)
		self.cont.append (19)
		self.player.append (-1)

	def answer34 (self):
		self.color = 0
		self.npc.append (35)
		self.cont.append (20)
		self.player.append (-1)

	def answer35 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (36)
		self.cont.append (-1)
		self.player.append (33)
		self.cont.append (18)
		self.player.append (-1)

	def answer33 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (37)
		self.cont.append (21)
		self.player.append (-1)

	def answer37 (self):
		self.color = 0
		self.npc.append (38)
		self.cont.append (22)
		self.player.append (-1)

	def answer38 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (-1)

	def answer24 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (39)
		self.cont.append (-1)
		self.player.append (40)
		self.cont.append (23)
		self.player.append (-1)

	def answer40 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = self.the_npc.get_color()
		self.npc.append (41)
		self.cont.append (24)
		self.player.append (-1)

	def answer41 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (42)
		self.cont.append (-1)
		self.player.append (43)
		self.cont.append (25)
		self.player.append (-1)

	def answer43 (self):
		self.color = self.the_npc.get_color()
		self.npc.append (44)
		self.cont.append (26)
		self.player.append (-1)

	def answer44 (self):
		self.color = 0
		self.npc.append (45)
		self.cont.append (27)
		self.player.append (-1)

	def answer45 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (-1)

	def answer16 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (25)
		self.cont.append (-1)
		self.player.append (26)
		self.cont.append (14)
		self.player.append (-1)

	def answer26 (self):
		self.set_npc (self.the_npc.get_id())
		self.color = self.the_npc.get_color()
		self.npc.append (27)
		self.cont.append (-1)
		self.player.append (28)
		self.cont.append (15)
		self.player.append (-1)

	def answer28 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (17)
		self.cont.append (-1)
		self.player.append (-1)

	def answer2 (self):
		self.set_npc ("Imoen Silverhair")
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (3)
		self.cont.append (-1)
		self.player.append (4)
		self.cont.append (2)
		self.player.append (-1)

	def answer4 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (5)
		self.cont.append (-1)
		self.player.append (6)
		self.cont.append (3)
		self.player.append (9)
		self.cont.append (5)
		self.player.append (-1)

	def answer9 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (10)
		self.cont.append (6)
		self.player.append (-1)

	def answer10 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (60)
		self.cont.append (-1)
		self.player.append (13)
		self.cont.append (7)
		self.player.append (-1)

	def answer13 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (-1)
		self.player.append (-1)

	def answer12 (self):
		pass

	def answer6 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (7)
		self.cont.append (-1)
		self.player.append (8)
		self.cont.append (4)
		self.player.append (-1)

	def answer8 (self):
		self.color = adonthell.gamedata_get_character("Imoen Silverhair").get_color()
		self.npc.append (11)
		self.cont.append (-1)
		self.player.append (12)
		self.cont.append (-1)
		self.player.append (-1)
