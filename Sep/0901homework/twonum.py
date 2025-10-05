# nums = [3,2,5,6,0,2]
# target = 7
#
# def twonum(nums , target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return (i, j)
#             else:
#                 continue
#     return ('the number cannot be found in the list')
# print(twonum(nums, target))

square = lambda x: x ** 2
print('Square of 4:', square(4))

multiply = lambda a, b: a*b
print('3 multiplied by 5:', multiply(3, 5))

numbers = [1,2,3,4,5]
squares = list(map(lambda x: x ** 2, numbers))
print('Squares using map and lambda:', squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print('Even numbers using filter and lambda:', evens)

pairs = [(1,5), (2,1), (3,2), (4,3), (5,4)]
sorted_pairs = sorted(list(map(lambda x: x[1], pairs)))
print('Sorted by second element:',sorted_pairs)