# 02_conditionals_solved.py
# 🎮 Mini Project: Luigi’s Moral Compass

# Get Luigi's mood
mood = input("How is Luigi feeling today? ").lower()

# Is there an enemy nearby?
enemy_input = input("Is there an enemy nearby? (yes/no): ").lower()
enemy_nearby = enemy_input == "yes"

# Does Luigi have a powerup?
powerup_input = input("Does Luigi have a powerup? (yes/no): ").lower()
has_powerup = powerup_input == "yes"

print("\n🟢 Luigi's Decision:")

# Decision logic
if mood == "brave":
    if enemy_nearby and has_powerup:
        print("Luigi is ready to kick butt with fire!")
    elif enemy_nearby:
        print("Luigi might win, but it's risky...")
    else:
        print("Luigi charges forward, ready for anything.")

elif mood == "lazy":
    if enemy_nearby:
        print("Luigi hides under the blanket and pretends the enemy isn’t real.")
    else:
        print("Luigi watches TV and eats chips.")

elif mood == "hangry":
    print("Luigi needs pasta. Now. Everything else can wait.")

elif mood == "happy":
    if has_powerup:
        print("Luigi skips through the fields throwing fireballs for fun.")
    else:
        print("Luigi hums a tune and goes for a walk.")

elif mood == "tired":
    print("Luigi yawns and goes back to bed. Adventure cancelled.")

else:
    print("Luigi stares blankly into the void, unsure of what to do.")

# End of adventure
print("\n🎬 End of Luigi’s day.\n")
