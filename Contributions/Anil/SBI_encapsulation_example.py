from time import sleep
from datetime import datetime
class SBI:
    name='State Bank of India'
    location='BTM Layout'
    chairman='Ram'
    ifsc_code='SBIN0002722'
    def __init__(self,name:str,acc_no:int,pin:int,balance:int):
        self.name=name
        self._acc_no=acc_no
        self.__pin=pin
        self.balance=balance
        self.transactions=[]
    def deposit(self,amount:int):
        print(f'Depositing Rs. {amount} into your account')
        self.balance+=amount
        self.transactions.append(f'Deposited Rs.{amount} on {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
        sleep(3)
        print(f'Dear user A/C {self._acc_no} credited by Rs.{amount} on {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
    def withdraw(self,amount:int):
        
        for i in range(3):
            self.pin=int(input('Enter your pin:'))
            if self.__pin == self.pin:
                if self.balance > amount:
                    self.balance-=amount
                    self.transactions.append(f'Withdrawn Rs.{amount} on {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
                    sleep(3)
                    print(f'Dear user A/C {self._acc_no} debited by Rs.{amount} on {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
                    break
                else:
                    print('Insufficient Balance')
                    break
            else:
                print('Wrong Pin Try Again..')
                i+=1
        else:
            print('Wrong Pin Try Again After 4hrs')
        
    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)
            sleep(3)
    def display_balance(self):
        print(f'Your Current Balance is {self.balance}')

Anil=SBI("MANDALA ANIL KUMAR",35423457491,9999,100000)
print(Anil.balance)
print(Anil.ifsc_code)
Anil.deposit(50000)
sleep(2)
Anil.display_balance()
Anil.deposit(150000)
sleep(2)
Anil.display_balance()
Anil.withdraw(10000)
sleep(2)
Anil.display_balance()
Anil.withdraw(5000)
sleep(2)
Anil.display_balance()
sleep(4)
Anil.display_transactions()
