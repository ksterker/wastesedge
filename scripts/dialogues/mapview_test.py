class mapview_test:
    loop = []
    strings = ["Hello My Lord. Do you want to see what Frostbloom is doing? I bet she's walking around the tree!", "Let's see it!", "I'm not interested, thanks.", "Well, see you later then.", "Here it is. Press the <space> key to see her, then <space> again when you have enough.", "Hope you liked it.", "Hello again, Milord. Do you want to see what Frostbloom is doing?", ""]

    def set_name (self, new_name):
        pass

    def set_npc (self, new_npc):
        pass

    def set_portrait (self, new_portrait):
        pass

    def __init__(self):
        self.dialogue = [self.start, self.answer1, self.answer2, self.answer4, None]

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
        if the_npc.get("alreadymet")==1:
            self.color = the_npc.get_color()
            self.npc.append (6)
            self.cont.append (-1)
            self.player.append (1)
            self.cont.append (1)
            self.player.append (2)
            self.cont.append (2)
            self.player.append (-1)
        if the_npc.get("alreadymet")==0:
            self.color = the_npc.get_color()
            self.npc.append (0)
            self.cont.append (-1)
            the_npc.set("alreadymet",1)

            self.player.append (1)
            self.cont.append (1)
            self.player.append (2)
            self.cont.append (2)
            self.player.append (-1)

    def answer2 (self):
        self.color = the_npc.get_color()
        self.npc.append (3)
        self.cont.append (-1)
        self.player.append (-1)

    def answer1 (self):
        self.color = the_npc.get_color()
        self.npc.append (4)
        self.cont.append (3)
        self.player.append (-1)

    def answer4 (self):
        self.color = the_npc.get_color()
        self.npc.append (5)
        self.cont.append (-1)
        from ins_modules import *
        
        otherview=mapview()
        otherview.attach_map(map_engine.get_landmap())
        otherview.resize(120,100)
        otherview.set_schedule("follow_frostbloom")
        while not input_has_been_pushed(SDLK_SPACE):
          map_engine.mainloop()
          for i in range(gametime_frames_to_do()):
            otherview.update()
          otherview.draw(100,70)
          screen_show()
          gametime_update()
          input_update()
        input_clear_keys_queue()

        self.player.append (-1)
