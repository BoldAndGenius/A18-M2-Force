
# Question - 1
# Write a Python program to create a class called Person with private instance variables name, age, and country. Provide public getter and setter methods to access and modify these variables. 

class Person:
    __name = "Kiran"
    __age = 23 
    __country = "India"
    
    
    def getter(self):
        print(self.__name)
        print(self.__age)
        print(self.__country)
    def setter(self, new_name, new_age, new_country):
        self.__name = new_name
        self.__age = new_age
        self.__country = new_country
        print(self.__name)
        print(self.__age)
        print(self.__country)

Kiran = Person()
Kiran.getter()
Kiran.setter("Kunal", 25, "USA")