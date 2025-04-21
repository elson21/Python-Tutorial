# 02_conditionals.py
#########################################################################################
# Conditionals are used to execute different code based on certain conditions.
# They are the "if this happends, do that" things.

# Difference betwen '=' and '=='
# '=' is used to assign a value to a variable.
# '==' is used to compare two values.
# For example:
# mood = "brave"  # This assigns the value "brave" to the variable mood.
# mood == "brave"  # This compares the value of mood to the string "brave".
# If the value of mood is "brave", this will return True. Otherwise, it will return False.
# Google assignment vs comparison operators to learn more about this.
# You can also use '!=' to check if two values are not equal.
#########################################################################################
#########################################################################################
# CHANGE THESE VARIABLES TO TEST THE CODE
# The code will change depending on the values of these variables.
#########################################################################################

mood = "brave"       # Try changing the mood to "lazy", or "hangry" (yes, hangry, you grammar nazi, google it!).
enemy_nearby = True  # What variable is this?
has_powerup = False  # And this?

#########################################################################################
# If statement
# If statements are used to execute code if a certain condition is true.
#########################################################################################

# if mood == "brave":
#     print("Let's go fight the enemy!")

#########################################################################################
# if-else statement
# If-else statements are used to execute code if a certain condition is true, and another code if it is false.
#########################################################################################

# if enemy_nearby:
#     print("Let's fight!")
# else:
#     print("Nothing to do here. Let's go home.")

#########################################################################################
# Nested if statement
# Nested if statements are used to execute code if a certain condition is true, and another code if it is false.
#########################################################################################

# if enemy_nearby:
#     print("Time to b-b-b-battle!")

#     # Nested if statement inside the previous if statement
#     if has_powerup:
#         print("Let's use the powerup!")
#     else:
#         print("Let's fight without the powerup.")

# else:
#     print("Nothing to do here. Let's go for a walk.")

#########################################################################################
#if-elif-else statement
# If-elif-else statements are used to execute code if a certain condition is true, and another code if it is false.
#########################################################################################

# if mood == "lazy":
#     print("Let's stay home and play video games.")
# elif mood == "hangry":
#     print("Don't talk to me, I need food. Now.")
# elif mood == "tired":
#     print("Let's go to bed.")
# elif mood == "happy":
#     print("Let's go for a walk.")
# else:
#     print("I don't know what to do. Let's just sit here and stare at the wall.")

#########################################################################################
# Some times, multiple conditions can be true at the same time, and we want to run all of them.
# In this case we can use multiple if statements.
#########################################################################################

# if mood == "brave":
#     print("Feeling brave!")
# if enemy_nearby:
#     print("Exterminate! Exterminate! Exterminate!")
# if has_powerup:
#     print("It's over 9000!")

#########################################################################################
# We can also use the 'and' and 'or' operators to combine conditions.
# The 'and' operator is used to check if two conditions are true at the same time.
# The 'or' operator is used to check if at least one of the conditions is true.
#########################################################################################

# if mood == "brave" and enemy_nearby:
#     print("Let's fight!")
# if mood == "lazy" or enemy_nearby:
#     print("Let's go home.")
# if mood == "happy" and has_powerup:
#     print("Let's go for a walk with the powerup.")
# if mood == "happy" or has_powerup:
#     print("Let's go for a walk with or without the powerup.")

#########################################################################################
# Let's see how this works with Luigi.
#########################################################################################

# print("\nLuigi's adventure:")
# if mood == "brave":
#     if enemy_nearby and has_powerup:
#         print("Luigi is ready to kick butt with fire!")
#     elif enemy_nearby:
#         print("Luigi might win, but it's risky...")
#     else:
#         print("Luigi charges forward, ready for anything.")
# else:
#     print("Luigi is not in the mood for danger today.")