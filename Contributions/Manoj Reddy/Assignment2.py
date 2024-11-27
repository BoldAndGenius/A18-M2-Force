# # Q1. Write a program to print the following using while loop
# # a. First 10 Even numbers
# # b. First 10 Odd numbers
# # c. First 10 Natural numbers
# # d. First 10 Whole numbers        

# even = 1
# even_numbers = []
# while even <= 20:
#     if even % 2 == 0:
#         even_numbers.append(even)
#     even+=1
# print(even_numbers)

# odd = 1
# odd_numbers = []
# while odd <= 20:
#     if odd % 2 :
#         odd_numbers.append(odd)
#     odd+=1
# print(odd_numbers)

# start = 1
# natural_numbers = []
# while start <= 10:
#     natural_numbers.append(start)
#     start+=1
# print(natural_numbers)

# start = 0
# whole_numbers = []
# while start < 10:
#     whole_numbers.append(start)
#     start+=1
# print(whole_numbers)

# # Q2. Write a program to print first 10 integers and their squares using while loop. 

# start = 1 
# integers = []
# squares = []
# while start <= 10:
#     integers+=[start]
#     squares+=[start**2]
#     start+=1
# print(f"Integers:{integers}")
# print(f"Squares:{squares}")

# # Q3. Write while loop statement to print the following series: 10, 20, 30 ... ... 300 

# start = 10
# end = 300
# series = []
# while start <= end:
#     series.append(start)
#     start += 10
# print(series)

# # Q4. Write a while loop statement to print the following series 105, 98, 91 .........7.

# start = 105
# end = 7
# series = []
# while start >= end:
#     series.append(start)
#     start -= 7
# print(series)
    
# # Q5. Write a program to print first 10 natural number in reverse order using while loop.

# start = 11
# end = 1
# rev_order = []
# while start > end:
#     start -= 1
#     rev_order.append(start)
# print(rev_order)

# # Q6. Write a program to print sum of first 10 Natural numbers.

# start = 1
# end = 10
# sum = 0
# while start <= end:
#     sum+=start
#     start+=1
# print(sum)

# # Q7. Write a program to print sum of first 10 Even numbers.

# start = 1
# end = 20
# even_sum = 0
# while start <= end:
#     if start % 2 == 0:
#         even_sum+=start
#     start+=1
# print(even_sum)

# # Q8. Write a program to print table of a number entered from the user.

# start = 1
# end = 10
# num = int(input("Enter Number: "))
# while start <= end:
#     print(f"{num}X{start}={num*start}")
#     start += 1

# # Q9. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.

# num1 = int(input("Enter Number: "))
# num2 = int(input("Enter Number: "))
# start = min(num1,num2)
# end = max(num1,num2)
# even_numbers = []
# while start <= end:
#     if start % 2 == 0:
#         even_numbers.append(start)
#     start += 1
# print(even_numbers)

# # # Q10. Write a program to check whether a number is prime or not using while loop.

# num = int(input("Enter Number: "))
# prime = True
# if num < 2:
#     prime = False
# else:
#     for factor in range(2,num):
#         if num % factor == 0:
#             prime = False
#             break
# if prime == True:
#     print("Prime Number")
# else:
#     print("Not Prime Number")
    
# ## Q11. Write a program to find the sum of the digits of a number accepted from the user.

# num = int(input("Enter Number: "))
# sum = 0
# while num != 0:
#     last_digit = num%10
#     num = num//10
#     sum+=last_digit
# print(sum)

# # Q12. Write a program to find the product of the digits of a number accepted from the user.

# num = int(input("Enter Number: "))
# product = 1
# while num != 0:
#     last_digit = num%10
#     num = num//10
#     product = product*last_digit
# print(product)

# # Q13. Write a program to reverse the number accepted from user using while loop.

# num = int(input("Enter Number: "))
# rev = 0
# while num != 0:
#     last_digit = num%10
#     num = num//10
#     rev = rev*10+last_digit
# print(rev)

# # Q14. Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One

# num = int(input("Enter Number: "))
# final = []
# if num == 0:
#     print("Zero")
# else:
#     while num != 0:
#         last_digit = num%10
#         num  = num//10
#         new_num = str(last_digit)
#         nums = {'1':"One",'2':"Two",'3':"Three",'4':"Four",'5':"Five",'6':"Six",'7':"Seven",'8':"Eight",'9':"Nine",'0':"Zero"}
#         output = nums.get(new_num)
#         final.insert(0,output)
# print(final)

