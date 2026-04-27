# is_student = False
# has_coupone = True

# if is_student and has_coupone:
#     print ("You will get the Student discount")
# else:
#     print("You will not get the student discount")

# while True:
#     age = input("Enter your age: ").strip()

#     if age.isdigit():
#         age = int(age)
#         break
#     else:
#         print("Please enter a valid number (e.g., 18).")

########################################################################################################
# age = int(age)

# has_id = True
# is_vip = False

# if age >= 18 and has_id and is_vip:
#     print("Allowed as a VIP")

# elif age >=18 and has_id:
#     print("Allowed as a not VIP")

# elif age >=18 and not has_id:
#     print("You need an ID")

# else:
#     print("You are not allowed")

# while True:
#     age = int(input("Enter the age: ").strip())

#     if age.isdigit():
#         #age = int(age)
#         print(f"You are {age} years old")
#         break
#     else:
#         print("Please enter the valid number (e.g., 18)")

#########################################################################################################
# while True:
#     numbers = input("Please enter two numbers: ").strip()

#     split_numbers = numbers.split()

#     if len(split_numbers) == 2 and split_numbers[0].isdigit() and split_numbers[1].isdigit():
#         num1, num2 = map(int, split_numbers)
#         # num1 = int(split_numbers[0])
#         # num2 = int(split_numbers[1])
#         total = num1 + num2
#         print ("Total number is: ", total)
#         break
#     else:
#         print("Please enter the whole number.")

# is_student = True

# if total % 2 == 0 and is_student:
#     print("You will get the 50% discount")
    
# elif total % 2 == 1 and is_student:
#     print("You will get 30% discount")
# else:
#     print("You are out of the discount programm")

# while True:
#     numbers = input("Enter the two numbers: ").strip().split()

#     if len(numbers) != 2:
#         print(f"You enterd {len(numbers)} values. Enter exactly two numbers")
#         continue

#     if not (numbers[0].isdigit() and numbers[1].isdigit()):
#         print("Please enter the whole numbers (e.g. 10 20)")
#         continue
    
#     num1, numb2 = map(int, numbers)
#     total = num1 + numb2
#     print("Total number is: ", total)
#     break


# is_student = True

# if total % 2 == 0 and is_student:
#     print("You will get the 50% discount")
    
# elif total % 2 == 1 and is_student:
#     print("You will get 30% discount")
# else:
#     print("You are out of the discount programm")


# name = ""
# if name:
#     print("Name exists")
# else:
#     print("Empty name")


# a = -10
# if 1<= a >= 10:
#     print("Valid Number")
# else:
#     print("Invalis Number")
    
# name = "Shams"

# print("Valid name" if name else "Invalid" )

# age = int(input("Enter the age: ").strip())



# print(f"your age is {age}, so you are Student" if age <= 25 else f"your age is {age}, So you are Not Student")

# user = None
# if user:
#     print("User is there")
# else:
#     print("There is no user")
# user = None

# if user is not None and user.is_active:
#     print("The user is there")
# else:
#     print("No userS")

# user = {"name": "Shams", "is_active": False}

# active = user.get("is_active")

# if active is None:
#     print("There is nobody")
# elif active:
#     print("Active User")
# else:
#     print("User is there but not active")

# raw = input("Enter key=value pairs: ").split()
# data = {}
# for part in raw:
#     key, value = part.split("=", 1)
#     data[key] = value
# print(data)
# while True:
#     cmd = input(">>> ").strip().lower()
#     if cmd == "exit":
#         break

#     parts = cmd.split()
#     if len(parts) != 3:
#         print("Use: add 5 7")
#         continue

#     op, a_str, b_str = parts
#     if not (a_str.lstrip("-").isdigit() and b_str.lstrip("-").isdigit()):
#         print("Numbers only")
#         continue

#     a, b = int(a_str), int(b_str)

#     if op == "add":
#         print(a + b)
#     elif op == "mul":
#         print(a * b)
#     else:
#         print("Unknown operation")

# day = input("Enter the day here: ")


# match day:
#     case "Sat" | "Sun":
#         print("It's weekend")
#     case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
#         print("Weekdays")
    
#     case _:
#         print("Something Error")

# new_tuple = (10, 20)

# match new_tuple:

#     case (0, 0):
#         print("Origin")
    
#     case (0, y):
#         print(f"The value of x is x = {x}")
    
#     case (x, 0):
#         print(f"The value of y is y = {y}")
    
#     case (x, y):
#         print(f"The value of y is y = {y}")


# value_list = [10, 20]

# match value_list:
#     case [a, b]:
#         print("The total value is: ", a+b)

