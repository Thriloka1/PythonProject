# utils.py
import logging
import functools

logging.basicConfig(filename="logs/game.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def ability_limit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Using ability: {func.__name__}")
        logging.info(f"Ability used: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def print_map(game_map, player_position):
    for i, row in enumerate(game_map):
        row_str = ""
        for j, cell in enumerate(row):
            if (i,j) == player_position:
                row_str += " P "
            elif not cell["visited"]:
                row_str += " ? "
            else:
                if cell["type"] == "Enemy":
                    row_str += " E "
                elif cell["type"] == "Item":
                    row_str += " I "
                elif cell["type"] == "Trap":
                    row_str += " T "
                else:
                    row_str += " . "
        print(row_str)
    print("\n")
