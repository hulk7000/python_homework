def adding_list(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

number_list = [1,2,3,4,5]
result = adding_list(number_list)
print(result)

def adding_dic(dic):
    total = 0
    for k,v in dic.items():
        total += v
    return total
number_dic = {"f":1, "k":2, "a":3, "l":4}
result = adding_dic(number_dic)