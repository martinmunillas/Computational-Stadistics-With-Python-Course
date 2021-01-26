class Coords:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        return Coords(self.x + x, self.y + y)

    def distance(self, coord):
        return ((self.x - coord.x)**2) + ((self.y - coord.y)**2)**0.5