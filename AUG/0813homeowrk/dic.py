import re

data = '''
TCP Student : 192.168.189.167:32806 Teacher : 137.78.5.128:65247, idle 0:00:00 : bytes 74, flags UIO
TCP Student : 192.168.189.167:80 Teacher : 137.78.5.128:65233, idle 0:00:03 : bytes 334516, flags UIO
'''

# match = re.findall(r'TCP Student\s*:\s*(\d{1,3}(?:\.\d{1,3}){3}:\d+)\s*Teacher\s*:\s*(\d+\.\d+\.\d+\.+\d+):(\d+),\s*idle\s*[\d:]+\s*:\s*bytes\s*(\d+),\s*flags\s*(\w+)', data)
# print(match)

# result = {}
# for student_ip, student_port, teacher_ip, teacher_port, bytes_count, flags in match:
#     key = (student_ip, student_port, teacher_ip, teacher_port)
#     value = (bytes_count, flags.lower())  # flags 转小写（可选）
#     result[key] = value
#
# print(result)

# test = 'student : 192.168, teacher : 10.0.0.1'
# match = re.findall(r'student\s*:\s*(\d+.\d+),\s*teacher\s*:\s*(\d+.\d+.\d+.\d+)', test)
# print(match)

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
    for j in range(2 * i - 1):
        print('*', end='')
    print()