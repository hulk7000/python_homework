def valid_number(num):
    if type(num) == int:
        return num
    else:
        return 0

def add(a,b):
    total = a+b
    return total

if __name__ == "__main__":
    result=add(2,4)
    print(result)