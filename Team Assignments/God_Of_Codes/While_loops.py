# 61.Write a program to extract all the string values present in the list collection only if the last character is upper case. Concatenate the extracted output using ‘*’.

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


# 62.write a program to extract all the list data items present in list collection only if it is having middle value , that value is integer and having even number at start

list_collection = [[1, 2, 3, 4, 5],[10, 12, 14],[6, 7, 8, 9, 10],[1, 2, 'a', 5, 6],[2, 4, 6],[8, 10, 12, 14, 16]]
result = []
index = 0

while index < len(list_collection):
    current_list = list_collection[index]

    if len(current_list) % 2 == 1:
        middle_value = current_list[len(current_list) // 2]

        if type(middle_value) == int:
            first_digit = abs(middle_value)

            while first_digit >= 10:
                first_digit //= 10
            if first_digit % 2 == 0:
                result.append(current_list)

    index += 1
print(result)