#A function to determine blocking for a given entity
def get_blocking_entity(entities, dest_x, dest_y):
    for entity in entities:
        if entity.blocks and entity.x == dest_x and entity.y == dest_y:
            return entity

    return None


#A class to represent the generic game object

class GameObject:
    def __init__(self, x, y, char, color, name, blocks=False): #Initialize the object to the passed parameters
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks

    def move(self, x, y): #Move the object
        self.x += x
        self.y += y

