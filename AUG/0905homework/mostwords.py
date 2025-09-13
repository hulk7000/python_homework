# import re
#
# sentence = "Python is bad, and Python is hard Python hardhard hard hard hard"
# word = re.findall(r'\b\w+\b', sentence)
# print(word)
# result = []
# for i in word:
#     count = 0
#     for j in word:
#         if i == j:
#             count = count + 1
#             print(count)

# lst= [1,2,3,4,5]
# def rotate(lst, n):
#     return lst[-n:] + lst[:-n]
#
# rotated_lst = rotate(lst, 3)
# print(rotated_lst)

# from collections import Counter
# lst = [1,2,2,3,4,4,4,5]
# duplicates = [item for item, count in Counter(lst).items() if count > 1]
# print(duplicates)

# from itertools import groupby
# lst = [1,2,2,3,3,3,4,4,5,6,6]
# result = [key for key, _ in groupby(lst)]
# print(result)


nested_list = [1,[2,3,[4,5]],6]               #[1, 2, 3, 4, 5, 6]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten(nested_list))

# def chunk(lst, n):
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# chunks = list(chunk(lst, 4))
# print(chunks)

# lst = [10,20,10,30,10,40]
# indices = [i for i, x in enumerate(lst) if x == 10]
# print(indices)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# transposed = list(map(list, zip(*matrix)))
# print(transposed)