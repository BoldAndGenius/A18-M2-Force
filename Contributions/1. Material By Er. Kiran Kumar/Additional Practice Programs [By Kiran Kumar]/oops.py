
class Bottle: 
    # print("Debugging1") # This gonna print no matter we create a class 
    colour = "blue"
    size = 8
    shape = "round"
    material = ['plastic','silicon','artificial agents']
    def manufacturing(self): # as python see def, it will ignore it..and execute the next lines
        print("Manufacturing is going on!")
    # print("Debugging2") # this get prints 

print(id(Bottle))  # 2858944448800   (Address of Class)
mybottle = Bottle()
print(mybottle) # <__main__.Bottle object at 0x000002BC0502C980>    # id of object reference 
                # hexadecimal 

# using dot operator, we can access the data members & member functions 
print(mybottle.colour) # blue
print(mybottle.size)  #  8 
print(mybottle.shape)  # round
print(mybottle.material) # ['plastic', 'silicon', 'artificial agents']
print(mybottle.manufacturing())  # Manufacturing is going on! and None

mybottle.manufacturing  # Manufacturing is going on!   (at the time of function call, only print statement gets printed)

# But when we print it.......it will print ...what is returning it...so therefore None 
print(mybottle.manufacturing())  #None
