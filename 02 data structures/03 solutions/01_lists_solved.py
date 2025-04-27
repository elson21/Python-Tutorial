# 01_lists_solved.py
#########################################################################################
# 🎮 Managing Luigi's Inventory
# Alright, we learned new stuff. Now we’re going to use them to help Luigi manage his gear.

# Luigi is about to go find his brother, who was kidnapped by King Boo.
# He’s got a bag full of gear, and we need to help him organize it.
# We’ll be using lists to keep track of his inventory. Let’s get started!
#########################################################################################

# 🟢 Step 1: Create a list, called `inventory`, and add things that Luigi may need.
# For example:
# A Poltergust, a flashlight, a mushroom, a plunger, and a bone.
# Then print those items to make sure we put them in bag.
inventory = ['Poltergust', 'flashlight', 'mushroom', 'plunger', 'bone']
print("\nLuigi starts with: ", inventory)

# ✂️ Step 2: Luigi is on his way to the Boo Woods, and he wants to check his bag.
# Print the first three items in his bag.
print("\nMy first three items are: ", inventory[:3])

# So far so good. We pwned some ghosts, and we have some moneys to spend.
# 🛠️ Step 3: Let's upgrade the Plunger to a Golden Plunger!
print("\nMoney used!")
old_item = inventory[3]
inventory[3] = "Golden Plunger"
print(f"{old_item.capitalize()} upgraded to {inventory[3]}!")

# Bonus: What does the capitalize() method do?

# Nice! Now print that Golden Plunger to admire it.
# Also print the entire list one more time, I wanna see if everything is still there.
print(f"\n{inventory[3]}, my precious!")
print(f"\nWhat's in here now: {inventory}")

# While running through the woods, Luigi found a Super Star! Let's toss it in.
# ➕ Step 4: Luigi found a Super Star! Throw it in the bag.
inventory.append("Super Star")
print("\nUpdate inventory: ", inventory)

# Oh look, a Dark Light Device! Let's put this at the front of the bag.
inventory.insert(0, "Dark Light Device")
print("\nUpdate inventory: ", inventory)

# Bling: Mushroom used!
# ❌ Step 5: Oops. Mushroom used — remove it.
print(f"\nUsed: Mushroom!")
inventory.remove("mushroom")
print("\nUpdate inventory: ", inventory)

# Let's check our inverntory again.
# ...
# Oh no! We dropped the Bone, I must remove it from the list.
inventory.remove("bone")
print("\nUpdate inventory: ", inventory)

# 🔁 Step 6: Let’s go through his stuff one by one, to make sure that everything is here.
# Loop through the inventory and print the items one by one.
print("\nLuigi's Inventory:")
for item in inventory:
    print(" - ", item)

# 📏 Step 7: How packed is that bag?
print("\nInventory Size: ", len(inventory))

# Looks ok... but the order confuses me!
# 🔤 Step 9: Let’s get it sorted (alphabetically), then reverse it.
sorted_inventory = sorted(inventory)
print("\nSorted by abc: ", sorted_inventory)
sorted_inventory.reverse()
print("\nSorted and reversed: ", sorted_inventory)

# Bonus: Why is this not entirely correct? Can you make it perfect?

#########################################################################################
# 🧠 Recap:
# - You created an inventory of items
# - You managed to change, add, and remove items
# - You used slicing, loops, and sorting
# - You kept things organized no matter what happened on the way
# - You even reversed the order like a boss

# If you can’t help Luigi, then who can?! 🔥

# Bonus: Can you name all the methods you used in the recap?
## Yes I can, but I won't show you ;)
#########################################################################################