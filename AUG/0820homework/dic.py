# def star(row=0, printnum=0):
#     count = 0
#     for i in range(row):
#         for j in range(i):
#             print('', end=' ')
#         for h in range(2 * (row - i) - 1):
#             print('*', end='')
#             count += 1
#         print()
#     if printnum == 1:
#         print(count)

# star(6,1)

# def star(row=0, printnum=0):
#     count = 0
#     for i in range(row):
#         for j in range(row - i - 1):
#             print('', end=' ')
#         for h in range(2 * i + 1):
#             print('*', end='')
#             count += 1
#         print()
#     if printnum == 1:
#         print(count)
# star(6)

for i in range(9):
    i = i + 1
    for j in range(i):
        j = j + 1
        print(f'{i}*{j} = {i * j}',end='   ')
    print('\n',end='')