
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





# Question - 2
# Write a Python program to create a class called BankAccount with private instance variables accountNumber and balance. Provide public getter and setter methods to access and modify these variables. 



class BankAccount:
    __accountNumber = 123456789
    __balance = 10000 
    
    def getter(self):
        print(self.__accountNumber)
        print(self.__balance)
    def setter(self, new_account_number, new_balance):
        self.__accountNumber = new_account_number
        self.__balance = new_balance
        print(self.__accountNumber)
        print(self.__balance)

Kiran = BankAccount()
Kiran.getter()
Kiran.setter(987654321, 20000)