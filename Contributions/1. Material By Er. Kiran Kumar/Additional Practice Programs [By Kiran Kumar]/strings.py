'''

Here are 10 basic Python string program prompts:

1.  Write a program to reverse a string.
2.  Write a program to check if a string is a palindrome.
3.  Write a program to count the number of vowels in a string.
4.  Write a program to find the length of a string without using the `len()` function.
5.  Write a program to check if a substring exists within a given string.
6.  Write a program to concatenate two strings without using the `+` operator.
7.  Write a program to count the number of words in a string.
8.  Write a program to convert all characters in a string to uppercase.
9.  Write a program to replace all spaces in a string with underscores.
10.  Write a program to extract digits from a string.




'''


# 1.  Write a program to reverse a string. 

string = "kiran"
reverse = string[::-1]
print(reverse)

# 2.  Write a program to check if a string is a palindrome.

string = "maam"
reverse = string[::-1]
if string == reverse:
    print("Palindrome")
    
    
    
# 3.  Write a program to count the number of vowels in a string.

string = "kiran"
count = 0
for char in string:
    if char in 'aeiouAEIOU':
        count = count + 1
print(count)


#  4. Write a program to find the length of a string without using the `len()` function.

string = "kiran kumar"
length = 0
for char in string:
    length = length + 1 
print(length)


# 5.  Write a program to check if a substring exists within a given string. 
string = 'kiran kumar'
substring = 'ir'
if substring in string:
    print("Exist")
    
    
# 6.  Write a program to concatenate two strings without using the `+` operator.

string1 = "kiran"
string2 = "kumar"
# use join method 

result = " ".join([string1,string2])
print(result)




# 7.  Write a program to count the number of words in a string.
string = "kiran is a good boy"
print(string.count(" ")  + 1)



# 8.  Write a program to convert all characters in a string to uppercase.

string = "kiran IsA"
print(string.upper())



# 9.  Write a program to replace all spaces in a string with underscores.
string = "kiran is a"
print(string.replace(" ","_"))


# 10.  Write a program to extract digits from a string.

string = "kiran 232 dfai424"
for char in string:
    if char in "0123456789":
        print(char, end="")










'''


Here are 10 intermediate-level Python string program prompts:

1.  Write a program to find the first non-repeating character in a string.
2.  Write a program to check if two strings are anagrams of each other.
3.  Write a program to find and replace all occurrences of a substring in a string.
4.  Write a program to remove all duplicate characters from a string.
5.  Write a program to find the frequency of each character in a string.
6.  Write a program to split a string into a list of words and sort them in alphabetical order.
7.  Write a program to check if a string is a valid email address.
8.  Write a program to reverse the order of words in a sentence.
9.  Write a program to capitalize the first and last character of every word in a string.
10.  Write a program to count the number of uppercase and lowercase letters in a string.



'''


# 11.  Write a program to find the first non-repeating character in a string.

string = "kiran"
for char in string: 
    if string.count(char) == 1:
        print(f"First Non-Repeating Character is {char}")
        break