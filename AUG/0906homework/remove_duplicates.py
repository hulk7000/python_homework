nums = [0,0,1,1,1,2,2,3,3,4]

def rd(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
print(rd(nums))