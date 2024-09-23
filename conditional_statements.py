######################################################################
######################################################################
'''SIMPLE IF'''








#######################################################################
#######################################################################
'''IF ELSE'''








#######################################################################
#######################################################################
'''ELIF'''







#######################################################################
#######################################################################
'''NESTED IF'''

82). Write a program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3 

tpl = eval(input("Enter a Tuple: "))    

mid_index = len(tpl) // 2
middle_value = tpl[mid_index]

if type(middle_value) == str:
    if len(middle_value) > 3:
        print(middle_value)
    else:
        print("It is a string but the length is not greater than 3")
else:
    if type(middle_value) != str:
        print("the mid vale is not string")
      




#######################################################################
#######################################################################
