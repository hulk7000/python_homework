# l1 = [94,29,21,43,3,76]
# def avg():
#     count = 0
#     total = 0
#     for i in l1:
#         total += i
#         count += 1
#         avg = total / count
#     print(avg)
#
# l2 = [10,21,2,11,1,22,21,21]
# def mostnum(l2):
#     result =[]
#     for i in l2:
#         count = 0
#         for j in l2:
#             if i == j:
#                 count = count + 1
#         # print(f'i = {i} , count = {count}')
#         result.append(count)
#     zipped = list(zip(l2, result))
#     zipped=set(zipped)
#     mostnum=0
#     for x in zipped:
#         if x[1]>mostnum:
#             mostnum = x[1]
#             num=x[0]
#     return num,mostnum
# print(mostnum(l2))
import re

sentence = "Python is bad, and Python is hard Python hardhard hard hard hard"
word = re.findall(r'\b\w+\b', sentence)
print(word)
result = []
for i in word:
    print(f'i = {i}')
    for j in word:
        print(f' --j = {j}')
        count = 0
        if i == j:
            count = count + 1
        print(count)
    # result.append(count)
# zipped = list(zip(word, result))
# zipped=set(zipped)
# words = 0
# for x in zipped:
#     if x[1]>words:
#         words = x[1]
#         num=x[0]
# print(num,words)