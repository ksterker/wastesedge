class oliver_start:
    loop = []
    strings = ["As he notices you, the boy stops whatever he's been doing. With a cheerful grin on his face, he turns towards you.", "Hello sir! Welcome to Waste's Edge.", "Oh! I am Oliver, sir. I help Mum and Dad with the Inn. Looking after the stables and such.", "Why yes! Would you belive that we have an actual Elven Lady staying at the Inn?", "Really? An Elven Lady?", "Yes, sir. Lady Silverbeard. From Cirdanth. And her two servants! She frightened me a bit, but now she's locked up in her room.", "And who would you be?", "You can surely tell me something about Waste's Edge, then.", "Did something unusual happen here lately, Oliver?", "Have you heard about the theft, sir? Everybody speaks about it.", "Then I don't want to keep you off your work any longer.", "Are there other guests too?", "Yes, but they are just ordinary people. Merchants and such.", "What can you tell me about that?", "Can you imagine, sir? The Elven Lady robbed Master Fingolson in his sleep. And none of the adults noticed anything.", "Why would anyone want to lock her up?", "Then you better tell me about the Elven Lady, Oliver.", "Well, thank you for the information. Until later.", "Who is Master Fingolson?", "But you heard something that night?", "Just another Dwarf from Uzdun'kal. He sells jewels and such. We get a lot of them here, but none of them got robbed so far.", "Speaking of that, you say you noticed something that night?", "Yeah. Someone must have been in the stables. But when I went and had a look, they were gone.", "I see. Thank you for your help, Oliver. Until later.", "Oliver looks pleased as he sees you nearing.", "Uh, hello again sir. Do you have more questions?", "Can you tell me something about Waste's Edge, Oliver?", "What do you know about the theft?", "Oliver leads you to a room on the first floor.", "I hope you like it, sir. All the other rooms are occupied.", "You have a lot of guests here at the moment, then?", "Don't worry Oliver. This one is fine.", "Yes sir. And with that theft, nobody can leave.", "Nobody can leave?", "No. As long as Master Fingolsons jewels are not found, the guards don't allow it.", "I see. Thank you Oliver. Until later.", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer0, self.answer4, self.answer6, self.answer7, self.answer8, self.answer11, self.answer13, self.answer15, self.answer16, self.answer18, self.answer19, self.answer21, self.answer24, self.answer26, self.answer27, self.answer28, self.answer30, self.answer33, None]

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
        if the_npc.get_val ("goto_players_room") == 3:

            self.color = 0
            self.npc.append (28)
            self.cont.append (16)
            the_npc.set_val ("goto_players_room" , 0)
            the_npc.set_val ("talked_to" , 1)
            the_npc.set_val ("goto_barn" , 1)

            self.player.append (-1)
        elif the_npc.get_val ("talked_to") == 0:

            self.color = 0
            self.npc.append (0)
            self.cont.append (1)
            the_npc.set_val ("talked_to" , 1)

            self.player.append (-1)
        else:

            self.color = 0
            self.npc.append (24)
            self.cont.append (13)
            self.player.append (-1)

    def answer24 (self):
        self.color = the_npc.get_color()
        self.npc.append (25)
        self.cont.append (-1)
        self.player.append (26)
        self.cont.append (14)
        self.player.append (27)
        self.cont.append (15)
        self.player.append (-1)

    def answer27 (self):
        self.color = the_npc.get_color()
        self.npc.append (14)
        self.cont.append (-1)
        self.player.append (19)
        self.cont.append (11)
        self.player.append (18)
        self.cont.append (10)
        self.player.append (-1)

    def answer18 (self):
        self.color = the_npc.get_color()
        self.npc.append (20)
        self.cont.append (-1)
        self.player.append (21)
        self.cont.append (12)
        self.player.append (-1)

    def answer21 (self):
        self.color = the_npc.get_color()
        self.npc.append (22)
        self.cont.append (-1)
        quests["demo"].set_val ("know_olivers_noise" , 1)

        self.player.append (23)
        self.cont.append (-1)
        self.player.append (-1)

    def answer23 (self):
        pass

    def answer19 (self):
        self.color = the_npc.get_color()
        self.npc.append (22)
        self.cont.append (-1)
        quests["demo"].set_val ("know_olivers_noise" , 1)

        self.player.append (23)
        self.cont.append (-1)
        self.player.append (-1)

    def answer26 (self):
        self.color = the_npc.get_color()
        self.npc.append (3)
        self.cont.append (-1)
        self.player.append (4)
        self.cont.append (2)
        self.player.append (11)
        self.cont.append (6)
        self.player.append (-1)

    def answer11 (self):
        self.color = the_npc.get_color()
        self.npc.append (12)
        self.cont.append (-1)
        self.player.append (16)
        self.cont.append (9)
        self.player.append (17)
        self.cont.append (-1)
        self.player.append (-1)

    def answer17 (self):
        pass

    def answer16 (self):
        self.color = the_npc.get_color()
        self.npc.append (5)
        self.cont.append (-1)
        self.player.append (15)
        self.cont.append (8)
        self.player.append (-1)

    def answer15 (self):
        self.color = the_npc.get_color()
        self.npc.append (14)
        self.cont.append (-1)
        self.player.append (19)
        self.cont.append (11)
        self.player.append (18)
        self.cont.append (10)
        self.player.append (-1)

    def answer4 (self):
        self.color = the_npc.get_color()
        self.npc.append (5)
        self.cont.append (-1)
        self.player.append (15)
        self.cont.append (8)
        self.player.append (-1)

    def answer0 (self):
        self.color = the_npc.get_color()
        self.npc.append (1)
        self.cont.append (-1)
        self.player.append (6)
        self.cont.append (3)
        self.player.append (-1)

    def answer6 (self):
        self.color = the_npc.get_color()
        self.npc.append (2)
        self.cont.append (-1)
        self.player.append (7)
        self.cont.append (4)
        self.player.append (8)
        self.cont.append (5)
        self.player.append (10)
        self.cont.append (-1)
        self.player.append (-1)

    def answer10 (self):
        pass

    def answer8 (self):
        self.color = the_npc.get_color()
        self.npc.append (9)
        self.cont.append (-1)
        self.player.append (13)
        self.cont.append (7)
        self.player.append (-1)

    def answer13 (self):
        self.color = the_npc.get_color()
        self.npc.append (14)
        self.cont.append (-1)
        self.player.append (19)
        self.cont.append (11)
        self.player.append (18)
        self.cont.append (10)
        self.player.append (-1)

    def answer7 (self):
        self.color = the_npc.get_color()
        self.npc.append (3)
        self.cont.append (-1)
        self.player.append (4)
        self.cont.append (2)
        self.player.append (11)
        self.cont.append (6)
        self.player.append (-1)

    def answer28 (self):
        self.color = the_npc.get_color()
        self.npc.append (29)
        self.cont.append (-1)
        self.player.append (30)
        self.cont.append (17)
        self.player.append (31)
        self.cont.append (-1)
        self.player.append (-1)

    def answer31 (self):
        pass

    def answer30 (self):
        self.color = the_npc.get_color()
        self.npc.append (32)
        self.cont.append (-1)
        self.player.append (27)
        self.cont.append (15)
        self.player.append (33)
        self.cont.append (18)
        self.player.append (-1)

    def answer33 (self):
        self.color = the_npc.get_color()
        self.npc.append (34)
        self.cont.append (-1)
        self.player.append (35)
        self.cont.append (-1)
        self.player.append (-1)

    def answer35 (self):
        pass
