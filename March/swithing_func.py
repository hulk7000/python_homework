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

# print(oppist(5,8))

def count_char(s):
    dic1 = {}
    for letter in s:
        if letter not in dic1:
            times = s.count(letter)
            dic1[letter] = times
    return dic1

# print(count_char("asa"))


def intersect(a, b):
    result = []
    for x in a:
        if x in b:
            result.append(x)

    return result

list1 = [2, 3, 4]
list2 = [1, 2, 3]

answer = intersect(list1, list2)
print(answer)