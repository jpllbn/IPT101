# languages = ["Python", "Swift", "C++"]
#
# print(languages[-3], languages[-1])
#
# print(languages[2])

#
#
# # Slicing
# my_list = ["p", "r", "o", "g", "r", "a", "m", "i", "z"]
#
# print(my_list[2:5]) # items form index 2 to 4
#
# print(my_list[5:]) # items form index 5 to end
#
# print(my_list[:]) # items beginning to end
#
# # Negative Slicing
# print(my_list[-7:-4])
#
# numbers = [21, 34, 54, 12]
#
# print("Before Append: ", numbers)
#
# # append() function
# numbers.append(32)
#
# for i in range(1, 101):
#     numbers.append(i)
#
# print("After Append", numbers)
#
# prime_numbers = [2, 3, 5]
# print("List 1:", prime_numbers)
#
# even_numbers = [4, 6, 8]
# print("List 2:", even_numbers)
#
# prime_numbers.extend(even_numbers)
#
# print("List after append:", prime_numbers)
#
#
# # Changing List
# languages = ["Python", "Swift", "C++"]
# print(languages)
#
# languages[2] = "C"
#
# print(languages)

# del Statement
# languages = ["Python", "Swift", "C++", "C", "Java",  "Rust", "R"]
# del languages[0:3 ]
# print(languages)

# remove() function
languages = ["Python", "Swift", "C++", "C", "Java",  "Rust", "R"]
languages.remove("Python")
print(languages)


