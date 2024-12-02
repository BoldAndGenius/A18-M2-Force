import time
from datetime import datetime

'''This is a class of Quotify which is a social media application in which users can post their thoughts'''
class Quotify:
    accounts = {'raishan':'rai'}
    
    '''This is constructor'''
    def __init__(self):
        self.post = {}
        self.unique_id_post_list = []
        print()
        print("Welcome to Quotify")

        while True:
            print()
            choice = input("Would you like to:\n1.Sign up \n2.Sign in \n3.Exit: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
                while True:
                    
                    choice = input("1.New Post\n2.Your Posts\n3.Logout ")
                    if choice == "1":
                        #add a new post
                        self.add_a_post()

                    elif choice == "2":
                        # get your own posts
                        self.get_own_post()
                        print()
                    else:
                        self.logout()
                        break
            elif choice == "3":
                break
            else:
                print("invalid choice")
        
    '''This Method is for Register a New User'''
    def register(self):
        username = input("Enter Username:")
       
        # Validation where the account is present or not
        if username not in Quotify.accounts:
            for _ in range(5):
                actual_password = input("Enter Password:") 

                # the length should be > 8
                if len(actual_password) > 8:
                    # isalnum will only give false when there is atleast one special character
                    if actual_password.isalnum() == False:
                        confirm_password = input("Confirm Password:")

                        if actual_password == confirm_password:
                            #assigning password as value to that username which is key
                            Quotify.accounts[username] = actual_password 
                            print("Account Created Successfully...")
                            break   
                        else:
                            print("password and confirm password should be same")
                    else:
                        print("Password should be combination of alphabets,numbers and special characters....Please Enter Again")
                else:
                    print("Password length should be greater than 8")
            else:
                print("5 attempts done...Thank you for visit")
        else:
            print("Username Already Exists!")
    
    '''This Method is for Login'''
    def login(self):
        print()
        username = input("Enter Username:")
        self.temp_user = username
        if username in Quotify.accounts:
            for _ in range(3):
                password = (input("Enter Password:"))
            
                # checking whether the password is same as actual password or not
                if password == Quotify.accounts[username]:       
                    print("Login Successfull...")
                    print()
                    break
                else:
                    print("Wrong Password")
            else:
                print("3 Attempts Failed, you are blocked for 24 hours")
                # raise PermissionError("3 Attempts Failed, you are blocked for 24 hours")
        else:
            print("User Not Found!!")
            choice = input("1.Create a New Account\n2.Sign In ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()

    '''This method is for adding a new post'''
    def add_a_post(self):
            print()
            actual_time_now = datetime.now()
            
            # Format it as YYYYMMDDHHMMSSmmm (Date + Time in ms)
            unique_id_post = actual_time_now.strftime("%Y%m%d%H%M%S%f")[:-6]  # Remove last 6 digits to get only YYYYMMDDHHMMSS
        
            quote = input("Write Your Quote Here...\n")
            
            # each post has some unique id which is combination of username and current time

            self.post[self.temp_user + f"{unique_id_post}"] = quote

            # post uploading
            print("Uploading...")
            time.sleep(5)
            print("Posted Succesfully...")

            # append the unique id of post into a list so that it will be helpful when we want to delete a post
            self.unique_id_post_list.append(self.temp_user + unique_id_post)
            print()
                           
    '''This method is for printing all posts of an user'''
    def get_own_post(self):
        print()
        print("----------  POSTS  ----------")
        

        if not self.post:
            print("No Post")
        else:  
            count = 0
            for item in self.post:
                count += 1
                print(f"{count}.{self.post[item]}")

            choice = input("Do you want to delete a post(Y/N)")
            if choice in ('Y','y'):
                self.delete_a_post()

    '''This method is for deleting an existing post'''
    def delete_a_post(self):
        if not self.unique_id_post_list:
            print("Nothing to Delete!! Please add some post...")
        else:
            user_choice = int(input("Choose the post from above to delete: "))

            # list index value start from 0 and posts index starts from 1 so to start our list index from 1 i took it start = 1
            for choice in range(1, len(self.unique_id_post_list)+ 1):

                # if both the choices become same
                if choice == user_choice:

                    # delete the element from the list which will be the key in form of string
                    deleted_key = self.unique_id_post_list.pop(choice-1)

                    # finally delete that particular key from the post{}
                    self.post.pop(deleted_key)

                    print("Deleting...")
                    time.sleep(3)
                    print("Post Deleted Successfully...")

    '''This Method is for logging out from the application'''
    def logout(self):
        self.temp_user = None
        print("Logged Out Successfully")
        print()
        print("---------- THANK YOU!! VISIT AGAIN ----------")
        
shan = Quotify()
