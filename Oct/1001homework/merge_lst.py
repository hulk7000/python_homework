list1 = [1,2,4]
list2 = [1,3,4]

def mergelst(l1,l2):
    result = []
    result.extend(l1)
    result.extend(l2)
    result.sort()
    print(result)
# mergelst(list1,list2)

l1 = ["h","e","l","l","o"]

def reverse(lst):
    result = []
    for i in lst:
        result.insert(0, i)
    return result
print(reverse(l1))
