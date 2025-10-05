nums = [0,0,1,1,1,2,2,3,3,4]
setnums = set(nums)
print(f"type nums  :   {type(nums)}")
print(nums)
print(f"type setnums  :   {type(setnums)}")
print(setnums)
nums=list(setnums)
print(f'list nums : {nums}')


# def rd(lst):
#     result = []
#     for i in lst:
#         if i not in result:
#             result.append(i)
#     return result
# print(rd(nums))

def rd(lst):
    setnums = list(set(lst))
    return setnums
print(rd(nums))
