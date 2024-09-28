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