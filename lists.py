# ==========================================
# STEP 4: Python Lists (Data Collections)
# ==========================================

# 1. Creating lists with multiple items
my_teams = ["Simba SC", "Juventus", "Real Madrid", "Arsenal"]
match_odds = [1.50, 1.85, 2.10, 3.40]

print("Initial teams:", my_teams)

# 2. Accessing items in a list (Indexing starts at 0)
print("First team on the list:", my_teams[0])   # Simba SC
print("Last team on the list:", my_teams[-1])  # Arsenal

# 3. Adding a new item to the list (.append())
my_teams.append("AC Milan")
print("After adding a new team:", my_teams)

# 4. Modifying an existing item value
my_teams[1] = "Barcelona"
print("After changing the second item:", my_teams)

# 5. Removing an item from the list (.remove())
my_teams.remove("Arsenal")
print("After removing Arsenal:", my_teams)

# 6. Checking the size/length of the list (len())
total_teams = len(my_teams)
print("Total number of teams remaining:", total_teams