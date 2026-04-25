import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Marks2.csv")

print(df)

plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Student Marks Distribution")
plt.show()