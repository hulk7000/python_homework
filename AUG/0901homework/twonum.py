nums = [3,2,5,6,0,2]
target = 7

def twonum(nums , target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
            else:
                continue
    return ('the number cannot be found in the list')
print(twonum(nums, target))