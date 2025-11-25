import sqlite3

message_dic = {
    "greetings":[
        "✨ Welcome, brave adventurer!",
        "🧙‍♂️ Greetings, wizard of numbers!",
        "🌟 Hello, superstar coder!",
        "🐉 Are you ready to face the number dragon?"
    ],
    "start_message":[
        "I'm thinking of a number between 1 and 100...",
        "Type 'answer' anytime to reveal the secret number! 👀"
    ],
    "hints_low":[
        "Too low! Aim higher! 🔼",
        "Nope, that's small. Try a bigger number!",
        "You're below the magic number!"
    ],
    "hints_high":[
        "Too high! Go lower! 🔽",
        "Woah! That’s too big!",
        "The magic number is smaller!"
    ],
    "win_messages":[
        "🎉 You did it! You're a number genius!",
        "🏆 Victory! You cracked the code!",
        "✨ Amazing! You guessed the secret number!",
        "🐱‍🏍 Boom! You win!"
    ]
}