import threading, time, random

def spawn_treasure(game_map):
    while True:
        time.sleep(30)
        x, y = random.randint(0,len(game_map)-1), random.randint(0,len(game_map[0])-1)
        game_map[x][y]["type"] = "Item"
        print("\nA treasure appeared somewhere on the map!")

def start_background_events(game_map):
    threading.Thread(target=spawn_treasure, args=(game_map,), daemon=True).start()
