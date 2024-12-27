import os
bidder_details={}
def auction():
    name=input('Enter your name : ')
    bid=int(input('Enter your bid : '))
    bidder_details[name]=bid
    choice=input("Are there any other bidders? Type 'yes' or 'no'\n ")
    if choice=='yes':
            os.system('cls')
    else:
        print(f'Here the bidders details : {bidder_details}')
        res=max(bidder_details.values())
        for name in bidder_details:
            if bidder_details[name]==res:
                '''displaying winner with highest bid'''
                print(f"The winner is {name} with a bid price of {bidder_details[name]}") 
    return choice

def silent_auction():
    print('\n************ Welcome to The Silent Auction Program *************\n')

    while True:
        user_choice=auction()
        if user_choice=='yes':
            os.system('cls')  # to clear the screen
            auction()
        else:
             break
        
            
            
silent_auction()
                

           

