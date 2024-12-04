# Property Decoration

# class MechCoder:
#     __masala = ['x','y','z']
#     def get_masala(self):
#         return MechCoder.__masala
#     def set_masala(self,new_masala):
#         self.__masala = new_masala
# manoj = MechCoder()
# print(manoj.get_masala())
# print(manoj.set_masala(['m','n','o']))
# print(MechCoder.__dict__)
# print(manoj.__dict__)

class MechCoder:
    __masala = ['x','y','z']
    @property
    def masala(self):
        return MechCoder.__masala
    @masala.setter
    def masala(self,new_masala):
        self.__masala = new_masala
man = MechCoder()
print(man.masala)
man.masala(['m','n','o'])
