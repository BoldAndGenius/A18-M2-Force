'''Check user entered word is a keyword or not'''

# import keyword
# keywords = keyword.kwlist
# word = input("Enter a word: ")
# if word in keywords:
#     print(f"{word} is a keyword...")
# else:
#     print(f"{word} is not a keyword...")

'''Adding all the digits from a user entered number'''

# num = int(input("Enter a number: "))
# sum = 0
# while num != 0:
#     last_digit = num % 10
#     sum += last_digit
#     num //= 10
# print(f"Sum of digits = {sum}")

'''Add digits of user entered number only if it is even number'''

# num = int(input("Enter a number: "))
# sum = 0
# if num % 2 == 0:
#     while num != 0:
#         last_digit = num % 10
#         sum += last_digit
#         num //= 10
#     print(f"Sum of digits = {sum}")

'''add digits only if last digit is even using while loop'''

# num = int(input("Enter a number: "))
# sum = 0
# ldigit = str(num)
# if int(ldigit[-1]) % 2 == 0:
#     while num != 0:
#         last_digit = num % 10
#         sum += last_digit
#         num //= 10
# print(f"Sum of digits = {sum}")

'''add digits only if digits are even using while loop'''

# num = int(input("Enter a number: "))
# sum = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit % 2 == 0:
#         sum += last_digit
#     num //= 10
# print(f"Sum of digits = {sum}")

'''check for number palindrome without typecasting'''

# num = int(input(": "))
# temp = num
# rev = 0
# while num != 0:
#     last_digit = num % 10
#     num //= 10
#     rev = (rev * 10) + last_digit
    
# if temp == rev:
#     print(f"{temp} is palindrome...")
# else:
#     print(f"{temp} is not palindrome...")

'''check for word palindrome without using built-in functions'''    

# word = input("Enter a word: ")
# rev = ""
# idx = 0
# while idx < len(word):
#     rev = word[idx] + rev
#     idx += 1

# if word == rev:
#     print(f"{word} is a Palindrome...")
# else:
#     print(f"{word} is not a Palindrome...")

'''extract string from heterogenous list and add string to another list only if it is palindrome using while loop'''

# items = [(10, 20), 71, "racecar", ['a', 'b'], 'test', {1, 2, 3}, 'chepauk', 'malayalam', 'rotator']
# palindrome = []
# idx = 0
# while idx <  len(items):
#     if type(items[idx]) is str:
#         rev = ""
#         i = 0
#         while i < len(items[idx]):
#             rev = items[idx][i] + rev
#             i += 1
#         if rev == items[idx]:
#             palindrome.append(rev)
#     idx += 1
  
# print(palindrome)

'''display a dictionary where keys are the characters in a string and values are its ASCII value'''

# word = input("Enter a word: ")
# indx = 0
# output = {}
# while indx < len(word):
#     char = word[indx]
#     if char not in output:
#         output[char] = ord(char)
#     indx += 1
# print(output)

'''display a dictionary where keys are the characters in a string and values are its number of occerences'''

# word = input("Enter a word: ")
# indx = 0
# output = {}
# while indx < len(word):
#     char = word[indx]
#     if char in output:
#         output[char] += 1
#     else:
#         output[char] = 1
#     indx += 1
# print(output)

'''display a dictionary where keys are the words in a string and values are length of that word'''

# line = input("Enter a sentence: ")
# words = line.split()
# indx = 0
# output = {}
# while indx < len(words):
#     word = words[indx]
#     if word not in output:
#         output[word] = len(word)
#     indx += 1
# print(output)

'''catagorize all the file names w.r.t its extensions'''

# files = ['start.py', 'demo.txt', 'hello.py', 'new.py', 'bye.txt', 'some.csv']
# output = {}
# indx = 0
# while indx < len(files):
#     file = files[indx]
#     file_info = file.split('.')
#     name = file_info[0]
#     ext = file_info[1]
#     if ext in output:
#         output[ext] += [name]
#     else:
#         output[ext] = [name]
#     indx += 1
    
# print(output)

