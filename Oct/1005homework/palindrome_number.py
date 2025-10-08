number = [1,2,1]

def pn(lst):
    times = (len(lst) - 1) // 2
    for i in range(0, times):
        j = -(i + 1)
        # print(i,j)
        if lst[i] != lst[j]:
            return False
    return True

print(pn(number))