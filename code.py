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

new_dict = {"Gender": "Male", "Name": "Shams"}

match new_dict:
    case {"Gender": g, "Name": n}:
        print(f"He is {g}, and his name is {n}")

    case{"Sex": g, "Name": n}:
        print(f"He is {g}, and his name is {n}")