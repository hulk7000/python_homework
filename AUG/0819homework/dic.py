def star(row=9,printnum=0):
    count = 0
    for i in range(row):
        for j in range(i):
            print('',end=' ')
        for h in range(2 * (row - i) - 1):
            print('*',end='')
            count += 1
        print()
    if printnum == 1:
        print(count)


star()


# for i in range(9):
#     i = i + 1
#     for j in range(i):
#         j = i + 1
#         print(f'{i}*{j} = {i * j}',end='  ')
#     print('\n',end='')
