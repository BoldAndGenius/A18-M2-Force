
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



 
 
 
 
 
# Coding Interview Question - 3 
# Write a Python Program to count the frequency of words appearing in a string.

# Sheena loves eating apple and mango. Her sister also loves eating apple and mango. 

string = "Sheena loves eating apple and mango. Her sister also loves eating apple and mango"
list = string.split()
# print(list) # ['Sheena', 'loves', 'eating', 'apple', 'and', 'mango.', 'Her', 'sister', 'also', 'loves', 'eating', 'apple', 'and', 'mango']

new_list = []
for item in list:
  if item not in new_list: 
    new_list.append(item)
    print(item , " : ", list.count(item))
  # print(item)
  
  



# Coding Interview Question - 4 (Logic -1)
# Write a Python Program to convert two lists inta a dictionary 

'''
eg -
list1 = ["Naina", "Kimi", "Sheena"]
list2 = [852345, 763567, 691276]

'''

list1 = ["Naina", "Kimi", "Sheena"]
list2 = [852345, 763567, 691276]

my_dictionary = {}

for index in range(0, len(list1)):
  my_dictionary[list1[index]] = list2[index]
  
print(my_dictionary)



# Logic - 2

# Using Zip function 
# zip function is used to map elements 

list1 = ["Naina", "Kimi", "Sheena"]
list2 = [852345, 763567, 691276] 
mapped_value = zip(list1, list2)
print(list(mapped_value)) # [('Naina', 852345), ('Kimi', 763567), ('Sheena', 691276)]

# now to get the dictionary, tyepcase it 

mapped_value = dict(zip(list1, list2))
print(mapped_value)
# {'Naina': 852345, 'Kimi': 763567, 'Sheena': 691276} 



# Dictionary to converted into tuple pairs 

my_dict = {'Naina': 852345, 'Kimi': 763567, 'Sheena': 691276} 
# print(my_dict.items())  # dict_items([('Naina', 852345), ('Kimi', 763567), ('Sheena', 691276)])
# my_dict.items()  -- dictionary to list of pairs of tuple, in which key value will be there. 
for item in my_dict.items():
  print(item)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# Coding Interview Question - 5 
# Remove the duplicates 


# Logic - 1 : Using Typecasting 
arr = [1,3,2,1,2,2,5,6,3,2,4,5]
print(list(set(arr)))

# Logic - 2: Using For Loop
new_list = []
for num in arr:
  if num not in new_list:
    new_list.append(num)
print(new_list)
    
