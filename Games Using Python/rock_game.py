# rock, paper, scissor

computer = 0
player = 0    
options = {"rock", "paper", "scissor"}

while True:
    user_option = input("Enter rock/ paper/ scissor/ quit: ")
    if user_option == "quit" or computer == 10 or player == 10:
        break
    
    computer_option = options.pop()

    if user_option == 'rock' and computer_option == "paper":
        print("computer won")
        computer += 1
    elif user_option == "rock" and computer_option == "scissor":
        print("player won")
        player += 1
    elif user_option == "rock" and computer_option == "rock":
        print("game is draw")
    elif user_option == "paper" and computer_option == "paper":
        print("game is draw")
    elif user_option == "paper" and computer_option == "rock":
        print("player won")
        player += 1
    elif user_option == "paper" and computer_option == "scissor":
        print("computer won")
        computer += 1
    elif user_option == "scissor" and computer_option == "rock":
        print("computer won")
        computer += 1
    elif user_option == "scissor" and computer_option == "paper":
        print("player won")
        player += 1
    elif user_option == "scissor" and computer_option == "scissor":
        print("game is draw")
    
    options.add(computer_option)

print(f"player point: {player}")
print(f"computer points: {computer}")