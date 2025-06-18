# list = [
# 'K', '1', 'n', '5', 'w', 'x', 'T', 'b', '2', 'D', 'f', 'H', 'V', 'g', 'j', 'l', 'n', 'P', 'r',
# '6', 'o', 'x', 'A', 's', '5', 't', 'd', 'F', 'M', 'g', 'u', 'K', '3', 'Y', 'v', 'L', 'p', 'w']
# # for i in range(len(list)):
# #      print("position {} :  {}".format(i+1,list[i]))
# i=8
# j=6
#
# # 九九乘法口诀表
# for i in range(1, 10):  # 外层循环控制行数，从1到9
#     for j in range(1, i + 1):  # 内层循环控制每一行的内容
#          print(j, end=' ')
#          print(f"{j}×{i}={i*j}", end="\t")  # \t 制表符使输出对齐
#     print()  # 每一行结束后换行

# import re
# a = re.match('cmd\.exe','cmdaexe')
# print(a)

# a = re.match('a{3}','aaa')
# print(a)

# pattern = 'cat'
# text = 'catfish is swimming'
# result = re.match(pattern, text)
# if result:
#     print('you find me')
# else:
#     print('you did not find me')

# show = 'FastEthernet1        192.168.1.1     YES manual up                    up'
# import re
# re.match('[A-Z][a-zA-Z]+\d+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+YES manual\s+\w+\s+up',show)