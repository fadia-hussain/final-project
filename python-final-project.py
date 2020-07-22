# final-project
# Fadia Hussain


# file = open("groups", "a")
import random
students = ["Hasan", "John", "Amira", "Salma", "Ashley", "Peter","Omar", "Shehnaz","Claudio", "Kaie","Mariam", "Rubel", "Mishika", "Fadia"]

length = len(students)

# number_of_groups = 7
# while students>0 and number_of_groups>0:

for student in range (0,7):
    print("Group : ", random.choice(students) + " + " + random.choice(students) )
    del(students([-1]))
    print(students)



# print (students)
# file.close()




