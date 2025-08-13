import re

data = '''
TCP Student : 192.168.189.167:32806 Teacher : 137.78.5.128:65247, idle 0:00:00 : bytes 74, flags UIO
TCP Student : 192.168.189.167:80 Teacher : 137.78.5.128:65233, idle 0:00:03 : bytes 334516, flags UIO
'''

pattern = r"Student\s*:\s*(\d+\.\d+\.\d+\.\d+):(\d+)\s*Teacher\s*:\s*(\d+\.\d+\.\d+\.\d+):(\d+),\s*idle\s*[\d:]+\s*:\s*bytes\s*(\d+),\s*flags\s*(\w+)"

matches = re.findall(pattern, data)

result = {}
for student_ip, student_port, teacher_ip, teacher_port, bytes_count, flags in matches:
    key = (student_ip, student_port, teacher_ip, teacher_port)
    value = (bytes_count, flags.lower())  # flags 转小写（可选）
    result[key] = value

print(result)

# list1 = ['aaa', 111, (4, 5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# only_in_list1 = []
# only_in_list2 = []
# in_both = []
#
# for i in list1:
#     if i in list2:
#         in_both.append(i)
#     else:
#         only_in_list1.append(i)
#
# for i in list2:
#     if i not in list1:
#         only_in_list2.append(i)
#
# print("Only in list1:", only_in_list1)
# print("Only in list2:", only_in_list2)
# print("In both lists:", in_both)