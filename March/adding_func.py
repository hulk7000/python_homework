def add_numbers_lst(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

number_list = [1,2,3,4]
# result = add_numbers_lst(number_list)


def add_number_dic(dic):
    total = 0
    for k,v in dic.items():
        total += v
    return total

number_dic = {"f":1, "k":2, "a":3, "l":4}
result = add_number_dic(number_dic)
print(result)