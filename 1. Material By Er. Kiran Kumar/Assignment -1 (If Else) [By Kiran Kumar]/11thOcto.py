# 85. Write a program.To check the type of a given character.

character = input("Enter any character : ")
if 'a'<=character<='z' or 'A'<= character<= "Z":
    print("Alphabets")
elif '0'<character<='9':
    print("Digits.")
else:
    print("Special Characters")