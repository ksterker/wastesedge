from adonthell import *

def update_im (im, x):
    if x <= -im.length (): x = x + im.length ()
    else: x = x - 1
    return x

def draw_im (im, x):
    im.draw (x, 0, da)
    if x < screen_length () - im.length (): im.draw (im.length () + x, 0, da)

# Our drawing area for the scrolling forest.
da = drawing_area ()
da.resize (screen_length (), screen_height ())
da.move (0, 0)

# The images...
im1 = image ()
im2 = image ()
im3 = image ()
bg = image ()
inn_close = image ()

im1.load_raw ("gfx/cutscene/forest3.img")
im2.load_raw ("gfx/cutscene/forest2.img")
im2.set_mask (1)
im3.load_raw ("gfx/cutscene/forest1.img")
im3.set_mask (1)
bg.load_raw ("gfx/cutscene/intro_bg.img")
bg.set_alpha (0)

imblack = image ()
imblack.resize (screen_length (), screen_height ())
imblack.fillrect (0, 0, imblack.length (), imblack.height (), 0)

# ...their x coordinate...
x1 = 0
x2 = 0
x3 = 0
bgy = 0

# ...and their delay time.
o1 = 0
o2 = 0
o3 = 0

# The text window.
theme = win_manager_get_theme ("original")
font = win_manager_get_font ("white")
cont = win_container ()
cont.resize (250, 100)
cont.move ((screen_length () - cont.length ())/2,
           (screen_height () - cont.height ())/4)

cont.set_border (theme)
cont.set_background (theme)
cont.set_trans_background (1)

lab = win_label ()
lab.move (5, 5)
lab.resize (cont.length () - 10, cont.height () - 10)
lab.set_font (font)
lab.pack ()

cont.add (lab)

wintext = ("One week out of Cirdanth, the trail had\nbecome hard. I had begun to wonder\ndays ago whether \
it could still be called\na trail, but it was the only way the\ncaravans had.",
           "There were no caravans now, only me,\nand I had seen few others on the road.\nEven those had \
become more scarce the\nfurther I went.",
           "It was easy to see why.",
           "The Lady Silverhair, intent on her\nmission, had gone on ahead while I was\nleft to complete \
business in her name,\ntrusting me to follow in good speed.",
           "A lone Half-Elf, may travel with much\nmore speed than an Elven lady and her\nservants, so she \
was now only a day\nahead.  The thought nearly caused me\nto forget \
the harshness of the road.",
           "Still, Waste's Edge was a welcome sight.",
           "As you approach the trading post, there\nseems to be little sign of life. Eventually\nyou find the \
Redwyne Inn, which seems\nto be the main building here.",
           "The heavy wooden doors are closed,\nand no one is there \
to let you in. As you\napproach the gate, you suddenly hear a voice from within.")

cont.set_visible_background (0);
cont.set_visible_border (0);
cont.set_visible_all (1);
cont.set_activate (1)

# Images for the speech
bubbg = (image (), image(), image())
bubbg[0].load_raw ("gfx/cutscene/intro_inn.img")
bubbg[1].load_raw ("gfx/cutscene/intro_guard.img")
bubbg[2].load_raw ("gfx/cutscene/intro_player.img")

# Text for the speech
if gamedata_player () != None: myname = gamedata_player ().get_name ()
else: myname = "Banec"

bubtext = (("Halt! Stand and declare yourself, stranger!", "red", 25, 5, 350, 1),
           ("I am " + myname + ", come as an agent for my employer. Tell me, is this the trading \
post of Waste's Edge?", "yellow", 130, 5, 500, 2),
           ("That it is, but this is all you'll see of it.", "red", 25, 5, 300, 1),
           ("If you turn now and make haste, you should be able to make safe camping \
before dark.", "red", 25, 5, 400, 1),
           ("Turn back?  Whatever for?  And why is the gate of a free trading post locked \
against a footsore traveller?", "yellow", 130, 5, 500, 0),
           ("I am sorry, traveller, but the post is barred and you must be off.", "red", 25, 5, 300, 0),
           ("There has been trouble inside and I have instructions to turn away all who \
need not be here.", "red", 25, 5, 400, 0),
           ("Trouble?  Why then, I must get inside.  My employer will need me close at \
hand!", "yellow", 130, 15, 500, 0))

