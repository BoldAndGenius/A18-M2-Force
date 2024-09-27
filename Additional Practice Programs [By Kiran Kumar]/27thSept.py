# Armstrong Number 
# input - 153 --- 1*1*1+3*3*3+5*5*5 = 153
# output - Armstrong Number
# the sum of cube of each digits will equal to final number, it is armstrong.


number = int(input("Enter a number :"))  # 153
temp = number
sum = 0

while number > 0: # True # True   # True
    last = number % 10    # 3   # 5   # 0
    sum = sum + last*last*last    # sum = 0 + 3*3*3 = 27  # sum = 27 + 5*5*5 = 27+125 =  152
    number = number // 10    # 15  # 1
if temp == sum:
    print("Armstrong Number ")
else:
    print("Not an Armstrong Number")

