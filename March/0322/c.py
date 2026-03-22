def valid_number(num):
    if type(num) == int:
        return num
    else:
        return 0

def add(dic):
    total = 0
    for k,v in dic.items():
        v = valid_number(v)
        total += v
    return total
if __name__ == "__main__":
    number_dic = {"f":1, "k":2, "a":3, "l":4,"b":"o"}
    result = add(number_dic)