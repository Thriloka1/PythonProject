import random

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack
        self.status = None

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", random.randint(20,40), random.randint(5,10))
    def special_move(self, player):
        print("Goblin uses Sneak Attack!")
        player.health -= 10

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 150, 25)
    def special_move(self, player):
        print("Dragon breathes fire!")
        player.health -= 30

def enemy_generator():
    enemy_types = [Goblin, Dragon]
    while True:
        yield random.choice(enemy_types)()
