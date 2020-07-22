# final-project
# Fadia Hussain

import random
students = ["Hasan", "John", "Amira", "Salma", "Ashley", "Peter","Omar", "Shehnaz","Claudio", "Kaie","Mariam", "Rubel", "Mishika", "Fadia"]

length = len(students)

print("The number of students in this class is: ",length)

print("And now they will be separated into groups of two: \n")
for student in range (0,7):

    print("Group : ", random.choice(students) + " + " + random.choice(students) )


# team = random.choice(students) + random.choice(students)
# print("Group: " + team)
# del (team)












