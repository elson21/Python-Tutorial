# 05_tuples_extended.py
#########################################################################################
# This is another demonstration on why tuples are important

# Scenario: Spawn Points in a Game

# Imagine you have a game where enemies spawn at specific places on a map.
# You don't want the locations themselves to ever change randomly — 
# you just want to add or remove spawn points if needed.
# ✅ So you use:
    # List → to add/remove entire spawn points.
    # Tuple → to lock each (x, y) coordinate.
# Let's see
#########################################################################################

# 🎮 Fixed enemy spawn points on a map
enemy_spawn_points = [
    ("Forest", (5, 10)),
    ("Castle Entrance", (12, 3)),
    ("Dungeon", (7, 14)),
    ("River", (1, 9))
]

print("\n===============================================================\n")

# 🚶‍♂️ A new wave of enemies is being spawned:
print("⚔️ Enemies are spawning at:")
for location, coords in enemy_spawn_points:
    print(f"- {location} at coordinates {coords}")

# ❌ Let's try to move the "Castle Entrance" spawn point (not allowed directly)
# enemy_spawn_points[1][1] = (0, 0)  # This would crash: tuple is immutable.

# ✅ Instead, if we REALLY want to move it, we replace the whole tuple:
enemy_spawn_points[1] = ("Castle Entrance", (15, 5))  # Moved the entrance!

print("\n🔄 Updated spawn points:")
for location, coords in enemy_spawn_points:
    print(f"- {location} at coordinates {coords}")

print("\n===============================================================\n")

# This gives a bunch of ideas for Luigi's adventure, right?