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





# Display a Dictionary whose Keys are Words of a Sentence and Values are Lenght of each word using for loop.

sentence = input("Enter any sentence : ")  #kiran is a good boy
words_list = sentence.split()  # ['kiran', 'is', 'a', 'good', 'boy']   -- list of words
# print(word)
# word = ['kiran','is', 'a', 'good', 'boy']
dictionary = {}
for word in words_list:   # apply for loop on the list of word that we split it
    # print(word)
    if word not in dictionary:
        dictionary[word] = len(word)    #if not present this key value pair, create this key value pair

print(dictionary)






sentence = input("Enter any sentence :")
words_list = sentence.split()
# print(words_list)
dictionary = {}
for word in words_list:
    if word not in dictionary:
        dictionary[word] = len(word)
print(dictionary)






# Mimic the Length Function 
# Lenght Function -- It finds the lenght of a collection

string = input("Enter any string :")
length = 0
for characters in string:
    length = length + 1
print(f"The lenght of {string} is {length} ")





# Display the Largest Number from the Given Collection 

collection = [1,2,3,45,89]
max = 0   #let's assume the maximum is 0 -- assume any minimum value
for item in collection:
    if item > max:
        max = item
print(f"The Maximum Number is {max}")



# Display the Smallest Number from the Given Collection 

collection = [1,2,4,59,90,100]
min = 1000  # assume any maximum value
for item in collection:
    if item < min:
        min = item
print(f"The Smallest Number is {min}")



# Display the Sum of All Items from the Given Collection 
collection = [1,2,3,4,5]
sum = 0
for item in collection:
    sum = sum + item
print(f"The Sum of Collection is {sum}")


# Display the Average of All Items from the Given Collection
collection = [1,2,3,4,5]
sum = 0
length = len(collection)
for item in collection:
    sum = sum + item 
# print(sum, length)
print("The Average of Collection is ",sum/length)
    


