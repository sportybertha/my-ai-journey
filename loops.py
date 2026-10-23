# ==========================================
# STEP 5: Python Loops (Iteration)
# AI Journey: Learning how to repeat tasks
# ==========================================

# 1. FOR LOOP: Iterating through a list of teams
my_teams = ["Simba SC", "Juventus", "Real Madrid", "Arsenal"]

print("--- List of My Teams (Using For Loop) ---")
for team in my_teams:
    print("I support the team:", team)

print("\n-----------------------------------\n")

# 2. FOR LOOP with range(): Repeating an action a specific number of times
print("--- Counting and Repeating 5 Times ---")
for number in range(1, 6):  # Starts at 1 up to 5
    print("This is iteration number:", number)

print("\n-----------------------------------\n")

# 3. WHILE LOOP: Repeating until a condition changes
print("--- While Loop Example (Energy Level Tracker) ---")
energy = 3

while energy > 0:
    print("Remaining energy level:", energy)
    energy -= 1  # Reduces energy by 1 each cycle

print("Energy depleted! System stopped.")