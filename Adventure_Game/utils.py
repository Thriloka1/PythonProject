import logging
import functools
import time

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(filename="logs/game.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# -----------------------------
# Decorators
# -----------------------------
def ability_limit(func):
    """Decorator to announce ability usage."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Using ability: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Ability used: {func.__name__}")
        return result
    return wrapper

def timed_event(interval):
    """Decorator to repeat a function every 'interval' seconds."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            import threading
            def run_event():
                while True:
                    func(*args, **kwargs)
                    time.sleep(interval)
            t = threading.Thread(target=run_event, daemon=True)
            t.start()
        return wrapper
    return decorator

# -----------------------------
# Helper Functions
# -----------------------------
def print_map(game_map, player_position):
    """Prints a simple representation of the map with the player position."""
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
