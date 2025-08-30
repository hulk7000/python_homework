def star(row=0, printnum=0):
    count = 0
    for i in range(row):
        for j in range(i):
            print('', end=' ')
        for h in range(2 * (row - i) - 1):
            print('*', end='')
            count += 1
        print()
    if printnum == 1:
        print(count)
