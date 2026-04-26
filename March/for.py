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
    if not isinstance(num, int):
        return "Wrong input! Not a number."
    if num < 0:
        return "Wrong input! Must be non-negative."

    result = 1
    for i in range(num, 0, -1):
        result = result * i
    return result


print(jie_cheng(0))