def pick_item(player, item):
    if item["name"] in player.inventory:
        player.inventory[item["name"]]["count"] += 1
    else:
        player.inventory[item["name"]] = {"count":1, "effect": item["effect"]}
    print(f"Picked up {item['name']}! Current inventory: {player.inventory}")
