import random
import time
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_pratice2_model import Car_game, Base

# Database setup
engine = create_engine("sqlite:///guessgame.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

# Word list
words = [
    "dog", "cat", "house", "tree", "book",
    "chair", "table", "turtle", "water", "smile",
    "jump", "happy", "pencil", "flower", "rainbow",
    "family", "music", "candy", "cookie", "river",
    "mountain", "snow", "cloud", "window", "garden",
    "animal", "balloon", "banana", "orange", "purple",
    "friend", "school", "butterfly", "summer", "winter",
    "ocean", "planet", "rocket", "doctor", "robot"
]

# Draw the race track
def draw_track(position, target):
    track = ""
    for i in range(target + 1):
        track += "🚗" if i == position else "-"
    print(f"START |{track}| FINISH (目标: {target})")

# Main game
def car_game_main():
    player_name = input("请输入玩家名字: ")
    random.shuffle(words)
    car_pos = 0
    all_words = []
    error_words = []
    word_times = []

    # Ask user how many correct words are needed to finish (number of steps)
    while True:
        try:
            WIN_DISTANCE = int(input("请输入汽车需要前进多少步才能到达终点: "))
            if WIN_DISTANCE <= 0:
                print("请至少输入 1 步")
                continue
            break
        except ValueError:
            print("请输入有效数字")

    print(f"\n🏁 欢迎 {player_name}! 你需要拼对 {WIN_DISTANCE} 个单词才能到达终点!\n")

    for word in words:
        draw_track(car_pos, WIN_DISTANCE)
        print(f"\n请拼写这个单词: {word}")

        start_word = time.time()
        answer = input("你的答案: ")
        elapsed = round(time.time() - start_word, 2)

        all_words.append(word)
        word_times.append(elapsed)

        if answer.lower() == word:
            car_pos += 1
            print(f"✅ 拼写正确，汽车前进 1 步! 当前步数: {car_pos}/{WIN_DISTANCE}\n")
        else:
            error_words.append(word)
            print("❌ 拼写错误，汽车停住!\n")

        if car_pos >= WIN_DISTANCE:
            draw_track(car_pos, WIN_DISTANCE)
            print(f"\n🏆 恭喜 {player_name}! 你的汽车到达终点!\n")
            status = "WIN"
            break

    else:
        draw_track(car_pos, WIN_DISTANCE)
        print(f"\n⛔ 很遗憾 {player_name}, 你的汽车没有到达终点。\n")
        status = "LOSE"

    # Save record to database
    record = Car_game(
        player_name=player_name,
        status=status,
        words_spelled=json.dumps({
            "all_words": all_words,
            "error_words": error_words,
            "time_per_word": word_times
        }),
        all_words=json.dumps(all_words),
        error_count=len(error_words),
        time_taken=sum(word_times)
    )
    session.add(record)
    session.commit()

    return player_name, all_words, error_words, word_times, status, car_pos, WIN_DISTANCE

# Run standalone
if __name__ == "__main__":
    name, all_words, error_words, times, status, car_pos, WIN_DISTANCE = car_game_main()
    print("📁 游戏记录已保存到数据库!")
    print(f"⏱ 总用时: {sum(times)}s")
    print(f"📝 所有单词: {', '.join(all_words)}")
    print(f"❌ 错误单词: {', '.join(error_words)}")
    print(f"⚠️ 错误次数: {len(error_words)}")
    print(f"🚗 汽车最终步数: {car_pos}/{WIN_DISTANCE}")
    print(f"📊 游戏结果: {status}")
