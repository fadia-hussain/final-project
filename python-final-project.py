# final-project
# Fadia Hussain

import random
students = ["Hasan", "John", "Amira", "Salma", "Ashley", "Peter","Omar", "Shehnaz","Claudio", "Kaie","Mariam", "Rubel", "Mishika", "Fadia"]

length = len(students)

print("The number of students in this class is: ",length)

print("And now they will be separated into groups of two: \n")
for index, value in enumerate(students):
    if index % 2 == 0:
        print('Group : ' + value + ' + ' + students[index + 1])


# team = random.choice(students) + random.choice(students)
# print("Group: " + team)
# del (team)












