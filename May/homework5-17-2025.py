import random

def guess(player_name):
    secret = random.randint(1, 100)
    guess_num = 0
    times = 0
    print(f"{player_name} 开始猜数字！")
    while guess_num != secret:
        guess_num = int(input(f"{player_name}，猜一个 1 到 100 的数字: "))
        times += 1
        if guess_num < secret:
            print("太小了。")
        elif guess_num > secret:
            print("太大了。")
        else:
            print("猜对了！")
    print(f"{player_name} 猜了 {times} 次。\n")
    return times

# 两位玩家开始比赛
duzi = int(input(f"这局的赌注为 $"))
frank_times = guess("Frank")
hulk_times = guess("Hulk")

# 比较结果
if frank_times < hulk_times:
    print(f"Frank 赢了！,hulk lost ${duzi}")
elif hulk_times < frank_times:
    print(f"Hulk 赢了！,frank lost ${duzi}")
else:
    print(f"平局！lili lost ${duzi}, frank and hulk take each ${duzi/2}")




# scores={
#     "Tom": [100, 98, 79],
#     "Alice": [85, 90, 88],
#     "Bob": [75, 80, 72],
#     "Lucy": [95, 92, 89],
#     "John": [60, 70, 65]
# }
# def Printscore(namescore, return_list=[]):
#     for k in namescore:
#         name = k
#         math = namescore.get(k)[0]
#         english = namescore.get(k)[1]
#         science = namescore.get(k)[2]
#         # print(f"xingming:{k}")
#         # print(f"math:    {namescore.get(k)[0]}")
#         # print(f"enlish:  {namescore.get(k)[1]}")
#         # print(f"science: {namescore.get(k)[2]}")
#         return_list.append((name, math, english, science))
#     return return_list
#
# def avgscore(scorelist):
#     for k in scorelist:
#         name = k[0]
#         scores = k[1:]
#         average = sum(scores) / len(scores)
#         print(f"name: {name} \naverage: {average:.2f}\n")
#
# print(Printscore(scores))
# (avgscore(Printscore(scores)))
#
#
#
