#03_sets.py
#########################################################################################
# Sets are unordered collections of unique elements.
# Sets automatically remove duplicates and don't maintain the order of elements.
# Think of them as a menu on a restaurant. Would you put Linguine alla Carbonara twice? 
# Well I'm not even gonna answer that...

# A set is created using curly braces {} or the set() constructor.

# Let's see how sets could help us manage a traditional Italian restaurant!
#########################################################################################

print("\n===============================================================\n")
dishes = {"Pasta alla Carbonara", "Ossobuco alla Milanese", "Caponata", "Cacciucco", "Agnolottu del Plin"}
print("🍝 Today's Menu: ", dishes)

# The chef said he made another dish today. Let's add it to the menu using the .add() method!
dishes.add("Caponata")
print("\nRevised Menu: ", dishes)
print("\n===============================================================\n")

# Wait, what happened?
# Ah yes, we added the wrong dish. It's a good thing that sets helped us!
dishes.add("Tiramisu")
print("Really revised menu: ", dishes)
print("\n===============================================================\n")

# Btw, let's clarify something
empty_set = set()   # This is a set
empty_not_set = {}  # This is not a set (Bonus: what is this?)
print(type(empty_set))
print(type(empty_not_set))

# Just a reminder, cause you're definitely gonna make this mistake a couple dozen of times.
# Use set() to create an empty set, or variable = {<add stuff in here>} to create a set with elements

print("\n===============================================================\n")

#########################################################################################
# Accessing elements
# Sets are unordered, so you cannot access elements by index like lists.
# However, you can loop through the set to access its items.
#########################################################################################

print("Let's loop through the menu:")
for dish in dishes:
    print(f"- {dish}")

# Run this loop 3-4 times. Do you notice something weird.
# Teap the order changes every time. That's because, as we said, sets are unordered lists!
print("\n===============================================================\n")

# Bonus: What would happen if you try to access dishes[0]?

#########################################################################################
# Let's go through some sets operations
# FYI we already saw the .add() method
#########################################################################################
# Removing items
# You can remove items from a set using .remove() or .discard().
# .remove() raises a KeyError if the item doesn't exist, while .discard() won't raise an error.
# You can also use .pop() to remove an arbitrary item from the set (since sets are unordered).
#########################################################################################

# I wonder why the following codeblock is commented.
# I'll uncomment and run it.

# print("Mister manager says that we are losing money from that damn fish soup.\n")
# print("Removing 'Cacciucco' from the menu...")
# dishes.remove("Cacciuco")
# print("Updated menu:", dishes)

# Oh no, my code doesn't work!
# Oh no, oh god no no no, my life is destroyed!!
# Calma... it's the .remove method that's popping an error! 
# Just comment the code block and move on, sheesh...

print("Let's try removing an item using .discard()...")
dishes.discard("Caponata")  # No error if the item is missing.
print("Set after trying to remove 'Caponata':", dishes)

print("\n===============================================================\n")


#########################################################################################
# Membership
# You can check if an item is in a set using the 'in' keyword, just like with lists.
#########################################################################################

print("Is 'Tiramisu' in the menu?", "Tiramisu" in dishes)
print("Is 'Caponata' in the set?", "Caponata" in dishes)
# Bonus: Instead of "True" or "False", make it print "Yes" or "No"
print("\n===============================================================\n")

#########################################################################################
# Set Operations
# You can perform operations like union, intersection, and difference between sets (These are math operations in math sets).


# You're still here after reading the word math? Nice, I like you, let's move on!

# These operations return new sets and don't modify the original sets.
#########################################################################################
#Let's go through some sets operations
# Union (combining sets)
# Union combines all unique elements from two sets.
# Example: set1.union(set2) or set1 | set2
#########################################################################################

# Time to get serious. Proper menus have more stuff in them:
# - antipasti
# - salads
# - main course
# - desserts
# Bonus: If you feel like getting your first Michelin star, also add drinks.
# Let's create some sets to make a proper menu.-+

antipasti = {"Bruschetta al Pomodoro", "Prosciutto e Melone", "Carpaccio di Manzo", "Fiori di Zucca Ripieni", "Arancini"}
salads = {"Insalata Caprese", "Panzanella", "Insalata di Polpo", "Insalata di Finocchi e Arance", "Insalata Verde"}
main_course = {"Ossobuco alla Milanese", "Agnolotti del Plin", "Caponata", "Pasta alla Carbonara", "Pasta all'Arrabbiata"}
desserts = {"Panna Cotta", "Tiramisu", "Gelato"}

# Let's throw everything into the menu
menu = antipasti | salads | main_course | desserts
print("Today's menu and specials: ")
for dish in menu:
    print(f" - {dish}")
print("\n===============================================================\n")

#########################################################################################
# Intersection (common elements)
# Intersection returns elements that are in both sets.
# Example: set1.intersection(set2) or set1 & set2

# Our menu is a bit cluttered.
# Since our gues is done eating, let's show them only the desserts for now.
#########################################################################################

menu_food = menu.intersection(desserts)
print("Our menu contains: ")
for dish in menu_food:
    print(f" - {dish}")

# Bonus: A couple is waiting at the bar, drinking. Can you show them only the antipasti while they're waiting?
# Bonus: If you made a drinks set, show them the drink menu only.
print("\n===============================================================\n")

#########################################################################################
# Difference (elements in set1 but not in set2)
# Example: set1.difference(set2) or set1 - set2

# Una pasticcieri has opened next door, and our customers spend their shinies there!
# Let's see how their menu differs to ours!
#########################################################################################

# This is our nemesis' menu!
pasticcerie = {"Gelato", "Panna Cotta", "Tiramisu", "Zabaglione", "Struffoli"}
print("Let's study the difference in the menus.")
print(f"\nThey are selling {pasticcerie.difference(desserts)}.\nWe should do something about this!")

# You can also try these 2:
# pasticcerie - desserts -> Shows what they have that we don't
# desserts - pasticcerie -> Show what we have that they don't (buhuhu)

# Info:
# A.difference(B) -> Show what A has that B does not
# B.difference(A) -> Show what B has that A does not
print("\n===============================================================\n")

#########################################################################################
# Length of the set
# You can check how many items are in a set using len().
#########################################################################################

print("Number of dishes in the menu:", len(menu_food))

# Bonus 1: Why is the length of menu_food "wrong"?
# Bonus: How can you check if the set is empty?
print("\n===============================================================\n")

#########################################################################################
# We got a new intern. He said he knows about sets, so we let him make our menu awesome!
#########################################################################################

# Intern:
menu_food.clear()
print(menu_food)
print("Intern: Something happened I have to go, bye!")
print("\n===============================================================\n")

# Wait what? Shit, you're fired!

#########################################################################################
# There are a lot more to sets than what I just showed here, 
# however, since sets are mostly used for Data Science, I'm gonna skip them.
# I rarely use sets, I usually just write scripts.
# Maybe we'll go over sets during the Deep Learning thing.
#########################################################################################
#########################################################################################
# ✨ Set Cheatsheet
#########################################################################################

# .add() – add an item to the set
# .remove() – remove an item (raises KeyError if item is not found)
# .discard() – remove an item (does not raise KeyError if item is not found)
# .pop() – remove an arbitrary item (sets are unordered)
# .union() – combine two sets
# .intersection() – find common items between two sets
# .difference() – find items in one set but not the other
# .symmetric_difference() – find items in either set, but not both
# len() – get the number of items
