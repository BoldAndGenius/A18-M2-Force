# Extract All Numeric Values From a Collection

# Numeric Values means - int, float, complex
collection = [1,2,3.4,True,3+5j,{1,2,4}]
numeric_collection = []
for item in collection:
    if type(item) in [int,float,complex]:
        numeric_collection.append(item)
print(f"The Numeric Collection is : {numeric_collection}")




# Extract lowercase characters from a string

string = input("Enter any string : ") #"kIran"
lowercase = ""
for characters in string:
    if characters.islower():
        lowercase = lowercase + characters   # ''+'k' = 'k'
print(f"The lowercase characters are : {lowercase}")
