# Adding Two Numbers
def add(num1,num2):
    return num1+num2
num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
sum = add(num1,num2)
print(sum)

# Check Palindrome or Not
def check_Palindrome(word):
    rev = word[::-1]
    if word == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
word = input("Enter Word: ")
check = check_Palindrome(word)
print(check)

#To display 1st element given collection
def first_element():
    first = collection[0]
    return first
collection = eval(input("Enter: "))
last = first_element()
print(last) 
