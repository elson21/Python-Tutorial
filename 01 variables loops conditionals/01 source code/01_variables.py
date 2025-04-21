# 01_variables.py
#########################################################################################
# Variables are used to store data in Python. They can be of different types, such as integers, floats, strings, and booleans.
# Strings
#########################################################################################

name = "Mario"  # Try changing the name to "Luigi" or "Peach" and see what happens.
greeting = f"It's a me, {name}!"    # What happens if you change the name to "Luigi" or "Peach"?    
print(greeting) 

#########################################################################################
# Numbers
# Integers and floats are used to represent numbers in Python.
# Integers are whole numbers, while floats are numbers with decimal points.
#########################################################################################

# age = 42        # Integer
# height = 154.9  # Float
# print(f"{name} is {age} years old and {height} cm tall.")
# pi = 3.14159
# print(f"Pi is approximately {pi}.") # Try to print the value of pi with 2 decimal places, without changing the value of pi (google is yor friend).

#########################################################################################
# Booleans (Only two values: True or False)
#########################################################################################

# is_green = False
# is_red = True
# print(f"{name} is green: {is_green}")
# print(f"{name} is red: {is_red}")

#########################################################################################
# You can change types midway
#########################################################################################

# mystery = 42    # This is an integer
# print(type(mystery))
# mystery= "Now i'm a string!"    # This is a string
# print(type(mystery))

#########################################################################################
# Constants
# Constants are variables that the developer does not expect to change.
# They are usually written in all uppercase letters.
# This is a convention, not a rule. Python does not enforce constants.
# Be good human being (or apache helicopter, or pokemon...) and follow this convention.
#########################################################################################

# PI = 3.14159
# MAX_USERS = 100
# print(f"Pi is approximately {PI}.")
# print(f"Max users is {MAX_USERS}.")

#########################################################################################
# Type hints
# Type hints are a way to indicate the expected type of a variable.
# They are not enforced by Python, but they can help with code readability and IDE support.
#########################################################################################

# score: int = 100    
# username: str = "chaotic_learner"   
# active: bool = True

#########################################################################################
# Can you print these variables to see their values?
#########################################################################################
