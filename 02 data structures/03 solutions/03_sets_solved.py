# 03_sets_exercise.py
#########################################################################################
# 🧠 Unique Enemies & Loot (with Sets)
# We learned that sets make sure no duplicates sneak into our data.
# Now that Luigi is OP, he doesn't find small fries anymore. He fights bosses!
# All the enemies he encoutners are Leaders, and there is only one leader for each species.
#########################################################################################

# 👾 Step 1: Create a set called `enemies_encountered`.
# Add some enemies Luigi might meet in a haunted forest:
# - Grand Goomba
# - Big Boo
# - Super Shy Guy
# - Grand Goomba (twice... to see if it duplicates)
# Then print the set to confirm no duplicate Goombas exist.

enemies_encountered = {"Grand Goomba", "Big Boo", "Super Shy Guy", "Grand Goomba"}
print("\n===============================================================\n")
print("👾 Enemies encountered: ")
for enemy in enemies_encountered:
    print(f" - {enemy}")

print("\n===============================================================\n")

# 🎁 Step 2: Create another set called `items_found`.
# Add some cool loot items Luigi finds in his travels:
# - Mushroom
# - Poltergust
# - Super Star
# - Mushroom (again, see what happens)
# Print the items too.

items_found = {"Mushroom", "Poltergust", "Super Star", "Mushroom"}
print("🛠️ Items found: ")
for item in items_found:
    print(f" - {item}")

print("\n===============================================================\n")
#########################################################################################

# 🧹 Step 3: Oh no, Luigi tripped and lost the Poltergust!
# Remove it from the `items_found` set using .discard().
# Print the set after that.

items_found.discard("Poltergust")
print("🧮 Inventory: ")
for item in items_found:
    print(f" - {item}")

print("\n===============================================================\n")

# 👻 Step 4: Luigi fights a Big Boo and wins!
# Remove Big Boo from the `enemies_encountered` set.
# Use .discard() for this one too — Luigi doesn't want a KeyError ruining his day.

# Now that I think about it, let's be more efficient, and put Big Boo in an enemies_defeated list
# We may use it... or not

enemies_defeated = []   # Create a list with defeated enemies
enemy_defeated = "Big Boo"  # Save a defeated enemy
enemies_encountered.discard(enemy_defeated)   # Remove it from the set
enemies_defeated.append(enemy_defeated)   # Save it in the list with defeated enemies

print("👾 Enemies left to defeated:")
for enemy in enemies_encountered:
    print(f" - {enemy}")

print("\n☠️ Enemies defeated:")
for enemy in enemies_defeated:
    print(f" - {enemy}")

print("\n===============================================================\n")

#########################################################################################

# 💥 Step 5: New enemies spawn!
# There's a second wave: Shiny Skeleton and Vampirous Vampire appear.
# Add them to the `enemies_encountered` set using .update().

enemies_encountered.update({"Shiny Skeleton", "Vampirous Vampire"})
print("👾 Oh no, more enemies are coming!")
print("I am now against: ")
for enemy in enemies_encountered:
    print(f" - {enemy}")

# Bonus: Go into the documentation of sets and find another way to use .update()!

print("\n===============================================================\n")


# 💎 Step 6: New loot appears!
# Luigi finds:
# - Gold Coin
# - Healing Herb
# Update the `items_found` set with these new treasures.

items_found.update({"Gold COin", "Healing Herb"})
print("🧃 Oh lala, I found more items!")
print("Inventory:")
for item in items_found:
    print(f" - {item}")

print("\n===============================================================\n")

#########################################################################################

# 🔍 Step 7: Let's do a security check.
# Print:
# - How many enemies Luigi still has to face? (hint: len())
# - How many items Luigi has collected so far

print(f"👾 Luigi still has to go over {len(enemies_encountered)} enemies to find his brother! 👀")
print(f"💥 Good news though, he has already stomped on {len(enemies_defeated)} enemies!")
print(f"🎒 He still has {len(items_found)} items left in his inventory, so he feels safe.")

print("\n===============================================================\n")

# Bonus: Print "Ready!" if there are more items than enemies.

#########################################################################################

# 🎲 Step 8: Let's simulate a rare case where Luigi clears a whole area.
# Clear both sets with .clear().
# Then print both sets to confirm they’re empty.

enemies_encountered.clear() # Enemies are defeated
items_found.clear() # All items are used up
print("💢 It's been a brutal combat, there are stomped enemies all over the place...")
print("🍄 You can see a half-munched mushroom in a corner, and a broken Super Star that lost its shine. 💫")
print("\n🎵 Sad and lonely music plays... 🎶\n")
print("Luigi managed to overcome his hurdles, and is now united with his brother.")
print("\n- Luigi: The forest is finally clear...")
print("\n- Mario: For now... 👀")

# Bonus: Print a dramatic message like:
# "Luigi: 'The forest is clear... for now.'"

print("🥁 Doom...")
print("🥁 Dam...")
print("🥁 Badoom..")
print("\nThere are drums in the deep...")
print("\n👹 Something is coming... Run! 🏃💨")

#########################################################################################

# 🧠 Bonus Bonus:
# Create a third set called `special_items`:
# - Gold Coin
# - Healing Herb
# - Dark Light Device

# Find:
# - Which items Luigi found that are *not* special (use .difference()).
# - Which items are shared (use .intersection()).
# - All unique items combining both sets (use .union()).

# Write a short message for each result, like:
# "Items Luigi found that are NOT special:", etc.

#########################################################################################

# 🏁 Recap:
# - You used sets to guarantee no duplicates.
# - You added and removed items safely.
# - You checked sizes, intersections, differences, and unions.
# - You learned how to control chaos with a simple data structure.
# - You protected Luigi's world from infinite Goombas. Respect.