# nums = int(input("Enter Number: "))
# new_num = str(nums)
# for num in new_num:
#     if num == "0":
#         print("Zero")
#     elif num == "1":
#         print("One")
#     elif num == "2":
#         print("Two")
#     elif num == "3":
#         print("Three")
#     elif num == "4":
#         print("Four")
#     elif num == "5":
#         print("Five")
#     elif num == "6":
#         print("Six")
#     elif num == "7":
#         print("Seven")
#     elif num == "8":
#         print("Eight")
#     else:
#         print("Nine")
    
# # Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.

# series = [0,1]
# num = int(input("Enter Number: "))
# if num == 1:
#     print(series[0])
# elif num == 2:
#     print(series[1])
# else:
#     for i  in range(num-2):
#         fib = series[-1]+series[-2]
#         series.append(fib)
#     print(series)

# # Q16. Write a program to print the factorial of a number accepted from user.

# num = int(input("Enter Number: "))
# factorial = 1
# n = 1
# while n <= num:
#     factorial*=n
#     n+=1
# print(factorial)

# # Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)

# num = int(input("Enter Number: "))
# string = str(num)
# count = len(string)
# amstrong_num = 0
# digit = int(string)
# while digit != 0:
#     last_digit = digit%10
#     digit = digit//10
#     amstrong_num = amstrong_num+last_digit**count
# if num == amstrong_num:
#     print("Its Armstrong Number")
# else:
#     print("Not Amstrong Number")


# # Q18. Write a program to add first n terms of the following series using a while loop: 1/1! + 1/2! + 1/3! + ........ + 1/n!

# num = int(input("Enter Number: "))
# factorial = 1
# sum = 0
# i = 1
# while i <= num:
#     factorial*=i
#     sum+=1/factorial
#     i+=1
# print(sum)

# # Q19. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.

# sum = 0
# while True:
#     num = input("Enter Number or quit: ")
#     if num.lower() == 'quit':
#         break
#     sum+=int(num)
# print(sum)

# ## Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered.
  
# postive = []
# negative = []
# while True:
#     num = int(input("Enter Number: "))
#     if num == 0:
#         break
#     else:
#         if num<0:
#             negative+=[num]
#         else:
#             postive+=[num]
# print(f"Postive Numbers count is {len(postive)}")
# print(f"Negative Numbers count is {len(negative)}")  

# # Q21. Write a program to find the HCF of two numbers entered from the user.

# def find_hcf(num1,num2):
#     while num1 != num2:
#         if num1 > num2:
#             num1 -= num2
#         else:
#             num2 -= num1
#         return num2
# num1 = int(input("Enter Number: "))
# num2 = int(input("Enter Number: "))
# hcf = find_hcf(num1,num2)
# print(hcf)



# # #Q24. Write a program to check whether a number is palindrome or not.

# num = int(input("Enter Number: "))
# temp = num
# rev = 0
# while temp != 0:
#     last = temp%10
#     rev=rev*10+last
#     temp//=10
# if num == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # Q25. Write a python program to sum the sequence: 1 + 1/1! + 1/2! + 1/3! + ........ + 1/n!

# num = int(input("Enter Number: "))
# sum = 1
# factorial = 1
# start = 1
# while start <= num:
#     factorial*=start
#     sum += 1/factorial
#     start += 1
# print(sum)

# # Q26. Write a program to accept 10 numbers from the user and display it’s average

# start = 0
# sum = 0
# while start<10:
#     num = int(input("Enter Number: "))
#     sum+=num
#     start+=1
# print(sum//10)

# #Q27. Write a program to accept 10 numbers from the user and display the largest & smallest number number.

# start = 0
# numbers = []
# while start<10:
#     num = int(input("Enter Number: "))
#     numbers+=[num]
#     start+=1
# print(f"Largest Number is {max(numbers)}")
# print(f"Smallest Number is {min(numbers)}")

# # Q28. Write a program to display sum of odd numbers and even numbers separately that fall between two numbers accepted from the user.(including both numbers) using while loop.

