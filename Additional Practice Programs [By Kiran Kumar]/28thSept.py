# Questions on Loop

# Question - 1
# Counting Positive Numbers 
# Problem - Given a list of numbers, count how many are positive 


numbers = [1, -2, 3, -4, 5, 6 -7, -8, 9, 10]

# firstly I need to iternate on this list, one element by element -- therefore use for loop (very easy to iterate on a list)
count = 0
for element in numbers:
    if element > 0:
        # print(element) # it will print all the positive numbers, but I want a count of it, therefore initialise a count variable with 0 & everytime update by 1
        count = count + 1
print(f"The Number of Positive Numbers in the list are {count}")



# Question - 2
# Sum of Even Numbers 
# Problem - Calculate the sum of even numbers up to a given number n


given_number = int(input("Enter any number :"))   # 10
sum = 0
for num in range(0,given_number+1,2):
    print(num)  # what are those numbers   # 0,2,4,6,8,10
    sum = sum + num  # 30
print(f"The sum of even numbers upto {given_number} is {sum}")



# Question - 3
# Multiplication Table Printer
# Problem - Print the multiplication table from a given number up to 10, but skip the fifth iteration

# skip means, I need to use continue. That will skip the current iteration & continues the further iteration.


given_number = int(input("Enter a number : "))


for num in range(1,11):
    if num == 5:
        continue
    print(num*given_number)
    




# Question - 4
# Reverse a String 
# Problem - Reverse a String using a loop

string = input("Enter a String :")
# to reverse, I need to firstly access each chracters of a string, therefore need to use loop.
# for loop will be easily implemented, since on iterations we can easily implement

reverse = ''
for char in string:
    # print(char)  # print chracter by chracter
    # to reverse it
    reverse = char + reverse  # 'k'+'' = 'k'  # 'i'+'k' = 'ik'  # 'r'+'ik' = 'rik'
print(reverse)




# Question - 5   [[ Revise  ]] [*********************************]
# Find the First Non-Repeated Character 
# Problem : Given a String, Find the First Non-Repeated character 


given_string = input("Enter a string : ")  # kkiirran
non_repeated_character = ''
for character in given_string:
    if given_string.count(character) == 1:
        non_repeated_character = character
        break 
print("The First Non Repeated Character is ",non_repeated_character)
