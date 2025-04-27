# 04_tuples_exercise.py
#########################################################################################
# 🧠 Coordinate System (with Tuples)
# Lists and dictionaries are great, but sometimes you need something immutable:
# Enter: tuples. They let you store data that you don't want to change.
# Let's make coordinates for Luigi and Mario!

#########################################################################################

# 🧌 Step 1: Create Luigi's coordinates.
# Let’s say Luigi is standing at a location in a 2D grid.
# Use a tuple to store his (x, y) coordinates.

luigi_coordinates = (2, 3)
print(f"🚶‍♂️ Luigi is standing at {luigi_coordinates}.")
print("\n===============================================================\n")


# 💥 Step 2: Create Mario's coordinates.
# Mario is off doing something else. Let's set his coordinates.
# Use a tuple like you did for Luigi.

mario_coordinates = (10, 7)
print(f"🏃‍♂️ Mario is at coordinates: {mario_coordinates}")

print("\n===============================================================\n")

# 🧩 Step 3: Calculate the distance between Luigi and Mario.
# You can use the formula for distance in a 2D grid:
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
# Use the math module to do this!

import math
distance = math.sqrt((mario_coordinates[0] - luigi_coordinates[0]) ** 2 + (mario_coordinates[1] - luigi_coordinates[1]) ** 2)
print(f"📏 The distance between Luigi and Mario is {distance:.2f} units.")

print("\n===============================================================\n")

# 🧭 Step 4: Swap their positions! 
# Use tuple unpacking to swap Luigi and Mario’s coordinates.
luigi_coordinates, mario_coordinates = mario_coordinates, luigi_coordinates
print(f"🔄 After the swap, Luigi is now at: {luigi_coordinates}")
print(f"🔄 After the swap, Mario is now at: {mario_coordinates}")

print("\n===============================================================\n")

# 👾 Step 5: Create a list of coordinates.
# Let’s create a list of 3 other characters, each with their own coordinates.
# Use tuples for each character's position.

character_coordinates = [("Yoshi", (3, 5)), ("Princess Peach", (8, 2)), ("Bowser", (12, 9))]
print("👾 Character positions: ")
for character, coords in character_coordinates:
    print(f"{character} is at {coords}")

print("\n===============================================================\n")

# 🧮 Step 6: Create a function that checks if two characters are at the same position.
# The function should take two tuples and return True if they are the same.

def are_coordinates_same(coords1, coords2):
    return coords1 == coords2

# Test the function
print(f"Are Luigi and Mario at the same position? {are_coordinates_same(luigi_coordinates, mario_coordinates)}")

print("\n===============================================================\n")

# 🧠 Bonus Challenge:
# Make a function that calculates the Manhattan distance (sum of the absolute differences of their coordinates).
# Hint: Manhattan distance = |x2 - x1| + |y2 - y1|

def manhattan_distance(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])

manhattan_dist = manhattan_distance(luigi_coordinates, mario_coordinates)
print(f"🏙️ The Manhattan distance between Luigi and Mario is {manhattan_dist} units.")

print("\n===============================================================\n")

# 🏁 Recap:
# - You used tuples to store immutable data (coordinates).
# - You calculated distances using math functions.
# - You learned to swap values and use functions to compare data.
# - You organized multiple tuples in a list for easy access.
# - You got a feel for using immutable data structures in a game world! 🎮

# Tuples are powerful because they can't be changed accidentally — they’re your trusty sidekicks in coding.
# Luigi and Mario might not always be in the same place, but you can always count on tuples to help you keep track of their coordinates!

# 🔥 Bonus Bonus:
# Extend the program with an inventory system where each item has coordinates as well.
# Maybe Yoshi's Egg, or Princess Peach’s Toadstool — but the twist is: items also have positions!
# Think of it like a game where items drop at specific coordinates and you have to reach them.
