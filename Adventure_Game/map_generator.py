import random

def generate_map(size):
    cell_types = ["Empty", "Enemy", "Item", "Trap"]
    return [[{"type": random.choices(cell_types, weights=[50,20,20,10])[0], "visited": False}
             for _ in range(size)] for _ in range(size)]
