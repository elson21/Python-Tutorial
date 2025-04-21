# 03_loops.py

# Loops help us repeat stuff without copy-pasting code like a monkey.
# They are the "do this until you run out of memory" things.

# There are two types of loops in Python:
# 1. for loops - when you know how many times you want to repeat something
# 2. while loops - when you wanna repeat something until I say so

#########################################################################################
# for loops
# Let's loop through our pokemon team and print their names:
#########################################################################################

# team = ["Charizard", "Venusaur", "Snorlax", "Gengar", "Mewtwo", "Dragonite"]

# print("Your pokemon team:")
# for pokemon in team:
#     print(f"    - {pokemon}")

#########################################################################################
# You can also loop through a range of numbers using the range() function.
# This is useful when you want to repeat something a specific number of times
#########################################################################################

# for number in range(10):
#     print(f"{number}")

#########################################################################################
# Range is a function that you will use a lot in Python.
# It generates a sequence of numbers, starting from 0 by default, and ending at the number you specify (exclusive).

# Bonus: Why does range(5) stop at 4? Check the next example to find out (can you though?).
# range() can also be used in reverse order.
#########################################################################################

# print("\nCountdown to launch:")
# for number in range(5, 0, -1):
#     print(f"{number}")
# print("Liftoff!\n")

######################################### INFO ##########################################
# 'range(n)' gives 0 to n-1
# 'range(start, stop)' gives start to stop-1
# 'range(start, stop, step)' lets you count up or down
#########################################################################################
#########################################################################################
#########################################################################################
# While loops
# Let's say Marshal has 10 coins and he wants to buy a sandwich that costs 2 coins.
# After finishing his sandwich, Marshal buys another sandwich, until he runs out of coins.
#########################################################################################

# coins = 8
# sandwich_cost = 2
# while coins >= sandwich_cost:
#     print(f"Marshal buys a sandwich for {sandwich_cost} coins.")
#     coins -= sandwich_cost
#     print(f"Marshal has {coins} coins left.\n")
# print("Marshal is out of coins!")

#########################################################################################
# Be careful, while loops run forever, unless you stop them. It's easy to make a mistake!
# If you don't stop a while loop, it becomes an infinite loop.
# ⚠️ This means it will keep running forever, until you stop it manually (Ctrl+C in most terminals).
#########################################################################################
#########################################################################################
#########################################################################################
# Break and continue
# Sometimes you want to break out of a loop or skip an iteration.
# break : stops the loop
# continue: skip the current iteration and continue with the next one
#########################################################################################

# tall_grass = ["Ratata", "Pidgey", "Zubat", "Pikachu", "Meowth"]

# print("\nRed is looking for a Pikachu in the tall grass...\n")
# for pokemon in tall_grass:
#     if pokemon == "Pikachu":
#         print("A wild Pikachu appeared!\n")
#         break   # This will stop the loop when Pikachu is found
#     print(f"A {pokemon} is nice, but not what Red is looking for.")

# print("Red is looking for a Pokemon in the tall grass...\n")
# for pokemon in tall_grass:
#     if pokemon == "Pikachu":
#         continue    # This iteration will be skipped, we already have a Pikachu!
#     print(f"{pokemon} found, let's catch it!")

#########################################################################################
# Nested loops
# Let's combine loops with some conditions
#########################################################################################

# print("\nMario & Luigi's inventory check:")
# characters = ["Mario", "Luigi"]
# items = ["Mushroom", "Fire Flower", "Star"]

# for character in characters:
#     print(f"\n{character}'s inventory:")
#     for item in items:
#         print(f" - {item}")

#########################################################################################
# 🧪 Experiment Zone:
# Try these:
# - Add more powerups
# - Loop through your name letter by letter
# - Write a while loop that breaks when the user guesses a secret number

# Also try these:
# - Create three dream teams to beat the Elite Four (team = ["Fire Power", "Panzer Batalion", "Catch me if you can"])
# - Put 6 of the best Pokemon that you have tamed in each team
# - Print out the team names and their Pokemon

# Only for geniuses (don't try this if you're not one):
#   Write a while loop that asks the user to input a password until they get it right.
#   If they get it right, print "You are a genius!" and break the loop.
#########################################################################################