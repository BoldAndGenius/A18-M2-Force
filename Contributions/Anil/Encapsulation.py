'''
Encapsulation:
The practice of bundling data (attributes) and methods (functions) that operate on the data 
into a single unit, or class, while restricting direct access to some of the class's components to protect data from unintended interference.
'''

#Encapsulating variables into a class

class SpecialShawarma:
    wrapping='rumal roti'                        #public
    _chicken_quality='okayish'                   #protected
    veggis=['cabbage','capsicum']                #public
    __masala=['X','Y','Z']                       #private
    
    def get_masala(self):
        return "Alert!!! Can't access private member"
    def set_masala(self,new_masala):
        print("Alert!!! Can't modify private member")

plate1=SpecialShawarma()   
print(plate1.wrapping)         #rumal roti
print(plate1._chicken_quality)  #okayish
print(plate1.veggis)   #['cabbage','capsicum']  
# print(plate1.__masala)   AttributeError: 'SpecialShawarma' object has no attribute '__masala' Did you mean: 'get_masala'?
print(plate1.get_masala())   #Alert!!! Can't access private member
plate1.set_masala(['P','Q','R'])  #Alert!!! Can't modify private member

print(SpecialShawarma.__dict__)   #{'__module__': '__main__', 'wrapping': 'rumal roti', '_chicken_quality': 'okayish', 'veggis': ['cabbage', 'capsicum'], '_SpecialShawarma__masala': ['X', 'Y', 'Z'], 'get_masala': <function SpecialShawarma.get_masala at 0x0000021E5F938B80>, 'set_masala': <function SpecialShawarma.set_masala at 0x0000021E5F938E00>, '__dict__': <attribute '__dict__' of 'SpecialShawarma' objects>, '__weakref__': <attribute '__weakref__' of 'SpecialShawarma' objects>, '__doc__': None}