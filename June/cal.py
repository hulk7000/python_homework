def cal():
    numbers = []
    functions = ['+' , '-', '*', '/']
    while True:
        while True:
            a_input = input('Number1: ')
            try:
                a = int(a_input)
                break
            except ValueError:
                print('Invalid input')
        while True:
            func = input('+ - * /: ')
            if func in functions:
                break
            print('Invalid input')
        while True:
            b_input = input('Number2: ')
            try:
                b = int(b_input)
                break
            except ValueError:
                print('Invalid input')
        break
    try:
        if func == "+":
            c = a + b
        elif func == "-":
            c = a - b
        elif func == "*":
            c = a * b
        else:
            c = a / b
        return c
    except ValueError as e:
        return e

print(cal())
#10