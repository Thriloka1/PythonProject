# Adventure Quest

**Adventure Quest** is a master-level, text-based Python game where players explore procedurally generated 2D maps, battle unique enemies, collect and craft items, and complete dynamic quests. The project demonstrates advanced Python concepts including OOP, decorators, threading, generators, JSON save/load, deep copy checkpoints, and logging.

---

## Features

- **Procedurally Generated Maps** – Explore dynamic 2D grids with enemies, treasures, and traps.  
- **Advanced Combat System** – Turn-based battles with unique enemy behaviors, buffs/debuffs, and player abilities.  
- **Inventory & Crafting** – Manage items, combine resources, and strategically use buffs and healing.  
- **Persistent Progress** – Save/load game state using JSON and restore checkpoints with deep copies.  
- **Dynamic Events** – Threaded background events like treasure spawns and timed effects.  
- **Generators & Quests** – Procedurally generated quests and enemy spawns for replayability.  
- **Logging & Analytics** – Track player actions, errors, and game events.  
- **OOP & Advanced Python Concepts** – Demonstrates inheritance, decorators, lambdas, context managers, and modular design.



                ┌─────────────────────┐
                │  Start Game         │
                │ (adventure_quest.py)│
                └─────────┬───────────┘
                          │
              ┌───────────▼───────────┐
              │ Check savegame.json   │
              └───────┬───────────────┘
        Save Found?    │
       ┌───────────────┴───────────────┐
       │ Yes                           │ No
       ▼                               ▼
Load Player, Map, Quests       Generate New Map & Player
       │                               │
       └───────────────┬───────────────┘
                       ▼
             ┌─────────────────────┐
             │  Main Game Loop     │
             │  (Explore / Act)    │
             └─────────┬───────────┘
                       │
        ┌──────────────┼───────────────┐
        ▼              ▼               ▼
    Move Player    Enemy Encounter   Item Found
        │              │               │
        │          ┌───┴─────────┐     │
        │          │ Battle Mode │     │
        │          └───┬─────────┘     │
        │              │               │
        │        Win or Lose?          │
        │      ┌───────┴────────┐      │
        │      │ Win -> Gain XP │      │
        │      │ Lose -> Respawn│      │
        │      └────────────────┘      │
        │              │               │
        └───────┬──────┼──────┬────────┘
                │      │      │
                ▼      ▼      ▼
         Quest Progress  Inventory Updated
                │
                ▼
        ┌───────────────┐
        │ Quest Complete│
        │? Generate New │
        └───────┬───────┘
                │
                ▼
        ┌────────────────┐
        │ Save & Continue│
        └───────┬────────┘
                │
                ▼
         Quit -> Savegame.json Updated


The player starts a session by loading a save or starting fresh.

The main loop allows movement, combat, item collection, and quest progression.

Every action updates logs, inventory, and quest progress.

The game continues until the player quits, at which point it saves progress.
