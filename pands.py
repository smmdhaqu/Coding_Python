import pandas as pd

calories = {"Day 1": 1850, "Day 2": 1900, "Day 3": 2250}
series_calories = pd.Series(calories)
print(series_calories [series_calories >= 1900 ])