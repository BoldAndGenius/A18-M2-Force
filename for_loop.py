#wap stands for write a program 

#1.wap to extract all the numeric values in a given collection  --(ASHA S)
collection=eval(input('Enter a collection :'))
numbers=[]
for item in collection:
    if type(item) in [int,float,complex]:
        numbers.append(item)
print(f"All numbers in a collection are :{numbers}")

#2.wap to extract all lowercase characters in a given string using for loop --(ASHA S)
string=input('Enter a string :')
lower=''
for char in string:
    if char.islower():
        lower+=char
print(f"Lowercase characters are {lower}")

#3.wap to display a dictionary whose keys are words of a sentence  and the values are the length of each word using for loop  --(ASHA S)
sentence=input("Enter a sentence :")
output={}
words=sentence.split()
for word in words:
    if word not in output:
        output[word]=len(word)
print("Dictionary :",output)

#4.wap to mimic len function  --(ASHA S)
string=input('Enter a string :')
count=0
for char in string:
    count+=1
print(f"Length of string {string} is {count}")

#5.wap to display a largest number in a given collection  --(ASHA S)
collection=eval(input('Enter a collection of numbers :'))
max=0
for num in collection:
    if num>max:
        max=num
print(f"Largest number of a collection is {max}")

#6.wap to print range of natural numbers entered by the user using for loop --(ASHA S)
num=int(input('Enter the ending number :'))
for nums in range(1,num):
    print(nums)

#7.wap to print even numbers by using range entered by the user --(ASHA S)
last_num=int(input('Enter a number :'))
for even in range(last_num):
    if even%2==0:
        print(even)

  #(or)
last_num=int(input('Enter a number :'))
for even in range(0,last_num,2):
    print(even)

#8.wap to print square of a numbers by using range entered by the user --(ASHA S)
last_num=int(input('Enter a last number :'))
for num in range(last_num):
    print(f"Square of {num} is {num**2}")

#9.wap to print multiples of 5 and 10 by using range entered by the user --(ASHA S)
last_num=int(input('Enter a last number :'))
for num in range(last_num):
    if num%5==0 and num%10==0:
        print(f"{num} is multiple of both 5 and 10")

#10.wap to print countdown of a game using for loop --(ASHA S)
start=int(input("Eneter a countdown starting number :"))
for count in range(start,-1,-1):
    print(count)

#11.wap to add all the digits in a user entered number using for loop --(ASHA S)
num = input('Enter a number :')
sum=0
for digit in num:
    sum+=int(digit)
print(f"Sum of the digits of a number {num} is {sum} ")

#12.wap to swap keys and values from a given dictionary using for loop --(ASHA S)
dictionary={'Name':'Asha','Batch':"A18","YOP":2024,'Trainer':'Shashank B G','CGPA':9.16}
output={}
for key in dictionary:
    value=dictionary[key]
    if value not in output:
        output[value]=key
print(output)

#13.wap to filter to have only single value datatype using for loop --(ASHA S)
items={10,9+9j,'python',True,'12.99',91.09,(90,'course')}
output=set()
for item in items:
    if type(item) not in [str,tuple]:
        output.add(item)
print(output)

#14.wap to display most occuring  words from a given string --(ASHA S)
string='dont trouble the trouble if you trouble the trouble then trouble troubles you'
words=string.split()
output={}
for word in words:
    if word in output:
        output[word]+=1
    else:
        output[word]=1
max_val=max(output.values())
max_occurance=[]
for key in output:
    if output[key]==max_val:
        max_occurance.append(key)
print(output)
print(max_occurance)

#15.wap to print all even numbers from 0 to 100 using for loop --(ASHA S)
for even in range(0,101,2):
    print(even)

#16.wap to print all even numbers from 0 to 100 in a reverse order using for loop --(ASHA S)
for even in range(100,-1,-2):
    print(even)

