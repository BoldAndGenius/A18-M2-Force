# rock ,paper and scissor game
game={"rock","paper","scissor"}
computer=0
player=0
while True:
  
    user_option=input("enter rook/paper/scissor/exit")
    if user_option=="exit" or computer==10 or player==10:
        break

    if user_option not in game:
        print("invalid input")
        continue   

    computer_option=game.pop()

    if user_option==computer_option:    
        print("draw")
    elif user_option=="rock" and computer_option=="scissor":
        print("player win")
        player+=1
    elif user_option=="rock" and computer_option=="paper":
        print("computer win")
        computer+=1
    elif user_option=="paper" and computer_option=="rock":
        print("player win")
        player+=1
    elif user_option=="paper" and computer_option=="scissor":
        print("computer win")
        computer+=1
    elif user_option=="scissor" and computer_option=="paper":
        print("player win")
        player+=1
    elif user_option=="scissor" and computer_option=="rock":
        print("computer win")
        computer+=1
    game.add(computer_option)
print(f"computer score is {computer}")
print(f"player score is {player}")
    
    
