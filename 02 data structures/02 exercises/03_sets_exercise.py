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

# 🎁 Step 2: Create another set called `items_found`.
# # Add some cool loot items Luigi finds in his travels:
# - Mushroom
# - Poltergust
# - Super Star
# - Mushroom (again, see what happens)
# Print the items too.

#########################################################################################

# 🧹 Step 3: Oh no, Luigi tripped and lost the Poltergust!
# Remove it from the `items_found` set using .discard().
# Print the set after that.

# 👻 Step 4: Luigi fights a Big Boo and wins!
# Remove Big Boo from the `enemies_encountered` set.
# Use .discard() for this one too — Luigi doesn't want a KeyError ruining his day.

# Now that I think about it, let's be more efficient, and put Big Boo in an enemies_defeated list
# We may use it... or not

#########################################################################################

# 💥 Step 5: New enemies spawn!
# There's a second wave: Shiny Skeleton and Vampirous Vampire appear.
# Add them to the `enemies_encountered` set using .update().

# 💎 Step 6: New loot appears!
# Luigi finds:
# - Gold Coin
# - Healing Herb
# Update the `items_found` set with these new treasures.

#########################################################################################

# 🔍 Step 7: Let's do a security check.
# Print:
# - How many enemies Luigi has faced so far (hint: len())
# - How many items Luigi has collected so far

# Bonus: Print "Ready!" if there are more items than enemies.

#########################################################################################

# 🎲 Step 8: Let's simulate a rare case where Luigi clears a whole area.
# Clear both sets with .clear().
# Then print both sets to confirm they’re empty.

# Bonus: Print a dramatic message like:
# "Luigi: 'The forest is clear... for now.'"

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