#     case _:
#         print("Something Error")

# item_list = [10.5, 2.4, 3.6, 7.0, 8, 15]

# match item_list:
#     case [first, second, *restofnumbers]:
#         print(first, second, restofnumbers)

# event = {"type": "login", "user": "bulbul"}

###########################################################

## In the dictionary it is important to match the Key.

# new_dict = {"Gender": "Male", "Name": "Shams"}

# match new_dict:
#     case {"Gender": g, "Name": n}:
#         print(f"He is {g}, and his name is {n}")

#     case{"Sex": g, "Name": n}:
#         print(f"He is {g}, and his name is {n}")

#########################################################################
# x = 12

# match x:
#     case n if n <= 5:
#         print ("The value is less than 5")
#     case n if 0 <= n <= 10:   
#         print("The number is between 0 t0 10")
#     case n:
#         print("The number is above 10")
# info_dict= {"name": "Shams", 
#             "gender": "Male", 
#             "login": "active", 
#             "time": "2025-12-25T10:00:00Z"}



# def data(e: dict) -> str:
#     match e:
#         case {"name": n, "gender": g, "login": l, "time": t}:
#             return f"He is {n}, he is {l} from {t}"
        
#         case {"name": n, "login": l, "time": t}:
#             return f"He is {n}, he is {l} from {t}"


# print(data(info_dict))

###############################################################
##################### For Loop ################################


# for x in range(10, 0, -1):
#     print(x)




# values = ["a", "b", "c"]

# for i, x in enumerate(values, start = 1):
#     print(i, x)


# items = ("x", "y", "z")

# print(list(enumerate(items)))
# print(list(enumerate(items, start=1)))



# name = "Data Engineering"
# count = 0
# for x in name:
#     if x != " ":
#         count += 1
    
# print(count)

# pairs = [("Shams", 26), ("Raaju", 25), ("Putul", 22)]

# print(f"{'Name': <10} {'Age': >3}")

# print("-"*14)

# for name, age in pairs:
#     print(f"{name: <10} {age: >3}")


# infor_list =  [("Shams", 28), ("Ahmed", 26), ("Raaju", 25)]

# print (f"{'Name': <7} {'Age':>3}")

# print ("-"*13)

# for name, age in infor_list:
#     print(f"{name:<10} {age:>3}")


# new_list =["Shams", "Raaju", "Ahmed"]
# for number, name in enumerate (new_list, start = 1):
#     print(number, name)


### Adding 2 List using zip and for loop
# names = ["Shams", "Raaju", "Ahmed"]
# ages = [25, 26, 27]

# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")

# matrix = [[5, 7], [8, 9]]

# for row_count, real_row in enumerate(matrix):
#     for column_count, value_show in enumerate(real_row):
#         print(f"row = {row_count}, column = {column_count}, Value = {value_show}")


# new_list = [2, 3, 4, 5, 6]

# square = [n*n for n in new_list if n%2 ==1]
# print(square)

# names = "Shams"
# for letter in names:
#     if letter == "a":
#         pass
#         print("This letter is blocked")
#

# list_dict = [
#     {"person": "Male", "number": 1},
#     {"person": "Female", "number": 2},
#     {"person": "Male", "number": 3}
#     ]


# count = {}

# for x in list_dict:
#     t = x.get("person", "Unknown")
#     count [t] = count.get(t, 0) + 1

# print(count)
# info = dict (Name = "Shams", Profession = "Student", Age = 25)
# name = info.get("Name")

# print("Name is: ", name)


# information = {"Name": "Shams", "Profession": "Student", "Age":30}

# names = information.get("Name")
# print("Names is: ", names)

# info = {"Name": "Shams",  "Profession":  "Student", "Age": 25}

# all_keys = info.keys()
# print(all_keys)

# all_values = info.values()
# print(all_values)

# getting_info1 = info.get("Name")
# print("Your name is", getting_info1)

# getting_info2 = info["Profession"]
# print("and you are a", getting_info2)


# adding_info = info.get("Graduation", "Computer Engineer")
# print("You are a", adding_info)


# info.update ({"Name": "Shamsul Haque", "Age": 28})

# print(info)

# if info["Age"] == 28:
#     info["Age"] = 26
# print(info)

# for key in info:
#     print(key, ":", info[key])

##############################################################################

# product_name = {"Fruits": ["Malta, Apple, Blueberry"], "Flowers": ["Hibiscus, Rose, Lily"]}
# print(product_name)

# all_keys = product_name.keys()
# print(all_keys)

# all_values = product_name.values()

# print(all_values)

