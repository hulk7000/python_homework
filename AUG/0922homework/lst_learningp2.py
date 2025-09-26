# l1 = [1,21,31,32,1,3,21,3,3,5,43,5,4,76,5]
# sorted_l1 = sorted(l1, reverse=True)
# print(sorted_l1)

# x = [1,2,3]
# l = ['a', x, 'b']
# d = {'x': x, 'y': 2}

# l1 = [433,324,5,456,657,8767,867,64,5466,4,3,54,90]
# l2 = l1.copy()
# l2.sort()
# print(l2)
# print(l1)

# import copy
# l1 = [1,2,['a', 'b']]
# l2 = l1
# l3 = l1.copy()
# l4 = copy.deepcopy(l1)
# l1.append(3)
# l1[2].append('c')
# print(l1)
# print(l2)
# print(l3)
# print(l4)

string = [1,2,3,3,4,4,43,53,1]
def reverse(lst):
    result = []
    for i in lst:
        result.insert(0, i)
    print(result)
    return result
reverse(string)

origin_list = [5, 9, 3, 77, 2, 6, 99, 8, 21, 6, 4]

def sortlst(lst):
    total = 0
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                print(f'{lst[j]} , {lst[j+1]}', end=' ')
                lst[j], lst[j+1] = lst[j+1], lst[j]
                total += 1
                print(f'changed to : {lst[j]}, {lst[j+1]}')
    print(f'total times {total}')
    return lst

# print(sortlst(origin_list))

def reverse_sort(lst):
    for i in range(len(lst)):
        j = len(lst) - i - 1
        print(lst[j])

# reverse_sort(origin_list)
