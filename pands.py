import pandas as pd

my_data = [50, 60, 70]


convert_data = pd.Series(my_data, index = ["a", "b", "c"])
convert_data.loc["c"] = 100

print(convert_data)
print(convert_data[convert_data>=60])
