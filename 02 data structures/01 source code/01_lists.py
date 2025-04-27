# 01_lists.py
#########################################################################################
# Lists store ordered sequences of items.
# A list is created using square brackets [] and can contain any data type.
#########################################################################################

cocktails = ["Old Fashioned", "Negroni", "Mojito", "Margarita", "Mai Tai"]

#########################################################################################
# Accessing elements
# Lists are indexed starting from 0. This means that the first element is numbered as 0.

# example:
# list = ["a", "b", "c"]
# list[0] = "a"
# list[1] = "b"
# list[2] = "c"

# The last element can be accessed using -1.
# list[-1] = "c"
# list[-2] = "b"
# list[-3] = "a"
#########################################################################################

print("\n🍹 First cocktail:", cocktails[0])
print("🍹 Last cocktail:", cocktails[-1])
print("\n===============================================================")

# Bonus: How can you print the Old Fashioned cocktail using negative indexing?

#########################################################################################
# Slicing lists
# Slicing allows you to access a range of elements in a list.
# The syntax is list[start:stop], where start is inclusive and stop is exclusive.
# For example, cocktails[1:4] will return a Margarita, Old Fashioned, and Negroni.

# concktails[1:5:2] will return a Margarita and a Negroni.
# cocktails[0::2] will return a Mojito, Old Fashioned, and Mai Tai.
# Bonus if you explain why.
#########################################################################################

print("\n🍹 Let's see all the cocktails at even indexes: ", cocktails[::2])
print("\n🔪 First three cocktails:", cocktails[:3])
print("🍸 Cocktails 2 through 4:", cocktails[1:4])
print("\n===============================================================")

#########################################################################################
# Modifying elements
# By accessing an element of a list, you can change its value.

# For example:
# list = ["a", "b", "c"]
# list[0] = "x"
# list[1] = "y"
# list[2] = "z"
# Now you have a brand new list: ["x", "y", "z"]
#########################################################################################

print("\n🍸 The cocktails menu has been the same for too long. Time for a change!")
print("\n🧪 Let's swap the Old Fashioned for a Robin Scherbatsky.")
cocktails[2] = "Whiskey Sour"
print("Updated list:", cocktails)
print("\n================================================================")

# Bonus: How can you change the last cocktail to a beer?

#########################################################################################
# Adding items
# Let's add some new cocktails to the list! You can use .append() to add an item to the end of the list.
# You can also use .insert() to add an item at a specific index.

# For example:
# list = ["a", "b", "c"]
# list.append("d") # list = ["a", "b", "c", "d"]
# list.insert(1, "x") # list = ["a", "x", "b", "c", "d"]
# list.insert(0, "y") # list = ["y", "a", "x", "b", "c", "d"]
#########################################################################################

print("\n🍹 Our bar got bigger! Let's add some new cocktails to the menu")
print("\n➕ Adding 'Cosmopolitan' to the end of the list...")
cocktails.append("Cosmopolitan")
print("Updated list:", cocktails)

print("\n🍍 Inserting 'Pina Colada' at position 1...")
cocktails.insert(1, "Pina Colada")
print("Updated list:", cocktails)
print("\n================================================================")

#########################################################################################
# Removing items
# You can remove items from a list using .remove() or .pop().
# .remove() removes the first occurrence of a value, while .pop() removes an item at a specific index (default: last).

# For example:
# list = ["a", "b", "c"]
# list.remove("b") # list = ["a", "c"]
# list.pop(0) # list = ["b", "c"]
# list.pop() # list = ["a", "b"]
# list.pop(-1) # list = ["a", "b"]
#########################################################################################

print("\n🍹 The weather is getting colder. Time to make some changes to the menu.")
print("\n❌ Removing 'Pina Colada'...")
cocktails.remove("Pina Colada")
print("Updated list:", cocktails)

print("\n🍹 The Margarita is also not making enough money, limes are too expensive!")
print("\nLet's make sure that I am removing the right cocktail...")
cocktail = cocktails.pop(1)
print(f"❌ Removed: {cocktail}")
print("Updated list:", cocktails)
print("\n================================================================")

