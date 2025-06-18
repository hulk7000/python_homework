def chengcheng(rows):
    for i in range (rows):
        for j in range(i+1):
            print("{} * {} = {}".format(j+1, i+1, (i+1)*(j+1)),end=' ')
        print('')
def checknum(a,b):
    while True:
        try:
            rows_input = int(input(f"please input rows （from： {a} to {b}）: "))
            if a <= rows_input <= b:
                break
            else:
                print(f"not in our range，please input int from {a} to {b}")
        except ValueError:
            print("invalid, please input a number")
    return rows_input

chengcheng(checknum(2,12))

# rows = 5
# b = 0
# for i in range(rows, 0,-1):
#     b +=1
#     for j in range(1, i +1):
#         print(b, end=' ')
#     print('\r')

# rows = 5
# b = 0
# for i in range(rows, 0, -1):
#     b +=1
#     for j in range(1, i +1):
#         print(b, end=' ')
#     print('\r')

# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, -1, -1):
#         print(end="")
#     k = k+1
#     for j in range(0, i +1):
#         print("*", end="")
#     print("")

# age = 10
# if age < 18:
#     print('You are a Minor')
# elif age < 65:
#     print('You are an Adult')
# else:
#     print('You are a Senior')

# numbers = -10
# if numbers > 0:
#     print('positive')
# else:
#     print('negative')

