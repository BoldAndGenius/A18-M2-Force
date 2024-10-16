#WAP to extract all the numeric values in a given collection
collection = [10,7.5,'bye',[20,80],2+3j,65]
values = []
for item in collection:
    if type(item) in [int,float,complex]:
        values.append(item)
print(values)

#WAP to extract all lowercase character from a given string using for loop
string = "heLLomam"
values=[]
for char in string:
    if 'a' <= char <= 'z':
        values.append(char)
print(values)

#WAP to display a dictionary whose keys are words of a sentence and value are length of each word using for loop
sentence = "hey shan how are you"
words = sentence.split()
output = {}
for word in words:
    output[word] = len(word)
print(output)

#WAP to mimic len function.
collection = eval(input("Enter any collection:"))
count = 0
for _ in collection:
    count += 1
print(count)

#WAP to display a largest number from a given collection.
nums = [7,21,5,17,81]
max=0
for num in nums:
    if num > max:
        max = num
print(f"The largest number from a given collection is:{max}")

#WAP to swap keys and values from a given dictionary using for loop.
dictionary = {'a':10,'b':20,'c':30}
output = {}
for item in dictionary:
    value = dictionary[item]
    output[value] = item
print(output)

#WAP to filter a set to have only single-value data types using for loop.
set_ = {10,20+3j,30.0,"string",(10,20)}
output = set()
for item in set_:
    if type(item) in [int,float,complex,bool]:
        output.add(item)
print(output)

#WAP to display most occuring words from a given string.
string = "dont trouble the the the the trouble otherwise trouble start trouble you"
words = string.split()    #split all the words in a single word
output = {}
for word in words:
    if word not in output: #if word is not present in the dictionary then make that word as key and assign its value  1 as first occurence
        output[word] = 1
    else:
        output[word] += 1  #if word is already present as key then increment the value by 1 as its further occurences

max_value = max(output.values())   #we store the max value of key here

list_of_word = []                 #the word may be more than one so we take an empty list so that we can store the most occuring words
for item in output:
    if output[item] == max_value: #comparing all the values of keys by the maximum value.if value of key and max value got matched
        list_of_word.append(item) #Here we got the most occuring word and store in the empty list
if len(list_of_word) == 1:
    print(list_of_word)
else:
    print(f"The string has more than one word whose occurences are same that is {list_of_word}")
    
#WAP to print n natural numbers using for loop.
num = int(input("Enter a num:"))
for n in range(1,num+1):   #in range function end point is always excluded so we use +1 to include that number,and
                           #to show natural number till num entered by the user
    print(n)

#WAP to print all even numbers from 0 to 100.
for num in range(0,101,2):
    print(num,end=",")

#WAP to print multiplication table of a given number.
number = int(input("Enter a num:"))
for factor in range(1,11):
    print(f"{number} x {factor} = {number * factor}")

#WAO to print odd numbers from 0 to 100 in reverse order.
for num in range(99,0,-2):
    print(num,end=",")

#WAP to print factorial of given number using for loop.
fact = 1
number = int(input("Enter a num:"))
for num in range(1,number+1):
    fact = fact * num
print(fact)

#WAP to print fibonacci series upto n terms entred by the user.
start = 0
end = 1
series = [0,1]
n_terms = int(input("Enter n:"))
if n_terms == 1:
    print(start)
else:
    for _ in range(n_terms-2):
        item = series[start] + series[end]
        start +=1
        end += 1
        series.append(item)
    
    print(series)

###################################### one more optimized solution of fibonacci series ####################################
n_terms = int(input("Enter n:"))
series = [0,1]
if n_terms == 1:
    print(series[0])
else:
    for _ in range(n_terms-2):
        series.append(series[-1] + series[-2])
    print(series)           