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
#    myself, a pointer to the mapcharacter
#    speech, an array of remarks for the NPC, and 
#    speech_delay, a tuple with the minimum and maximum delay 
#        between two remarks
#
#    The derived schedule needs to call speak.__init__ (self) after
#    setting the above values.
class speak:
    def __init__ (self):
        # -- sanity checks
        if not hasattr (self, "myself"):
            print "*** speak::__init__: character 'myself' not found!"
        if not hasattr (self, "speech") and \
            type (self.speech) != types.ListType:
            print "*** speak::__init__: 'speech' list not found!"
        if not hasattr (self, "speech_delay") and \
            type (self.speech_delay) != types.TupleType:
            print "*** speak::__init__: 'speech_delay' tuple not found!"
        elif len (self.speech_delay) != 2:
            print "*** speak::__init__: 'speech_delay' has wrong size!"
            
        # -- member initialization
        self.speech_length = len (self.speech)
               
    # -- make remark and set delay for the next one
    def speak (self):
        self.myself.speak (self.speech[random.randrange (0, self.speech_length)])

        delay = "%it" % random.randrange (self.speech_delay[0], self.speech_delay[1])
        self.myself.time_callback (delay, self.speak)
