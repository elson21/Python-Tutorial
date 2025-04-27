# 02_dictionaries_exercise.py
#########################################################################################
# 🧠 Enemy Stat System (with Dictionaries)
# Welcome to the stat system! Lists were great for ordered stuff,
# but now we need something smarter: something that can *label* things.
# Enter: dictionaries. They let you give names to values.

# You’re going to use dictionaries to give enemies and items their stats:
# - HP (Hit Points)
# - Attack
# - Defense
# - Element Type
#########################################################################################

# 🧌 Step 1: Make a Goomba.
# Give it HP, attack, defense, and element type.
# Hint: A dictionary can be declared as:
# dictionary = { 
#     "key 1": "value 1"
#     "key 2": value_2
# }

# Give that Goomba 
# - a name, 
# - health points, 
# - attack, defense, 
# - and an element (I'm a badass mushroom bro!).

# 🔍 Step 2: Print it out like a stat sheet.
# There are different ways to do it, but I would use a for loop.
# If you think you're better than me, do something else.

# ⚔️ Step 3: Luigi stepped on it and the Goomba takes damage! Subtract 5 HP.
# Print if it's dead or alive (No hardcoding, use a conditional ;) )

# 🧌🧌 Step 4: Oh no, a second Goomba appeared, and it got a power up
# Give the second Goomba a temporary power-up (increase hp or attack by 2!)

# Luigi easily pwned the second Goomba and he entered the mansion

# 👹 Step 5: Now let’s create a second enemy — a Boo!
# Give it a name (obviously its name is Boo, duh), health points, attack, defense, and an element.
# Don't forget, Boos are ghosts!

# Now that we have two enemies, let's put them in a list, so that we don't forget about them.
# Create an empty list called "enemies", and append the two enemies.

# 🧾 Step 7: Let's see how that turned out.
# Loop through each enemy and print their full stat sheet.
# That's gonna be a nested for loop for you.

# 🧠 Bonus Challenge:
# Add a third enemy called "Shy Guy" with custom stats.
# Print out an enemy’s stats according to user input. 
#  - Hint: use strip(), lower() and a for-else loop (yup, you read that correctly).
# Then simulate a turn-based battle between Luigi and Shy Guy! 
# - Each one should attack in turn until one runs out of hp.
# - Hint: You must create Luigi's stats ;)
# Let's see if you can do this, it's hard ;)

# You thought this was over, didn't you?

# Part 2: Surprise!
#########################################################################################
# 🎒 Item Stat System (with Dictionaries)
# Enemies are cool, but Luigi also needs ITEMS to survive in this haunted mess.
# Now you’ll make dictionaries for gear and consumables.
# We’re talking weapons, potions, maybe even a spooky vacuum cleaner.
#########################################################################################

# 🪠 Step 8: Let’s make an item — the Plunger.
# It’s not just a toilet tool anymore. Give it:
# - name
# - type (weapon, consumable, key item, etc)
# - damage (if applicable)
# - durability

# 🍄 Step 9: Make a Super Mushroom too.
# Give it:
# - name
# - type (consumable)
# - healing value
# - usage (one-time or reusable?)

# 💼 Step 10: Make an empty list called `items`, and add both items to it.
# We want to keep track of all inventory gear just like we did with enemies.

# 🧾 Step 11: Print each item’s stats with a for loop.
# Use formatting to make it look cool. Bonus: use .capitalize() to clean up the stat names.

# 🧪 Step 12: Let’s simulate using the Mushroom.
# Decrease Luigi's HP and then "use" the item to heal him.
# You’ll need a variable like `luigi_hp = 8`, simulate the healing,
# and print how much HP he has after munching that mushroom.
# That's a 5 star difficulty, do you think you can code?

# 🛠️ Step 13: The Plunger hits an enemy!
# Decrease its durability by 1, and print a message:
# “Plunger used! Durability now: X”
# If the durability hits 0, say it broke. R.I.P. 🪠

# 🧠 Bonus:
# - Add a new item: “Dark Light Device” that doesn’t do damage but reveals hidden doors.
# - Give items rarity levels (common, rare, epic) and sort them by rarity.

# Actually you know what? Go back to the lists exercise and make all the items in the bag!

#########################################################################################

# You survived the Mansion of Dictionaries!
# You now know how to:
# - Create and update dictionaries for both enemies and items
# - Organize them in lists
# - Simulate usage and effects
# - Loop through nested structures and print clean stat sheets
# - Start thinking like a game developer 👾

# I get a bonus, you get a bonus, the Goomba gets a bonus...
# EVERYBODY GETS A BONUS!!!

# 🔥 Bonus Bonus:
# Build an actual inventory system that lets the player “equip” an item or “use” one in battle.
# But only if you’re not afraid of the dark…

# That's gonna keep you busy for a week... if you don't use ChatGPT ofc...