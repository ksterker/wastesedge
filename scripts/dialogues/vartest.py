class vartest:
    loop = []
    strings = ["Hello sir. Do you like me?", "You told me you don't like me. Have you changed your mind?", "You told me you like me. Do you still like me?", "Yes", "No", "That's nice of you.", "I feel so sorry.", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer3, self.answer4, None]

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
        if the_npc.get("lstanswer")==2:
            self.color = the_npc.get_color()
            self.npc.append (2)
            self.cont.append (-1)
            self.player.append (3)
            self.cont.append (1)
            self.player.append (4)
            self.cont.append (2)
            self.player.append (-1)
        if the_npc.get("lstanswer")==1:
            self.color = the_npc.get_color()
            self.npc.append (1)
            self.cont.append (-1)
            self.player.append (3)
            self.cont.append (1)
            self.player.append (4)
            self.cont.append (2)
            self.player.append (-1)
        if the_npc.get("lstanswer")==0:
            self.color = the_npc.get_color()
            self.npc.append (0)
            self.cont.append (-1)
            self.player.append (3)
            self.cont.append (1)
            self.player.append (4)
            self.cont.append (2)
            self.player.append (-1)

    def answer4 (self):
        self.color = the_npc.get_color()
        self.npc.append (6)
        self.cont.append (-1)
        the_npc.set("lstanswer",1)

        self.player.append (-1)


    def answer3 (self):
        self.color = the_npc.get_color()
        self.npc.append (5)
        self.cont.append (-1)
        the_npc.set("lstanswer",2)

        self.player.append (-1)
