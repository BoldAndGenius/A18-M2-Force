# Q10. Write a program to check whether a number is prime or not using while loop and def keyword


def is_prime(num):
    if num<=1:
        return False
    i=2
    while i<num:
        if num%i==0:
            return False
        i+=1
    return True

integer=int(input('num: '))

if is_prime(integer):
    print('prime')
else:
    print('not prime')


