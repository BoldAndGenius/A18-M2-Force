def factorial(num):
    fact = 1
    if num == 0 or num==1 :
        return fact
    else:
        for num in range(1,num+1):
            fact = fact * num 
        return fact 
