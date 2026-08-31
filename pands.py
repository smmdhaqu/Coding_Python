import pandas as pd

# calories = {"Day 1": 1850, "Day 2": 1900, "Day 3": 2250}
# series_calories = pd.Series(calories)
# print(series_calories [series_calories >= 1900 ])

# names = ["Bulbasaur", "Ivysaur", "Vanusaur", "Charmander", "Charmeleon", "Charizard"]
# name_convert = pd.Series(names, index = [1, 2, 3, 4, 5, 6])

# print(name_convert)

employes = {"Name": ["Shams", "Tuhin", "Shakib"],
            "Age": [29, 31, 32]
            }
df = pd.DataFrame(employes, index= ["Employe 1", "Employe 2", "Employe 3"])

df[["Title", "Contract", "Salary"]] = [
    ["Data Engineer", "Full-Time", 4000],
    ["Software Engineer", "Full-Time", 5000],
    ["Technical Engineer", "Part-Time", 3000]
    ]


print(df)