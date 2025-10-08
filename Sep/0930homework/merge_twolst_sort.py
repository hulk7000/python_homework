list1 = [1,2,4]
list2 = [1,3,4]

def mergelst(lst1, lst2):
    result = []
    result.extend(lst1)
    result.extend(lst2)
    result.sort()
    print(result)

mergelst(list1, list2)