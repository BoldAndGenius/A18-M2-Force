# Q97.Write a program to check weather the first and last value in the collection is float if yes add those 2 values

coll=[0.3,1,True,('a','b'),35,{'name':'nitin'},6.2]
if isinstance(coll[0],float) and isinstance(coll[-1],float):
    sum=coll[0]+coll[-1]
    coll.append(sum)
else:
    print('either 1st or last item in your list is not a float datatype')

print(coll)