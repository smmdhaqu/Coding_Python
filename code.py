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
# user_input = input("Search the new words): ")

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


# # txt = "Writing the Python Script"

# # print("Text split [:6] at first, then print [:2]", txt[:6][:4])

# text = "Shams"

# text2 = list(text)

# print(text)

# print(text2)

# text2.insert(5, "s")

# text = ''. join(text2)

# print("Modifid text is: ", text)
#####################################################################################################

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduction(self):
#         print(f"The person name is {self.name} and he is {self.age} years old")

# person1 = Person("Shams", 27)
# person2 = Person("Raaju", 26)

# person1.introduction()
# person2.introduction()



# class Account:
#     def __init__(self, owner_name, currenr_balance):
#         self.owner_name = owner_name
#         self.__current_balance = currenr_balance
    

#     def display_info(self):
#         print("The account holder name is: ", self.owner_name)
#         print("His account balance is now: $", self.__current_balance)

    
#     def get_balance(self):
#         return self.__current_balance


#     def set_balance(self, amount):
#         if amount < 0:
#             print("Account balance can not be less than 0")
#         else:
#             self.__current_balance = amount


# my_account = Account ("Shams", 5000)

# my_account.display_info()


# my_account.set_balance(500)
# my_account.set_balance(-500)

# print("The Updated Balance is: $", my_account.get_balance())


######################################################################################################

# class Account:
#     def __init__(self, account_owner, account_balance= 0):
#         self.account_owner = account_owner
#         self.__account_balance = account_balance

#     def withdraw (self, amount):
#         if 0 < amount <= self.__account_balance:
#             self.__account_balance -= amount
#             print(f"Withdraw amount was ${amount} and now account balance remains ${self.__account_balance}")
#         else:
#             print("Insufficient balance or Invalid amount")


#     def deposit(self, amount):
#         if amount > 0:
#             self.__account_balance += amount
#             print(f"Deposit amount is {amount}, now your balance is {self.__account_balance}")
#         else:
#             print("You gave the wrong amount")


#     def final_balance(self):
#         return self.__account_balance

#     def display_info(self):
#         print(f"The account holder name is {self.account_owner}")
#         print(f"Account balance is: {self.__account_balance}")

# my_account = Account("Shams Ahmed", 5000)

# my_account.display_info()

# my_account.withdraw(500)

# my_account.deposit(1000)

# print("Now your account balance is", my_account.final_balance())



# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance  # private attribute

    
#     def get_balance(self):
#         return self.__balance

    
#     def set_balance(self, balance):
#         if balance >= 0:
#             self.__balance = balance
#             print(f"Balance updated to: ${self.__balance}")
#         else:
#             print("Balance can't be negative!")

    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.__balance}")
#         else:
#             print("Deposit amount must be positive!")

    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
#         else:
#             print("Insufficient funds or invalid amount!")

#     def display_info(self):
#         print(f"Account owner: {self.owner}")
#         print(f"Account balance: ${self.__balance}")


# owner = input("Enter account owner's name: ")
# initial_balance = float(input(f"Enter initial balance for {owner}: $"))


# account = BankAccount(owner, initial_balance)


# account.display_info()


# deposit_amount = float(input("Enter amount to deposit: $"))
# account.deposit(deposit_amount)


# withdraw_amount = float(input("Enter amount to withdraw: $"))
# account.withdraw(withdraw_amount)


# print("Final balance:", account.get_balance())


#####################################################################################################

# class BankAccount:
#     def __init__ (self, account_name, account_balance= 0):
#         self.account_name = account_name
#         self.__account_balance = account_balance


#     def set_balance(self, account_balance):
#         if account_balance >= 0:
#             print(f"Account Balance updated to &{self.__account_balance}")
#         else:
#             print("You may entered the negative or wrong amount.")

#     def deposit_balance(self, amount):
#         if amount > 0:
#             self.__account_balance += amount
#             print(f"Your diposit amount was {amount}, now your balance is {self.__account_balance}")
#         else:
#             print("Plese enter the positive number")
    
#     def withdraw_balance(self, amount):
#         if 0 < amount <= self.__account_balance:
#             self.__account_balance -= amount
#             print("The amount ") 


