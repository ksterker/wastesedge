class frostbloom_start:
    loop = []
    strings = ["Hm?  What do you want?", "I am a servant of Lady Imoen Silverhair, and I'd like to ask ...", "I know who you are, and I do not care what you wish to ask.  Now go away.  The Yeti of my soul must have silence.", "You again?  I thought I told you to leave me alone.", "But lady, I must ask you about the theft...", "The theft?  You mean your theft of my precious time, when I could be receiving inspiration?  I've lost enought of that already, thank you.  Now be gone, silly servant, you begin to annoy me.", "But, lady...", "Off, I say!  I have no patience for this chatter!", "I will go, but I will return to ask my questions.  I must have what you know of my Lady.", "The half-elf fixes you with a withering gaze.  For a moment, you feel as if you had been skewered.  Her voice is full of sarcasm.", "I look forward to it with all my heart.  For now, just go away.", "Back again, eh?  You do hunger for punishment, don't you.", "I try to be diligent, lady.", "Well, I must admit that such devotion deserves a reward.  Very well, you may stay for a while.  A short while.  My name is Rhayne Frostbloom.  Take care you remember it.", "Thank you, lady.  I would ask you about the theft, if I may.", "For goodness sake, do not bother me with that nonsense.  It's been all anyone speaks about here, and I for one am sick of it.", "I have seen the lovely Yeti you carved for my mistress.  It is quite impressive.", "Do you really think so?  I tried to make it worthy of the noble beast, but I always wonder if I have given it enough life.", "I'm hardly an exprert, lady, but to my eye it is excellent.", "It is important.  The Lady Silverhair is in terrible danger.", "I know, I know.  And even if she is not hung, the Dwarves will be outraged.  What a foolish noise over such a little thing.  Gems are showy trash.  They cannot comprehend the complex soul of a Yeti.", "But this is hardly foolish, you must understand that.", "Frostbloom doesn't appear to hear you.  She stares off into space, occasionally whispering something about Yetis and souls, but you can make little sense of it.", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer1, self.answer4, self.answer6, self.answer8, self.answer9, self.answer12, self.answer14, self.answer16, self.answer19, self.answer21, None]

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
        if the_npc.get_val ("spoken_to") == 0:

            self.color = characters["Rhayne Frostbloom"].get_color()
            self.npc.append (0)
            self.cont.append (-1)
            the_npc.set_val ("spoken_to" , 1)

            self.player.append (1)
            self.cont.append (1)
            self.player.append (-1)
        elif the_npc.get_val ("spoken_to") == 1:

            self.color = characters["Rhayne Frostbloom"].get_color()
            self.npc.append (3)
            self.cont.append (-1)
            the_npc.set_val ("spoken_to" , 2)

            self.player.append (4)
            self.cont.append (2)
            self.player.append (-1)
        else:

            self.color = characters["Rhayne Frostbloom"].get_color()
            self.npc.append (11)
            self.cont.append (-1)
            self.player.append (12)
            self.cont.append (6)
            self.player.append (-1)

    def answer12 (self):
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (13)
        self.cont.append (-1)
        self.player.append (14)
        self.cont.append (7)
        self.player.append (16)
        self.cont.append (8)
        self.player.append (-1)

    def answer16 (self):
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (17)
        self.cont.append (-1)
        self.player.append (18)
        self.cont.append (-1)
        self.player.append (-1)

    def answer18 (self):
        pass

    def answer14 (self):
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (15)
        self.cont.append (-1)
        self.player.append (19)
        self.cont.append (9)
        self.player.append (-1)

    def answer19 (self):
        self.set_npc (the_npc.get_name())
        self.color = the_npc.get_color()
        self.npc.append (20)
        self.cont.append (-1)
        self.player.append (21)
        self.cont.append (10)
        self.player.append (-1)

    def answer21 (self):
        self.color = 0
        self.npc.append (22)
        self.cont.append (-1)
        self.player.append (-1)

    def answer4 (self):
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (5)
        self.cont.append (-1)
        self.player.append (6)
        self.cont.append (3)
        self.player.append (8)
        self.cont.append (4)
        self.player.append (-1)

    def answer8 (self):
        self.set_npc (the_npc.get_name())
        self.color = 0
        self.npc.append (9)
        self.cont.append (5)
        self.player.append (-1)

    def answer9 (self):
        self.set_npc ("Rhayne Frostbloom")
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (10)
        self.cont.append (-1)
        self.player.append (-1)

    def answer6 (self):
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (7)
        self.cont.append (-1)
        self.player.append (-1)

    def answer1 (self):
        self.color = characters["Rhayne Frostbloom"].get_color()
        self.npc.append (2)
        self.cont.append (-1)
        self.player.append (-1)
