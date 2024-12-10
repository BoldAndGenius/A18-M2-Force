
# Coding Interview Question - 1
# From a list of numbers, mover 0 to the end of the list. 

my_list = [1,0,2,0,4,6]
new_list = []
for item in my_list:
  if item == 0:
    my_list.remove(item)  # it will remove that element from the list. 
    new_list.append(item)
print(my_list + new_list)
    
    
  
# Coding Interview Question - 2  
# Write a Python Program to find out common letters between two strings.
# eg. -  NAINA 
#        REENE   
# Here in the above two, "N" is common letter between two strings 

string1 = "NAINA"
string2 = "REENE"

# The best and efficient way is to first convert it into a set, and then use set 

# Main Logic 
set1 = {1,2,3}
set2 = {4,5,1}
print(set1.intersection(set2))  # {1}



string1 = "NAINA"
string2 = "REENE"
set1 = set(string1)  # {'N','A','I','N','A'}
set2 = set(string2)
print(set1.intersection(set2))
# or 
print(set1 & set2)  # & is for intersection 




# Wrong Logics - 
# common_letter = ''
# for char1 in string1:  # N # A
#   for char2 in string2:  # R #E
#     if char1 == char2:
#       common_letter = common_letter + char1 
    
# print(common_letter)
      



# name = "kiran"
# for char in name: 
#   print(char)



 