# diposit_amount= float(input("Please enter the diposit money: "))
# account.deposit_balance(diposit_amount)


# account_name = input("Enter your Name: ")

# inset_amount = float(input(f"Enter the amount for the {account_name}: $"))

# account = BankAccount(account_name, inset_amount)
##############################################################################################################################
#################################### Inheritance #############################################################################

# class Vichel:
#     def __init__(self, speed, type):
#         self.speed = speed
#         self.type = type
    

#     def display_info(self):
#         print(f"It is running with {self.speed} km/h.")
#         print(f"It is a {self.type}.")

# class Car (Vichel):
#     def __init__(self, speed, type, brand):
#         super().__init__(speed, type)
#         self.brand = brand

#     def display_info(self):
#         super().display_info()
#         print(f"The brand of the {self.type} is a {self.brand}.")

# # my_car = Car(200, "Car", "Marcedes Benz")

# # my_car.display_info()

# class Electric_Car(Car):
#     def __init__(self, speed, type, brand, battery_capacity):
#         super().__init__(speed, type, brand)
#         self.battery_capacity = battery_capacity

#     def display_info(self):
#         super().display_info()
#         print(f"The {self.type} called {self.brand} has a battery_capacity of {self.battery_capacity} kw.")


# type = input("What type of Vichle is it? ")
# brand = input("Which brand is the Vichele? ")
# battery_capacity = float(input("What is the battery capacity of this vichele? "))
# speed = float(input("What is the maximum speed of the Vichle: "))


# my_car = Electric_Car(speed, type, brand, battery_capacity)

# my_car.display_info()

################################################################################################

# class Vehicle:
#     def __init__(self, speed, fuel_capacity):
#         self.speed = speed
#         self.__fuel_capacity = fuel_capacity
    
#     def get_capacity(self):
#         return self.__fuel_capacity
    
#     def set_capacity(self, fuel_capacity):
#         if fuel_capacity > 0:
#             self.__fuel_capacity = fuel_capacity
#             print(f"Your set fuel capacity was {self.__fuel_capacity} liters")
#         else:
#             print("Capacity must be positive.")

#     def display_info(self):
#         print(f"Speed is: {self.speed} km/h")
#         print(f"Fuel Capacity: {self.__fuel_capacity} liters") # This is also correct -> self.get_capacity()

# class Car (Vehicle):
#     def __init__(self, speed, fuel_capacity, car_brand):
#         super().__init__(speed, fuel_capacity)
#         self.car_brand = car_brand

#     def display_info(self):
#         super().display_info()
#         print(f"The brand of the Car is: {self.car_brand}")

# class Truck(Vehicle):
#     def __init__(self, speed, fuel_capacity, load_capacity):
#         super().__init__(speed, fuel_capacity)
#         self.load_capacity = load_capacity
    
#     def display_info(self):
#         super().display_info()
#         print(f"The truck can carry upto {self.load_capacity} tons")

# vehicle_type = input("Enter the Vehicle type (Car/Truck): ").lower()
# if vehicle_type == "car":
#     car_brand = input("What is the Brand of the Car? ")
#     fuel_capacity = float(input("How much fuel can be carried the Car? "))
#     speed = float(input("Enter the maximum speed of the Car: "))
#     my_car = Car(speed, fuel_capacity, car_brand)
#     my_car.display_info()

# elif vehicle_type == "truck":
#     fuel_capacity = float(input("How much fuel can be carried the Truck? "))
#     speed = float(input("Enter the maximum speed of the Truck: "))
#     load_capacity = float(input("Enter the highest Load Capacity: "))
#     my_truck = Truck(speed, fuel_capacity, load_capacity)
#     my_truck.display_info()

# else:
#     print("Invalid Vehicle type!")

#######################################################################################################################################

# from abc import ABC, abstractmethod

# #Abstract Class
# class BankAccount(ABC):
#     @abstractmethod

#     def deposit(self, money):
#         pass

#     @abstractmethod

#     def withdraw(self, money):
#         pass

# #Subclass

