# Q91.Write a program to check weather the given collection is having nested collection or not

collection = eval(input("Enter the collection (list/tuple/set/dict): "))

collection_index = 0
nested = False
while collection_index < len(collection):
    if type(collection[collection_index]) in [list, tuple, set, dict]:
        nested = True
        break
    collection_index += 1

if nested:
    print("The collection has a nested collection.")
else:
    print("The collection does not have a nested collection.")


# Q92. Write a program to return the positions of vowels present in the given string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
positions = []

string_index = 0
while string_index < len(string):
    if string[string_index] in vowels:
        positions.append(string_index + 1)
    string_index += 1

print(f"positions of vowels : {positions}")


# Q93:Write a program to find length of collection without using len function

collection = eval(input("Enter a collection (list/tuple): "))
count = 0
i = 0

while True:
    try:
        collection[i]
        count += 1
        i += 1
    except IndexError:
        break

print(f"Length of the collection is: {count}")


# Q94.Write a program to whether the entered username and password is correct or not if not correct print enter again

credentials = {
    "Shraddha": "sh@123",
    "Rohit": "ro@123",
    "admin": "adminpass",
    "guest": "guest@123"
}

while True:
    action = input("Enter 'login' to login or 'sign_up' to sign up: ").lower()
    
    if action == 'login':
        username = input("Enter username: ")
        
        if username in credentials:
            password = input("Enter password: ")
            if credentials[username] == password:
                print("Login successful!")
                break
            else:
                print("Incorrect password, try again.")
        else:
            print("Incorrect username, try again.")
    
    elif action == 'sign_up':
        new_username = input("Enter new username: ")
        
        if new_username in credentials:
            print("Username already exists, try a different one.")
        else:
            new_password = input("Enter new password: ")
            credentials[new_username] = new_password
            print("Sign-up successful! You can now log in.")
    
    else:
        print("Invalid input, please enter 'login' or 'sign_up'.")


# Q95.Write a program to extract all integer data items from tuple

data_tuple = eval(input("Enter a tuple: "))
integers = []

data_tuple_index = 0
while data_tuple_index < len(data_tuple):
    if type(data_tuple[data_tuple_index]) == int:
        integers.append(data_tuple[data_tuple_index])
    data_tuple_index += 1

print("Extracted integers:", integers)