#17.wap to print multiplication of a number entered by the user using for loop --(ASHA S)
num = int(input("Enter a number :"))
for factor in range(1,11):
    print(f"{num} X {factor} = {num*factor}")

#18.wap to print all odd numbers from 1 to 100  using for loop --(ASHA S)
for odd in range(1,100,2):
    print(odd)

#19.wap to print all even numbers from 0 to 100 in a reverse order using for loop --(ASHA S)
for odd in range(99,0,-2):
    print(odd)

#20.wap to print factorial of a given number using for loop --(ASHA S)
num=int(input('Enter a number :'))
fact=1
for factor in range(1,num+1):
    fact*=factor
print(f"factorial of a {num} is {fact}")

#21.wap to print fibonacci series of a given number using for loop --(ASHA S)
num=int(input('Enter a number :'))
series=[0,1]
if num==1:
    print(series[0])
elif num==2:
    print(series)
else:
    for _ in range(num-2):
        fib=series[-1]+series[-2]
        series.append(fib)
print(series)

#22.wap to check for a word pallindrome using for loop --(ASHA S)
word=input('Enter a word :')
reverse=''
for char in word:
    reverse=char+reverse
if reverse==word:
    print('Palindrome.....')
else:
    print('Not palindrome')

#23.wap to check for a number pallindrome using for loop --(ASHA S)
num=int(input('enter a number :'))
number=str(num)
reverse=''
for digit in number:
    reverse=digit+reverse
if int(reverse)==num:
    print('Palindrome...')
else:
    print("Not palindrome...")

# ( or )

num=int(input('enter a number :'))
org_num=num
reverse=0
for _ in range(len(str(num))):
    last_digit=num%10
    reverse=reverse*10+last_digit
    num//=10
if reverse==org_num:
    print('Palindrome...')
else:
    print("Not palindrome...")

#24.wap to display a dictionary   
# i.if datatype of an item is immutable then
#   keys are the items of a collection and  the values are datatype of each item in a collection
#ii.if datatype of an item is mutable then
#  keys are the data type of items of a collection and assign value as a 'mutable data'  --(ASHA S)
collection=[10,2+3j,'Pyspider',{'flower','fire','water'},['asha','shashi',10,20.6],(45,420),True]
output={}
for item in collection:
    if type(item) not in [set,dict,list]:
        output[item]=type(item)
    else:
        output[type(item)]='mutable data'
print(output)

#25.wap to categorize all file names with respect to its extenction using for loop --(ASHA S)
files=['whileloop.py','sample.py','indext.html','vedio.mp4','audio.mp3','document.txt','requirement.csv','first.php','style.css','logic.js']
output={}
for file in files:
    item=file.split('.')
    name=item[0]
    ext=item[1]
    if ext in output:
        output[ext]+=[name]
    else:
        output[ext]=[name]
print(output)

#26.wap to display a dictionary where the keys are the characters ina string and its values are its ascii values --(ASHA S)
string=input('Enter a string :')
output={}
for char in string:
    if char not in output:
        output[char]=ord(char)
print(output)

#27.wap to display a dictionary where the keys are the characters ina string and its values are its number of occurances --(ASHA S)
string=input('Enter a string :')
output={}
for char in string:
    if char in output:
        output[char]+=1
    else:
        output[char]=1
print(output)

#28.wap to print sum of natural numbers from 1 to 100 using for loop --(ASHA S)
sum=0
for num in range(1,101):
    sum+=num
print('sum is :',sum)

#29.wap to print sum of even numbers from 0 to 100 using for loop --(ASHA S)
sum=0
for even in range(0,101,2):
    sum+=even
print('sum is :',sum)

#30.wap to print square of numbers from 1 to 10 using for loop --(ASHA S)
for square in range(1,21):
    print(f"{square} X {square} = {square**2}")

#31.wap to print sum of cube numbers from 1 to 20 using for loop --(ASHA S)
sum=0
for num in range(1,21):
    print(f"{num} X {num} X {num} = {num**3}")
