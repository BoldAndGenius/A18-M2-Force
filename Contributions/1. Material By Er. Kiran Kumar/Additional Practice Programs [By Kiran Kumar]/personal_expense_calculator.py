

pg_rent = int(input("Enter Your PG Rent = "))
snacks = int(input("Enter Amount for Snacks = "))
fruits = int(input("Enter Amount for Fruits = "))
personal_thing = int(input("Enter Amount for Personal Thing = "))
emergency_funds = int(input("Enter Emergency Funds = "))
savings = int(input("Enter Savings Amount = "))
print()

total = pg_rent + snacks + fruits + personal_thing + emergency_funds + savings 
print(f"Total Personal Expense is = {total} Rs.")