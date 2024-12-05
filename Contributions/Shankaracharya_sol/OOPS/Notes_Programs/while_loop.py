#WAP to print 'python' 5 timnes using while loop
count = 1
while count <= 5:
    print("python")
    count += 1

#WAP to print n number of natural number using while loop
num = int(input("Enter n:"))
count = 1
while count <= num:
    print(count)
    count += 1

#WAP to print countdown(reverse order) of the no. using while loop
num = int(input("Enter a num:"))
end = 0
while end <= num:
    print(num)
    num -= 1

#WAP to add all the digits in a user entered number using while loop.
num = int(input("Enter num:"))
sum = 0
while num != 0:
    last_digit = num % 10   #to get last digit
    sum += last_digit
    num //= 10              #to remove last digit
print(sum)

#WAP to add all the digits in a user entered number only if it is an even number using while loop.
num = int(input("Enter num:"))
sum=0
if num % 2 == 0:  #to check whether the num is even or not
    while num != 0:
        last_digit = num % 10    #to get last digit
        sum += last_digit
        num //= 10           #after summation,remove last digit
    print(sum)
else:
    print("num is not an even number")


#WAP to add all the digits in a user entered number only if it is an odd number using while loop.
num = int(input("Enter num:"))
sum = 0
if num % 2 == 1:  #to check whether the last digit is odd or not
    while num != 0:
        last_digit = num % 10    #to get last digit
        sum += last_digit
        num //= 10           #after summation,remove last digit
    print(sum)
else:
    print("num is not odd number")               


#WAP to add each digit in a number only if the digits is even.
num = int(input("Enter num:"))
sum = 0
while num != 0:
    last_digit = num % 10     #to get last digit
    if last_digit % 2 == 0:
        sum += last_digit     #summation of last digit
        num //= 10            #to remove last digit after summation
    else:
        num //= 10            #to remove last digit without summation
print(sum)

#WAP to check for number palindrome without using typecasting.
num = int(input("Enter a num:"))
temp = num
rev = 0
while num != 0:
    last_digit = num % 10        #to get last digit  from the number
    rev = last_digit + rev * 10  #pushing last digit to tens place by multiplying by 10 and then adding the last_digit at ones place
    num //= 10                   #to remove last digit from the number
if temp == rev:
    print("its a palindrome number")
else:
    print("Its not a palindrome number")
    
#WAP to check for word palindrome without using typecasting.
word = input("Enter a word:")
rev = ''
index = 0
while index < len(word):        #run this loop until length of the word
    rev = word[index] + rev     #add character before the given reverse character to make the word reverse
    index += 1
if rev == word:
    print("its a palindrome")
else:
    print("its not a palindrome")

#WAP to extract all uppercase & lowercase character using while loop.
string = input("Enter a string:")
lower = ''
upper = ''
index = 0
while index < len(string):
    char = string[index]    #to get each character from the string
    index += 1
    if 'A' <= char <= 'Z':
        upper += char       #add the item in empty string if it is uppercase
    elif 'a' <= char <= 'z':
        lower += char       #add the item in empty string if it is lowercase
print(upper,lower, sep=",")

#WAP to extract all alphabet,numeric and special character from a user entered word using while loop.
word = input("Enter a word:")
alpha = ''
numeric = ''
special_char = ''
index = 0
while index < len(word):
    char = word[index]
    index += 1
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        alpha += char
    elif '0' <= char <= '9':
        numeric += char
    else:
        special_char += char
print(alpha,numeric,special_char,sep=",")


#WAP to extract all immutable and mutable data from a given collection.
list_ = [(10,20),10,10.5,2+1j,{10,20},{'a':23}]
mutable = []
immutable = []
index = 0
while index < len(list_):
    element = list_[index]
    index += 1
    if type(element) not in [list,set,dict]:   #if data type is not mutable means it will be immutable
        immutable.append(element)
    else:
        mutable.append(element)
print(f"Mutable data:{mutable}")
print(f"Immuatble data:{immutable}")

#WAP to check whether an element in a given list is string or not,if it is a string check whether it is palindrome or not,if the string is palindrome store it in another list.
list_ = ['hello',10,"level",(10,20),"malayalam"]
palindrome = []   #taking an empty list so that we can store the palindrome element if present
index_list = 0    #to trace list element
while index_list < len(list_):
    element = list_[index_list]
    index_list += 1
    if type(element) == str:
        index_element = 0    #to trace each char of the string
        rev = ''             #to store all the characters after reversing it char by char
        while index_element < len(element):
            rev = element[index_element] + rev
            index_element += 1
        if rev == element:
            palindrome.append(element)
print(palindrome)

