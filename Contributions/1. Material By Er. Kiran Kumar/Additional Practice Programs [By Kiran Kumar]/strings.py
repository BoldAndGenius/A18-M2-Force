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