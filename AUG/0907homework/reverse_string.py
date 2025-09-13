# string = [1,2,3,3,4,4,43,53,1]
# def reverse(lst):
#     result = []
#     for i in lst:
#         result.insert(0,i)
#     print(result)
#     return result
#
# reverse(string)

list1 = [1, 2, 4]
list2 = [1, 3, 4]

def cs(l1, l2):
    l1.extend(l2)
    l1.sort()

cs(list1, list2)
print(list1)
