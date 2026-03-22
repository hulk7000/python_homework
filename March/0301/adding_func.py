def valid_number(num):
    if type(num) == int:
        return num
    else:
        return 0

def add(a,b):
    total = a+b
    return total

add(2,4)

def add(numbers_list):
    total = 0
    for num in numbers_list:
        num = valid_number(num)
        total += num
    return total

number_list = [1,2,3,4,5,"p"]
# result = add_numbers_lst(number_list)

from adding_func import add as add_num
from adding_func import valid_number
def add(dic):
    total = 0
    for k,v in dic.items():
        v = valid_number(v)
        total += v
    return total

number_dic = {"f":1, "k":2, "a":3, "l":4,"b":"o"}
result = add(number_dic)
print(result)