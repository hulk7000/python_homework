import os,random,string,calendar,datetime

# lis = [5,3,2,1]
# def sortport():
#     for i in range(len(lis)-1):
#         for j in range(len(lis)-1-i):
#             if lis[j] > lis[j+1]:
#                 lis[j],lis[j+1] = lis[j+1], lis[j]
#     return lis
#
# print(sortport)

# def power(x, n):
#     h=1
#     while n>0:
#         n=n-1
#         h=h*x
#     return h
#
# print(power(2,4))

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum+n*n
#     return sum
#
# print(calc(2,3))

# def fac():
#     num = int(input("please enter a number:"))
#     factorial = 1
#
#     if num < 0:
#         print("sorry invalid number")
#     elif num == 0:
#         print("The factorial of 0 is 1")
#     else:
#         for i in range(1,num+1):
#             factorial = factorial * i
#         print("The factorial of %d is %d" % (num, factorial))

# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result = result * i
#     return result

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n-1)

# print([d for d in os.listdir(".")])

# for d in os.listdir("."):
#     if d.endswith(".py"):
#         print(d)

# l = ["Hello", "World", "IBM", "Apple"]
# lowercase_list = [s.lower() for s in l]
#
# print(lowercase_list)

# def print_dir():
#     filepath = input("Enter a directory path: ")
#
#     if filepath == "":
#         print("please input a right path")
#     else:
#         try:
#             for i in os.listdir(filepath):
#
#                 print(os.path.join(filepath, i))
#         except:
#             print("Please input a correct path.")
# print_dir()

# num=["harden","lampard",3,34,45,56,76,87,78,45,3,3,3,87686,98,76]

# for i in range(num.count(3)):
#     ele_index = num.index(3)                #ele = element
#     num[ele_index]="3a"
#     print(num)

# l = ["James","Meng","Xin"]
# for i in range(len(l)):
#     print("Hello, %s"%l[i])

# l1=[2,3,8,4,9,5,6]
# l2=[5,6,10,17,11,2,"apple"]
# l3 = l1+l2
# print(l3)
# print(set(l3))                             #set = no duplicit
# print(list(set(l3)))

# str1 = "0123456789"
# str2 = string.ascii_letters
# str3 = str1+str2
# ma1 = random.sample(str3,9)
# ma1 = ''.join(ma1)
# print(ma1)

# i = 1
# a = random.randint(0,100)
# b = int(input("Please enter a number from 0-100 : "))
# while a != b:
#     if a > b:
#         print("too low")
#         b = int(input("guess again : "))
#     else:
#         print("too high")
#         b = int(input("guess again : "))
#     i+=1
# else:
#     print(f"Nice job! You guessed the correct number {a} in {i} tries.")

# chri = "一"
# # chri = "1"
# print(chri.isdigit())
# print(chri.isnumeric())

# while True:
#     try:
#         num = int(input("Please enter an integer: "))
#     except ValueError:
#         print("This is not an integer")
#         continue
#
#     if num % 2 == 0:                                                       #remander
#         print("The number is even")
#     else:
#         print("The number is odd")
#     break

# year = int(input("Enter a year : "))
# if (year % 4)==0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("{0} is a leap year".format(year))
#         else:
#             print("{0} is not a leap year".format(year))
#     else:
#         print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))

# n=int(input("How many numbers you want to compare : "))
# print("Enter the numbers you want to compare")
# num = []
# for i in range(1,n+1):
#     temp = int(input("Enter number %d : " % i))
#     num.append(temp)

# print("Your numbers are:",num)
# print("Your biggest number is :",max(num))

# yy = int(input("Enter the year : "))
# mm = int(input("Enter the month : "))
#
# print(calendar.month(yy,mm))

# yy = int(input("Enter the year : "))
# mm = int(input("Enter the month : "))

# monthRange = calendar.monthrange(yy,mm)
# print(monthRange)                     #(first_weekday, number_of_days)

# def add(x,y):
#     return x+y
#
# def subtract(x,y):
#     return x-y
#
# def multiply(x,y):
#     return x*y
#
# def divide(x,y):
#     return x/y
#
# print("Math equations : ")
# print("1, add")
# print("2, subtract")
# print("3, multiply")
# print("4, divide")
#
# choice = input("Plz enter(1/2/3/4): ")
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
#
# if choice == "1":
#     print(num1, "+", num2, "=", add(num1,num2))
#
# elif choice == "2":
#     print(num1, "-", num2, "=", subtract(num1,num2))
#
# elif choice == "3":
#     print(num1, "*", num2, "=", multiply(num1,num2))
#
# elif choice == "4":
#     if num2 !=0:
#         print(num1, "/", num2, "=", divide(num1,num2))
#     else:
#         print("You can't enter 0")
# else:
#     print("invalid number"))

# def getYesterday():
#     today=datetime.date.today()
#     oneday=datetime.timedelta(days=1)
#     yesterday = today-oneday
#     return yesterday
# print(getYesterday())

# path_prefix = "abc.com/ss"
#
# numlist = range(1000)
#
# def a():
#     for num in numlist:
#         url = path_prefix + f"{num:02d}"
#         print(url)
# a()