# quests.py

import random

def quest_generator():
    quests = [
        {"type": "collect", "target": "Potion", "amount": 3, "description": "Collect 3 potions"},
        {"type": "defeat", "target": "Goblin", "amount": 5, "description": "Defeat 5 goblins"},
        {"type": "explore", "target": "map", "amount": 10, "description": "Explore 10 new locations"}
    ]
    for quest in quests:
        yield quest

def check_quest_completion(player, quest):
    if quest["type"] == "collect":
        return player.inventory.get(quest["target"], {}).get("count", 0) >= quest["amount"]
    # Add more logic for other quest types if needed
    return False

def get_random_quest():
    quest_types = ["collect", "defeat", "explore"]
    quest_type = random.choice(quest_types)
    if quest_type == "collect":
        return {"type": "collect", "target": "Potion", "amount": random.randint(1,5),
                "description": "Collect some potions"}
    elif quest_type == "defeat":
        return {"type": "defeat", "target": "Goblin", "amount": random.randint(1,3),
                "description": "Defeat some goblins"}
    else:
        return {"type": "explore", "target": "map", "amount": random.randint(3,8),
                "description": "Explore unknown areas"}
