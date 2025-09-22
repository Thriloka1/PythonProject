import logging

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.inventory = {}
        self.position = (0,0)
        self.status = None
        self.level = 1

    def move(self, direction, game_map):
        x, y = self.position
        if direction == "up" and x > 0:
            self.position = (x-1, y)
        elif direction == "down" and x < len(game_map)-1:
            self.position = (x+1, y)
        elif direction == "left" and y > 0:
            self.position = (x, y-1)
        elif direction == "right" and y < len(game_map[0])-1:
            self.position = (x, y+1)
        logging.info(f"{self.name} moved {direction} to {self.position}")
