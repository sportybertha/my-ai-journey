# ==========================================
# STEP 7: Mini Project - Football Match Evaluator
# AI Journey: Combining Variables, Input, Conditionals, Lists & Loops
# ==========================================

print("=== WELCOME TO FOOTBALL MATCH EVALUATOR ===")

# 1. List of favorite teams
favorite_teams = ["Simba SC", "Juventus", "Real Madrid", "Arsenal"]

# 2. Get user input for a team name
user_team = input("Enter your team name: ")

# 3. Conditional: Check if the team is in our favorite list
if user_team in favorite_teams:
    print(f"Awesome! {user_team} is in our favorite teams list.")
else:
    print(f"{user_team} is not in the favorite list, but we will evaluate it anyway!")

# 4. Get odds input from the user
try:
    match_odd = float(input("Enter the match winning odds (e.g. 1.75): "))
    
    # 5. Conditional logic to evaluate risk level
    if match_odd < 1.50:
        status = "High chance of winning (Low Risk)"
    elif 1.50 <= match_odd <= 2.20:
        status = "Competitive match (Moderate Risk)"
    else:
        status = "Unpredictable match (High Risk)"
        
    print(f"\n--- MATCH REPORT FOR {user_team.upper()} ---")
    print(f"Odds: {match_odd}")
    print(f"Evaluation: {status}")

except ValueError:
    print("Please enter a valid numeric value for Odds!")

# 6. Loop: Displaying the entire list of teams
print("\n--- ALL TEAMS IN THE SYSTEM ---")
for index, team in enumerate(favorite_teams, 1):
    print(f"{index}. {team}")