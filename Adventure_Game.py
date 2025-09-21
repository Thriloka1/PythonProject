# -----------------------------
# Master-Level Adventure Game
# -----------------------------
import random, json, time, threading, logging, copy

# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(filename="game.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# -----------------------------
# Classes
# -----------------------------
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

# -----------------------------
# Map Generation
# -----------------------------
def generate_map(size):
    cell_types = ["Empty", "Enemy", "Item", "Trap"]
    return [[{"type": random.choices(cell_types, weights=[50,20,20,10])[0], "visited": False} for _ in range(size)] for _ in range(size)]

# -----------------------------
# Inventory & Items
# -----------------------------
def pick_item(player, item):
    if item["name"] in player.inventory:
        player.inventory[item["name"]]["count"] += 1
    else:
        player.inventory[item["name"]] = {"count":1, "effect": item["effect"]}
    print(f"Picked up {item['name']}! Current inventory: {player.inventory}")

# -----------------------------
# Abilities
# -----------------------------
def ability_limit(func):
    def wrapper(*args, **kwargs):
        print(f"Using ability: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@ability_limit
def heal(player, amount):
    player.health = min(player.max_health, player.health + amount)
    print(f"{player.name} healed for {amount} HP!")

damage = lambda attack, defense: max(0, attack - defense)

# -----------------------------
# Save & Load
# -----------------------------
def save_game(player, game_map, filename="savegame.json"):
    with open(filename, "w") as f:
        json.dump({"player": player.__dict__, "map": game_map}, f, indent=4)
    print("Game saved!")

def load_game(filename="savegame.json"):
    with open(filename, "r") as f:
        data = json.load(f)
        player = Player(data["player"]["name"])
        player.__dict__.update(data["player"])
        return player, data["map"]

# -----------------------------
# Battle System
# -----------------------------
def fight(player, enemy):
    print(f"A wild {enemy.name} appeared! HP: {enemy.health}")
    while player.health > 0 and enemy.health > 0:
        action = input("Choose action (attack/heal/run): ").lower()
        if action == "attack":
            dmg = damage(random.randint(5,15), 0)
            enemy.health -= dmg
            print(f"You dealt {dmg} damage to {enemy.name}")
        elif action == "heal":
            heal(player, 20)
        elif action == "run":
            if random.random() > 0.5:
                print("You escaped!")
                return
            else:
                print("Failed to escape!")
        if enemy.health > 0:
            enemy_attack = random.randint(0, enemy.attack_power)
            player.health -= enemy_attack
            print(f"{enemy.name} attacked for {enemy_attack} damage!")
    if player.health <= 0:
        print("You died! Restoring checkpoint...")
        logging.warning(f"{player.name} died at {player.position}")

# -----------------------------
# Generators
# -----------------------------
def enemy_generator():
    enemy_types = [Goblin, Dragon]
    while True:
        yield random.choice(enemy_types)()

enemy_gen = enemy_generator()

def quest_generator():
    quests = ["Collect 3 potions", "Defeat 5 enemies", "Find the hidden treasure"]
    for quest in quests:
        yield quest

quest_gen = quest_generator()

# -----------------------------
# Threaded Background Events
# -----------------------------
def spawn_treasure(game_map):
    while True:
        time.sleep(30)
        x, y = random.randint(0,len(game_map)-1), random.randint(0,len(game_map[0])-1)
        game_map[x][y]["type"] = "Item"
        print("A treasure appeared somewhere on the map!")

# -----------------------------
# Game Loop
# -----------------------------
def game_loop(player, game_map):
    threading.Thread(target=spawn_treasure, args=(game_map,), daemon=True).start()
    while True:
        print(f"Player at {player.position}, HP: {player.health}")
        move = input("Move (up/down/left/right) or quit: ").lower()
        if move == "quit":
            save_game(player, game_map)
            break
        player.move(move, game_map)
        x, y = player.position
        cell = game_map[x][y]
        if not cell["visited"]:
            if cell["type"] == "Enemy":
                fight(player, next(enemy_gen))
            elif cell["type"] == "Item":
                item = {"name": "Potion", "effect": 20}
                pick_item(player, item)
            elif cell["type"] == "Trap":
                player.health -= 15
                print("You stepped on a trap! Lost 15 HP")
            cell["visited"] = True
        if player.health <= 0:
            print("Restoring checkpoint...")
            player.health = player.max_health

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    try:
        name = input("Enter your player name: ")
        player = Player(name)
        game_map = generate_map(5)
        checkpoint = copy.deepcopy(player)
        game_loop(player, game_map)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("An error occurred. Check game.log")