# num1 = int(input("Enter Number: "))
# num2 = int(input("Enter Number: "))
# if num1 == num2:
#     print("Enter Valid Numbers not same")
# else:
#     large = max(num1,num2)
#     small = min(num1,num2)
#     sum_even = 0
#     sum_odd = 0
#     while small<=large:
#         if small % 2 == 0:
#             sum_even += small
#         else:
#             sum_odd += small
#         small+=1
#     print(f"Sum of Even Numbers {sum_even}")
#     print(f"Sum of Odd Numbers {sum_odd}")

# # Q29. Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.(exclusive both numbers)

# start = 101
# end = 500
# while start < end:
#     if start % 13 == 0 and  start % 3 :
#         print(start)
#     start+=1

# # Q30. Write a program to print the following series till n terms. 2 , 22 , 222 , 2222 _ _ _ _ _ n terms

# num = int(input("Enter Number: "))
# start = 1
# list1 = []
# while start <= num:
#     list1 += [int('2'*start)]
#     start += 1
# print(list1)

# # Q31. Write a program to print the following series till n terms. 1 4 9 16 25 _ _ _ _ _ n terms.

# start = 1
# end = int(input("Enter Number: "))
# square_series = []
# while start <= end:
#     square_series += [start**2]
#     start += 1
# print(square_series)

# # Q32. Write a program to find the sum of the following series(accept values of x and n from user) 1 + x/1! + x2/2! + ..........xn/n!

# n = int(input("Enter Number: "))
# x = int(input("Enter Number: "))
# start = 1
# factorial = 1
# sum = 1
# while start <= n:
#     factorial*=start
#     sum+=(x*start)/factorial
#     start+=1
# print(sum)

# # Q33. Write a program to find the sum of following series : x + x2/2 + ..........xn/n

# n = int(input("Enter Number: "))
# x = int(input("Enter Number: "))
# start = 1
# sum = 0
# while start <= n:
#     sum+=(x*start)/start
#     start+=1
# print(sum)

# #Q34. Write a program to find the sum of following series 1 + 8 + 27 ............n terms

# num = int(input("Enter Number: "))
# start = 1
# sum = 0
# while start <= num:
#     sum+=start**3
#     start+=1
# print(sum)

# #Q35. Write a program to find the sum of following series: 1 + 2 + 6 + 24 + 120 . . . . . n terms

# num = int(input("Enter Number: "))
# sum = 1
# start = 0
# while start < num:
#     sum+=start*sum
#     start+=1
# print(sum)

# # Q36. Write a program to find the sum of following series: S = 1 + 4 – 9 + 16 – 25 + 36 – ... ... n terms

# # Q37. Write a Program to print all the characters in the string ‘PYTHON’ using while loop.

# string = 'PYTHON'
# index = 0
# while index < len(string):
#     print(string[index])
#     index+=1

# # Q38. Write a program to print only odd numbers from the given list using while loop. L = [23, 45,32, 25, 46, 33, 71, 90]

# L = [23,45,32,25,26,33,71,90]
# index = 0
# list1 = []
# while index < len(L):
#     if L[index]%2:
#         list1+=[L[index]]
#     index+=1
# print(list1)

# # Q41.Write a program to extract all the upper case character from the given string

# string = input("Enter string: ")
# index = 0
# upper = ''
# while index < len(string):
#     if 'A'<=string[index]<='Z':
#         upper+=string[index]
#     index+=1
# print(upper)
        
# # Q42.Write a Program to separate positive and negative number from a list.

# list1 = eval(input("Enter Numbers in a list: "))
# pos = []
# neg = []
# index = 0
# while index < len(list1):
#     if list1[index]>0:
#         pos.append(list1[index])
#     else:
#         neg.append(list1[index])
#     index+=1
# print(pos)
# print(neg)
    
# # Q45.Write a program to extract all the string data items from the given list only if string is palindrome

# list1 = eval(input("Enter a list: "))
# index = 0
# new_list = []
# while index < len(list1):
#     char = list1[index]
#     if type(char) == str:
#         if char == char[::-1]:
#             new_list+=[char]
#     index += 1
# print(new_list)

# # Q46.Write a program to extract all the special characters from the given string



## Q47.Write a program to extract all the upper case character ,lower case character ,numbers and special characters into four different output variables from the given string