#WAP to mimic replace function(method) in string.
line="if you are bad i will be mad"        #output"if_you_are_bad_i_will_be_mad"
index = 0
string =''
while index < len(line):
    char = line[index]
    index += 1
    if char != ' ':               #char is not equal to space,just add the char as it is
        string += char
    else:                          
        string += '_'             #char is space i want to replace space with underscore
print(string)

#WAP to mimic string swapcase method.
string = input("Enter an string")
index = 0
output = ''
while index < len(string):
    char = string[index]
    index += 1
    if 'a' <= char <= 'z':
        ascii = ord(char)         #to know the ascii value of a char we use ord function
        ascii -= 32               #in between the ASCII value of uppercase and lowercase there is difference of 32(A=65,a=97)
        char =chr(ascii)          #to know the character of an ascii value we use chr function
        output += char
    else:
        if 'A' <= char <= 'Z':
            ascii = ord(char)
            ascii += 32
            char += chr(ascii)
            output += char
print(output)

#WAP to mimic string isalpha method.
string = input("Enter an string:")
index = 0
isalpha = True
while index < len(string):
    char = string[index]
    index += 1
    if not ('A' <= char <='Z' or 'a' <= char <= 'z'):   #if char not in between A-Z or a-z means char is either numeric or special char
        isalpha =  False                                #so make isalpha False
        break                                           #to come out from the loop we use break
print(isalpha)
#WAP to mimic string upper method.
string = input("Enter a string:")
index = 0
output = ''
while index < len(string):
    char = string[index]
    index += 1
    if 'a' <= char <= 'z':
        ascii = ord(char)
        ascii -= 32
        char = chr(ascii)
        output += char
    else:
        output += char
print(output)
#WAP to mimic string lower method.
string = input("Enter a string:")
index = 0
output = ''
while index < len(string):
    char = string[index]
    index += 1
    if 'A' <= char <= 'Z':
        ascii = ord(char)
        ascii += 32
        char = chr(ascii)
        output += char
    else:
        output += char
print(output)
#WAP to mimic string isnumeric method.
string = input("Enter an string:")
index = 0
isnumeric = True
while index < len(string):
    char = string[index]
    index += 1
    if not ('0' <= char <='9'):   #if char not in between 0-9 means char is either alphabet or special char
        isnumeric =  False        #so make isnumeric False
        break                     #to come out from the loop we use break
print(isnumeric)

#WAP to mimic string isupper method.
string = input("Enter an string:")
index = 0
isupper = True
while index < len(string):
    char = string[index]
    index += 1
    if not ('A' <= char <='Z'):   #if char not in between A-Z char is either lowercase or numeric or special char
        isupper =  False          #so make isupper False
        break                     #to come out from the loop we use break
print(isupper)

#WAP to mimic string islower method.
string = input("Enter an string:")
index = 0
islower = True
while index < len(string):
    char = string[index]
    index += 1
    if not ('a' <= char <= 'z'):   #if char not in between a-z means char is either uppercase or numeric or special char
        islower =  False           #so make islower False
        break                      #to come out from the loop we use break
print(islower)

#WAP to display a dictionary where the keys are the characters in a string and its value will be its ASCII value.
string = "hey shan how are you"
index = 0
output = {}
while index < len(string):
    char = string[index]
    index += 1
    if char not in output:
        output[char] = ord(char)
print(output)

#WAP to display a dictionary,where the keys are the characters of the string and the values are its number of occurences.
string = "aaabcdhay"
index = 0
output = {}
while index < len(string):
    char = string[index]       #we fetch the the each char 
    index += 1
    if char not in output:     #if is not present make that char as new key 
        output[char] = 1       #and give occurence as 1 for the first time
    else:
        output[char] += 1      #if char is already present just increment the occurence of that char by 1
print(output)

#WAP to display a dictionary whose keys are words of a sentence and its values are length of each word.
sentence = input("Enter a sentence:")
words = sentence.split()         #split method,split the whole sentence as single-single words
index = 0
output={}
while index < len(words):
    word = words[index]          #take each word from the group of words
    output[word] = len(word)     #assign the length of the word to the key named word
    index += 1
print(output)

#WAP to categorized all the file nbames with respect to its extensions.
# given (files=['start.py','demo.txt','hello.py','new.py','bte.txt','same.csv'])
files=['start.py','demo.txt','hello.py','new.py','bte.txt','same.csv']
index = 0
output = {}
while index < len(files):
    item = files[index]         #take each each item from the given string
    file = item.split('.')      #split that item from their . character
    name = file[0]              #store the first element as name
    ext = file[1]               #store the second element as extension
    index += 1
    if ext not in output:       #if extension is not present in dictionary make that extension as key
        output[ext] = [name]    #and assign name of file to that key into a list
    else:
        output[ext] += [name]   #if key is already present just update the value of the list and perfrom list concatenation
print(output)