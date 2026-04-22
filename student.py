import matplotlib.pyplot as plt
import numpy as np

students = ["Arun", "Bina", "Chetan", "Divya", "Esha"]
marks = [75, 85, 90, 70, 95]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

ax1.bar(students, marks, color=['red', 'blue', 'green', 'orange', 'purple'])
ax1.set_xlabel('Students')
ax1.set_ylabel('Marks')
ax1.set_title('Marks of Students')

ax2.pie(marks, labels=students, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'orange', 'purple'])
ax2.set_title('Marks Distribution of Students')

ax3.plot(students, marks, marker='o', color='blue')
ax3.set_xlabel('Students')
ax3.set_ylabel('Marks')
ax3.set_title('Marks of Students')

plt.tight_layout()
plt.show()