# def extract_all(string:str):
#     index = 0
#     upper = ''
#     lower = ''
#     numbers = ''
#     spcl_charcs = ''
#     while index < len(string):
#         char = string[index]
#         if char.isupper():
#             upper+=char
#         elif char.islower():
#             lower+=char
#         elif char.isnumeric():
#             numbers+=char
#         else:
#             spcl_charcs+=char
#         index += 1
#     print(f"Uppercase --> {upper}")
#     print(f"Lowercase --> {lower}") 
#     print(f"Numbers --> {numbers}")
#     print(f"Special Characters--> {spcl_charcs}") 
# string = input("Enter String: ")     
# extract_all(string)

## Q49.Write a program to convert all the lower case charater to upper case characters present in a given string

# string = input("Enter String: ")
# index = 0
# output = ''
# while index < len(string):
#     char = string[index]
#     var = ord(char)
#     if 'A'<=char<='Z':
#         var+=32
#         output+=chr(var)
#     elif 'a'<=char<='z':
#         var-=32
#         output+=chr(var)
#     index += 1
# print(output)
        
## Q50.Write a program to convert all the lower case character to upper case character and upper case character to lower case character by keeping number and special character as it is

# string = input("Enter String: ")
# index = 0
# output = ''
# while index < len(string):
#     char = string[index]
#     var = ord(char)
#     if 'A'<=char<='Z':
#         var+=32
#         output+=chr(var)
#     elif 'a'<=char<='z':
#         var-=32
#         output+=chr(var)
#     else:
#         output+=char
#     index += 1
# print(output)

## Q51.Write a program to extract all the lower case character from the given string only if its ascii value is even

# string = input("Enter String: ")
# index = 0
# output = ''
# while index < len(string):
#     char = string[index]
#     var = ord(char)
#     if 'a'<=char<='z':
#         if var%2 == 0:
#             output += char
#     index += 1
# print(output)

## Q52.Write a program to get the following output
## Q53.Write a program to get the following output
## input=’hello’
## output={0:’h’ , 1:’e’ , 2:’l’ , 3:’l’ , 4:’o’}

# input = 'hello'
# index = 0
# output = {}
# while index < len(input):
#     output[index] = input[index]
#     index+=1
# print(output)

# '''Q54.Write a program to get the following output
#        input=[‘hai’ , 89 ,3.4 , ‘hello’ , 90 , ‘py’]
#        output={‘hai’:’hi’ , ‘hello’:’ho’ , ‘py’:’py’} '''

# input = ['hai' , 89 ,3.4 , 'hello' , 90 , 'py']
# output = {}
# index = 0
# while index < len(input):
#     string = input[index]
#     if type(string) == str:
#         output[string] = string[0]+string[-1]
#     index+=1
# print(output)

'''Q55.Write a program to get the following output
   input='hai hello'
   output='olleh iah'   '''
   
# input = 'hai hello'
# output = ''
# index = 0
# while index < len(input):
#     output = input[index]+output
#     index += 1
# print(output)

## Q56.write a program to count the number of vowels present in a given string

# string = input("Enter string: ")
# index = 0
# output = 0
# while index < len(string):
#     char = string[index]
#     if char in 'aeiouAEIOU':
#         output+=1
#     index += 1
# print(output)

# '''Q57.Write a program to get the following output
#     input=‘hai hello good morning’
#     output={‘hai’:’a’ , ‘hello’: ‘l’ , ‘good’:’gd’ , ‘morning’:’n’}      '''
    
# input = 'hai hello good morning'
# words = input.split()
# output = {}
# index = 0
# while index < len(words):
#     char = words[index]
#     length = len(char)
#     if length%2:
#         output[char] = char[length//2]
#     else:
#         output[char] = char[0]+char[-1]
#     index += 1
# print(output)

'''Q58.Write a program to get the following output
   input=['jiocinema.com' , 'file.py' , 'web.html']
   output=['com' , 'py' , 'html']                '''
   
input=['jiocinema.com' , 'file.py' , 'web.html']
output = []
new_list = []
index = 0
while index < len(input):
   char = input[index]
   string = str(char)
   char1 = string.split('.')
   new_list += [char1]
   last = new_list[-1]
   output.append(last)
   index += 1
print(last)

   


       
       


