#################################################################################
#################################################################################
'''SVDT TYPECASTING'''

'''int to other datatype'''
digit = 20
print(float(digit))         #20.0
print(complex(digit))       #20 + 0j
print(bool(digit))          #True
print(str(digit))           #'20'

'''following gives TypeError'''
# print(list(digit))
# print(tuple(digit))
# print(set(digit))
# print(dict(digit))

#################################################################################
#################################################################################
'''float to other datatype'''
number = 15.0
print(int(number))              #15
print(complex(number))          #15 + 0j
print(bool(number))             #True
print(str(number))              #

'''following gives TypeError'''
# print(list(number))
# print(tuple(number))
# print(set(number))
# print(dict(number))

#################################################################################
#################################################################################
'''boolean to other datatype'''
bool_value = True
print(int( bool_value))          #1
print(complex(bool_value))      #1 + 0j
print(float(bool_value))        #1.0
print(str(bool_value))          #'True'

'''following gives TypeError'''
# print(list(bool_value))
# print(tuple(bool_value))
# print(set(bool_value))
# print(dict(bool_value))

#################################################################################
#################################################################################
'''COLLECTION TYPECASTING'''

'''str to other datatype'''

string = "10"
print(int( string))          #10

string = "20.0"
print(float(string))        #20.0

string = "2+3j"
print(complex(string))      #(2+3j)

string = "False"
print(bool(string))         #True(checks if default or not)

string = "hello"
print(list(string)) #['h', 'e', 'l', 'l', 'o']
print(tuple(string))#('h', 'e', 'l', 'l', 'o')
print(set(string))#{'l', 'o', 'e', 'h'}
# print(dict(string))       #ValueError


#################################################################################
#################################################################################
'''list to other datatype'''
numbers = [10, 20, 30, 40]

'''following gives TypeError'''
# print(int(numbers))     #TypeError
# print(float(numbers))   #TypeError
# print(complex(numbers)) #TypeError

print(bool(numbers))        #True(non default)
print(tuple(numbers))       #(10, 20, 30, 40)
print(set(numbers))         #{40, 10, 20, 30}


items = [{10, 20}, ("a", "hello"), ["b", 100], {"a":100, "c":200}, "xy"]
print(dict(items))

#################################################################################
#################################################################################
'''converting tuple to other datatype'''
items = ("hey", 10.0, True, (10, 20))

# print(int(items))     #TypeError
# print(float(items))   #TypeError
# print(complex(items)) #TypeError

print(bool(items))      #True
print(str(items))       #'('hey', 10.0, True, (10, 20))'
print(list(items))      #['hey', 10.0, True, (10, 20)]
print(set(items))       #{True, 10.0, 'hey', (10, 20)}


items = ("cd", ["a",10], ("b", 100), ("d", 50))
print(dict(items))  #{'c': 'd', 'a': 10, 'b': 100, 'd': 50}

#################################################################################
#################################################################################
'''converting set to other datatype'''
items = {10, "string", 9.5, (10, 20)}

# print(int(items))     #TypeError
# print(float(items))   #TypeError
# print(complex(items)) #TypeError

print(bool(items))   #True
print(str(items))    #{9.5, 10, 'string', (10, 20)}   
print(list(items))   #['string', 10, 9.5, (10, 20)]
print(tuple(items))  #('string', 10, 9.5, (10, 20))

items = {"xy", ("b", 100), ("d", 50)}
print(dict(items))  #{'x': 'y', 'b': 100, 'd': 50}

#################################################################################
#################################################################################
'''converting dict to other datatype'''
student_info = {"name":"abarna", "native": "TN", "education":"BTech"}

# print(int(student_info))     #TypeError
# print(float(student_info))   #TypeError
# print(complex(student_info)) #TypeError

print(bool(student_info))#True
print(str(student_info))#'{"name":"abarna", "native": "TN", "education":"BTech"}'
print(list(student_info))#['name', 'native', 'education']
print(tuple(student_info))#('name', 'native', 'education') 
print(set(student_info)) #{'name', 'native', 'education'}

#################################################################################
#################################################################################