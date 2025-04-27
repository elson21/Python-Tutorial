# 02_dictionaries.py
#######################################################################
# Dictionaries are used to store data in key-value pairs.
# Think of them like real dictionaries: you look up a word (the key),
# and get the definition (the value).

# A dictionary is created using curly braces {} and key-value pairs.

# dictionary = {
#     "key1": "value1",
#     "key2": "value2"
# }

# You can also use the dict() constructor:
# dictionary = dict(key1="value1", key2="value2")
# But the first method is more common and easier to read.

# Finally, the most common dictionary is the nested dictionary.
# This is a dictionary inside another dictionary.
# This is useful for representing complex data structures.

# dictionary_nest = {
#     "key1": {
#         "key1.1": "value1.1",
#         "key1.2": "value1.2"},
#     "key2": {
#         "key2.1": "value2.1",
#         "key2.2": "value2.2"}
# }
#######################################################################

# A dictionary to describe a bunch of dinosaurs
dino_db = {
    "T-Rex": {
        "era": "Cretaceous",
        "diet": "carnivore",
        "height": 1200,
        "weight": 8000
    },
    "Triceratops": {
        "era": "Cretaceous",
        "diet": "herbivore",
        "height": 1000,
        "weight": 12000
    },
    "Velociraptor": {
        "era": "Cretaceous",
        "diet": "carnivore",
        "height": 600,
        "weight": 15
    }
}

#######################################################################
# Accessing Values
# Use square brackets with the key name to get a value.
#######################################################################

print("\n🦖 T-Rex Info:")
print("Era:", dino_db["T-Rex"]["era"])
print("Diet:", dino_db["T-Rex"]["diet"])
print("\n==================================================")

# Bonus: Show me how much does the Velociraptor weigh

#######################################################################
# Changing Values
# Just assign a value to a new or existing key.
#######################################################################

print("\nAfter decades of research, scientists found out that the velociraptor weights 16 kg, not 20!")
print("\n🔧 Updating Velociraptor's weight...")
dino_db["Velociraptor"]["weight"] = 16
print("Updated Weight: ", dino_db["Velociraptor"]["weight"])
print("\n==================================================")

########################################################################
# Adding new key-value pairs using the update() method.
# This is useful for adding new information to an existing dictionary.
#######################################################################

print("\n🔧 Adding new dinosaur: Spinosaurus...")
dino_db.update({
    "Spinosaurus": {
        "era": "Cretaceous",
        "diet": "carnivore",
        "height": 1500,
        "weight": 2000
    }
})
print("Spinosaurs added!:", dino_db["Spinosaurus"])
print("\n==================================================")

#######################################################################
# Removing Keys
# Use the del statement to remove a key-value pair.
#######################################################################

print("\n After a long day of research, scientists found out that the Velociraptor is not actually a dinosaur.")
print("\n🔧 Removing Velociraptor from the database...")
del dino_db["Velociraptor"]
print("Velociraptor removed!")
print("\n==================================================")

#######################################################################
# Looping Through a Dictionary
# Use .items() to get both key and value.
# Print the database to check if the Velociraptor was indeed removed.
#######################################################################

print("\n🔍 Checking the database...")
for dinosaur, info in dino_db.items():
    print(f"{dinosaur}:")
    print(f"  Era: {info['era']}")
    print(f"  Diet: {info['diet']}")
    print(f"  Height: {info['height']} bananas")
    print(f"  Weight: {info['weight']} stones")
print("\n==================================================")

#######################################################################
# .get() Method
# Safer way to get values — avoids crashes if key doesn’t exist.
# Try to access the Velociraptor without using .get() and see what happens.
# Then, try using .get() to access the Velociraptor.
#######################################################################

# If you wanna get an error, run these two lines:
# chicken = dino_db["Velociraptor"]
# print(chicken)

# Correct way to access the Velociraptor:
chicken = dino_db.get("Velociraptor")
if chicken:
    print("\nVelociraptor found!")
else:
    print("\nVelociraptor not found!")
print("\n==================================================")

#######################################################################
# Bonus lesson: json.dumps()
# As you saw, printing a dictionary directly can be messy.
# Use json.dumps() to convert it to a pretty string.
#######################################################################

# To use this, open the terminal and type in `pip install json`.
# If you are using Anaconda, type in `conda install json`.
# If you are using jupyter, you are doomed, I can't help you, but maybe google can.

# import json

# print("\n🔍 Pretty printing the database...")
# print(json.dumps(dino_db, indent=4))
# print("\n==================================================")

#########################################################################################
# ✨ Some extra stuff ✨
#########################################################################################

# .update() – add/update keys
print("\n.update(): Adding new Dino...")
dino_db.update({"Ankylosaurus": {"era": "Cretaceous", "diet": "herbivore", "height": 6, "weight": 6000}})
print("Ankylosaurus added:", dino_db["Ankylosaurus"])

# .pop() – remove a key and return its value
print("\n.pop(): Removing Spinosaurus...")
spiky = dino_db.pop("Spinosaurus")
print("Removed:", spiky)

# .copy() – create a shallow copy
print("\n.copy(): Cloning the database...")
dino_clone = dino_db.copy()
print("Clone successful! Dino count:", len(dino_clone))

#######################################################################################
# Last thing before going to the next lesson.
# Remember those cocktails we made in the last lesson? And that menu with no prices?
# Well, now we can add prices to the cocktails using dictionaries.

# Can you do it? 
# #Or were you just wasting your time halucinating infront of this ultra-processed rock?
#######################################################################################

#######################################################################
# That’s it for dictionaries. They're perfect for representing things
# with named attributes, like characters, settings, inventory items, etc.
#######################################################################
