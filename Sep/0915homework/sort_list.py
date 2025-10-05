origin_list = [5, 9, 3, 77, 2, 6, 99, 8, 21, 6, 4]

def sort(lst):
    total_num = 0
    for i in range(len(lst)):
        eachtime = 0
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                total_num += 1
                eachtime += 1
        print(f'attempt {i+1} , changed times {eachtime}')
    print(f'total times {total_num}')
    return lst
print(sort(origin_list))
