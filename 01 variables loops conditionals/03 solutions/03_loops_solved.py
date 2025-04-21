# 03_loops_exercise_solution.py
# 🥊 Micro Project: Luigi vs The Infinite Goombas

stamina = 100
goombas_defeated = 0
goomba_damage = 7

print("💥 Luigi enters the Goomba-infested plains with 100 stamina!")

while stamina >= goomba_damage:
    print(f"\nLuigi jumps on a Goomba and squashes it! (-{goomba_damage} stamina)")
    stamina -= goomba_damage
    goombas_defeated += 1
    print(f"Goombas defeated: {goombas_defeated} | Stamina left: {stamina}")

    keep_fighting = input("Keep going? (yes/no): ").lower()
    if keep_fighting != "yes":
        print("\nLuigi decides to retreat and eat some pasta. 🍝")
        break
else:
    print("\nLuigi collapses from exhaustion. 😵")

print(f"\n🏁 Battle over! Luigi defeated {goombas_defeated} Goombas and has {stamina} stamina left.")
