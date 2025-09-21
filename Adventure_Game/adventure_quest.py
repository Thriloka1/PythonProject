from player import Player
from map_generator import generate_map
from battle_system import fight
from inventory import pick_item
from events import start_background_events
from save_load import save_game, load_game
from enemy import enemy_generator
from quests import quest_generator, check_quest_completion, get_random_quest
from utils import print_map, ability_limit
import copy


# -----------------------------
# Example Special Ability
# -----------------------------
@ability_limit
def heal(player, amount):
    player.health = min(player.max_health, player.health + amount)
    print(f"{player.name} healed for {amount} HP!")


# -----------------------------
# Main Game Loop
# -----------------------------
def game_loop(player, game_map):
    enemy_gen = enemy_generator()
    quests = quest_generator()
    current_quest = next(quests, None)
    start_background_events(game_map)

    while True:
        print(f"\nPlayer: {player.name}, HP: {player.health}, Inventory: {player.inventory}")
        if current_quest:
            print(f"Current Quest: {current_quest['description']}")
        print_map(game_map, player.position)

        move = input("Move (up/down/left/right) or quit/heal: ").lower()
        if move == "quit":
            save_game(player, game_map)
            print("Game saved! Goodbye.")
            break
        elif move == "heal":
            heal(player, 20)
            continue

        # Move player
        player.move(move, game_map)
        x, y = player.position
        cell = game_map[x][y]

        if not cell["visited"]:
            if cell["type"] == "Enemy":
                fight(player, next(enemy_gen))
            elif cell["type"] == "Item":
                pick_item(player, {"name": "Potion", "effect": 20})
            elif cell["type"] == "Trap":
                player.health -= 15
                print("You stepped on a trap! Lost 15 HP")
            cell["visited"] = True

        # Check quest completion
        if current_quest and check_quest_completion(player, current_quest):
            print(f"Quest Completed: {current_quest['description']}")
            current_quest = next(quests, get_random_quest())

        # Restore checkpoint if player dies
        if player.health <= 0:
            print("You died! Restoring checkpoint...")
            player.health = player.max_health


# -----------------------------
# Game Entry Point
# -----------------------------
if __name__ == "__main__":
    name = input("Enter your player name: ")
    player = Player(name)
    game_map = generate_map(5)
    checkpoint = copy.deepcopy(player)
    game_loop(player, game_map)
