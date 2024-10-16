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


score = int(input("Enter you score : "))
if 90 <= score <= 100:
    print("Your Grade is A")
elif 80 <= score <= 89:
    print("Your Grade is B")
elif 70 <= score <= 79:
    print("Your Grade is C")
elif 60 <= score <= 69:
    print("Your Grade is D")
elif score < 60:
    print("Your Grade is F")
else:
    print("Invalid")





# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (eg. Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


color = input("Enter your Banana Color : ").lower()
if color == 'green':
    print("Your Banana is Unripe.")
elif color == 'yellow':
    print("Your Banana is Ripe.")
elif color == "brown":
    print("Your Banana is Overripe.")
else:
    print("Invalid")













# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)


weather = input("Enter the weather : ").lower()
if weather == 'sunny':
    print("Go for a walk! ")
elif weather == 'rainy':
    print("Read a Book.")
elif weather == 'snowy':
    print("Build a Snowman.")
else:
    print("Invalid.")






# 6. Transportation Mode Selection
# Problem - Choose a mode of transportation based on the distance (e.g - <3Km : Walk,  3-15 Km: Bike, >15Km: Car)

distance = float(input("Enter the distance : "))
if distance < 3:
    print("Go By Walk")
elif 3 <= distance <= 15:
    print("Go By Bike")
elif distance > 15:
    print("Go By Car")
else:
    print("Invalid")






# 7. Coffee Customization.
# Problem : Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso


coffee_order = input("Enter the coffee order - (small, medium, large) : ").upper()
option = int(input("How much Extra Shot of Espresso you want : "))

print(f"Your Coffee Customization is, {coffee_order} Size of Coffee with {option} Extra Shot of Espresso ")








# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: <6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password : ")
length_password = len(password)
# print(length_password)

if length_password < 6:
    print("Weak Level Password")
elif 6 < length_password < 10:
    print("Medium Level Password")
elif length_password > 10:
    print("Strong Level Password")
else:
    print("Invalid")





# 9. Leap Year Checker
# Problem: Determine if a year is a leap (Leap years are divisible by 4, but not by 100 unless also divisible by 400)




# 10. Pet Food Recommendation
# Problem : Recommend a type of pet food based on the pet's species and age. (eg. Dog: <2years - Puppy food,  Cat: >5 years - Senior Cat food)

age = int(input("Enter the pet's age : "))
species = input("Enter the species name : ").lower()

if age < 2 and species == 'dog':
    print("Puppy Food.")
elif age > 5 and species == 'cat':
    print("Senior Cat Food.")
else:
    print("Invalid.")