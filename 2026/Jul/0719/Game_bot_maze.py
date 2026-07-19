import random
import os
import time
from collections import deque

from DB_database import Maze_record


WIDTH = 21
HEIGHT = 9


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def generate_maze():

    maze = [["#" for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def carve(x, y):

        maze[y][x] = " "

        directions = [
            (2, 0),
            (-2, 0),
            (0, 2),
            (0, -2)
        ]

        random.shuffle(directions)

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                1 <= nx < WIDTH - 1
                and 1 <= ny < HEIGHT - 1
            ):

                if maze[ny][nx] == "#":

                    maze[y + dy // 2][x + dx // 2] = " "

                    carve(nx, ny)


    carve(1, 1)

    maze[HEIGHT - 2][WIDTH - 2] = "E"

    return maze



def draw(maze, bot):

    clear()

    for y in range(HEIGHT):

        line = ""

        for x in range(WIDTH):

            if [x, y] == bot:
                line += "🤖"

            elif maze[y][x] == "#":
                line += "█"

            elif maze[y][x] == "E":
                line += "🏁"

            else:
                line += " "

        print(line)

    print("\n🤖 Bot solving maze...")



def find_path(maze):

    start = (1, 1)

    end = (
        WIDTH - 2,
        HEIGHT - 2
    )


    queue = deque()

    queue.append(
        (start, [])
    )


    visited = {start}


    moves = [
        (0, -1, "W"),
        (0, 1, "S"),
        (-1, 0, "A"),
        (1, 0, "D")
    ]


    while queue:

        (x, y), path = queue.popleft()


        if (x, y) == end:
            return path


        for dx, dy, key in moves:

            nx = x + dx
            ny = y + dy


            if (
                0 <= nx < WIDTH
                and 0 <= ny < HEIGHT
                and maze[ny][nx] != "#"
                and (nx, ny) not in visited
            ):

                visited.add(
                    (nx, ny)
                )


                queue.append(
                    (
                        (nx, ny),
                        path + [key]
                    )
                )


    return []



def move_bot(bot, key):

    x, y = bot


    if key == "W":
        y -= 1

    elif key == "S":
        y += 1

    elif key == "A":
        x -= 1

    elif key == "D":
        x += 1


    return [x, y]



def main():

    # Automatic username
    username = "Bot"


    # Generate ONE maze
    maze = generate_maze()


    bot = [1, 1]


    # Find path in this same maze
    path = find_path(maze)


    print("🤖 Bot found a path!")

    time.sleep(2)


    start_time = time.time()

    steps = 0


    for move in path:

        bot = move_bot(
            bot,
            move
        )

        steps += 1


        draw(
            maze,
            bot
        )


        print(
            "Bot pressed:",
            move
        )


        time.sleep(0.3)



    time_used = round(
        time.time() - start_time,
        2
    )


    print("\n🎉 Bot escaped!")

    print(
        "Steps:",
        steps
    )

    print(
        "Time:",
        time_used,
        "seconds"
    )


    # Save to database
    Maze_record(
        player_name=username,
        game_type="Bot",
        steps=steps,
        time_used=time_used,
        winner=username,
        status="Completed"
    ).add_info()



if __name__ == "__main__":
    main()