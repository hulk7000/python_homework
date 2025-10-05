lst1  = [1,3,5]
tple1 = (1,3,5)
lst1[0] =10
lst1.extend(tple1)
print(lst1)






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

nums = [0,0,1,1,1,2,2,3,3,4]

def removedup(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
# print(removedup(nums))