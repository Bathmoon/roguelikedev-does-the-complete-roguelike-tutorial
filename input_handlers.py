#Function to determine actions to take on user input

def gameKeys(keyStroke):
    print(keyStroke)
    if keyStroke.key == 'ESCAPE':
        return {'exit': True}
    elif keyStroke.key == 'KP8':
        return {'move': (0,-1)}
    elif keyStroke.key == 'KP2':
        return {'move': (0, 1)}
    elif keyStroke.key == 'KP4':
        return {'move': (-1, 0)}
    elif keyStroke.key == 'KP6':
        return {'move': (1, 0)}
    elif keyStroke.key == 'KP9':
        return {'move': (1, -1)}
    elif keyStroke.key == 'KP7':
        return {'move': (-1, -1)}
    elif keyStroke.key == 'KP1':
        return {'move': (-1, 1)}
    elif keyStroke.key == 'KP3':
        return {'move': (1, 1)}
    elif keyStroke.key == 'ENTER' and keyStroke.alt:
        return {'fullscreen': True}
    else:
        exit()

