# def factorial(n):
#     if n <=0:
#         return 1
#
#     return n * factorial(n-1)
#
# num = 5
# result = factorial(num)
# print(f"{num} : {result}")


def jie_cheng(num):
    result = 1
    for i in range(num,0,-1):
        result = result * i
    # print(result)
    return result
print(jie_cheng(5))