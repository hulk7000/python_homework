list1 = [1,2,4]
list2 = [1,3,4]

def cs(l1,l2):
    result = []
    result.extend(l1)
    result.extend(l2)
    result.sort()
    print(result)
# cs(list1, list2)

s = ["h","e","l","l","o"]

def reversestring(lst):
    result = []
    for i in lst:
        result.insert(0, i)
    print(result)
# reversestring(s)

# nums = [0,0,1,1,1,2,2,3,3,4]

def removedup(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)
# removedup(nums)

num = [2,7,11,15]
target = 9

def twonum(nums , target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
            else:
                continue
    return 'the number cannot be found in the list'
# print(twonum(num, target))