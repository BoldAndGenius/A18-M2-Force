
"""
Question - 1
Given an array with some integer type values. Write  a python script to sort array values ?

"""


given_array = [34,56,12,37,78]
print(sorted(given_array))



'''
Question - 2 : 
Given a list of heterogenous elements. Write a Python script to remove all the non int values from the list. 

'''

given_list = [12, 4.5, "kiran", True]
new_list = []
for item in given_list:
  if type(item) == int:
    new_list.append(item)
print(new_list)




'''

Question - 3 : 
Write a Python script to calculate average of elements of a list. 

'''

given_list = [0,2,4,6,8,10]
sum_of = sum(given_list)
avg = sum_of // len(given_list)
print(avg)




##### Revise ! 

'''
Question - 4 : 
Write a Python Script to create a list of first N Prime Numers. 
'''

prime_list = []

# prime  = 2,3,5,7,11 
num = 2
for number in range(2,num+1):  # 2,3  # 2,4 -- 2,3
  if num % number != 0: # 2%2 == 0  # 3%2
    prime_list.append(num)
  num = num + 1
print(prime_list)
    
    
 
prime_list = []
number = 200 
for num in range(2,number):
  if number % num == 0:
    print("Not Prime")
  else:
    # print("Prime")
    prime_list.append(number)
  number = number + 1
print(prime_list)





'''
Question - 5 
Write a Python Script to create a list of first N terms of Fibonnaci Series 

'''