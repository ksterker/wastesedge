class jelom_start:
    loop = []
    strings = ["Halt there! No-one is allowed into the prisoner's room!", "Stop right there, half-elf! You know that you are not allowed in there!", "No-one is allowed into the prisoner's room, so please leave this hallway!", "You again, half-elf? What do you want this time?", "Ah, you must be Jelom. Talan told me that I could find you here.", "And just who are you to prevent me from entering, sir?", "Nice to see you again, Jelom. Look, I have some more questions for you.", "Look, Jelom, I found out something that will cast some serious doubt on Lady Silverhair having committed the theft!", "My name is Jelom, and I am the chief of the guard at Waste's Edge! Who the hell are you?", "Who are you, and why were you looking for me?", "My name is $name, and I am here to investigate the theft. And I have a few questions for you regarding the incident.", "And what might those questions be, half-elf?", "I doubt that, but since I won't get any peace from your pestering until you tell me, go ahead.", "On the night of the theft, Talan was standing guard near the stables, correct?", "Yeah, so what?", "Well, when I talked to the stableboy, Oliver, he told me that he heard a noise late in the stables. He heard this noise well after both Bjarn and Lady Silverhair had gone to their rooms, so someone else was out and about that night, and it was not her.", "The overactive imagination of some little kid hardly changes anything!", "By itself, I admit, it does not. I myself was not sure to believe it or not, so I asked Talan, who did not hear anything.", "You see! I take the word of my own guard over Oliver's!", "The reason, however, that Talan did not hear anything that night, was that he was not at his post.", "What do you mean? Why do you think that?", "Because he admitted it.", "Just what did he admit?", "That he had sneaked away to take a nap.", "That he had sneaked off to practise singing, of all things!", "A nap? I knew it! I had suspected that he caught some shuteye on duty from time to time, but have never caught him at it! He is in big trouble, this time!", "Singing? What, does the fool want to be a bard now? He is in big trouble now!", "Well, regardless of what you do to him, you have to admit that it is highly likely that someone was out and about last night, and that someone was not Lady Silverhair. This casts more than a little doubt on your conviction that she is the thief!", "You are right, half-elf. Something strange is going on.", "Will you please allow me to speak to Lady Silverhair now? She may be able to tell me something that will help me, er, us, to catch the real thief.", "Yes, I suppose I will let you in.", "Erek actually packed the gems, according to Alek. Do you think he could be mixed up in this?", "Alek Endhelm was eavesdropping outside the room during the negotiations, according to Erek. Do you think he could be mixed up in this?", "Erek? Come on, don't be stupid. You are a more likely thief than Erek, and you weren't even here! It is just like Alek to tell you things like that!", "Why do you say that?", "Don't get excited, half-elf. Alek looks like scum, and probably is, being a mercenary, but there is no reason to suspect him of the theft. In fact, I hear that he offered his services to Bjarn as a guard.", "You don't think that is a little suspicious?", "Look, half-elf, I am getting pretty damn tired of you and your questions. This investigation has nothing to do with you, so why don't you keep your nose out of it? Now get the hell out of here!", "Can you tell me what happened on the night of the theft?", "No, I can't. Talan was on guard duty. Go bother him.", "You won't tell me anything about your own investigation, then?", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer4, self.answer5, self.answer6, self.answer7, self.answer10, self.answer13, self.answer15, self.answer17, self.answer19, self.answer21, self.answer23, self.answer24, self.answer27, self.answer29, self.answer31, self.answer32, self.answer34, self.answer36, self.answer38, self.answer40, None]

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
        if the_player.get_val ("at_silverhairs_door") == 1 and quests["demo"].get_val ("know_jelom") != 2:
        

            self.color = the_npc.get_color()
            self.npc.append (0)
            self.cont.append (-1)
            if quests["demo"].get_val( "know_jelom" ) == 1:

                self.player.append (4)
                self.cont.append (1)
            else:

                self.player.append (5)
                self.cont.append (2)
            self.player.append (-1)
        elif the_player.get_val( "at_silverhairs_door" ) == 1:

            self.color = the_npc.get_color()
            self.npc.append (1)
            self.cont.append (-1)
            if quests["demo"].get_val ("know_talan_singing") != 2:

                self.player.append (6)
                self.cont.append (3)
            elif quests["demo"].get_val ("know_talan_singing") == 2:

                self.player.append (7)
                self.cont.append (4)
            self.player.append (-1)
        elif the_player.get_val ("at_silverhairs_door") != 1 and quests["demo"].get_val ("know_jelom") != 2:

            self.color = the_npc.get_color()
            self.npc.append (2)
            self.cont.append (-1)
            if quests["demo"].get_val( "know_jelom" ) == 1:

                self.player.append (4)
                self.cont.append (1)
            else:

                self.player.append (5)
                self.cont.append (2)
            self.player.append (-1)
        else:
        

            self.color = the_npc.get_color()
            self.npc.append (3)
            self.cont.append (-1)
            if quests["demo"].get_val ("know_talan_singing") != 2:

                self.player.append (6)
                self.cont.append (3)
            elif quests["demo"].get_val ("know_talan_singing") == 2:

                self.player.append (7)
                self.cont.append (4)
            self.player.append (-1)

    def answer7 (self):
        self.color = the_npc.get_color()
        self.npc.append (12)
        self.cont.append (-1)
        self.player.append (13)
        self.cont.append (6)
        self.player.append (-1)

    def answer13 (self):
        self.color = the_npc.get_color()
        self.npc.append (14)
        self.cont.append (-1)
        self.player.append (15)
        self.cont.append (7)
        self.player.append (-1)

    def answer15 (self):
        self.color = the_npc.get_color()
        self.npc.append (16)
        self.cont.append (-1)
        self.player.append (17)
        self.cont.append (8)
        self.player.append (-1)

    def answer17 (self):
        self.color = the_npc.get_color()
        self.npc.append (18)
        self.cont.append (-1)
        self.player.append (19)
        self.cont.append (9)
        self.player.append (-1)

    def answer19 (self):
        self.color = the_npc.get_color()
        self.npc.append (20)
        self.cont.append (-1)
        self.player.append (21)
        self.cont.append (10)
        self.player.append (-1)

    def answer21 (self):
        self.color = the_npc.get_color()
        self.npc.append (22)
        self.cont.append (-1)
        self.player.append (23)
        self.cont.append (11)
        self.player.append (24)
        self.cont.append (12)
        self.player.append (-1)

    def answer24 (self):
        quests["demo"].set_val( "told_on_talan", 1 );

        self.color = the_npc.get_color()
        self.npc.append (26)
        self.cont.append (-1)
        self.player.append (27)
        self.cont.append (13)
        self.player.append (-1)

    def answer27 (self):
        self.color = the_npc.get_color()
        self.npc.append (28)
        self.cont.append (-1)
        self.player.append (29)
        self.cont.append (14)
        self.player.append (-1)

    def answer29 (self):
        self.color = the_npc.get_color()
        self.npc.append (30)
        self.cont.append (-1)
        quests["demo"].set_val( "silverhair_free", 1 );

        self.player.append (-1)

    def answer23 (self):
        self.color = the_npc.get_color()
        self.npc.append (25)
        self.cont.append (-1)
        self.player.append (27)
        self.cont.append (13)
        self.player.append (-1)

    def answer6 (self):
        self.color = the_npc.get_color()
        self.npc.append (11)
        self.cont.append (-1)
        if quests["demo"].get_val ("know_alek_eavesdrop") == 1 and quests["demo"].get_val ("know_talan_singing") != 2:

            self.player.append (32)
            self.cont.append (16)
        if quests["demo"].get_val ("ask_packed_gems") == 1 and quests["demo"].get_val ("know_talan_singing") != 2:

            self.player.append (31)
            self.cont.append (15)
        elif quests["demo"].get_val ("know_talan_singing") == 2:

            self.player.append (7)
            self.cont.append (4)
        else:

            self.player.append (38)
            self.cont.append (19)
        self.player.append (-1)

    def answer38 (self):
        self.color = the_npc.get_color()
        self.npc.append (39)
        self.cont.append (-1)
        self.player.append (40)
        self.cont.append (20)
        self.player.append (-1)

    def answer40 (self):
        self.color = the_npc.get_color()
        self.npc.append (37)
        self.cont.append (-1)
        quests["demo"].set_val ("know_jelom" , 2)

        self.player.append (-1)

    def answer31 (self):
        self.color = the_npc.get_color()
        self.npc.append (33)
        self.cont.append (-1)
        self.player.append (34)
        self.cont.append (17)
        self.player.append (-1)

    def answer34 (self):
        self.color = the_npc.get_color()
        self.npc.append (35)
        self.cont.append (-1)
        self.player.append (36)
        self.cont.append (18)
        self.player.append (-1)

    def answer36 (self):
        self.color = the_npc.get_color()
        self.npc.append (37)
        self.cont.append (-1)
        quests["demo"].set_val ("know_jelom" , 2)

        self.player.append (-1)

    def answer32 (self):
        self.color = the_npc.get_color()
        self.npc.append (35)
        self.cont.append (-1)
        self.player.append (36)
        self.cont.append (18)
        self.player.append (-1)

    def answer5 (self):
        self.color = the_npc.get_color()
        self.npc.append (8)
        self.cont.append (-1)
        self.player.append (10)
        self.cont.append (5)
        self.player.append (-1)

    def answer10 (self):
        self.color = the_npc.get_color()
        self.npc.append (11)
        self.cont.append (-1)
        if quests["demo"].get_val ("know_alek_eavesdrop") == 1 and quests["demo"].get_val ("know_talan_singing") != 2:

            self.player.append (32)
            self.cont.append (16)
        if quests["demo"].get_val ("ask_packed_gems") == 1 and quests["demo"].get_val ("know_talan_singing") != 2:

            self.player.append (31)
            self.cont.append (15)
        elif quests["demo"].get_val ("know_talan_singing") == 2:

            self.player.append (7)
            self.cont.append (4)
        else:

            self.player.append (38)
            self.cont.append (19)
        self.player.append (-1)

    def answer4 (self):
        self.color = the_npc.get_color()
        self.npc.append (9)
        self.cont.append (-1)
        self.player.append (10)
        self.cont.append (5)
        self.player.append (-1)
