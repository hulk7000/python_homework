def valid_number(num):
    if type(num) == int:
        return num
    else:
        return 0

def add_numbers_lst(numbers_list):
    total = 0
    for num in numbers_list:
        num = valid_number(num)
        total += num
    return total

number_list = [1,2,3,4,5,"p"]
# result = add_numbers_lst(number_list)


def add_number_dic(dic):
    total = 0
    for k,v in dic.items():
        v = valid_number(v)
        total += v
    return total

number_dic = {"f":1, "k":2, "a":3, "l":4,"b":"o"}
result = add_number_dic(number_dic)
print(result)