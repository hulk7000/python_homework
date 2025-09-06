# scores = {'Bob' : 69, 'c00lkid' : 99, 'ipad_kid' : 50, 'MLG_PRO' : 100}

# count = 0
# total = 0
# for k,v in scores.items():
#     count += 1
#     total += v
# 0903homework = total / count
# print(0903homework)

# import re
#
# data = '''
# TCP Student : 192.168.189.167:32806 Teacher : 137.78.5.128:65247, idle 0:00:00 : bytes 74, flags UIO
# TCP Student : 192.168.189.167:80 Teacher : 137.78.5.128:65233, idle 0:00:03 : bytes 334516, flags UIO
# '''
#
# pattern = r'Student\s*:\s*(\d+.\d+.\d+.\d+):(\d+)\s*Teacher\s*:\s*(\d+.\d+.\d+.\d+):(\d+),\s*idle\s*[\d:]+\s*:\s*bytes\s*(\d+),\s*flags\s*(\w+)'
# matches = re.findall(pattern, data)
#
# result = {}
# for student_ip, student_port, teacher_ip, teacher_port, bytes_count, flags in matches:
#     key = (student_ip, student_port, teacher_ip, teacher_port)
#     value = (bytes_count, flags.lower())
#     result[key] = value
#
# print(result)

# row = 6
# for i in range(row):
#     for j in range(i):
#         print(' ', end='')
#     for g in range(2 * (row - i) - 1):
#         print('*', end='')
#     print()

# for i in range(row):
#     for j in range(row - i - 1):
#         print(' ', end='')
#     for g in range(2 * i + 1):
#         print('*', end='')
#     print()

for i in range(9):
    i = i + 1
    # print(i)
    for j in range(i):
        j = j + 1
        print(f'{i}*{j}={i*j}', end=' ')
    print("\n",end="")