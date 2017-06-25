import tdl

#Global variables
WIDTH =80
HEIGHT = 50
xloc = WIDTH/2
yloc = HEIGHT/2

#Handle user keystrokes
def gameKeys():
    global xloc, yloc
    keyStroke = tdl.event.key_wait()

    if(keyStroke.key == 'ENTER'):
        return True
    else:
        return True #Just close on any keypress for now


#Initialize the console
tdl.set_font('./lucida12x12_gs_tc.png', greyscale=True, altLayout=True)
rootWindow = tdl.init(WIDTH, HEIGHT, 'Roguelike', fullscreen=False)

#Game loop
while not tdl.event.is_window_closed():

    rootWindow.drawStr(xloc-6, yloc, "Here we go")
    tdl.flush()

    input = gameKeys()
    if (input == True):
        break