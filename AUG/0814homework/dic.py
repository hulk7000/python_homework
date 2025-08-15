# import re

# test = 'student : 192.168, teacher : 10.0.0.1'
# match = re.findall(r'student\s*:\s*(\d+.\d+),\s*teacher\s*:\s*(\d+.\d+.\d+.\d+)', test)
# print(match)

# fruits = {'Apple' : 3, 'Banana' : 2, 'Watermelon' : 5}

# for k,v in fruits.items():
#     print(f'fruit : {k}, {v} dollar/pound')

# for k,v in fruits.items():
#     if v>2:
#         print(k)

scores = {'Bob' : 69, 'c00lkid' : 99, 'ipad_kid' : 50, 'MLG_PRO' : 100}

# for k,v in scores.items():
#     print(f'{k} score = {v}')

# for k,v in scores.items():
#     if v>=60:
#         print(f'{k} passed')

count = 0
total = 0
for k,v in scores.items():
    total += v
    count += 1
avg = total/count
print(avg)

row = 6

for i in range(row):
    for j in range(i):
        print(' ', end='')
    for j in range(2 * (row - i) - 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

