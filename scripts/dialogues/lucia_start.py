class lucia_start:
    loop = []
    strings = ["There is little doubt that this busy-looking woman is the unchallenged mistress of the Redwyne household. As she spots you, a look of resignation flashes across her face.", "You young people never learn to keep out of my kitchen, do you?", "Sorry madam, I did not mean to trespass, but I need to talk to you.", "I have no time for this, woman! I have some questions for you.", "What questions? Don't you see I'm busy? Who's going to put the food on the table, if I'm going to chat with you? Now out of my eyes you go!", "My apologies. Must have been the wrong door ...", "Calm down, please. It's important. I'm investigating the theft.", "It's always the same. No day I can do my work without interruptions. But you won't hear me complaining. So what is it you want?", "I am $name, Lady Silverhairs clerk. I'm investigating the theft.", "The Elven Lady you say? Then you must be from Cirdanth, ain't you?", "Yes I am from there.", "Listen madam ...", "Ah, the city. What would I give to live there! But no, Orloth had to buy the inn from his scoundrel brother. The deal of his life he said!", "Do you? Oh what an awful thing to happen! But I'm not surprised. Out here, in the middle of nowhere, something like this was bound to happen one day.", "I told Orloth. \"If you're going to buy this inn, you'll end up in trouble\", I said. But would he listen to me?", "Sorry to interrupt, but have you noticed something odd during the night of the theft?", "Something unusual? How should I? We're sleeping under the roof, whereas poor Master Fingolson has his room downstairs, in the cellar. Just as his kind likes it the most.", "He is such a regular and welcome guest, and of all people he gets robbed in our house. What a shame!", "So you know Fingolson?", "The Dwarf, madam! Do you know him?", "In Cirdanth that wouldn't have happened. And even if it had, there would be proper guards to track the thief down. But whom do I tell? Surely, you are from Cirdanth, ain't you?", "What about the guards here?", "He stays here quite often, and that for many years. I wouldn't say that I know him well, though. He behaves quite retained and formal, but he is a pleasant character. Not like the other types we get here usually.", "Oh, you mean Jhelom and Talan. They are good men, no doubt. Their task is to keep the piece, and usually they are well up to it.", "My name is $name. I am investigating the theft.", "You should have said so! It is about time that something is going to happen. I tell you, in Cirdanth, everything would have been solved by now.", "But here, in the middle of nowhere, they hold an Elven Lady responsible and nobody seems interested in finding poor Master Fingolson's gems.", "I am Lady Silverhair's clerk madam, and I'm going to find the real thief, if you'd only let me ask you some questions!", "Then you are from Cirdanth? What would I give to live there! But no! Orloth has to buy the inn from his scoundrel brother. As if it'd bring him anything but trouble.", "True, Waste's Edge is quite a remote place, but ...", "Could we perhaps return to more pressing matters?", "Just take a look at that mercenary. What a dreadful man! You wouldn't find people like him in the city!", "What about the guards you have here?", "Oh forgive me. Orloth always says I'm talking too much, but actually, he never keeps his mouth shut. He always denies when I tell him, but I'm sure you have noticed yourself.", "Now don't keep me off my work. Ask what you want to know and then out with you!", "Yes, madam. Have you noticed anything unusual in the night of the theft?", "Remote!? The edge of the world couldn't be more remote! Mind you, I'm not complaining. It's just ... -", "All these filthy types we get here. Like that Endhelm fellow. I don't think you'd meet people like him in Cirdanth.", "What about him? Do you think he is involved into the theft?", "Oh, forgive me. I am sure you have more important things on your mind than listening to the sorrows of a woman.", "But perhaps you should ask Talan, as he was on duty that night. If somebody has noticed something, then it was him.", "You said Master Fingolson is a regular guest. What can you tell me about him?", "I was wondering whether you noticed anything unusual during the night of the theft.", "How should I know? But he does look suspicious to me. More than any others of our guests.", "Can you tell me a little more about them?", "Well, you were very ... helpful, madam. But if you'll excuse me now, I've got a thief to catch.", "I am afraid there is only little I know about him. He is such retained and formal, a calm and pleasant character. But he stays here regularly.", "Which is no surprise; much of the trade with the mines of Uzdun'kal is done here, and Master Fingolson is one of the few tradesmen the Dwarfs have.", "I didn't know that much trade with the Dwarfs runs through Waste's Edge.", "Lunch can wait, but if you don't help my investigations, the thief might get away!", "You are looking for the thief!? My apologies then, sir. It is about time that somebody takes an interest into this unlucky incident.", "Can you imagine they are suspecting the fair Lady Silverhair!? And bad types like that dreadful Endhelm are walking around unnoticed.", "I say, in a city like Cirdanth the true thief would have been tracked down by now. But out here, in the middle of nowhere, law and order are just hollow phrases.", "Rest assured that I will find out the truth, madam. But to do so I have to know whether you have noticed anything unusual during the night of the theft.", "I fear I haven't. See, our rooms are under the roof, while Master Fingolson sleeps below ground, like his kind is used to. Any noise hearable in our chamber would have woken up the whole house.", "But as far as I know, nobody has heard anything suspicious. It is really a shame, theft beneath our roof. And of all people, the good Master Fingolson is the victim.", "So you know the Dwarf well?", "I hardly get out of the kitchen during the day. Best you talk to my husband. He usually knows more about people than they know themselves.", "But a situation like this exceeds their abilities. Not that I'd blame them. Convicting this thief is no job for simple people. I hope you understand, sir.", "We're days from the next settlement out here. Were it not for all the trade passing through we couldn't even buy the most basic things to live.", "Although without the trade, Waste's Edge wouldn't even exist and we might run an Inn in Cirdanth instead. But as long as the mines of Uzdun'kal are open, there is no chance to get Orloth away from here.", "The easiest road to the mines runs past our gates. In the summer months. when the passes are open it is also possible to cross the mountains northwards and follow the shore of the Ayrithmere to the middle plains.", "But the big caravans come our way and either turn north here, towards Elgilad and the human cities, or follow the Elenstroem down to Cirdanth. But few Dwarves go further than Waste's Edge, so if you want to buy from them directly, you have to come here.", "But enough with chatting. This food won't prepare itself, and you still have a thief to catch.", "Just done blame him, if he hasn't, sir. He is a good lad and I don't want any harm coming to him.", "Don't worry, madam. I won't trouble the guards more than they deserve.", "I am relieved to hear that. But if you'll excuse me now. I have to prepare the food, and you still have your thief to catch.", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer0, self.answer2, self.answer3, self.answer6, self.answer8, self.answer10, self.answer11, self.answer13, self.answer15, self.answer16, self.answer18, self.answer19, self.answer21, self.answer22, self.answer23, self.answer24, self.answer25, self.answer27, self.answer29, self.answer30, self.answer32, self.answer33, self.answer35, self.answer36, self.answer38, self.answer40, self.answer41, self.answer42, self.answer44, self.answer46, self.answer48, self.answer49, self.answer50, self.answer53, self.answer54, self.answer56, self.answer57, self.answer59, self.answer61, self.answer62, self.answer65, None]

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
        self.color = 0
        self.npc.append (0)
        self.cont.append (1)
        self.player.append (-1)

    def answer0 (self):
        self.color = the_npc.get_color()
        self.npc.append (1)
        self.cont.append (-1)
        self.player.append (2)
        self.cont.append (2)
        self.player.append (3)
        self.cont.append (3)
        self.player.append (5)
        self.cont.append (-1)
        self.player.append (-1)

    def answer5 (self):
        pass

    def answer3 (self):
        self.color = the_npc.get_color()
        self.npc.append (4)
        self.cont.append (-1)
        self.player.append (6)
        self.cont.append (4)
        self.player.append (49)
        self.cont.append (32)
        self.player.append (-1)

    def answer49 (self):
        self.color = the_npc.get_color()
        self.npc.append (50)
        self.cont.append (33)
        self.player.append (-1)

    def answer50 (self):
        self.color = the_npc.get_color()
        self.npc.append (51)
        self.cont.append (-1)
        self.player.append (27)
        self.cont.append (18)
        self.player.append (38)
        self.cont.append (25)
        self.player.append (-1)
        self.color = the_npc.get_color()
        self.npc.append (52)
        self.cont.append (-1)
        self.player.append (53)
        self.cont.append (34)
        self.player.append (32)
        self.cont.append (21)
        self.player.append (-1)

    def answer32 (self):
        self.color = the_npc.get_color()
        self.npc.append (23)
        self.cont.append (15)
        self.player.append (-1)

    def answer23 (self):
        self.color = the_npc.get_color()
        self.npc.append (58)
        self.cont.append (-1)
        self.player.append (65)
        self.cont.append (41)
        self.player.append (-1)

    def answer65 (self):
        self.color = the_npc.get_color()
        self.npc.append (66)
        self.cont.append (-1)
        self.player.append (-1)

    def answer53 (self):
        self.color = the_npc.get_color()
        self.npc.append (54)
        self.cont.append (35)
        self.player.append (-1)

    def answer54 (self):
        self.color = the_npc.get_color()
        self.npc.append (55)
        self.cont.append (-1)
        self.player.append (56)
        self.cont.append (36)
        self.player.append (-1)

    def answer56 (self):
        self.color = the_npc.get_color()
        self.npc.append (22)
        self.cont.append (14)
        self.player.append (-1)

    def answer22 (self):
        self.color = the_npc.get_color()
        self.npc.append (31)
        self.cont.append (-1)
        self.player.append (38)
        self.cont.append (25)
        self.player.append (-1)

    def answer38 (self):
        self.color = the_npc.get_color()
        self.npc.append (43)
        self.cont.append (-1)
        self.player.append (44)
        self.cont.append (29)
        self.player.append (45)
        self.cont.append (-1)
        self.player.append (-1)

    def answer45 (self):
        pass

    def answer44 (self):
        self.color = the_npc.get_color()
        self.npc.append (57)
        self.cont.append (37)
        self.player.append (-1)

    def answer57 (self):
        self.color = the_npc.get_color()
        self.npc.append (63)
        self.cont.append (-1)
        self.player.append (-1)

    def answer27 (self):
        self.color = the_npc.get_color()
        self.npc.append (28)
        self.cont.append (-1)
        self.player.append (29)
        self.cont.append (19)
        self.player.append (30)
        self.cont.append (20)
        self.player.append (-1)
        self.color = the_npc.get_color()
        self.npc.append (33)
        self.cont.append (22)
        self.player.append (-1)
        if self.talked_about_fingolson == 1:

            self.color = the_npc.get_color()
            self.npc.append (17)
            self.cont.append (-1)
            self.player.append (18)
            self.cont.append (11)
            self.player.append (-1)

    def answer18 (self):
        self.color = the_npc.get_color()
        self.npc.append (20)
        self.cont.append (-1)
        self.asked_about_theft = 1

        self.player.append (10)
        self.cont.append (6)
        self.player.append (19)
        self.cont.append (12)
        self.player.append (21)
        self.cont.append (13)
        self.player.append (-1)
        self.color = the_npc.get_color()
        self.npc.append (22)
        self.cont.append (14)
        self.player.append (-1)

    def answer21 (self):
        self.color = the_npc.get_color()
        self.npc.append (23)
        self.cont.append (15)
        self.player.append (-1)

    def answer19 (self):
        self.color = the_npc.get_color()
        self.npc.append (22)
        self.cont.append (14)
        self.player.append (-1)

    def answer10 (self):
        self.color = the_npc.get_color()
        self.npc.append (12)
        self.cont.append (-1)
        self.player.append (29)
        self.cont.append (19)
        self.player.append (30)
        self.cont.append (20)
        self.player.append (-1)

    def answer33 (self):
        self.color = the_npc.get_color()
        self.npc.append (34)
        self.cont.append (-1)
        self.player.append (35)
        self.cont.append (23)
        self.player.append (-1)

    def answer35 (self):
        self.color = the_npc.get_color()
        self.npc.append (16)
        self.cont.append (10)
        self.talked_about_fingolson = 1

        self.player.append (-1)

    def answer16 (self):
        self.color = the_npc.get_color()
        self.npc.append (40)
        self.cont.append (26)
        self.player.append (-1)
        if self.talked_about_fingolson == 1:

            self.color = the_npc.get_color()
            self.npc.append (17)
            self.cont.append (-1)
            self.player.append (18)
            self.cont.append (11)
            self.player.append (-1)

    def answer40 (self):
        self.color = the_npc.get_color()
        self.npc.append (64)
        self.cont.append (-1)
        self.player.append (65)
        self.cont.append (41)
        self.player.append (-1)

    def answer30 (self):
        self.color = the_npc.get_color()
        self.npc.append (39)
        self.cont.append (-1)
        if self.asked_about_theft == 1:

            self.player.append (41)
            self.cont.append (27)
        else:

            self.player.append (42)
            self.cont.append (28)
        self.player.append (-1)

    def answer42 (self):
        self.color = the_npc.get_color()
        self.npc.append (54)
        self.cont.append (35)
        self.player.append (-1)

    def answer41 (self):
        self.color = the_npc.get_color()
        self.npc.append (46)
        self.cont.append (30)
        self.player.append (-1)

    def answer46 (self):
        self.color = the_npc.get_color()
        self.npc.append (47)
        self.cont.append (-1)
        self.player.append (48)
        self.cont.append (31)
        self.player.append (45)
        self.cont.append (-1)
        self.player.append (-1)

    def answer48 (self):
        self.color = the_npc.get_color()
        self.npc.append (61)
        self.cont.append (39)
        self.player.append (-1)

    def answer61 (self):
        self.color = the_npc.get_color()
        self.npc.append (62)
        self.cont.append (40)
        self.player.append (-1)

    def answer62 (self):
        self.color = the_npc.get_color()
        self.npc.append (63)
        self.cont.append (-1)
        self.player.append (-1)

    def answer29 (self):
        self.color = the_npc.get_color()
        self.npc.append (36)
        self.cont.append (24)
        self.player.append (-1)

    def answer36 (self):
        self.color = the_npc.get_color()
        self.npc.append (37)
        self.cont.append (-1)
        self.player.append (38)
        self.cont.append (25)
        self.player.append (-1)
        self.color = the_npc.get_color()
        self.npc.append (59)
        self.cont.append (38)
        self.player.append (-1)

    def answer59 (self):
        self.color = the_npc.get_color()
        self.npc.append (60)
        self.cont.append (-1)
        self.player.append (45)
        self.cont.append (-1)
        self.player.append (48)
        self.cont.append (31)
        self.player.append (-1)

    def answer6 (self):
        self.color = the_npc.get_color()
        self.npc.append (25)
        self.cont.append (17)
        self.player.append (-1)

    def answer25 (self):
        self.color = the_npc.get_color()
        self.npc.append (26)
        self.cont.append (-1)
        self.talked_about_fingolson = 1

        self.player.append (27)
        self.cont.append (18)
        self.player.append (32)
        self.cont.append (21)
        self.player.append (-1)

    def answer2 (self):
        self.color = the_npc.get_color()
        self.npc.append (7)
        self.cont.append (-1)
        self.player.append (8)
        self.cont.append (5)
        self.player.append (24)
        self.cont.append (16)
        self.player.append (-1)

    def answer24 (self):
        self.color = the_npc.get_color()
        self.npc.append (25)
        self.cont.append (17)
        self.player.append (-1)

    def answer8 (self):
        self.color = the_npc.get_color()
        self.npc.append (9)
        self.cont.append (-1)
        self.player.append (10)
        self.cont.append (6)
        self.player.append (11)
        self.cont.append (7)
        self.player.append (-1)
        self.color = the_npc.get_color()
        self.npc.append (13)
        self.cont.append (8)
        self.player.append (-1)

    def answer13 (self):
        self.color = the_npc.get_color()
        self.npc.append (14)
        self.cont.append (-1)
        self.player.append (15)
        self.cont.append (9)
        self.player.append (-1)

    def answer15 (self):
        self.color = the_npc.get_color()
        self.npc.append (16)
        self.cont.append (10)
        self.talked_about_fingolson = 1

        self.player.append (-1)

    def answer11 (self):
        self.color = the_npc.get_color()
        self.npc.append (12)
        self.cont.append (-1)
        self.player.append (29)
        self.cont.append (19)
        self.player.append (30)
        self.cont.append (20)
        self.player.append (-1)
