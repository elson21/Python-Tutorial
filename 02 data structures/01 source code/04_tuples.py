# 04_tuples.py
#########################################################################################
# Welcome to the World of Tuples!
#########################################################################################
# Tuples store ordered sequences of items, like lists, but with a twist.
# Once you create a tuple, it’s **immutable** — you can't change it after creation. Just like planets.
# I'm not sure about your age, but ever since I was born nothing has changed,
# and i'm pretty sure nothing will for the foreseeable future...
# Except if alliens attack a planet.# Shit I must take a look on the other planets

# Let's go on an adventure!

# FYI, tuples are created using parentheses ().
#########################################################################################

# Please remember this very serious fact:
# In Greek, tuples refers to a bunch of beautiful stars, called Πλειάδες.
# In English it literally means "a bunch of things"

# Let's make a list of planets, and check it twice.
print("\n===============================================================")
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

# Check 1:
print("Check 1: ", planets)

# Check 2:
print("\nCheck 2:")
for planet in planets:
    print(f" - {planet}")

print("\n===============================================================")
# I think these are all the planets of our solar system, right?
# At least according to Neil...

#########################################################################################
# Accessing elements
# Just like lists, tuples are indexed starting from 0. The first element is 0, the second is 1, and so on.

# Example:
# tuple = ("a", "b", "c")
# tuple[0] = "a"
# tuple[1] = "b"
# tuple[2] = "c"

# You can also access the last element using -1.
# tuple[-1] = "c"
# tuple[-2] = "b"
# tuple[-3] = "a"
#########################################################################################

# Intern's way
print("\n🚀 First planet:", planets[0])
print("🚀 Last planet:", planets[-1])

# Oh man, this is boring, i'll check all the indexes like a pro
# Also let's learn about enumerate().
# enumerate(planets) will return (index, planet)
# Try enumerate(planets, start=1)

# The pro way
print("Planet printer go brrrr...")
for index, planet in enumerate(planets):
    print(f"  At i[{index}] we can see planet {planet}")
print("\n===============================================================\n")

# Bonus: How can you print 'Mars' using negative indexing?

#########################################################################################
# Slicing tuples
# Slicing allows you to access a range of elements in a tuple.
# The syntax is tuple[start:stop], where start is inclusive and stop is exclusive.

# For example:
# planets[1:4] will return a tuple of Venus, Earth, and Mars.
# planets[::2] will return Mercury, Earth, and Jupiter.
# planets[1:4:2] will return Venus and Mars.
# Bonus if you explain why.
#########################################################################################

# Let's bunch the planets in BE and AE (before and after earth)
# But first of all, let's find where Earth is hidden
print(f"🌍 You can see a blue dot at i[{planets.index("Earth")}]")
print("\n🪐 Planets before the blue dot:")
for planet in planets[0:2]:
    print(f" - {planet}")

print("\n🌍 Planets after the blue dot: ")
for planet in planets[3:]:
    print(f" - {planet}")

print("\n===============================================================\n")

#########################################################################################
# Immutability
# You can't change the elements of a tuple once it's created. 
#########################################################################################

print("⚠️ Remember: tuples can't be modified after creation!")

# Please try to remove or add a planet. You can't can you?
# You though you were the simulation's master? Oops, turns out not...

print("\n===============================================================\n")

#########################################################################################
# Unpacking tuples
# Tuples love being unpacked into variables, making life easier.
# This is especially useful when you want to work with multiple variables at once.

# Let's talk about this before we start searching for alien bases on uranus.

# Here we make tuple called 'mission', and it has a bunch of items inside
mission = ("Apollo 11", "Neil Armstrong", "Buzz Aldrin", 1969)

# And here we assign a variable name to each of these items
# To make a short story long, we're doing this:
# mission_name = "Apollo 11"    # String
# astronaut1 = "Neil Armstrong" # String
# astronaut2 = "Buzz Aldrin"    # String
# year = 1969 # Integer
(mission_name, astronaut1, astronaut2, year) = mission

print(f"\n🌕 Mission {mission_name} launched in {year} with {astronaut1} and {astronaut2}.")

# You can also use underscores (_) to ignore some elements you don’t care about:
(x, y, _) = (100, 200, 300) # Never used it, but it may come in handy in the future
print("Coordinates:", x, y)

#########################################################################################
# Oh wait, another thing before we go on exploring. 
# Let's see how we could use tuples in real world cases
# Tuples are great for storing fixed collections of items, like coordinates, color codes, or high scores.

# 1. 2D Coordinates (Position in space for 2D beings!)
coordinates = (23.5, 54.2)
print(f"\n🛰️ Coordinates for 2D space station: {coordinates}")

# 2. RGB Color Codes (Space suit color)
space_suit_color = (255, 192, 203)  # A very manly color, right out of the Barbieverse
print("👨‍🚀 Space suit color (RGB):", space_suit_color)

# 3. High Scores (Top astronauts)
top_astronauts = (
    ("Neil Armstrong", 100),
    ("Buzz Aldrin", 95),
    ("Sally Ride", 90)
)

print("\n🎖️ Top astronauts by mission score:")
for astronaut, score in top_astronauts:
    print(f"{astronaut}: {score} points")
print("\n===============================================================\n")

# I'm too tired to go on an exploration now. I gotta take a siesta, you do the exploration.

#########################################################################################
# Bonus Challenge 🚀
# Search for alliens in our planets!
# Set up the coordinates like you did with with the astronauts.
# Then find some proper astronauts. I heard that Buzz Lightyear, Hal Jordan, and the Doctor are available today
# Now scan every planet according to their coordinates (for loop).
# If you find an allien run back home screaming...sorry I meant send a message to the HQ and move on.
# If empty, let out a sigh of relief, say how amazing you are, and scan the next planet.
# 
# If you're cool like me, you'll use the rand() method to put alliens in random planets.
#########################################################################################
# Tuple Cheatsheet
#########################################################################################

"""
✅ Tuples are immutable (can't be changed after creation).
✅ Use parentheses () to create them.
✅ Access elements by index: tuple[0]
✅ Slice them like lists: tuple[1:4]
✅ Unpack them into variables: (a, b, c) = tuple
✅ Great for fixed collections of items: coordinates, colors, database rows
"""
