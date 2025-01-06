import time

###  Encapsulation
class MBI:
    name = "Manoj Bank Of India"
    location = "Pamidi"
    chairman = "Gupta Ayer"
    ifsc_code = "MBI00124RG"
    def __init__(self,name,account_no,pin,balance):
        self.name = name
        self._account_no = account_no                            #Protected property
        self.__pin = pin                                         #Private property
        self.balance = balance
        self.transactions = []
    def deposit(self,name,amount):
        print(f"Depositing Rs.{amount} into {name} Account")
        self.balance += amount
        self.transactions.append(f"deposited Rs.{amount}")
    def withdraw(self,pin,amount):
        if self.__pin == pin:
            if self.balance > amount:
                print(f"{amount} Debited")
                self.balance -= amount
                self.transactions.append(f"Rs.{amount} debited ")
            else:
                print("Not Enough Money")
        else:
            print("You entered Wrong Pin")
    def display_transactions(self):
        start = 1
        for transaction in self.transactions:
            current_time = time.ctime()
            print(f"{start} --> {transaction} {current_time}")
            time.sleep(1)
            start += 1
            
person = MBI("Jagadessh","M1567290",4567,4000)
person.deposit("Ram",3000)
#print(person.balance)
person.withdraw(4567,1000)
#print(person.balance)
person.display_transactions()



## Getter Setter method
# class MechCoder:
#     __masala = ['x','y','z']
#     def get_masala(self):
#         return MechCoder.__masala
#     def set_masala(self,new_masala):
#         self.__masala = new_masala
# manoj = MechCoder()
# print(manoj.get_masala())
# print(manoj.set_masala(['m','n','o']))
# print(MechCoder.__dict__)
# print(manoj.__dict__)

## Property Decoration

# class MechCoder:
#     __masala = "Chicken masala"
#     @property
#     def masala(self):
#         return MechCoder.__masala
#     @masala.setter
#     def masala(self,new_masala):
#         self.__masala = new_masala
# man = MechCoder()
# # print(man.masala)
# man.masala = "Mutton Masala"
# print(man.masala)
# #print(man.__dict__)                      #{'_MechCoder__masala': "Mutton Masala"}

