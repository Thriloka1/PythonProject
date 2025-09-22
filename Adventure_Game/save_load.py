import json
import logging

def save_game(player, game_map, filename="checkpoints/savegame.json"):
    try:
        with open(filename, "w") as f:
            json.dump({"player": player.__dict__, "map": game_map}, f,indent=4,          # Pretty print
                sort_keys=True )
        print("Game saved!")
    except Exception as e:
        logging.error(f"Error saving game: {e}")

def load_game(filename="checkpoints/savegame.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            from player import Player
            player = Player(data["player"]["name"])
            player.__dict__.update(data["player"])
            return player, data["map"]
    except Exception as e:
        logging.error(f"Error loading game: {e}")
        return None, None
