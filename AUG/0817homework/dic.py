# for i in range(9):
#     i = i + 1
#     for j in range(i):
#         j = j + 1
#         print(f'{i}*{j} = {i*j}',end=' ')
#     print('\n',end='')

# l1 = [1,2,3,4,5]
# for i in l1:
#     print(i,end=' ')

# res = []
# for i in 'hello':
#     res.append(i*4)
# print(res)
# rest = [c*4 for c in 'hello']
# print(rest)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][1])

l1 = [1,2,3,4,5,6,7,8,9]
l1.insert(1,'p')
l1.remove('p')
l1.append(10)
l1.pop()
print(l1)