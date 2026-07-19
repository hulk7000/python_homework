import random
import os
import time

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

                    maze[y + dy//2][x + dx//2] = " "

                    carve(nx, ny)


    carve(1, 1)

    maze[HEIGHT-2][WIDTH-2] = "E"

    return maze



def draw(maze, player, username):

    clear()

    for y in range(HEIGHT):

        line = ""

        for x in range(WIDTH):

            if [x,y] == player:
                line += "😀"

            elif maze[y][x] == "#":
                line += "█"

            elif maze[y][x] == "E":
                line += "🏁"

            else:
                line += " "

        print(line)


    print()
    print(f"Player: {username}")
    print("W A S D = Move")
    print("Q = Quit")



def move(player, key, maze):

    x,y = player


    moves = {

        "w": (0,-1),
        "s": (0,1),
        "a": (-1,0),
        "d": (1,0)

    }


    if key not in moves:
        return player


    dx,dy = moves[key]


    nx = x + dx
    ny = y + dy


    if maze[ny][nx] != "#":

        return [nx,ny]


    return player



def main():

    clear()


    username = input(
        "Enter your username: "
    )


    # ONE maze only
    maze = generate_maze()


    player = [1,1]


    goal = [
        WIDTH-2,
        HEIGHT-2
    ]


    steps = 0


    start_time = time.time()



    while True:


        draw(
            maze,
            player,
            username
        )


        if player == goal:

            time_used = round(
                time.time() - start_time,
                2
            )


            print(
                f"\n🎉 {username} escaped!"
            )

            print(
                "Steps:",
                steps
            )

            print(
                "Time:",
                time_used,
                "seconds"
            )


            Maze_record(
                player_name=username,
                game_type="Single Player",
                steps=steps,
                time_used=time_used,
                winner=username,
                status="Win"
            ).add_info()


            break



        key = input(
            "\nMove: "
        ).lower()



        if key == "q":

            print("Game ended.")

            Maze_record(
                player_name=username,
                game_type="Single Player",
                steps=steps,
                time_used=round(
                    time.time()-start_time,
                    2
                ),
                winner="None",
                status="Quit"
            ).add_info()

            break



        new_position = move(
            player,
            key,
            maze
        )


        if new_position != player:
            steps += 1


        player = new_position




if __name__ == "__main__":
    main()