

                       Adonthell - Waste's Edge 0.3.3 
                           

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    COPYING file for more details.


Synopsis:
=========

Below you will find a description of Adonthell's configuration options, 
release notes and contact informations. If you need help with playing
Adonthell - Waste's Edge, please refer to the PLAYING file.


Philosophy:
===========

Adonthell was (and still is) primarily developed for GNU/Linux, but runs
on many UNiX flavours and various hardware platforms. This is the first 
official release for Windows.
  
Adonthell is free software, which means its source code is available for
everybody to modify and distribute, as long as those modifications are
open to everybody as well. See the COPYING files for the exact terms and
conditions.

In turn, Adonthell itself depends on various projects that are sharing 
the same philosophy, like SDL, Ogg Vorbis, Python and SWIG to name just
a few. Without these fundamental works of dozens of developers, we
wouldn't be where we are today. 

The same is true for the many individuals that contributed bugfixes or
larger portions of the code. Something that would be unthinkable with
closed source software.

In brief: "Use the Source, Luke!"


Configuring Adonthell:
======================

To bring up and edit the configuration file (adonthell.ini), use the
"Edit Configuration" link in the "Adonthell - Waste's Edge" program 
group. You will have to restart the game before your changes can take 
place.

The available options and what they do are:

- Screen-mode
  Whether Adonthell should run fullscreen or in windowed mode 
  0 = Windowed mode, 1 = Fullscreen mode
  
- Double-size
  Whether resolution should be scaled to 640x480 or not
  0 = disable, 1 = enable
  
  Enabling double-size mode significantly increases CPU usage. On
  old hardware you should consider turning this option off and run
  Adonthell in fullscreen mode instead.

- Language [locale]
  Specifies which language to use. As long as this option is unset,
  the language is determined by one of the following environment
  variables: LANG, LC_ALL or LC_MESSAGES. Once the option is set,
  it overrides any environment variable. For a listing of valid
  locale strings, run 'locale -a'.
  
  Of course, the game you run has to provide the translation you 
  chose here, otherwise you'll get the default (i.e. English) text.

- Quick-load
  Whether the last saved game should be automatically continued at
  startup. Only works if at least one saved game exists.
  0 = disable, 1 = enable

- Audio-channels
  Whether sound should be mono or stereo
  0 = Mono, 1 = Stereo

- Audio-resolution
  Whether audio output should be 8 or 16 bit
  0 = 8 bit, 1 = 16 bit

- Audio-sample-rate
  0 = 11025 Hz, 1 = 22050 Hz, 2 = 44100 Hz

- Audio-volume
  The mixer setting, 0 - 100 %
  
  (Note that a value of 0 will turn audio completely off)


Release Notes:
==============

The main purpose of this release is to attract new programmers, 
artists and writers in order to shorten the time until the next 
version.  So if you have experience in C++ (and optionally Python), 
or if you are good at computer graphics or writing we would like to
hear from you.  Please have a look at our developer's corner
  
  http://adonthell.linuxgames.com/development/

for further details.

Adonthell - Waste's Edge, or v0.3 for short is no complete RPG.
As the v0.3 implies, the engine is far from being finished, although
it should be free of severe bugs.  Missing features include combat, 
items and magic.  But you can interact with NPCs and the game world, 
and the internals enable us to create a basic plot, so v0.3 is actually
playable!

You're greatly invited to report us bugs, problems, or anything you
think we should know. Any feedback is appreciated, so don't hesitate!


Contact:
========

You can reach us in various ways:

Email:         adonthell@linuxgames.com
Mailing list:  adonthell-general@mail.freesoftware.fsf.org
Web site:      http://adonthell.linuxgames.com
Tech support:  http://savannah.gnu.org/support/?group_id=702

There is a Message Board for user to user discussion at
    http://www.3dforums.com/?action=forumpage&loc=49&forum_id=158

If you want to rate or comment on Adonthell, feel free to do so at
    http://www.happypenguin.org/show?Adonthell
    http://www.freshmeat.net/projects/adonthell


Reporting Bugs:
===============

We hope you'll never have to, but if you discover a problem, we
would like to hear about it. In that case, the files stdout.txt and
stderr.txt might contain further details to locate the source of
error. Please use the Development mailing list to contact us
(adonthell-devel@mail.freesoftware.fsf.org). Information on this and 
other mailing lists are available at 

    http://adonthell.linuxgames.com/contact/mailinglist.shtml


Thank you for trying this software.
- The Adonthell team.
