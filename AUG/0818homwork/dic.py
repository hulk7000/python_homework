row = 6
count = 0
for i in range(row):
    for j in range(row - i - 1):
        print('',end=' ')
    for g in range(2 * i + 1):
        print('*',end='')
        count += 1
    print()
print(f'total of {count} stars')

# for i in range(9):
#     i = i + 1
#     for j in range(i):
#         j = j + 1
#         print(f"{i}*{j} = {i * j}",end='  ')
#     print('\n',end='')