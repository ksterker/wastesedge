#
#  (C) Copyright 2002 Kai Sterker <kaisterker@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- various low level schedule base classes

import adonthell
import random
import types

# -- let NPC utter random remarks
#    requires the NPC schedule to have the members 
#
#    speech, an array of remarks for the NPC, and 
#    speech_delay, a tuple with the minimum and maximum delay 
#        between two remarks
#
#    The derived schedule needs to call speak.__init__ (self) after
#    setting the above values.
class speak:
    def __init__ (self):
        # -- sanity checks
        if type (self.speech) != types.ListType:
            print "*** speak::__init__: 'speech' list not found!"
        if type (self.speech_delay) != types.TupleType:
            print "*** speak::__init__: 'speech_delay' tuple not found!"
        if len (self.speech_delay) != 2:
            print "*** speak::__init__: 'speech_delay' has wrong size!"
            
        # -- member initialization
        self.speech_length = len (self.speech)
        
        # -- register first speech
        delay = "%it" % random.randrange (self.speech_delay[0], self.speech_delay[1])
        self.speak_event = adonthell.time_event (delay)
        self.speak_event.set_callback (self.speak)
        adonthell.event_handler_register_event (self.speak_event)

        
    # -- make remark and set delay for the next one
    def speak (self):
        self.myself.speak (self.speech[random.randrange (0, self.speech_length)])

        delay = "%it" % random.randrange (self.speech_delay[0], self.speech_delay[1])
        self.speak_event = adonthell.time_event (delay)
        self.speak_event.set_callback (self.speak)
        adonthell.event_handler_register_event (self.speak_event)
