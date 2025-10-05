string = [1,2,3,3,4,4,43,53,1]
def reverse(lst):
    result = []
    for i in lst:
        result.insert(0, i)
    print(result)
    return result
# reverse(string)

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

print(sortlst(origin_list))

def reverse_sort(lst):
    for i in range(len(lst)):
        j = len(lst) - i - 1
        print(lst[j])

# reverse_sort(origin_list)
