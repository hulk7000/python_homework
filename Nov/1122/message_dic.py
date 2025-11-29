# message_dic = {
#     "greetings":[
#         "✨ Welcome, brave adventurer!",
#         "🧙‍♂️ Greetings, wizard of numbers!",
#         "🌟 Hello, superstar coder!",
#         "🐉 Are you ready to face the number dragon?"
#     ],
#     "start_message":[
#         "I'm thinking of a number between 1 and 100...",
#         "Type 'answer' anytime to reveal the secret number! 👀"
#     ],
#     "hints_low":[
#         "Too low! Aim higher! 🔼",
#         "Nope, that's small. Try a bigger number!",
#         "You're below the magic number!"
#     ],
#     "hints_high":[
#         "Too high! Go lower! 🔽",
#         "Woah! That’s too big!",
#         "The magic number is smaller!"
#     ],
#     "win_messages":[
#         "🎉 You did it! You're a number genius!",
#         "🏆 Victory! You cracked the code!",
#         "✨ Amazing! You guessed the secret number!",
#         "🐱‍🏍 Boom! You win!"
#     ]
# }

from add_record_to_db import Add_message

message_dic = {
    "greetings": [
        "✨ Welcome, brave adventurer!",
        "🧙‍♂️ Greetings, wizard of numbers!",
        "🌟 Hello, superstar coder!",
        "🐉 Are you ready to face the number dragon?"
    ],
    "start_message": [
        "I'm thinking of a number between 1 and 100...",
        "Type 'answer' anytime to reveal the secret number! 👀"
    ],
    "hints_low": [
        "Too low! Aim higher! 🔼",
        "Nope, that's small. Try a bigger number!",
        "You're below the magic number!"
    ],
    "hints_high": [
        "Too high! Go lower! 🔽",
        "Woah! That’s too big!",
        "The magic number is smaller!"
    ],
    "win_messages": [
        "🎉 You did it! You're a number genius!",
        "🏆 Victory! You cracked the code!",
        "✨ Amazing! You guessed the secret number!",
        "🐱‍🏍 Boom! You win!"
    ]
}
if __name__ == '__main__':
    for k, v in message_dic.items():
        for i, message in enumerate(v):  # 遍历每个列表元素，i 是索引，message 是内容
            print(f"{k}, {message}")  # 打印键和值
            msg = Add_message(k, message)
            msg.add_content()
