option = input("Choose any option from below\nA:Pizza\nB:Burger\nC:Vadapav\nD:Golgappa\nEnter your option here:")

match option:
    case 'A':
        print("you have ordered pizza")
    case 'B':
        print("you have ordered burger")
    case 'C':
        print("you have ordered vadapav")
    case 'D':
        print("you have ordered golgappa")
    case _ :
        print("Invalid option")