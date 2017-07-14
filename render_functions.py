#File to handle all display functions

import tdl

#Render the game map and entities
def render_all(root, con, fov_recompute, entities, game_map, screen_width, screen_height, colors):
    if fov_recompute:
    #Check for tile objects in the array which block sight. If they do, draw a wall, otherwise draw ground
        for x, y in game_map:
            wall = not game_map.transparent[x, y]

            if game_map.fov[x, y]:
                game_map.explored[x][y] = True
                if wall:
                    con.draw_char(x, y, '#', fg=colors.get('light_wall'), bg=colors.get('wall_ground'))
                else:
                    con.draw_char(x, y, None, fg=None, bg=colors.get('light_ground'))
            elif game_map.explored[x][y]:
                if wall:
                    con.draw_char(x, y, '#', fg=colors.get('dark_wall'), bg=colors.get('wall_ground'))
                else:
                    con.draw_char(x, y, None, fg=None, bg=colors.get('dark_ground'))


    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity, game_map.fov)

    root.blit(con, 0, 0, screen_width, screen_height, 0, 0)

#Clear all entities from the screen
def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

#Draw a specific entity to the map console
def draw_entity(con, entity, fov):
    if fov[entity.x,entity.y]:
        con.draw_char(entity.x, entity.y, entity.char, bg=None, fg=entity.color)

#Clear specific entity from the map console
def clear_entity(con, entity):
    con.draw_char(entity.x, entity.y, ' ', bg=None, fg=entity.color)