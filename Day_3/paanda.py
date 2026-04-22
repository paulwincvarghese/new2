# import pandas

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)

# import pandas as pd

# data = {
#     'calories': [420, 380, 390],
#     'duration': [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df)

# print(df.loc[0])

import pandas as pd
name = ["Arun", "Bina", "Chetan", "Divya", "Esha", "Fahad", "Gita", "Hari", "Isha", "Jatin"]
marks = [75, 85, 90, 70, 95, 80, 88, 92, 78, 82]
data = {
    'Name': name,
    'Marks': marks
}
df = pd.DataFrame(data)
print(df)

print(df.loc[1:2])