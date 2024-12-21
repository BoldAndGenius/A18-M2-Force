############################################################
# 1.int to other
num=100
print(float(num))
print(bool(num))
print(complex(num))
print(str(num))

# print(list(num))
# print(set(num))
# print(tuple(num)) throws type error
# print(dict(num))

############################################################
############################################################
# 2.float to other
num=25.45
print(int(num))
print(bool(num))
print(complex(num))
print(str(num))

# print(list(num))
# print(set(num))
# print(tuple(num)) #throws type error
# print(dict(num))

############################################################
############################################################

# 3.complex to other
num=12+0j
print(bool(num))
print(str(num))

# print(int(num))
# print(float(num))
# print(list(num))
# print(set(num))
# print(tuple(num)) throws type error
# print(dict(num))

############################################################
############################################################

# 4.bool to other
num=True
print(int(num))
print(float(num))
print(complex(num))
print(str(num))

# print(list(num))
# print(set(num))
# print(tuple(num)) #throws type error
# print(dict(num))

############################################################
############################################################

# 5. string to other datatype
string='100'
print(int(string))
print(float(string))
print(complex(string))
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws value error
#print(dict(string))

string='34.67'

print(float(string))
print(complex(string))
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

# the following throws value error
# print(int(string))
# print(dict(string))

string='strings'

print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws error
#print(int(string))
#print(float(string))
#print(complex(string))
#print(dict(string))

string='23.90+9j'
print(complex(string))
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws error
#print(int(string))
#print(float(string))
#print(dict(string))

string="True"
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws error
#print(int(string))
#print(float(string))
#print(dict(string))
#print(complex(string))

string='[12,90,99,"asha"]'
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws error
#print(int(string))
#print(float(string))
#print(dict(string))
#print(complex(string))

string="('asha',123,[10,'''abc'''])"
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws error
# print(int(string))
# print(float(string))
# #print(dict(string))
# print(complex(string))

string='{45,90,"word","peter",{88,45}}'
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))
#the following throws error
# print(int(string))
# print(float(string))
# #print(dict(string))
# print(complex(string))

string='{"a":10,"b":90,"c":"letter"}'
print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))
#the following throws error
# print(int(string))
# print(float(string))
#print(dict(string))
# print(complex(string))

string='23.90 + 9j'

print(bool(string))
print(list(string))
print(tuple(string))
print(set(string))

#the following throws error
#print(complex(string))
#print(int(string))
#print(float(string))
#print(dict(string))

############################################################
############################################################

# 6. list to other datatype
list1=[10,23.90,2+9j,'this is python candidate',True,[1,2,'a'],{90,'asha',1},(10,45),{1:'as',2:'has'}]
print(bool(list1))
print(list(list1))
print(tuple(list1))
print(str(list1))
list2=[10,'asha',89.90]
print(set(list2))

#the following throws error
# print(complex(list1))
# print(int(list1))
# print(float(list1))
# print(dict(list1))

items=[{10,'number'},'as',['Type','bool'],('immutable_datatype','tuple'),{"key":'value','name':'asha'}]
print(dict(items))

############################################################
############################################################

# 7. tuple to other datatype

tup=(10,9.99,'asha',15,'78')
print(list(tup))
print(set(tup))
print(bool(tup))
print(str(tup))

#the following throws error
# print(complex(tup))
# print(int(tup))
# print(float(tup))
# print(dict(tup))

############################################################
############################################################

# 8. set to other datatype

set1={10,9.99,'asha',15,'78'}
print(list(set1))
print(tuple(set1))
print(bool(set1))
print(str(set1))

#the following throws error
# print(complex(tup))
# print(int(tup))
# print(float(tup))
# print(dict(tup))

############################################################
############################################################

# 9. dictionary to other datatype

dict1={"name":'asha','age':21,'education':'btech'}
print(list(dict1))
print(tuple(dict1))
print(bool(dict1))
print(set(dict1))
print(str(dict1))

#the following throws error
# print(complex(tup))
# print(int(tup))
# print(float(tup))
# print(dict(tup))

#list to dictionary based on condition
items=[{10,'number'},'as',['Type','bool'],('immutable_datatype','tuple'),{"key":'value','name':'asha'}]
print(dict(items))

#tuple to dictionary based on condition
item1=(['value',20],('item','tuple'),{'set','mutable'},"sa",{"a":10,'b':90})
print(dict(item1))  # type: ignore

#set to dictionary based on condition
item={('immutable','tuple'),'py',('key','value')}
print(dict(item))






