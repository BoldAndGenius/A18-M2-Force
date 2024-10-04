# Practice Questions on Conditionals 

# 1. Age Group Categorization 
# Classify a person's age group : Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter an age : "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif age > 60:
    print("Senior")
else:
    print("Invalid")




# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for childern. Everyone gets a $2 discount on Wednesday.


age = int(input("Enter an age : "))
day = input("Enter a day : ").lower()
if age >= 18:
    price = 12
else:
    price = 8

if day == "wednesday":
    price = price - 2
print("Your Final Ticket Pricing is",price, "$")
    


# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score:  A (90-100), B (80-89), C(70-79), D(60-69), F (Below 60)


# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (eg. Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)



# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)




# 6. Transportation Mode Selection
# Problem - Choose a mode of transportation based on the distance (e.g - <3Km : Walk,  3-15 Km: Bike, >15Km: Car)


# 7. Coffee Customization.
# Problem : Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso



# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: <6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


# 9. Leap Year Checker
# Problem: Determine if a year is a leap (Leap years are divisible by 4, but not by 100 unless also divisible by 400)


# 10. Pet Food Recommendation
# Problem : Recommend a type of pet food based on the pet's species and age. (eg. Dog: <2years - Puppy food,  Cat: >5 years - Senior Cat food)