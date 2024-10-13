# 61. Write a program to extract all the string values present in the list collection only if the last character is upper case. Concatenate the extracted output using ‘*’.

user_input = input("Enter elements separated by commas: ")
elements = [item.strip() for item in user_input.split(',')]
result = ''
index = 0
# print('debug')
while index < len(elements):
    if type(elements[index]) is str:
        last_char = elements[index][len(elements[index]) - 1]
        if 65 <= ord(last_char) <= 90:
            if result:
                result += '*'
            result += elements[index]
    index += 1
print(result)