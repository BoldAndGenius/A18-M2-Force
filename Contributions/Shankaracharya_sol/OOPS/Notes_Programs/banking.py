class SBI:
    name = "State Bank of India"
    Branch = "Ballia"
    IFSC = "SBIN002537"

    def __init__(self, name:str, dob:str, address:str, pin:int, mob_number:int, balance:int | float):
        self.name = name
        self.dob = dob
        self.address = address
        self.__pin = pin
        self._mobNumber = mob_number
        self.balance = balance
        self.transaction = []

    def deposit(self, amount:int | float):
        self.balance += amount
        # self.transaction.append(self.amount+ "credited to your bank account")
        print(f"Rs. {amount} credited to your bank account")
    
    def withdraw(self,amount:int|float, pin:int):
        if pin == self.__pin:
            if amount <= self.balance:
                self.balance -= amount
                # self.transaction.append(self.amount+"debitted from your bank account")
                print(f"Rs.{amount} debitted from your bank account")
            else:
                print("insufficient balance")
        else:
            print("wrong pin")
    
    def display_transactions(self):
        print(self.transaction)
    
shan = SBI("shankaracharya rai", "06-09-2002", "Ballia", 8006, 6394399793, 2000)
shan.withdraw(3000,8006)