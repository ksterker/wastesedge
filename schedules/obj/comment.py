from adonthell import gui

class comment:
    def say_text (self, actor, target, text):
       l = gui.layout(400, 400)
       la = gui.label(300, 300)
       la.set_string ('foo')
       l.add_child(la, 0, 0)
       la.thisown = 0
       l.thisown = 0
       gui.window_manager.add(0,0,l)
       print text

    def say_time (self, actor, target):
       from adonthell.event import date
       print date.format_time ("It is %h:%m o'clock") 

