import time
import random
import sys
from colorama import init
from add_record_to_db import *
from class_pratice2_model import *
import json
from datetime import datetime



def generate_times(num, total=30):
    """
    生成每匹马的赛程时间，总和固定为 total
    返回：
        arr2: 每匹马的赛程时间列表
        game_info: 每匹马编号和时间的元组列表
    """
    base = total / num
    arr = [base + random.uniform(-1, 1) for _ in range(num)]  # 添加扰动
    s = sum(arr)
    arr2 = [round(t * total / s, 2) for t in arr]  # 缩放总和为 total，保留两位小数
    game_info = list(zip(range(1, num + 1), arr2))  # 每匹马编号从1开始
    return arr2, game_info

def render_bar(p, bar_len=100):
    """
    绘制赛马进度条
    p: 进度百分比（0~1）
    bar_len: 条长度
    """
    filled = int(p * bar_len)
    return "-" * (bar_len - filled) + "🐟" + "=" * filled

def race_animation(num_horses, CIRCLE, race_times):
    """
    跑马动画，返回获胜马号
    race_times: 每匹马的赛程时间
    """
    start_time = time.time()
    progress = [0] * num_horses
    finished = [False] * num_horses
    winner = None

    # 先打印num_horses行空行，为覆盖动画做准备
    for _ in range(num_horses):
        print()

    while True:
        # 光标上移num_horses行，覆盖之前的进度
        sys.stdout.write(f"\033[{num_horses}A")
        sys.stdout.flush()
        all_done = True

        for i in range(num_horses):
            if not finished[i]:
                # 计算当前进度
                pct = (time.time() - start_time) / race_times[i]
                if pct >= 1:
                    pct = 1
                    finished[i] = True
                    if winner is None:
                        winner = i + 1  # 第一个完成的马就是胜者
                progress[i] = pct

            # 绘制进度条
            bar = render_bar(progress[i])
            percent = int(progress[i] * 100)
            sys.stdout.write(f"{CIRCLE[i]} {bar} {percent:3}%\n")
            sys.stdout.flush()

            if not finished[i]:
                all_done = False

        if all_done:
            break
        time.sleep(0.07)  # 控制刷新速度

    print(f"\n🏆 胜者：{CIRCLE[winner-1]}")
    return winner

def fish_bet(num_horses):
    """
    获取玩家下注信息
    返回：
        name: 玩家名字
        amount: 下注金额
        choice: 押注马编号
    """
    name = input("请输入玩家名字：")

    # 输入金额
    while True:
        try:
            amount = int(input(f"{name}，请输入下注金额："))
            if amount <= 0:
                print("金额必须大于0，请重新输入。")
                continue
            break
        except ValueError:
            print("请输入有效数字金额。")

    # 输入押注马编号
    while True:
        try:
            choice = int(input(f"{name}，请选择押注的马（1-{num_horses}）："))
            if 1 <= choice <= num_horses:
                break
            else:
                print(f"请输入 1 到 {num_horses} 之间的数字。")
        except ValueError:
            print("请输入有效数字。")

    return name, amount, choice

def race_result(player_name, bet_amount, horse_choice, winner):
    """
    根据赢家判断玩家输赢
    返回：
        win_amount: 赢或输的金额（输为负数）
        status: 'You Win' 或 'You Lose'
    """
    if horse_choice == winner:
        win_amount = bet_amount * 2  # 赢了翻倍
        status = "Win"
    else:
        win_amount = -bet_amount  # 输了扣掉金额
        status = "Lose"

    print(f"{player_name} You {status}，金额变化: {win_amount}")
    return win_amount, status

def fish_main():
    # 初始化 colorama（Windows 需要，用于支持光标控制）
    init()
    num_horses = 6
    CIRCLE = [f"({i+1})" for i in range(num_horses)]

    # 玩家下注
    player_name, bet_amount, horse_choice = fish_bet(num_horses)

    # 生成赛程时间和信息
    race_times, game_info = generate_times(num_horses)

    # 跑马动画并返回胜者
    winner = race_animation(num_horses, CIRCLE, race_times)

    # 判断玩家输赢
    win_amount, status = race_result(player_name, bet_amount, horse_choice, winner)

    # 排名（按时间排序）
    rankings = sorted(game_info, key=lambda x: x[1])
    winner_house = rankings[0][0]
    winner_house_time = rankings[0][1]
    ranking_list = [horse for horse, _ in rankings]  # <-- 新增这一行

    before_balance = Truck_record.get_latest_balance(player_name)
    balance = before_balance + win_amount
    print(f"{player_name} balance : {balance}")
    # 保存记录                          balance
    Fish_record(player_name,bet_amount,balance,horse_choice,win_amount,winner_house, winner_house_time, ranking_list, game_info, status).add_info()

if __name__ == "__main__":
    fish_main()