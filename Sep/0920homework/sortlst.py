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

nums = [3,2,5,6,0,2]
target = 7

def twonum(nums , target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return f'index : {i}, {j}  value : {nums[i]} + {nums[j]} = {target}'
            else:
                continue
    return 'the number cannot be found in the list'
print(twonum(nums, target))