# access_values = product_name.get("Fruits")
# print(access_values)

# print("Fruits" in product_name)
# print("Name" in product_name, "Not Found")

# print(product_name.get("Fruits"))

# # print(product_name["Name", "Not Found"])

# print(product_name.get("Name", "Not Found"))

# product_name.update({"Veg": ["Potatos", "Garlic", "Ginger"]})

# print(product_name)

############################################################################

# a = {"Name": "Shams", "Age": 26}

# b = a.copy()
# b["Age"] = 30

# print(a)
# print(b)

#############################################################################

# company = {
#     "Name" : "Siemens Energy",
#     "Department": {
#         "Software": ["Shams", "Maria"],
#         "Data Science" : ["Raaju", "Tuhin"]
#     }
# }

# print(company["Department"]["Data Science"][1])

#############################################################################

# square = {x : x * x for x in range (1,6)}
# print(square)

# words = ["Apple", "Banana", "Cherry"]
# word_length = {word : len(word) for word in words}

# print(word_length)

# square_even = {x : x * x for x in range(1, 11) if x % 2 == 0}

# print(square_even)

#############################################################################

#When the keys overlap, then the second dictionary will be counted

# a = {"x" : 10, "y" : 15, "z": 20}

# b = {"x" : 20, "y" : 25, "z" : 30, "a" : 40, "b": 50}

# c = a | b

# print(c)

#################################################################################

# # student= [
# #     ("Software", "Shams"),
# #     ("AI", "Raaju"),
# #     ("Software", "Tuhin"),
# #     ("AI", "A U M"),
# #     ("CSE", ' ')
# # ]

# # group = {}

# # for major, name in student:
# #     group.setdefault(major, []).append(name)

# # print(group)

# ################################################################################

# import copy
# a = {
#     "Student" : {
#         "Name": "Shams",
#         "Department": "Data",
#         "Age": 25
#     },

#     "Student_2" : {
#         "Name": "Raaju",
#         "Department": "CSE",
#         "Age": 26
#     }

# }

# b = copy.deepcopy(a)
# b["Student"]["Age"] = 30
# b["Student_2"]["Age"] = 35

# print(a)
# print(b)

##################################################################################

# student = {
#     "First_Person" : {"Name" : "Shams", "Marks" : 81},
#     "Second_Person" : {"Name" : "Raaju", "Marks" : 79},
#     "Third_Person" : {"Name" : "Tuhin", "Marks" : 85}
# }
# passed_students ={
#     key: value["Name"]
#     for key, value in student.items()
#     if value["Marks"] >= 80
# }

# print(passed_students)

##################################################################################

# number = [10, 20, 30, 40]

# # number.append(50)

# number.insert(1, 15)
# number.extend([50, 60])

# print(number)

# for x in number:
#     print(x)

# for  x in range(len(number)):
#     print(x, number[x]) 


# for index, value in enumerate(number):
#     print(index, value)

# a = [1, 2]
# b = [3, 4]

# print (a + b)

# numbers = [1, 2]
# print([2] *5)


# number = [10, 5, 15, 8]

# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)   # [0, 2, 4, 6, 8]
# new_number = sorted(number)
# print(new_number)
# print(number)


# num = [20, 15, "Shams", 30]

# for x in range(len(num)):
#     print(x, num[x])

# for index, value in enumerate(num):
#     print(index, value)


# number = [20, 28, 36, 15, 30]
# #number.sort(reverse=True)
# number.sort()
# print(number)
##########################################################################
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print (matrix[1])
# print(matrix[2][2])

# for row in matrix:
#     for item in row:
#         print(item, end= " ")

# #matrix = [[0] * 3] * 3
# print(matrix)

# matrix = [[0] * 3] * 3
# print(matrix)
# matrix = [[0] * 3 for _ in range(3)]
# matrix[0][0] = 99
# print(matrix)

# for row in matrix:
#     for item in row:
#         print(item, end = " ")


# for rows in matrix:
#     for elements in rows:
#         print(elements, end = " ")
#######################################################################

# from array import array

# unsignedint_number = array('I', [10, 20, 8, 17, 32, 29]) #Unsigned Integer contains only the positive values

# float_number = array('f', [10.3, 20.5, 8.2, 17.8, 32.6, 29.9])

# # print(unsignedint_number)
# # print(float_number)

# # for x in range(len(float_number)):

# #     print(x, float_number[x])

# for i in range(len(float_number)):
#     print(f"Index {i} = {float_number[i]}")

# float_number.append(31.6)
# print(float_number)

# float_number.extend([21.5, 19.8])
# print(float_number)
##############################################################################

# from array import array

