class janesta_start:
    loop = []
    strings = ["Oh, $name, we've been so worried for the Mistress.  Can't you do something to set her free?", "I will try, Janesta.  But you must be brave.  This is a difficult time for Lady Silverhair, and she needs us all to help her though.", "I will try.  Thank you, $name.", "Perhaps.  Do you know anything about this dwarf, Fingolson?", "Nothing, I'm afraid.  This is my first time here, and I was brought straight to the Mistress' room to make it ready.  This room is so awful, I cannot see how they expect a High Born to stand it.", "I see.  Thank you, Janesta.  I'm glad you are here to care for our Lady.", "Oh, $name.  I pray that this will turn out right.", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer1, self.answer3, self.answer5, None]

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
        self.color = characters["Janesta Skywind"].get_color()
        self.npc.append (0)
        self.cont.append (-1)
        self.player.append (1)
        self.cont.append (1)
        self.player.append (3)
        self.cont.append (2)
        self.player.append (-1)

    def answer3 (self):
        self.color = characters["Janesta Skywind"].get_color()
        self.npc.append (4)
        self.cont.append (-1)
        self.player.append (5)
        self.cont.append (3)
        self.player.append (-1)

    def answer5 (self):
        self.set_npc (the_npc.get_name())
        self.color = the_npc.get_color()
        self.npc.append (6)
        self.cont.append (-1)
        self.player.append (-1)

    def answer1 (self):
        self.color = characters["Janesta Skywind"].get_color()
        self.npc.append (2)
        self.cont.append (-1)
        self.player.append (-1)
