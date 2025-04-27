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

#########################################################################################
# 💥 Step 2: Create Mario's coordinates.
# Mario is off doing something else. Let's set his coordinates.
# Use a tuple like you did for Luigi.

mario_coordinates = (10, 7)
print(f"🏃‍♂️ Mario is at standing at {mario_coordinates}")
print("\n===============================================================\n")

#########################################################################################
# 🧩 Step 3: Calculate the distance between Luigi and Mario.
# You can use the formula for distance in a 2D grid:
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
# Use the math module to do this!

import math
distance = math.sqrt((mario_coordinates[0] - luigi_coordinates[0]) ** 2 +
                     (mario_coordinates[1] - luigi_coordinates[1]) ** 2)
print(f"📏 Mario is standing {distance:.2f} meters from Luigi.")

# Can you find out what .2f does?
print("\n===============================================================\n")

#########################################################################################
# 🧭 Step 4: Swap their positions! 
# Use tuple unpacking to swap Luigi and Mario’s coordinates.

luigi_coordinates, mario_coordinates = mario_coordinates, luigi_coordinates
# This does the following in the background:
# temp = (mario_coordinates, luigi_coordinates) # Creates a temporary tuple
# luigi_coordinates = temp[0]
# mario_coordinates = temp[1]

print(f"🔄 Now Luigi is at {luigi_coordinates}.")
print(f"🔄 Mario is at {mario_coordinates}.")
print("\n===============================================================\n")

#########################################################################################
# 👾 Step 5: Create a list of coordinates.
# Let’s create a list of 3 other characters, each with their own coordinates.
# Use tuples for each character's position.

characters_coordinates = [
                        (("Yoshi"), (3, 5)), 
                        (("Princess Peach"), (8, 2)), 
                        (("Bowser"), (12, 9))
                        ]           
print("👾 Character Positions: ")
for character, coords in characters_coordinates:
    print(f" - {character} is at {coords}")

print("\n===============================================================\n")

#########################################################################################
#Let's test the immutability of lists and tuples

print("Yoshi is at location ", characters_coordinates[0][1])
# characters_coordinates[0][1] = ((11, 8)) # Try to change the coordinates of Yoshi. You can't, he doesn't want to be moved!

# In order to move him, you have to replace the entire tuple with a new one. Let's see.
print(characters_coordinates[0]) # This is Yoshi and his coords
characters_coordinates[0] = (("DK Jr."), (3, 5))
print(characters_coordinates[0]) # Bye bye Yoshi
print("\n===============================================================\n")

# As you can see, combining mutable (lists) with immutable (tuples) gives you the best of both worlds:
#    - You can grow/shrink/change the outer list.
#    - You protect the inner data from accidental edits and interns.


#########################################################################################
#Let's test the immutability of lists and tuples

print("Yoshi is at location ", characters_coordinates[0][1])
# characters_coordinates[0][1] = ((11, 8)) # Try to change the coordinates of Yoshi. You can't, he doesn't want to be moved!

# In order to move him, you have to replace the entire tuple with a new one. Let's see.
print(characters_coordinates[0]) # This is Yoshi and his coords
characters_coordinates[0] = (("DK Jr."), (3, 5))
print(characters_coordinates[0]) # Bye bye Yoshi
print("\n===============================================================\n")

#########################################################################################
# Let's see some more examples that may help you
# They are not necessarily tuples, but they will help

print("\n###############################################################")
print("Tips and tricks to help tuples")
print("###############################################################\n")

# 1. Swapping 3 elements
a, b, c = 1, 2, 3   # This is valid in python
print(f"a = {a}, b = {b}. c = {c}\n")

a, b, c, = c, a, b  # Swap them
print(f"a = {a}, b = {b}. c = {c}")
print("\n###############################################################\n")

# 2. Splitting a tuple
# This is some advanced shit, it's ok if you don't get it at first
pokemons = ("Charmander", "Bulbasaur", "Squirtle", "Pikachu", "Eevee", "Mew")
for index, pokemon in enumerate(pokemons, start=1):
    print(f"👹 - Pokemon {index}: {pokemon}")
print("\nThis is ", pokemons[2])

print("\n-----------------------------------------------------------------\n")

# Try this, it's easier
# Add more coordinates, and iterate through them
coordinates = (100, 200)

x, y = coordinates

print(x)  # 100
print(y)  # 200
print("\n###############################################################\n")

# 3. Ignoring values using "_"
player_name, _, player_score = ("Luigi", "Green", 121)
print(player_name)
print(player_score)

# How this helps? Well, you are unpacking the tuple ("Luigi", "Green", 121) to:
# player_name = "Luigi"
# _ = "Green"
# player_score = 121
# When you are unpacking a tuple, it needs a variable for each item, so "_" acts
# as a placeholder for the item "Green", otherwise Python would complain

# Extended unpacking
# As mentioned earlier, "_" is just a placeholder, so you can actually put anything instead of "_"
# By using the asterisk (*), or else known as "wildcard", is like saying "everything"
# Example:

first_guardian, *_, last_guardian = ("Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Merry", "Pipin")
# You are saying to python that you only care about the first and last element.

print("\n", first_guardian)
print(_)
print(last_guardian)

# Now let's change the "_" placeholder to something that makes more sense
first_potus, *middle_potus, last_potus = ("Washington", "Adams", "Jefferson", "A bunch of others", "Lincoln", "Biden", "Trump")

print(f"\nFirst president of the USA was {first_potus}.")
print(f"Then there were some more ({middle_potus}).")
print(f"Current guy is {last_potus}.")

print("\n===============================================================\n")

#########################################################################################
# As you can see, the combination of lists and tuples is powerful!
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