# class SavingAccount(BankAccount):
#     def __init__(self, balance_money = 0):
#         self.balance_money = balance_money

#     def deposit(self, money):
#         self.balance_money += money
#         print(f"You deposited {money}, Now your balace is {self.balance_money}")


#     def withdraw (self, money):
#         if money <= self.balance_money:
#             self.balance_money -= money
#             print(f"You withdraw {money}, Now you your balance is {self.balance_money}")
#         else:
#             print("Invalid or Negative Number")


# saving = SavingAccount(5000)
# saving.deposit(1000)
# saving.withdraw(500)

# from abc import ABC, abstractmethod


# class Person(ABC):
#     @abstractmethod

#     def description(self):
#         pass

# class Student(Person):
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
    
#     def description(self):
#         return f"The student name is {self.name} and his grade is: {self.grade}"
    
# class Teacher(Person):
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject 

#     def description(self):
#         return f"Teacher name is {self.name}, he teaches {self.subject}"


# student_info = Student("Shams", 3.5)
# teacher_info = Teacher("Raaju", "Math")

# print(student_info.description())
# print(teacher_info.description())

# class Vehicle:
#     def wheels(self):
#         raise NotImplementedError

# class Car(Vehicle):
#     def wheels(self):
#         return "Most of the car has 4 Wheels"
    
# class Truck(Vehicle):
#     def wheels(self):
#         return "Truck has more than 4 Wheels"

# car = Car()
# truck = Truck()


# def display_wheels(vehicle):
#     print(vehicle.wheels())

# display_wheels(car)
# display_wheels(truck)

# class Payment:
#     def payment_method(self):
#         raise NotImplementedError

# class Paypal(Payment):
#     def payment_method(self):
#         return "Payment done by Paypal."

# class CreditCard(Payment):
#     def payment_method(self):
#         return "Credit Card is used to pay the bill."
    
# def show_payment(payment):
#     print(payment.payment_method())

# user_input = input("Enter the Payment methode between PayPal and Credit Card: ").lower()

# if user_input == "paypal":
#     paypal = Paypal()
#     show_payment(paypal)

# elif user_input == "credit card":
#     creditcard = CreditCard()
#     show_payment(creditcard)
# else:
#     print("Invalid Payment")


# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def calculate_salary(self):
#         return 0

#     def show_salary(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Salary: ${self.calculate_salary():.2f}")


# class FullTimeEmployee(Employee):
#     def __init__(self, name, base_salary, bonus):
#         super().__init__(name)
#         self.__base_salary = base_salary
#         self.__bonus = bonus

#     def calculate_salary(self):
#         return self.__base_salary + self.__bonus


# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.__hourly_rate = hourly_rate
#         self.__hours_worked = hours_worked

#     def calculate_salary(self):
#         return self.__hourly_rate * self.__hours_worked


# class Freelancer(Employee):
#     def __init__(self, name, project_payment):
#         super().__init__(name)
#         self.__project_payment = project_payment

#     def calculate_salary(self):
#         return self.__project_payment


# def print_payroll(employee):
#     employee.show_salary()
#     print("-" * 30)


# full_name = input("Enter full-time employee name: ")
# base_salary = float(input("Enter base salary: "))
# bonus = float(input("Enter bonus: "))

# part_name = input("Enter part-time employee name: ")
# hourly_rate = float(input("Enter hourly rate: "))
# hours_worked = float(input("Enter hours worked: "))

# free_name = input("Enter freelancer name: ")
# project_payment = float(input("Enter project payment: "))

# employees = [
#     FullTimeEmployee(full_name, base_salary, bonus),
#     PartTimeEmployee(part_name, hourly_rate, hours_worked),
#     Freelancer(free_name, project_payment)
# ]

# print("\nPayroll Report:")
# for employee in employees:
#     print_payroll(employee)

# n = 5
# for number in range(n):
#     print("*" * 5)


# n = 5

# for row in range (1, n + 1):
#     print("*" * row)

# n = 5
# for row in range(n):
#     print("*" * row)

number_of_row = 5
number_of_column = 6

for row in range(number_of_row):
    for column in range(number_of_column):
        print("*", end=" ")


    print()