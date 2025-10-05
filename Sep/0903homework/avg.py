l1 = [94,29,21,43,3,76]
def avg():
    total = 0
    count = 0
    for i in l1:
        total = total + i
        count = count + 1
        avg = total / count
    return (avg)
# print(avg())

l2 = [10,21,2,11,1,22,21,21]
def mostnum(l2):
    result =[]
    for i in l2:
        count = 0
        for j in l2:
            if i == j:
                count = count + 1
        # print(f'i = {i} , count = {count}')
        result.append(count)
    zipped = list(zip(l2, result))
    zipped=set(zipped)
    mostnum=0
    for x in zipped:
        if x[1]>mostnum:
            mostnum = x[1]
            num=x[0]
    return num,mostnum
print(mostnum(l2))
