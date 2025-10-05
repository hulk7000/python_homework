origin_list = [5, 9, 3, 77, 2, 6, 99, 8, 21, 6, 4]

def sort(lst):
    total_num = 0

    for i in range(len(lst)):
        changed_times = 0
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                total_num += 1
                changed_times +=1
        print(f' 第 {i+1} 次 ,changed times is {changed_times}')
    print(f'total changed times {total_num} ')
    return lst
print(sort(origin_list))

def reverse_sort(lst):
    for i in range(len(lst)):
        j = len(lst) - i - 1
        print(lst[j])

# reverse_sort(origin_list)

