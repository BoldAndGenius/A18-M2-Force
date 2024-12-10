'''
Core Features
    Account Management
        Open new accounts.
        Close accounts.
    Transactions
        Deposit money.
        Withdraw money.
        Transfer funds between accounts.
    Balance Inquiry
        Check current account balance.
    Transaction History
        Maintain a record of all transactions (statements).
    Authentication
        Secure user login with passwords or PINs.
    Reports
        Generate account statements or transaction summaries.
    Optional Features
        Loans (e.g., calculate EMI).
        Interest on savings accounts.
        Admin dashboard for managing customers.
        User roles (e.g., admin, customer).
# Reading from a JSON file
                # with open("data.json", "r") as file:
                #     stored_data = json.load(file)
                #     print(stored_data)
'''
import random
import json
##################################################################################################################################################

###################################################################################################################################################
class AccountManagement:
            def __init__(self, name:str, address:str, contact_info:int, intial_deposit:int|float,account_type:str):
                self.name = name
                self.address = address
                self.contact_info = contact_info
                self.balance = intial_deposit
                self.account_type = account_type

                # Generate a random 10-digit for account number
                self.account_number = random.randrange(1000000000, 10000000000)  # Range from 1000000000 to 9999999999

                # Generate a random 4-digit for PIN
                self.actual_pin = random.randint(0000,10000)  # Range from 0000 to 9999

                print("Account Created Successfully")
                print(f"Your Account Number is:{self.account_number}")
                print(f"Your pin is XXXX")

            def deposit(self,account_num,amount):
                if account_num == self.account_number:
                    self.balance += amount
                    print(f"{amount} credited to your bank account{account_num}")
                    print(f"Available Balance is Rs. {self.balance}")

            def withdrawl(self,amount,pin):
                  if pin == self.actual_pin:
                        self.balance -= amount
                        print(f"{amount} debited from your bank account{account_num}")
                        print(f"Available Balance is Rs. {self.balance}")
##################################################################################################################################################
while True:
    print("                                              Welcome to State Bank Of India                            ")

    Option = eval(input("How Can I help You\nChoose the service you want \n1-Open new accounts.\n2-Close accounts.\n3-Deposit money.\n4-Withdraw money.\n5-Transfer funds between accounts.\n6-Check current account balance.\n7-Statement.\n8-Change ATM PIN\n9-Loans\n10-Interest on savings accounts.\n12-User roles (e.g., admin, customer).\n13-Exit\nEnter here:"))

    match Option:
        case 1:
                print("                                 To Open Your Account Please Fill details")
                First_name = input("First Name:")

                mid_name_option = int(input("Middle Name\n1-Yes\n2-No\nEnter:"))
                if mid_name_option == 1:
                    Middle_name = input("Middle Name:")
                elif mid_name_option == 2:
                    Middle_name = "N/A"

                Last_name = input("Last Name:")

                name = [First_name,Middle_name,Last_name]

                address = input("Your Adress")

                contact_info = input("Contact No:")

                intial_deposit = input("Intial Deposit Rs.")

                Acc_option = int(input("Type Of Account\n1-Savings\n2-Current\nEnter:"))
                if Acc_option == 1:
                    account_type = "Savings"
                elif Acc_option == 2:
                    account_type = "Current"  

                First_name = AccountManagement(name,address,contact_info,intial_deposit,account_type)

        case 2:
                print("                                 To Close Your Account\n")

                account_num = input("Enter your account number:")
                pin = int(input("Enter your pin code:"))
                new_file = {account_num,pin}
                #Reading from a JSON file
                with open("data.json", "r") as file:
                    if new_file in json.load(file):
                        del new_file
                        print("Account 'account2' has been deleted.")
                        # stored_data = json.load(file)
                        # print(stored_data)
                    else:
                         print("Wrong Details")

        case 3:
                print("                                 To Deposit Money")
                account_num = input("Enter Your Account Number:")
                amount = int(input("Enter the amount:"))
    
                # AccountManagement.deposit(account_num,amount)

        case 4:
                print("                                 To Withdraw Money")
                account_num = input("Enter Your Account Number:")
                amount = int(input("Enter the amount:"))
                pin = int(input("Enter your PIN:"))
                First_name = AccountManagement.withdrawl(account_num,amount,pin)
        case 13:
                break
    ##################################################################################################################################################


