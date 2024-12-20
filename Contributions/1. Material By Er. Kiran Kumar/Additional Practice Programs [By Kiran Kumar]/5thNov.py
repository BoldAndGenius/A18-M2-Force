

# Human Class


class Human:
    eyes = 2
    nose = 1
    def mood(self):
        print(f"Mood is Depressed")
    def happy(self,percent):
        print(f"{percent}% Happy")
    def hobbies(self):
        pass
    def random(self,a,b):
        self.a = a
        self.b = b
    def general_info(self,height,weight,iq):
        self.height = height 
        self.weight = weight 
        self.iq = iq 
        print(height,weight,iq)
        

kiran = Human()
print(kiran.eyes)
print(kiran.nose)
kiran.mood()  # Internally it stores like this -- Human.mood(kiran)
kiran.happy(100)

kunal = Human()
kunal.hobbies()  
# kunal.c # get error 


kajal = Human()
kajal.general_info(5.1,55, 10)
  