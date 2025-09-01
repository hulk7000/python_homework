# def romatoint(s):
#     roman_dict = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     total = 0
#     prev_value = 0
#     for char in reversed(s):
#         value = roman_dict[char]
#         if value >= prev_value:
#             total += value
#         else:
#             total -= value
#         prev_value = value
#     return total
#
# print(romatoint("III"))

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
#
# def list2nums(l):
#     l.reverse()
#     nums = ''
#     for i in l:
#         nums += str(i)
#     nums = int(nums)
#     return nums
#
# def nums2list(j):
#     nums = []
#     j = str(j)
#     for i in j:
#         i=int(i)
#         nums.append(i)
#     return nums
#
#
# a = list2nums(l2)+list2nums(l1)
# print(a)
# print(nums2list(a))

















































nums = [3,2,5,6,0,2]
target = 7

def threesum(nums , target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j + 1,len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return (i, j, k)
                else:
                    continue
    return ('the number cannot be found in the list')
print(threesum(nums, target))