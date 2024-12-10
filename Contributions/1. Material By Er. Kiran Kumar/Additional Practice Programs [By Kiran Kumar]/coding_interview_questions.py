
# Coding Interview Question - 1
# From a list of numbers, mover 0 to the end of the list. 

my_list = [1,0,2,0,4,6]
new_list = []
for item in my_list:
  if item == 0:
    my_list.remove(item)  # it will remove that element from the list. 
    new_list.append(item)
print(my_list + new_list)
    
    