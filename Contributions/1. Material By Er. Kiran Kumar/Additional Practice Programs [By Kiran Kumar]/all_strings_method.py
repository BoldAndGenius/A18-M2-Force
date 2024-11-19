# All String Methods -  
# Total 47 String Methods we have - out of which, 28 we goona use mostly in day to day programming.

'''

1. .upper()
2. .lower()
3. .isupper()
4. .islower()
5. .isalpha()
6. .isalnum()
7. .isnumeric()
8. .isdigit()
9. .swapcase()
10. .title()
11. .capitalize()
12. .count()
13. .index()
14. .find()
15. .replace()
16. .split()
17. .strip()
18. .lstrip()
19. .rstrip()
20. .center()
21. .ljust()
22. .rjust()
23. .endswith()
24. .startswith()
25. len()
27. .casefold()
28. .zfill()



'''


name = "kiran"
print(name.upper())  # KIRAN  # all the alphabets to uppercase

name = "KiRan"
print(name.lower()) # kiran # all the alphabets to lowercase

name = "KII ran"
print(name.isupper())  # check, is all the alphabets are in uppercase or not # False 

name = "ki IRaan"
print(name.islower()) # check, is all the alphabets are in lowercase of not   # False 

name = "kiran"
print(name.isalpha())  # check, is all the characters are alphabets or not # True 

name = "kir 232 iII"
print(name.isalpha())  # False 


name = "2323"
print(name.isnumeric()) #check all the characters are numeric or not  #True 

name = "232kira"
print(name.isdigit())  #check, all the chracters are numeric or not # False 


name = "322Kian"
print(name.isalnum())  # check, all the characres are alphanumeric (alphabet, numeric, combination of alphabets & numers)

name = "343kira"
print(name.isalnum()) # True 

name = "2432 Kiran Kiran@"
print(name.isalnum()) # False 

name = "kiran kumar is a good boy"
print(name.count('a')) # for all the occurences   # 3 


name = "kiran kumar is a good boy"
print(name.count('a'))
print(len(name))  # 25
print(name.count('a',0, 10))  # from 0 to 10th index, it will check the occurences of 'a' alphabet 



name = "kiran is a superstar"
print(name.index('i')) # gives the first occurences of 'i' character's index 

print(len(name))  # 20 
print(name.index('i',5,20))  # 6  # in the range of 5th index to 20th index, what is the first occurence of 'i' character, it gives the index of that. 


favourite_dish = "dosa"
print(favourite_dish.replace('dosa', 'chicken curry & biryani'))
print(favourite_dish.count('a'))
print(favourite_dish.swapcase())

sentence = "i love my India"
print(sentence.capitalize()) # first character (alphabet) to capital, reset all are in lowercase  # I love my india

print(sentence.title())  # I Love My India 



name = "Kiran Kumar"
print(name.strip())
print(name.strip('K'))

print(name.lstrip('K'))
print(name.rstrip('r'))




name = 'I love my India'
print(name.split())
print("".join(name))



name = "center"
print(name.center(10))

print(name.ljust(10))
print(name.rjust(10))


name = "I love my India"
print(name.endswith("India"))
print(name.startswith("I"))
print(name.find("I"))
print(name.find("Z"))  # -1
# print(name.index("Z")) # ValueError: substring not found 


print(name.casefold())



name = "kiran"
print(name.zfill(10)) # put 0  # 00000kiran

print(name.zfill(4)) # kiran 
print(name.zfill(2))  # kiran


