# from sys import get_coroutine_origin_tracking_depth

#9

def avglist(lst):
    if not isinstance(lst, list):
        return "Error: Input is not a list."
    try:
        total = 0
        count = 0
        length = len(lst)
        for i in lst:
            i=int(i)          # This will raise an error if i is not a number
            total += i
            count += 1
        avg = total / count
        return avg
    except (ValueError, TypeError) as e:
        return f'your list not valid: \n{e}'


listnum=[87, 23, 14, 59, '{"44"}', 91, 89, 35, 11, 62, 48, 8, 20, 73, 5, 38, 84, 31, 16, 90, 55, 26, 64, 12, 79, 6]
output = avglist(listnum)
print(output)




# def evenorodd(num):
#     if num % 2 == 0:
#         print('{} is even'.format(num))
#     else:
#         print('{} is odd'.format(num))
# def sum(a,b):
#     c = a+b
#     output = '{} + {} = {}'.format(a,b,c)
#     return c
#
# def aavg(a,b):
#     a = float(a)
#     b = float(b)
#     c = (a+b)/2
#     output = 'avg is {}'.format(c)
#     return output
#
# print(aavg([1,2]))