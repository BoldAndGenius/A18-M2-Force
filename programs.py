# WAP to print Fibonacci Series starting from any two numbers
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
n = int(input("Enter the n value: "))
if n <= 1:
    print("The value of n should be greater than 1 to generate a Fibonacci series.")
else:
    seq = [first, second]
    for i in range(n - 2):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    print(f"The Fibonacci series for {n} terms is {seq}")
            



#  WAP to check whether a number is prime or not

num=int(input("Enter a number:"))
if num <= 1:
    print(f"{num} is neither prime nor composite")
else:
    for n in range(2,int(num**0.5)+1):    
        if num %n ==0:
            print(f"{num} is Composite Number")
            break
    else:
        print(f"{num} is Prime Number")

#   WAP to print Prime numbers between two ranges

# Input for start and end values
start=int(input("enter starting number:"))
end=int(input("enter ending number:"))

primes=[] 
is_prime=True # Assume the number is prime initially

for num in range(start,end+1):   
    if num <= 1:
        print(f"{num} is neither prime nor composite")
    else:
        for n in range(2,int(num**0.5)+1):    
            if num % n ==0:
                is_prime=False   
                break  # Exit the loop if a divisor is found
        if is_prime:
            primes.append(num)
print(f"prime numbers between range {start} and {end} is {primes}") 



# WAP to print Factors of a Number

num=int(input("Enter a Number:"))
list=[]
for factor in range(1,num+1):
    if num%factor==0:
        list.append(factor)
print(f"Factors of {num} are {list}")



# WAP to print prime factors of a Number

num = int(input("Enter a Number: "))
prime_factors = [] 

for factor in range(2, num + 1):  # Start from 2 since 1 is not a prime
    if num % factor == 0:
        is_prime = True  # Assume factor is prime
      
        # Check if the factor is prime
        for n in range(2, int(factor ** 0.5) + 1):
            if factor % n == 0:  
                is_prime = False
                break
        if is_prime:  # If still true, it's a prime factor
            prime_factors.append(factor)

# Print the results
print(f"Prime factors of {num} are {prime_factors}")





