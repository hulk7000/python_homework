root = [4,2,7,1,3,6,9]

def ibst(lst):
    result = []
    for i in range(len(lst)):
        j = 2**i
        # print(i,j)
        row = lst[(j-1):(j-1+j)]
        row.reverse()
        result.extend(row)
    print(result)
# ibst(root)


def ispoweroftwo(n: int) -> bool:
    for i in range(0,32):
        result = 2 ** i
        # print(f'2**{i} result = {result}')
        if result == n:
            return True
    return False
# print(ispoweroftwo(512))


number = [1,2,1]
def pn(lst):
    times = len(lst) - 1 // 2
    for i in range(0, times):
        j = -(i + 1)
        if lst[i] != lst[j]:
            return False
    return True
# print(pn(number))


string = ['h','i']
def reverse(lst):
    result = []
    for i in lst:
        result.insert(0,i)
    print(result)
    return result
# reverse(string)


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


def removedup(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)
# removedup(nums)


list1 = [1,2,4]
list2 = [1,3,4]

def cs(l1,l2):
    result = []
    result.extend(l1)
    result.extend(l2)
    result.sort()
    print(result)
# cs(list1, list2)