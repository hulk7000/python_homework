import random

# 随机生成两个 0~10 的整数
a = random.randint(0, 10)
b = random.randint(0, 10)

# 随机选择运算符（+ 或 -）
operator = random.choice(['+', '-','*','/'])

# 根据运算符计算正确答案
if operator == '+':
    correct_answer = a + b
elif operator == '-':
    correct_answer = a - b
elif operator == '*':
    correct_answer = a * b
else:
    correct_answer = a / b
# 显示题目，等待用户输入答案
user_input = int(input(f"请计算：{a} {operator} {b} = "))

# 判断答案对错
if user_input == correct_answer:
    print("✅ 答对了！")
else:
    print(f"❌ 答错了，正确答案是 {correct_answer}")

# numbers1 = [3, 15, -7, 22, 5]
# numbers = [3, 15, -7, 22, 5,33,4545,58]
# numbers.sort()
# print(numbers[-1]-numbers[0])
#

# def addandsub(x,y):
#     if x>y:
#         return x-y
#     if x<y:
#         return x+y
# print(addandsub(3,2))

# def sub(a,b):
#    if a>b:
#        c=a-b
#    else:
#        c=b-a
#    return c
# # print(sub(9,109))
# print(sub(209,109))
