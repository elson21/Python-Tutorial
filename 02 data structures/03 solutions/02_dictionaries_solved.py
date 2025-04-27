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

goomba = {
    "name": "Goomba",
    "hp": 10,
    "attack": 3,
    "defense": 1,
    "element": "porcini"
}

# 🔍 Step 2: Print it out like a stat sheet.
# There are different ways to do it, but I would use a for loop.
# If you think you're better than me, do something else.

print(f"\n🧾 {goomba["name"]}'s stats:")
for stat, value in goomba.items():
    print(f" - {stat.capitalize()}: {value}")
print("\n===================================================\n")

# ⚔️ Step 3: Luigi stepped on it and the Goomba takes damage! Subtract 5 HP.
# Print if it's dead or alive (No hardcoding, use a conditional ;) )

dmg = 5
print(f"💥 {goomba['name']} takes {dmg} damage!")
if goomba['hp'] <= 0:
    print(f"{goomba['name']} is dead!")
elif goomba['hp'] > 0 and goomba['hp'] <= goomba['hp']/2:
    print(f"{goomba['name']} is injured!")
else:
    print(f"{goomba['name']} is still alive and kicking!")
print("\n===================================================\n")

# 🧌🧌 Step 4: Oh no, a second Goomba appeared, and it got a power up
# Give the second Goomba a temporary power-up (increase hp or attack by 2!)
power_up = 2
goomba['attack'] += power_up
print(f"🦾 {goomba['name']}'s attack has increased by {power_up}!")
print(f" - Attack: {goomba['attack']}")
print("\n===================================================\n")

# Luigi easily pwned the second Goomba and he entered the mansion

# 👹 Step 5: Now let’s create a second enemy — a Boo!
# Give it a name (obviously its name is Boo, duh), health points, attack, defense, and an element.
# Don't forget, Boos are ghosts!
boo = {
    "name": "Boo",
    "hp": 15,
    "attack": 4,
    "defense": 1,
    "element": "ghost"
}

# Now that we have two enemies, let's put them in a list, so that we don't forget about them.
# Create an empty list called "gallery", and append the two enemies.
gallery = []
gallery.append(goomba)
gallery.append(boo)

# 🧾 Step 7: Let's see how that turned out.
# Loop through each enemy and print their full stat sheet.
# That's gonna be a nested for loop for you.
for enemy in gallery:
    print(enemy['name'].capitalize())
    for stat, value in enemy.items():
        print(f" - {stat}: {value}")
print("\n===================================================\n")

# 🧠 Bonus Challenge:
# Add a third enemy called "Shy Guy" with custom stats.
# Prints out an enemy’s stats according to user input.
# Then simulate a turn-based battle between Luigi and Shy Guy! 
# - Each one should attack in turn until one runs out of hp.
# Let's see if you can do this, it's hard ;)

shy_guy = {
    "name": "Shy Guy",
    "hp": 17,
    "attack": 6,
    "defense": 2,
    "element": "none"
}

gallery.append(shy_guy)

enemy_name = input("Show me the stats of: ")

for enemy in gallery:
    if enemy_name.strip().lower() == enemy['name'].lower():
        print("\n", enemy['name'])
        for stat, value in enemy.items():
            print(f" - {stat}: {value}")
        break
else:    
    print("Enemy not discovered yet...\n")
print("\n===================================================\n")
    
# Create Luigi's stats    
luigi = {
    "name": "Luigi",
    "hp": 25,
    "attack": 7,
    "defense": 2,
    "element": "bro"
}

# Simulate combat
print("🎉 On the green corner, we have L-L-L-Luigi!!! 🎉")
print("🔥 And on the red corner, the fierce S-S-S-Shy Guy!! 🔥")
print("\n🥊 Time to D-D-D-DUEL! 🥊\n")

turn = 0
while True:
    print(f"💥 Turn {turn + 1} 💥")
    if turn == 0:
        print("\n👊 Luigi jumps on Shy Guy's head!")
        print("💥 Luigi draws first blood!\n")
    elif turn % 2 == 0:
        print(f"\n🌟 Luigi attacks Shy Guy, dealing {luigi['attack'] - shy_guy['defense']} damage!")
        shy_guy['hp'] -= luigi['attack'] - shy_guy['defense']
        print(f"💔 Shy Guy's remaining HP: {shy_guy['hp']}\n")
        if shy_guy['hp'] <= 0:
            print("🚨 Shy Guy is down! Luigi wins!!! 🚨\n")
            break
    else:
        print(f"\n⚡ Shy Guy headbutts Luigi right in the nuts, dealing {shy_guy['attack'] - luigi['defense']} damage!")
        luigi['hp'] -= shy_guy["attack"] - luigi['defense']
        print(f"💔 Luigi's remaining HP: {luigi['hp']}\n")
        if luigi["hp"] <= 0:
            print("💥 Luigi is down!!! 💥")
            print("🔥 Shy Guy wins!!! 🔥\n")
            break
    turn += 1
print("\n===================================================\n")



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

plunger = {
    "name": "Plunger",
    "type": "Weapon",
    "damage": 2,
    "durability": 10
}

# 🍄 Step 9: Make a Super Mushroom too.
# Give it:
# - name
# - type (consumable)
# - healing value
# - usage (one-time or reusable?)

super_mushroom = {
    "name": "Super Mushroom",
    "type": "Consumable",
    "healing": 5,
    "durability": 1
}

# 💼 Step 10: Make an empty list called `items`, and add both items to it.
# We want to keep track of all inventory gear just like we did with the enemies.

items = []
items.append(plunger)
items.append(super_mushroom)

# 🧾 Step 11: Print each item’s stats with a for loop.
# Use formatting to make it look cool. Bonus: use .title() and .capitalize() to clean up the stat names.
# It should look like this:
# Plunger:
#  - Type: Weapon
#  - Damage: 2
#  - Durability: 10

for item in items:
    print(f"{item['name'].title()}:")
    for stat, value in item.items():
        if stat == 'name': continue
        print(f" - {stat.capitalize()}: {value}")
    print("")
print("==================================================\n")

# 🧪 Step 12: Let’s simulate using the Mushroom.
# Decrease Luigi's HP and then "use" the item to heal him.
# You’ll need a variable like `luigi_hp = 8`, simulate the healing,
# and print how much HP he has after munching that mushroom.
# That's a 5 star difficulty, do you think you can code?

print("💥 Oh no, Luigi got hit in the face by a Bullet Bill and lost 17 hp!\n")
luigi['hp'] = 8
print(f"💚 Luigi's HP: {luigi['hp']}\n")

print(f"🍄 Luigi munches on a {super_mushroom['name']} and restores {super_mushroom['healing']}.\n")
luigi["hp"] += super_mushroom['healing']
super_mushroom['durability'] -= 1
print(f"💚 Luigi's HP: {luigi['hp']}")
print("\n==================================================")

# 🛠️ Step 13: The Plunger hits an enemy!
# Decrease its durability by 1, and print a message:
# “Plunger used! Durability now: X”
# If the durability hits 0, say it broke. R.I.P. 🪠

enemies_around = True
while enemies_around:
    print("🪠 Luigi whacks an enemy with his trusted plunger!")
    plunger['durability'] -= 1
    print(f"⚙️ Plunger used! Durability: {plunger['durability']}")
    if plunger['durability'] == 0:
        print(f"⚙️ The Plunger has broken... R.I.P.")
        break
print("\n==================================================")

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

# That's gonna keep you busy for a week... if you don't use ChatGPT ofc...