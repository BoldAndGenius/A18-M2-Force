user=0
computer=0
options={'rock','paper','scissor'}
while 1==True:
    user_opt=input('choose one:\nrock / paper / scissor / quit \n').lower()
    comp_opt=options.pop()
    options.add(comp_opt)
    if user_opt not in ('rock','paper','scissor','quit'):
        print('choose one option in four')
        if user_opt=='quit'or user==10 or computer==10:
            break
    else:
        if user_opt == comp_opt:
            print('match tie')
        elif (user_opt=='rock' and comp_opt=='scissor') or (user_opt=='paper' and comp_opt=='rock') or (user_opt=='scissor' and comp_opt=='paper'):
            print('user won')
            user+=1
        else:
            print('computer won')
            computer+=1
print(f'user points {user} \n computer points is {computer}')