# marks = array("i", [59, 78, 69, 87, 75])

# print("Total Marks: ")

# for x in range(len(marks)):
#     print(f"Index {x} = {marks [x]}")

# print("Total Student: ", len(marks))
# print("First Student Marks: ", marks[0])

# marks.append(72)

# print("After adding the new studnet", marks)
##############################################################################


# my_str = " Learning String "

# print(my_str.strip())

# name = "Shams"
# department = "Data Science"

# new_string = f"My name is {name} and I'm studying master in {department}"


# print(new_string)


# text = "I am learning Python from the scract and wnat to be an expert"

# find_text = text.find("Python")

# print(f"I found the 'Python' at index: {find_text}")

# text = "I am learning Python from the scratch and want to be an expert"
# find_text = ["Python", "scratch"]

# start = 0
# while start < len(text):
#     # Find the next occurrence
#     index = text.find(find_text, start)
#     if index == -1:
#         break  # No more occurrences found
#     print(f"I found '{find_text}' at index: {index}")
#     start = index + 1  # Move the starting point to after the found substring

# text = "I am learning Python from the scratch and want to be an expert."

# # List of words to find
# words_to_find = ['Python', 'scratch', 'expert']

# # Dictionary to store the indexes of each word
# word_indexes = {word: [] for word in words_to_find}

# # Loop over each word and find all occurrences
# for word in words_to_find:
#     start = 0
#     while start < len(text):
#         # Find the next occurrence
#         index = text.find(word, start)
#         if index == -1:
#             break  # No more occurrences found
#         word_indexes[word].append(index)
#         start = index + 1  # Move the starting point to after the found word

# # Print out the indexes for each word
# for word, indexes in word_indexes.items():
#     print(f"'{word}' found at indices: {indexes}")


# text = "I am learning Python from the scratch and want to be an expert"

# find_words = ["Python", "scratch", "expert"]

# word_indexes = {word : [] for word in find_words}

# for word in find_words:
#     start = 0
    
#     while start < len(text):
#         index = text.find(word, start)

#         if index == -1:
#             break
        
#         word_indexes[word].append(index)
#         start =index + 1

# for word, indexes in word_indexes.items():
#     print(f"'{word}' found in  index: {indexes}")

# # মূল টেক্সট
# text = "I am learning Python from the scratch and want to be an expert."

# # ব্যবহারকারীর input নিন (capital letters-এ দিলে lowercase এ convert হবে)
# user_input = input("কোন শব্দটি খুঁজতে চান? ").lower()

# # পুরো text কে lowercase-এ convert করুন, যাতে case-insensitive খোঁজা যায়
# lower_text = text.lower()

# # খুঁজে পাওয়ার জন্য index list
# indexes = []

# start = 0
# while start < len(lower_text):
#     index = lower_text.find(user_input, start)
#     if index == -1:
#         break
#     indexes.append(index)
#     start = index + 1  # পরবর্তী খোঁজ শুরু করার জন্য

# # ফলাফল দেখানো
# if indexes:
#     print(f"'{user_input}' found at indices: {indexes}")
# else:
#     print(f"'{user_input}' শব্দটি টেক্সটে পাওয়া যায়নি।")

################################################################################################################


# text = "I am learning Python from the scratch and want to be an expert."

# # user input
# user_input = input("search the name): ")

# words_to_find = [word.strip() for word in user_input.split(",")]

# lower_text = text.lower()


# word_indexes = {}

# for word in words_to_find:
#     search_word = word.lower()   
#     start = 0
#     matches = []

#     while start < len(lower_text):
#         index = lower_text.find(search_word, start)

#         if index == -1:
#             break

#         original_match = text[index:index + len(search_word)]

#         matches.append((original_match, index))

#         # overlapping match 
#         start = index + 1

#     word_indexes[word] = matches

# # output
# for word, matches in word_indexes.items():
#     if matches:
#         print(f"\nInput word: '{word}'")
#         for found_word, index in matches:
#             print(f"Found '{found_word}' at index {index}")
#     else:
#         print(f"\nInput word: '{word}'")
#         print("Did not find the text")

# text = "I am learning Python from the scratch and want to be an expert."

# user_input = input("Which words do you want to find? Use comma between words")

# input_to_list = [word.strip() for word in user_input.split(",")] 


# text_to_lower = text.lower()


# txt = "Writing the Python Script"

# print("Text split [:6] at first, then print [:2]", txt[:6][:4])

text = "Shams"

text2 = list(text)

print(text)

print(text2)

text2.insert(5, "s")

text = ''. join(text2)

print("Modifid text is: ", text)
