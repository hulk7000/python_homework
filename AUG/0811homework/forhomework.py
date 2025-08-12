# list1 = ['aaa', 111, (4,5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4,5)]
#
# for i in list1:
#     if i in list2:
#         print(i)

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# only_in_list1 = []
# only_in_list2 = []
# in_both = []
#
# for i in list1:
#     if i in list2:
#         in_both.append(i)
#     else:
#         only_in_list1.append(i)
#
# for i in list2:
#     if i not in list1:
#         only_in_list2.append(i)
#
# print("Only in list1:", only_in_list1)
# print("Only in list2:", only_in_list2)
# print("In both lists:", in_both)

row = 6

for i in range(row):
    for j in range(i):
        print(' ',end='')
    for j in range(2 * (row - i) - 1):
        print('*',end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ',end='')
    for j in range(2 * i - 1):
        print('*',end='')
    print()