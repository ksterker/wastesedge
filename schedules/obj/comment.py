class comment:
    def say_text (self, actor, target, text):
       print text

    def say_time (self, actor, target):
       from adonthell.event import date
       print date.format_time ("It is %h:%m o'clock") 

