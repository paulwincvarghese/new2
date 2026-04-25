import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Marks.csv")

print(df)

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Graph")

plt.show()