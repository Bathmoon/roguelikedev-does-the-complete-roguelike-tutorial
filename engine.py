#Import statements
import tdl
from entity import GameObject, get_blocking_entity
from input_handlers import gameKeys
from render_functions import clear_all, render_all
from map_utils import make_map, GameMap
from game_states import GameState

#Size/Location variables
WIDTH =80
HEIGHT = 50
MWIDTH = 80
MHEIGHT = 50
xloc = WIDTH//2
yloc = HEIGHT//2

#Room variables
room_max_size = 10
room_min_size = 6
max_rooms = 30
max_mons = 3

#FOV variables
fov_algorithm = 'BASIC'
fov_light_walls = True
fov_radius = 10
fov_recompute = True
game_state = GameState.PLAYER_TURN

#Color dictionary
colors = {
    'wall_char':  (150,150,150),
    'dark_wall':  (0,0,0),
    'dark_ground':  (200, 200, 200),
    'player_color': (255,255,255),
    'npc_color': (150,100,70),
    'wall_ground': (150,150,150),
    'light_wall':(200,200,200),
    'light_ground':(220,220,220),
    'desaturated_green': (63, 127, 63),
    'darker_green': (0, 127, 0)
}

#Initialize a player and an npc
player = GameObject(0, 0, '@', colors.get('player_color'), 'Player', blocks=True)
#npc = GameObject((WIDTH // 2 - 5), (HEIGHT // 2), '$', colors.get('npc_color'))

#initialize a structure to hold entities (players, npcs)
entities = [player]

#Initialize the console
tdl.set_font('./lucida12x12_gs_tc.png', greyscale=True, altLayout=True) #Set font style
rootWindow = tdl.init(WIDTH, HEIGHT, 'Roguelike', fullscreen=False) #Root console
display = tdl.Console(MWIDTH, MHEIGHT) #Map console
game_map = GameMap(MWIDTH, MHEIGHT) #Map object
make_map(game_map,max_rooms,room_min_size,room_max_size,MWIDTH,MHEIGHT,player, entities, max_mons, colors)

#Game loop
while not tdl.event.is_window_closed():

    #If we are recomputing FOV, recompute it here
    if fov_recompute:
        game_map.compute_fov(player.x, player.y, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)

    #Display map and all entities
    render_all(rootWindow, display, fov_recompute, entities, game_map, WIDTH, HEIGHT, colors)

    #Send displayed data to the screen
    tdl.flush()

    #Do not recompute FOV by default
    fov_recompute = False

    #Clear screen in preparation for the next turn
    clear_all(display, entities)

    #Get keyboard input from the user
    keyStroke = tdl.event.key_wait()

    #Turn user input into game action
    input = gameKeys(keyStroke)

    #Check for movement actions
    move = input.get('move')

    #Check for exit action
    exit = input.get('exit')
    print(exit)
    #Check for screensize action
    fullscreen = input.get('fullscreen')

    #When a movement action is read, move the player in the appropriate direction
    if move and game_state == GameState.PLAYER_TURN:
        locX, locY = move

        dest_x = player.x + locX
        dest_y = player.y + locY

        if game_map.walkable[dest_x, dest_y]: #Do not move if tile is blocking
            target = get_blocking_entity(entities, dest_x, dest_y)
            if target:
                print('You clobber ' + target.name)
            else:
                player.move(locX, locY)

        game_state = GameState.FOE_TURN

        if game_state == GameState.FOE_TURN:
            for entity in entities:
                if entity.name != 'Player':
                    print(entity.name + ' ponders its existence')
            game_state = GameState.PLAYER_TURN

        fov_recompute = True

    #Switch to fullscreen on screensize action
    if fullscreen:
        tdl.set_fullscreen(not tdl.get_fullscreen())

    #Exit the game
    if exit:
        break