# Bonus: Remove all the cocktails and put them in a new list called 'removed_cocktails'.
# Hint: use pop() in a loop.

#########################################################################################
# Looping through the list, this is where you're going to be spending most of your time.
# This is where... things are gonna be hitting the fan.
#########################################################################################

print("\n Time to print the menu!")
print("\n🔁 Coctails:")
for drink in cocktails:
    print("-", drink)
print("\n================================================================")

#########################################################################################
# Membership
# In programming there is thing that checks if an item is in a list or not.
# Python however takes it to another level. It's easy AF, all you have to do is:
# if "item" in list:
#     print(item)

# It's like asking ChatGPT, right?
# You can also check if an item is not in a list using "not in".
#########################################################################################

print("\n🔍 Is 'Margarita' in the list?", "Margarita" in cocktails)
print("🍸 Is 'Martini' in the list?", "Martini" in cocktails)

# More examples:
# The waiter asks you what cocktail you want, and you respond with:
if "Mojito" in cocktails:
    print("\n🍹 Get me a Mojito senor.")
else:
    print("\n🍹 Get me a Mai Tai senor.")

# However, there is an issue here. What if the Mai Tai is not on the menu?
# Then you have to loop through the list and check if the Mai Tai is in the list.
while True:
    drink = input("\n🍹 What cocktail do you want? ")
    if drink in cocktails:
        print(f"🍹 Get me a {drink} senor.")
        break
    else:
        print(f"🍹 Sorry, we don't have {drink}.")
        # You can also use the 'continue' statement to skip to the next iteration of the loop.
        continue
print(f"\n Here is your {drink} senor.")
print("\n================================================================")

#########################################################################################
# Length of the list
# This is another huge thing. You're gonna be using len() so much that you can probably skip this part (just kidding).
# len() returns the number of items in a list.
#########################################################################################

# Let's see how many cocktails we have on the menu.
print("\n📏 Number of cocktails:", len(cocktails))

# Not much to do here, but spend some time trying to solve the bonus things.
# Bonus: How can you check if the list is empty?
# Bonus 2: How can you print half cocktails in the list using len()?

# The len() function is very versatile. Seriously, you'll be using it all the time.

#########################################################################################
# Sorting and reversing
# In Python, as well as other high level languages, sorting is a built-in function.

# sorted() vs .sort()
# sorted() returns a new sorted list.
# .sort() sorts the list in place.

# What happens here is that sorted() takes each element from the list, compares it to the next one,
# and if the first one is greater than the second one, it swaps them. It does this until the list is sorted.
# But...! It provides a brand new list, and you also get to keep the original list.

# .sort() on the other hand, takes the old list, breaks it into pieces and puts everything back. Sorted!
#########################################################################################

# As the owner of the bar, I decided that the cocktails should be sorted by name.
# Let's see how it looks like:
print("\n📚 Sorted cocktail list:", sorted(cocktails))

# Or maybe they should be in reverse? Arghh, I can't decide!
print("🔄 Reversing the list...")
cocktails.reverse()
print("Reversed list:", cocktails)
print("\n================================================================")

#########################################################################################
# BONUS: List Comprehensions 🍹
#########################################################################################

# Create a list of cocktail name lengths
name_lengths = [len(name) for name in cocktails]
print("\n🧠 Lengths of each cocktail name:", name_lengths)

# Filter cocktails with names longer than 8 characters
long_names = [name for name in cocktails if len(name) > 8]
print("🍸 Cocktails with long names:", long_names)

#########################################################################################
# ✨ List Cheatsheet
#########################################################################################

# .append() – add to the end
# .insert() – insert at index
# .remove() – remove by value
# .pop() – remove by index (default: last)
# .reverse() – reverse list in place
# sorted() – return a sorted copy
# len() – get number of items
# [start:stop] – slice a list
# [x for x in list] – list comprehension
