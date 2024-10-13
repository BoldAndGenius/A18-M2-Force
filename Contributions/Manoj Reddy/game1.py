game= {"scissor","rock","paper"}
user = 0
computer = 0
while True:
    user_option = input("Enter Your Option scissor/rock/paper/exit : ")
    computer_option = game.pop()
    
    if user_option == "exit" or computer == 10 or user == 10:
        break
    
    elif (user_option == "rock" and computer_option == "scissor") or (user_option == "paper" and computer_option == "rock") or (user_option == "scissor" and computer_option == "paper"):
        print("User Win")
        user+=1
    elif (computer_option == "rock" and user_option == "scissor") or (computer_option == "paper" and user_option == "rock") or (computer_option == "scissor" and user_option == "paper"):
        print("Computer win")
        computer+=1
    elif user_option == computer_option:
        print("Tie")
    else:
        print("Invalid option")
        continue
    
    game.add(computer_option)          
print(f"User Score is {user}")
print(f"Computer Score is {computer}")
    
    
