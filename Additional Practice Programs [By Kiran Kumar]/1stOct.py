# Extract All Numeric Values From a Collection

# Numeric Values means - int, float, complex
collection = [1,2,3.4,True,3+5j,{1,2,4}]
numeric_collection = []
for item in collection:
    if type(item) in [int,float,complex]:
        numeric_collection.append(item)
print(f"The Numeric Collection is : {numeric_collection}")