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

info = {"Name": "Shams",  "Profession":  "Student", "Age": 25}

all_keys = info.keys()
print(all_keys)

all_values = info.values()
print(all_values)

getting_info1 = info.get("Name")
print("Your name is", getting_info1)

getting_info2 = info["Profession"]
print("and you are a", getting_info2)


adding_info = info.get("Graduation", "Computer Engineer")
print("You are a", adding_info)


info.update ({"Name": "Shamsul Haque", "Age": 28})

print(info)

if info["Age"] == 28:
    info["Age"] = 26
print(info)

for key in info:
    print(key, ":", info[key])