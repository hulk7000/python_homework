def cal():
    numbers = []
    functions = ['+','-','*','/']
    while True:     #判断3个input
        while True:                               #判断num1
                a_input = input('Number 1: ')
                try:
                    a = float(a_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        while True:                                      #判断num2
                b_input = input('Number 2: ')
                try:
                    b = float(b_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        func = input('+ - * /: ')
        if func in functions:                                #判断符号
            break
        print('Invalid choice')
    try:                                                     #运算
        if func =="+":
            c=a+b
        elif func =="-":
            c=a-b
        elif func =="*":
            c=a*b
        else:
            c=a/b
        return c
    except ValueError as e:                                 #错误返回错误
        return e

print(cal())