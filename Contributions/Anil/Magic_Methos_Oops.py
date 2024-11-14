class Human:
    eyes=2
    ears=2
    hands=2
    ears=2
    bones=206
    def __init__(self):
        print('Human Object Created!!')
    def happiness(self,num):
        print(f'Feeling happy {num}%')
    def anger(self,num):
        print('Feeling anger {num}%')


print(Human.__dict__)
MrCool=Human()
print(MrCool.__dict__)
print(MrCool.eyes)
MrCool.anger(100)
print(Human.bones)
Human.happiness(MrCool,40)
MrCool.emotions='Aggressive'
MrCool.fullname='Coolest person'
print(MrCool.__dict__)
Human.hands=4
print(Human.__dict__)





class Greeter:
    def __init__(self,name):
        self.name=name
    def __call__(self,greeting='Hello'):
        print(f'{greeting} {self.name}!!')

person1=Greeter('Peter Parker')
person1()
person1('Hola')