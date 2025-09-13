# string = [1,2,3,3,4,4,43,53,1]
# def reverse(lst):
#     result = []
#     for i in lst:
#         result.insert(0,i)
#     print(result)
#     return result
#
# reverse(string)

# nums = [0,0,1,1,1,2,2,3,3,4]

# def rd(lst):
#     result = []
#     for i in lst:
#         if i not in result:
#             result.append(i)
#     return result
# print(rd(nums))

def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False
is_palindrome(123) 