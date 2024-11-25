##########################################################################
'''time module'''

# from time import sleep, time, ctime
import time
'''
time.time() -> float - gives the number of seconds since epoch(1970 Jan 1 00:00:00)
time.sleep(num) -> None - pauses the execution for num seconds
time.ctime() -> str - gives all the details including day, date, month, year and time
'''


# start = time.time()
# nums = []
# for num in range(100000000):
#     nums.append(num)
# end = time.time()
# print(end - start)

# print("start")
# time.sleep(2)
# print("end")

# print(time.ctime().split()[3])

##########################################################################
'''math module'''

import math

#degrees(num in radians) -> float - gives degree for a given number in radians
print(math.degrees(22 / 7))

#radians(num in radians) -> float - gives radians for a given number in degrees
print(math.radians(180))

#sin(num)/ cos(num)/ tan(num) -> float - gives sin/ cos/ tan of the number in radians
print(math.sin(math.radians(90)))
print(math.cos(0))
print(math.tan(math.radians(90)))

#factorial(num) -> int - gives factorial of a given integer
print(math.factorial(5))

#fabs(num) -> float - gives absolute value(positive) for any given number
print(math.fabs(-2))

#fsum(collection) -> float - gives sum of all the numbers in a given collection
print(math.fsum([1, 2.3, 5, 7]))

#gcd(*args) -> int - gives gcd for any number of given integers
print(math.gcd(12, 32, 90))
print((3 * 7) /math.gcd(3, 7))

#dist(collection1, collection2) -> float - gives distance between any two coordinates passed in a collection
print(math.dist([10, 12, 1], [1, 9, 3]))

#sqrt(num) -> float - gives square root of any number
print(math.sqrt(3))

#isqrt(num) -> int - gives integer part of square root of any given number
print(math.isqrt(3))

#isfinite(num) -> bool - checks if a given nunber is finite or not
print(math.isfinite(math.inf))

#isinf(val) -> bool - checks if the given value if infinite or not
#Note: infinite value cannot be stored in python. But it can be represented as math.inf or float('inf') 
print(math.isinf(9))

#ceil(num) -> int - gives nearest upper integer for the given number
print(math.ceil(2.95))

#floor(num) -> int - gives nearest lower integer for the given number
print(math.floor(-2.1))

#fmod(a, b) -> gives float modulus value of a and b
print(math.fmod(15.2, 6.5))

print(math.remainder(5, 100))
print(math.trunc(-3.9))

#cbrt(num) -> gives cube root of a given num
print(math.cbrt(8))

#exp(num) -> gives e raised to the power num
print(math.exp(1))

#pow(a, b) -> gives a raised to the power of b
print(math.pow(2, 4))

#log(num) -> gives logarithmic value of num to base e
print(math.log(math.e))

#tau -> gives the value of tau (2*pi)
print(math.tau)

##########################################################################
'''random module'''
import random

#random() -> gives a random float value between 0 and 1
print(random.random())

#randint(a, b) -> gives a random int in range a and b both are inclusive
print(random.randint(1, 6))

#randrange(start, stop, step) -> gives a number between start and stop with step, stop is exclusive
print(random.randrange(1, 5, 2))


brands = ["poma", "abidas", "krocs", "rebook"]
#shuffle(iterable) -> simply shuffles the existing iterable
# random.shuffle(brands)
# print(brands)

#choice(iterable) -> gives a random value from the given iterable
print(random.choice(brands))

# choices(iterable, weight, k) gives a list of k elements from iterable and can increase the probability using weight
print(random.choices([1, 2], weights=[0.1, .9], k=5))

# '''HAND CRICKET'''
# player_batting = False
# score = 0
# while True:
#     player_choice = int(input("Player choice: "))
#     computer_choice = random.randint(1, 6)
#     if player_choice == computer_choice:
#         if player_batting:
#             print("Player Out!")
#             print("Player score ->", score)
#             player_batting = False  
#         else:
#             print("Computer Out!")
#             print("Your target ->", score)
#             score = 0
#             player_batting = True
#         break
#     else:
#         score += player_choice

    
##########################################################################
'''os module'''

import os


#getcwd() -> gives the path of vurrent working directory
print(os.getcwd())

#mkdir(name/path) -> to create a directory 
# os.mkdir("collections")
# for num in range(1, 51):
#     os.mkdir(f"collections/modules_folder {num}")

#makedirs(path) -> to create a folder inside a folder that doesn't exist
# os.makedirs("hello/tata")``

#rename(old, new) -> to rename a folder from old to new
# os.rename("hello", "chammak challo")

#rmdir(folder) -> removes the folder
#removedirs(path) -> removes the folder and keeps removing the parent folder unless it is not empty
# os.removedirs("humpty/dumpty/sat/on/wall")

#listdir(folder) -> to list the items in a folder
files = os.listdir("chammak challo/tata")

#stat(folder/file) -> gives statistics of a given file or folder
for file in files:
    size = os.stat(f"chammak challo/tata/{file}").st_size
    print(file, " -> ", size)

    print()
    if size > 50000000:
        os.remove(f"chammak challo/tata/{file}")
    
##########################################################################