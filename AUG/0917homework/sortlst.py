origin_list = [5, 9, 3, 77, 2, 6, 99, 8, 21, 6, 4]

def sortlst(lst):
    total = 0
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                print(f'{lst[j]} , {lst[j+1]}',end=' ')
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                total += 1
                print(f'changed to : {lst[j]}, {lst[j+1]}')
                # print(f'{lst[j]}, {lst[j + 1]}  changed to  {lst[j + 1]}, {lst[j]}')
    print(f'total times {total}')
    return lst

print(sortlst(origin_list))