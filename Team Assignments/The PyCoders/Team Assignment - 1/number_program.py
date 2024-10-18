# Print all digits of a number on different lines 

num = int(input("Enter a number : "))  # 1234
while num>0:
    last = num % 10 
    print(last)
    num = num // 10