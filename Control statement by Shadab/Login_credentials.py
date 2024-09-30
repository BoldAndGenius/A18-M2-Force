# Done by Md Shadab Arshad


actual_username = "Ek Tha Tiger"              # if you're specifying wiht username, then must use else block after validation of username.
actual_password = "Zoya143"

while True:
    user_name = input("Enter the username: ")
    
    if user_name == actual_username:
        print("Username has been matched successfully!")
    else:                                     # use else block otherwise it'll continue keep asking the usename.
        print("Username does not match")
        break
    
    for attempt in range(4): #taking range value 4, bc'z of better understandable to user's countdown
        password = input(" \n Enter the password: ")
        
        if password != actual_password:
            attempts_left = 3 - attempt      # Calculate remaining attempts
            
            if attempts_left > 0 :           # if the countdown value is>0 then it'll print the remaining attempts left for user.
                print(f" You're Left out with remaining {attempts_left} ATTEMPTS..!\n please make sure to enter correct password.\n Otherwise You'll be BLOCKED")
            else:
                print(f"{actual_username} has been BLOCKED for exceeding maximum lIMITS..!")
                break
        else:                              # executing first password's block for credential validation.
            print(f" Welcome dear {actual_username} \n You've been successfully logged in!\n")
            break
    else:                                  # This else is associated with the for loop, if user exceeds limit's credential.
        
        print(f"{actual_username} has been BLOCKED for exceeding maximum limits!")
        
    break                                  # make sure to put break for Exiting the while loop, otherwise it'll keep asking username continously.



# Another format, just taking the credentials from user.
#The above program has pre-valid credentials.
#This format is referenced from --Asha S

print(' \n Another format, asking the credentials from user.')
actual_username=input('\n Please Enter your username :') 
actual_password=input('Please Enter your password \n :')
print(f"Thanks for submitting your credentials\nYour username has been fitted as {actual_username} and password is {actual_password} ")

while True:
    user_name = input("\n Please re-enter your valid username: ")
    
    if user_name == actual_username:
        print("Username has been matched successfully!")
    else:                                              # use else block otherwise it'll continue keep asking the usename.
        print("Username does not match")
        break
    
    for attempt in range(4):                           # taking range value 4, bc'z of better understandable to user's countdown
        password = input(" \n Please Re-enter your valid password: ")
        
        if password != actual_password:
            attempts_left = 3 - attempt                # Calculate remaining attempts
            
            if attempts_left > 0 :                     # if the countdown value is>0 then it'll print the remaining attempts left for user.
                print(f" OOPS..! You entered wrong password\n \n You're Left out with remaining {attempts_left} ATTEMPTS..!\n please make sure to enter correct password.\n Otherwise You'll be BLOCKED \n")
            else:
                print(f"{actual_username} has been BLOCKED for exceeding maximum lIMITS..!")
                break
        else:                                          #executing first password's block for credential validation.
            print(f" Welcome dear {actual_username} \n You've been successfully logged in!")
            break
    else:                                              # This else is associated with the for loop, if user exceeds limit's credential.
               
        print(f"{actual_username} has been BLOCKED for exceeding maximum limits!")
    break #for coming out of the while loop.
