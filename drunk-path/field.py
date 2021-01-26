class Field:

    def __init__(self):
        self.coords = {}
    
    def add_coord(self, drunk, coord):
        self.coords[drunk] = coord

    def move(self, drunk):
        x, y = drunk.walk()
        actual_coord = self.coords[drunk]
        new_coord = actual_coord.move(x, y)
        self.coords[drunk] = new_coord
    
    def get_coord(self, drunk):
        return self.coords[drunk]