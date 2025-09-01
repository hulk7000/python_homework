# def times(x,y):
#     return x*y
#
# def ptimes(x,y):
#     print(x+y)
#
# result = times(1,2)
# print(result)
# result = ptimes(1,2)
# print(result)

# def controltype(count: int, ws: str) -> dict:
#     return {count: count * ws}
#
# print(controltype(2, 'test'))

# print(controltype('sdf', 2))

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

# l1 = [1,2,3,4,5,6,7,8,9]
# l1.insert(1,'p')
# l1.remove('p')
# l1.append(10)
# l1.pop()
# print(l1)

# l1 = [1,23,2,3,4,34,4,4,6,4,65,7,6,5,4,5,6]
# l1.sort()
# print(l1)

# x = [1,2,3]
# l = ['a', x ,'b']
# d = {'x': x, 'y': 2}
#
# x[1] = 'qytang'
# print(d)

# def qyt(x):
#     return x**2
# qyt = lambda x:x**2
# print(qyt(3))

# l1 = [1,21,2,1,2,1,21,2,1,1,4]
# sorted_list = sorted(l1, reverse=True)
# print(sorted_list)

l1 = [[1,2], [1,5], [3,2], [2,3], [1,10]]
sorted_list = sorted(l1, key=lambda x:x[0])
print(sorted_list)