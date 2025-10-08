string = ['h','i']
def reverse(lst):
    result = []
    for i in lst:
        result.insert(0,i)
    print(result)
    return result
# reverse(string)

number = [1,2,1]
def pn(lst):
    times = len(lst) - 1 // 2
    for i in range(0, times):
        j = -(i + 1)
        if lst[i] != lst[j]:
            return False
    return True
# print(pn(number))

def ispoweroftwo(n: int) -> bool:
    for i in range(0,32):
        result = 2 ** i
        # print(f'2**{i} result = {result}')
        if result == n:
            return True
    return False
print(ispoweroftwo(512))