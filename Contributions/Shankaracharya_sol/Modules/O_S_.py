import os

# for num in range(50):
#     os.mkdir(f"{num}")     # it will make 50 different different directories

# os.makedirs("hello/ji")       #it will create directory inside that directory there will be one more directory

# for num in range(50):
#     os.rmdir(f"{num}")       # it will delete all 50  directories

# os.rmdir("chammak/ji")       #it will delete the last specified directory(leaf folder) i.e "ji"

# os.removedirs("chammak")      #it will delete the whole directory (the main as well as the nested one's) only  if the folder is empty.

# os.rename("hello","chammak")   #it will rename the existing directory

# print(os.listdir("assignment-1"))   #it will give you the list of sub-directories of the parent directory

# print(os.getcwd())      #it will give you the current working directory path

items = os.listdir("assignment-1")
for item in items:
    print(item,end="->")
    print(os.stat(f"assignment-1/{item}")).st_size
    # print(os.stat(f"assignment-1/{item}"))
    print()
