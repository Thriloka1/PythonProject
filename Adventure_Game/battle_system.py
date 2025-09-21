import random
from player import Player
from player import logging

def damage(attack, defense):
    return max(0, attack - defense)

def fight(player, enemy):
    print(f"\nA wild {enemy.name} appeared! HP: {enemy.health}")
    while player.health > 0 and enemy.health > 0:
        action = input("Choose action (attack/heal/run): ").lower()
        if action == "attack":
            dmg = damage(random.randint(5,15), 0)
            enemy.health -= dmg
            print(f"You dealt {dmg} damage to {enemy.name}")
        elif action == "heal":
            player.health = min(player.max_health, player.health + 20)
            print(f"You healed 20 HP!")
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
        logging.warning(f"{player.name} died during battle")
