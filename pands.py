import pandas as pd

# calories = {"Day 1": 1850, "Day 2": 1900, "Day 3": 2250}
# series_calories = pd.Series(calories)
# print(series_calories [series_calories >= 1900 ])

# names = ["Bulbasaur", "Ivysaur", "Vanusaur", "Charmander", "Charmeleon", "Charizard"]
# name_convert = pd.Series(names, index = [1, 2, 3, 4, 5, 6])

# print(name_convert)

# employes = {"Name": ["Shams", "Tuhin", "Shakib"],
#             "Age": [29, 31, 32]
#             }
# df = pd.DataFrame(employes, index= ["Employe 1", "Employe 2", "Employe 3"])

# df[["Title", "Contract", "Salary"]] = [
#     ["Data Engineer", "Full-Time", 4000],
#     ["Software Engineer", "Full-Time", 5000],
#     ["Technical Engineer", "Part-Time", 3000]
#     ]

# df["Bonus"] = df["Salary"] * 0.10
# df["Total Salary"] = df["Salary"] + df["Bonus"]
# print(df)

# def sum(a, b):
#     return a *b
# print(sum(5,6))

# (lambda a, b: a *b)(5,5)


# def function1(x, y):
#     return y(x)

# result = (function1(5, lambda x: x *2))
# print(result)

given_number = int (input("Enter the number: "))
check_number = lambda given_number: "Even" if given_number%2 == 0 else "Odd"

print(check_number(given_number))
