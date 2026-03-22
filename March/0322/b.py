def valid_number(num):
    if type(num) == int:
        return num
    else:
        return 0
    
def add(numbers_list):
    total = 0
    for num in numbers_list:
        num = valid_number(num)
        total += num
    return total
if __name__ == "__main__":
    number_list = [1,2,3,4,5,"p"]
    result = add(number_list)
    print(result)