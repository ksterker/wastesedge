class talan_start:
    loop = []
    strings = ["Oh, hullo again, $name.", "Listen, I really am sorry about that fuss at the gate. I hope you will not hold it against me.", "Please, my good man, do not mention it again. I assure you that I hold no grudge against you. Now, if we may go on to the business at hand?", "Oh... that. Yes, how may I help you?", "Hello, Talan. Look, I have a couple questions about the theft.", "Well, can you tell me what happened on the night of the theft?", "Sure, but there is not much to tell. I was out here, making my rounds, walking around the post like always. Later, of course, I heard that Master Fingolson's gems had been stolen and that Lady Silverhair herself was suspected of the theft.", "So you did not see or hear anything out of place that night?", "No... no, not at all.", "If you do not have any more questions...", "No, thank you, I have a lot of work to do. You have been most helpful.", "Well, Alek Endhelm was acting very interested in what Bjarn was doing. Have you noticed him doing anything suspicious?", "Oh, he's a nasty sort, he is, sir. But other than being a busybody, I haven't noticed him doing anything that would lead me to believe that he is the thief.", "Now, if you don't have any more questions...", "I wish you had not lied to me about the night of the theft.", "Wh... what do you mean?", "You were not, as you told me, manning your post the whole night.", "Now you look here! I was, and I do not appreciate you calling me a liar.", "I do not think you are a liar, my friend, but you did lie to me. I know about your singing.", "Oh.", "There is no need to be embarassed about the singing. It would normally be a harmless diversion. However, when you leave your post to practise, it ceases to be harmless. And you did leave your post that night, did you not, Talan?", "Yes, I did. But please do not tell Jelom, sir! He will have my hide for sure if he finds out! Please, I beg you!", "I am afraid that I have no choice. You see, Oliver told me about hearing a strange noise in the stables on that night, and when I talked to Lucia, she said that is was probably just your singing. But now, I rather think that what Oliver heard was something else, and that you missed it because you were off singing.", "I am terribly sorry. I know that I made a terrible mistake now. Please do not tell him!", "I do not know how else to convince him that he has made a mistake. You see, at the time that Oliver heard the noises in the stable, Lady Silverhair was in her room. So the noise that you missed means that she is innocent!", "Oh, please sir, I am so sorry. I did not know about the noise! It is my fault that Lady Silverhair is being held in her room!", "Calm down. It is not your fault. Something strange happened that night, Talan, and I am not sure yet what it was. You not being there was simply an unfortunate coincidence. However, I have no choice but to go to Jelom and try again to convince him of my Lady's innocence. I am sorry.", "I, I understand. I am very sorry, $name...", "And why was Lady Silverhair accused?", "Well, the most obvious reason is of course that she was interested in the gems, and made a trip here just to buy them.", "But she felt the quality of the gems was too low, and she is hardly pressed for money, so why would she turn around and steal the gems?", "Well, according to Jelom, what better way to throw suspicion off yourself then to claim that the stones are of low quality?", "Ah, Jelom said that, did he? What else did he say?", "Who is Jelom? Your boss?", "He is the other guard here. He is not exactly my boss, but he is older than me and has been here much longer, so he is kind of in charge.", "So what else did he have to say about this?", "Well, he also found her behaviour suspicious. I mean, she is all high and mighty, acting above the rest of us, and she obviously doesn't like dwarves...", "Wait, \"obviously doesn't like dwarves\"? To whom is it obvious, you or Jelom?", "To everyone, the way she acted!", "Whatever do you mean?", "Well, the way I heard the story, Bjarn made a point of insulting the entire elven race, loudly and publicly, upon her arrival!", "Well, as I heard it told, she had quite an argument with Master Fingolson in which she insulted the quality of his gems and then the dwarven race!", "Really? And he said nothing to provoke such words? That sounds not at all like her, I must say!", "Well, Master Fingolson can be, um... blunt, I guess, at times, but...", "Ah, I see. So you, or rather, your boss, excuse me, comrade, Jelom, suspect Lady Silverhair for not finding Master Fingolson's merchandise of sufficient quality, and then responding to his, \"bluntness\", as you put it, with some bluntness of her own? This makes her a thief?", "Well, I... ah, perhaps...", "Maybe you should speak to Jelom. He knows more about the theft and his reasons for suspecting her than I do...", "Well, you've talked to Jelom. You know what he thinks...", "And so I shall. Where is he?", "Yes. I do know what he thinks. That, however, does not help me too much.", "He is guarding the hallway leading to Lady Silverhair's room.", "Well, I shall go and talk to him, then. Thank you and good day.", "Ah, $name, hello.", "Hi there, Talan. Look, I...", "No, you did what you had to do, and it was only right that I got in trouble for leaving my post. And I owe you a big favour for covering for me!", "No, I understand. It was because of me shirking my duty that I did not see what happened that night. You had no choice, and I do not hold a grudge against you for doing your duty.", "All the same, I am still sorry for getting you into trouble with Jelom. Thank you for understanding.", "No, it was the least I could do. Do not worry about the favour...", "No, I do owe you. And I know something that might help you clear this whole mess up.", "Really? What might that be?", "Well, I think that something is not right. You see, Master Fingolson is quite a regular here. He comes every other month or so, and usually stays for a week before going back.", "Yes, so Orloth said. What of it?", "Well, the funny thing is, he usually shows up a few days before the client, just to relax, I guess. Until about a year ago, he would spend those few days in the common room, drinking ale and talking with Orloth and his apprentice, Erek.", "Anyway, about a year ago, things changed. When he came, he would still show up a couple of days ahead of the client, but he no longer visited the common room much. He just stayed down in his room. Also, he stopped bringing Erek along when he came here. I assumed that Erek had finished his apprenticeship and moved on.", "This most recent visit is the most unusual of all. You see, Bjarn got here only a day before Lady Silverhair, which was a little strange. What's more, he brought Erek with him this time. I have no idea what is going on, but something just feels odd...", "I see... that is strange. Maybe I had better have another talk with Master Fingolson. Thanks for your help, Talan!", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer2, self.answer4, self.answer5, self.answer7, self.answer8, self.answer11, self.answer12, self.answer14, self.answer16, self.answer18, self.answer20, self.answer22, self.answer24, self.answer26, self.answer28, self.answer30, self.answer32, self.answer33, self.answer35, self.answer37, self.answer39, self.answer40, self.answer42, self.answer44, self.answer45, self.answer48, self.answer53, self.answer57, self.answer59, self.answer61, self.answer62, self.answer63, None]

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
        if the_npc.get_val( "apologised" ) != 1:

            self.color = the_npc.get_color()
            self.npc.append (1)
            self.cont.append (-1)
            the_npc.set_val( "apologised", 1 );

            self.player.append (2)
            self.cont.append (1)
            self.player.append (-1)
        elif quests["demo"].get_val( "silverhair_free" ) != 1:

            self.color = the_npc.get_color()
            self.npc.append (0)
            self.cont.append (-1)
            if quests["demo"].get_val( "know_talan_singing" ) == 1:

                self.player.append (14)
                self.cont.append (8)
            if quests["demo"].get_val( "know_talan_singing" ) != 1:

                self.player.append (4)
                self.cont.append (2)
            self.player.append (-1)
        else:

            self.color = the_npc.get_color()
            self.npc.append (52)
            self.cont.append (-1)
            self.player.append (53)
            self.cont.append (27)
            self.player.append (-1)

    def answer53 (self):
        if quests["demo"].get_val( "told_on_talan" ) != 1:

            self.color = the_npc.get_color()
            self.npc.append (54)
            self.cont.append (-1)
            self.player.append (57)
            self.cont.append (28)
            self.player.append (-1)
        else:

            self.color = the_npc.get_color()
            self.npc.append (55)
            self.cont.append (-1)
            self.player.append (56)
            self.cont.append (-1)
            self.player.append (-1)

    def answer56 (self):
        pass

    def answer57 (self):
        self.color = the_npc.get_color()
        self.npc.append (58)
        self.cont.append (-1)
        self.player.append (59)
        self.cont.append (29)
        self.player.append (-1)

    def answer59 (self):
        self.color = the_npc.get_color()
        self.npc.append (60)
        self.cont.append (-1)
        self.player.append (61)
        self.cont.append (30)
        self.player.append (-1)

    def answer61 (self):
        self.color = the_npc.get_color()
        self.npc.append (62)
        self.cont.append (31)
        self.player.append (-1)

    def answer62 (self):
        self.color = the_npc.get_color()
        self.npc.append (63)
        self.cont.append (32)
        self.player.append (-1)

    def answer63 (self):
        self.color = the_npc.get_color()
        self.npc.append (64)
        self.cont.append (-1)
        self.player.append (65)
        self.cont.append (-1)
        self.player.append (-1)

    def answer65 (self):
        pass

    def answer4 (self):
        self.color = the_npc.get_color()
        self.npc.append (3)
        self.cont.append (-1)
        self.player.append (5)
        self.cont.append (3)
        if quests["demo"].get_val( "know_alek_eavesdrop" ) == 1:

            self.player.append (11)
            self.cont.append (6)
        self.player.append (-1)

    def answer11 (self):
        self.color = the_npc.get_color()
        self.npc.append (12)
        self.cont.append (7)
        self.player.append (-1)

    def answer12 (self):
        self.color = the_npc.get_color()
        self.npc.append (13)
        self.cont.append (-1)
        self.player.append (10)
        self.cont.append (-1)
        self.player.append (5)
        self.cont.append (3)
        self.player.append (-1)

    def answer10 (self):
        pass

    def answer5 (self):
        self.color = the_npc.get_color()
        self.npc.append (6)
        self.cont.append (-1)
        self.player.append (7)
        self.cont.append (4)
        self.player.append (28)
        self.cont.append (15)
        self.player.append (-1)

    def answer28 (self):
        self.color = the_npc.get_color()
        self.npc.append (29)
        self.cont.append (-1)
        self.player.append (30)
        self.cont.append (16)
        self.player.append (-1)

    def answer30 (self):
        self.color = the_npc.get_color()
        self.npc.append (31)
        self.cont.append (-1)
        if quests["demo"].get_val( "know_jelom" ) != 2:
        

            self.player.append (33)
            self.cont.append (18)
        else:

            self.player.append (32)
            self.cont.append (17)
        self.player.append (-1)

    def answer32 (self):
        self.color = the_npc.get_color()
        self.npc.append (36)
        self.cont.append (-1)
        self.player.append (37)
        self.cont.append (20)
        self.player.append (-1)

    def answer37 (self):
        self.color = the_npc.get_color()
        self.npc.append (38)
        self.cont.append (-1)
        if quests["demo"].get_val( "know_bjarns_insult" ) == 1:

            self.player.append (40)
            self.cont.append (22)
        if quests["demo"].get_val( "know_bjarns_insult" ) != 1:

            self.player.append (39)
            self.cont.append (21)
        self.player.append (-1)

    def answer39 (self):
        self.color = the_npc.get_color()
        self.npc.append (41)
        self.cont.append (-1)
        self.player.append (42)
        self.cont.append (23)
        self.player.append (-1)

    def answer42 (self):
        self.color = the_npc.get_color()
        self.npc.append (43)
        self.cont.append (-1)
        self.player.append (44)
        self.cont.append (24)
        self.player.append (-1)

    def answer44 (self):
        self.color = the_npc.get_color()
        self.npc.append (45)
        self.cont.append (25)
        self.player.append (-1)

    def answer45 (self):
        if quests["demo"].get_val( "know_jelom" ) != 2:

            self.color = the_npc.get_color()
            self.npc.append (46)
            self.cont.append (-1)
            self.player.append (48)
            self.cont.append (26)
            self.player.append (-1)
        else:

            self.color = the_npc.get_color()
            self.npc.append (47)
            self.cont.append (-1)
            self.player.append (49)
            self.cont.append (-1)
            self.player.append (-1)

    def answer49 (self):
        pass

    def answer48 (self):
        self.color = the_npc.get_color()
        self.npc.append (50)
        self.cont.append (-1)
        self.player.append (51)
        self.cont.append (-1)
        self.player.append (-1)

    def answer51 (self):
        pass

    def answer40 (self):
        self.color = the_npc.get_color()
        self.npc.append (43)
        self.cont.append (-1)
        self.player.append (44)
        self.cont.append (24)
        self.player.append (-1)

    def answer33 (self):
        self.color = the_npc.get_color()
        self.npc.append (34)
        self.cont.append (-1)
        quests["demo"].set_val( "know_jelom", 1 );

        self.player.append (35)
        self.cont.append (19)
        self.player.append (-1)

    def answer35 (self):
        self.color = the_npc.get_color()
        self.npc.append (36)
        self.cont.append (-1)
        self.player.append (37)
        self.cont.append (20)
        self.player.append (-1)

    def answer7 (self):
        self.color = the_npc.get_color()
        self.npc.append (8)
        self.cont.append (5)
        self.player.append (-1)

    def answer8 (self):
        self.color = the_npc.get_color()
        self.npc.append (9)
        self.cont.append (-1)
        self.player.append (28)
        self.cont.append (15)
        self.player.append (10)
        self.cont.append (-1)
        if quests["demo"].get_val( "know_alek_eavesdrop" ) == 1:

            self.player.append (11)
            self.cont.append (6)
        self.player.append (-1)

    def answer14 (self):
        self.color = the_npc.get_color()
        self.npc.append (15)
        self.cont.append (-1)
        self.player.append (16)
        self.cont.append (9)
        self.player.append (-1)

    def answer16 (self):
        self.color = the_npc.get_color()
        self.npc.append (17)
        self.cont.append (-1)
        self.player.append (18)
        self.cont.append (10)
        self.player.append (-1)

    def answer18 (self):
        self.color = the_npc.get_color()
        self.npc.append (19)
        self.cont.append (-1)
        self.player.append (20)
        self.cont.append (11)
        self.player.append (-1)

    def answer20 (self):
        self.color = the_npc.get_color()
        self.npc.append (21)
        self.cont.append (-1)
        self.player.append (22)
        self.cont.append (12)
        self.player.append (-1)

    def answer22 (self):
        self.color = the_npc.get_color()
        self.npc.append (23)
        self.cont.append (-1)
        self.player.append (24)
        self.cont.append (13)
        self.player.append (-1)

    def answer24 (self):
        self.color = the_npc.get_color()
        self.npc.append (25)
        self.cont.append (-1)
        self.player.append (26)
        self.cont.append (14)
        self.player.append (-1)

    def answer26 (self):
        self.color = the_npc.get_color()
        self.npc.append (27)
        self.cont.append (-1)
        self.player.append (-1)

    def answer2 (self):
        self.color = the_npc.get_color()
        self.npc.append (3)
        self.cont.append (-1)
        self.player.append (5)
        self.cont.append (3)
        if quests["demo"].get_val( "know_alek_eavesdrop" ) == 1:

            self.player.append (11)
            self.cont.append (6)
        self.player.append (-1)
