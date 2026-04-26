# name = "Alice"
# age = 25
# height = 5.6
# is_student = True
#
# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Student:", is_student)


def oppist(a, b):
    print("origin Input:", a, b)
    temp = a
    a = b
    b = temp
    return "new Output:", a, b

print(oppist(5,8))