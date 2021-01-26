import random

class Drunk:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return random.choice([(0,1), (1,0), (0,-1), (-1,0)])