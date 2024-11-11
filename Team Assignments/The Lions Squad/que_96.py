# Q96.Write a program to extract all the non default values from the list


list=["",[1,2],{'a','b'},(),{},1,True,0.0,0j]
def_list=["",[],(),set(),{},0,0.0,False,0j]
non_def_val=[]
index=0
while index<len(list):
    item=list[index]
    index+=1
    if item not in def_list:
        non_def_val.append(item)
print(non_def_val)
