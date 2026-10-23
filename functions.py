# ==========================================
# STEP 6: Python Functions (Reusable Code)
# AI Journey: Writing blocks of code you can reuse
# ==========================================

# 1. Defining a simple function
def greet_team(team_name):
    print(f"Hello, loyal fan of {team_name}!")

# Calling / using the function multiple times
greet_team("Simba SC")
greet_team("Arsenal")

print("\n-----------------------------------\n")

# 2. Function with a return value (e.g., calculating odds multiplication)
def calculate_odds(odd_one, odd_two):
    total_odds = odd_one * odd_two
    return total_odds

final_odds = calculate_odds(1.50, 2.00)
print("Calculated total odds:", final_odds)