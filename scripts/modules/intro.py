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

# The 3 forest images...
im1 = image ()
im2 = image ()
im3 = image ()
bg = image ()

im1.load_pnm ("gfx/cutscene/forest3.pnm")
im2.load_pnm ("gfx/cutscene/forest2.pnm")
im2.set_mask (1)
im3.load_pnm ("gfx/cutscene/forest1.pnm")
im3.set_mask (1)
bg.load_pnm ("gfx/cutscene/intro_bg.pnm")
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
font = win_manager_get_font ("original")
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
           "Still, Waste's Edge was a welcome sight.")

cont.set_visible_background (0);
cont.set_visible_border (0);
cont.set_visible_all (1);
cont.set_activate (1)

wintextocc = 0
wincpt = 0
windelay = 0
bgcpt = 0

status = -1

screen_clear ()

gametime_start_action ()

while not input_has_been_pushed (SDLK_ESCAPE) and not input_has_been_pushed (SDLK_SPACE):
    # Update the stuff
    input_update ()
    for i in range (0, gametime_frames_to_do ()):
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
                    if status == 0 and wintextocc == len (wintext) - 1 and windelay == - 250: status = 1
            else:
                wintextocc = wintextocc + 1
                wincpt = 0
                windelay = -500
            
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
    
    # Draw the entire scene
    if status < 3:
        draw_im (im1, x1)
        draw_im (im2, x2)
        draw_im (im3, x3)

    if status > 0:
        bg.draw (0, -bgy, da)

    if status == -1:
        imblack.draw (0, 0)

    cont.draw ()
    
    screen_show ()
    gametime_update ()

# Avoid a bad crash...
cont.remove (lab)