wintextocc = 0
wincpt = 0
windelay = 0
bgcpt = 0

status = -1

letsexit = 0

screen_clear ()

gametime_start_action ()

while not input_has_been_pushed (SDLK_ESCAPE) and not input_has_been_pushed (SDLK_SPACE) and not letsexit:
    # Update the stuff
    input_update ()
    for i in range (0, gametime_frames_to_do ()):

        # 1st part: forest scrolling and fade to the inn, with
        #the text appearing letter-by-letter
        if status < 4:
            # Magic number
            if o1 >= 4:
                x1 = update_im (im1, x1)
                o1 = 0
            else: o1 = o1 + 1

            # Magic number
            if o2 >= 2:
                x2 = update_im (im2, x2)
                o2 = 0
            else: o2 = o2 + 1

            # Magic number
            if o3 >= 1:
                x3 = update_im (im3, x3)
                o3 = 0
            else: o3 = o3 + 1

            # Update the label text
            if wintextocc < len (wintext):
                if wincpt < len (wintext[wintextocc]):
                    windelay = windelay + 1
                    if windelay >= 10:
                        if wincpt == 0: lab.set_text ("")
                        lab.add_text (wintext[wintextocc][wincpt])
                        wincpt = wincpt + 1
                        windelay = 0
                    else:
                        windelay = windelay + 1
                        # Shall we fade to the Inn view?
                        if status == 0 and wintextocc == 5 and windelay == - 250: status = 1
                else:
                    wintextocc = wintextocc + 1
                    wincpt = 0
                    windelay = -500
            else:
                # Switch to close inn view?
                if windelay == -300:
                    status = 4
                    windelay = 0
                    wintextocc = 0
                else: windelay = windelay + 1
            
            cont.update ()

            # Fade to the forest
            if status == -1:
                if (imblack.alpha ()) > 0:
                    imblack.set_alpha (imblack.alpha () - 1)
                else: status = 0

            # Fade to the Inn view.
            if status == 1 or status == 2:
                if (bg.alpha ()) < 255:
                    bg.set_alpha (bg.alpha () + 1)
                    if bg.alpha () == 150:
                        # Start scrolling
                        status = 2

            if status == 2:
                if bgy < bg.height () - screen_height ():
                    bgcpt = bgcpt + 1
                    if bgcpt == 2:
                        bgy = bgy + 1
                        bgcpt = 0
                else: status = 3

        # 2nd part: speech between Talan and the player.
        if status >=4:
            if windelay >= 0 and wintextocc < len (bubtext):
                windelay = -bubtext[wintextocc][4]
                bub = text_bubble (bubtext[wintextocc][0], bubtext[wintextocc][1], "original")
                bub.move (bubtext[wintextocc][2], bubtext[wintextocc][3])
                windelay = windelay + 1
                currentbg = bubtext[wintextocc][5]
            else:
                windelay = windelay + 1
                if windelay >= 0:
                    wintextocc = wintextocc + 1
                    if wintextocc == len (bubtext): letsexit = 1
    
    # Draw the entire scene
    if status < 3:
        draw_im (im1, x1)
        draw_im (im2, x2)
        draw_im (im3, x3)

    if status > 0 and status < 4:
        bg.draw (0, -bgy, da)

    if status == -1:
        imblack.draw (0, 0)

    if status < 4:
        cont.draw ()

    if status >= 4:
        bubbg[currentbg].draw (0, 0)
        bub.draw ()
    
    screen_show ()
    gametime_update ()

# Avoid a bad crash...
cont.remove (lab)
