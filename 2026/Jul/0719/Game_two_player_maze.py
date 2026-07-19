import random
import os
import time
import threading

import keyboard

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
            (2,0),
            (-2,0),
            (0,2),
            (0,-2)
        ]

        random.shuffle(directions)


        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                1 <= nx < WIDTH-1
                and 1 <= ny < HEIGHT-1
            ):

                if maze[ny][nx] == "#":

                    maze[y+dy//2][x+dx//2] = " "

                    carve(nx,ny)


    carve(1,1)

    maze[HEIGHT-2][WIDTH-2] = "E"

    return maze



def draw(maze, p1, p2, name1, name2):

    clear()

    for y in range(HEIGHT):

        line = ""

        for x in range(WIDTH):

            if p1 == [x,y] and p2 == [x,y]:
                line += "👥"

            elif p1 == [x,y]:
                line += "😀"

            elif p2 == [x,y]:
                line += "😎"

            elif maze[y][x] == "#":
                line += "█"

            elif maze[y][x] == "E":
                line += "🏁"

            else:
                line += " "

        print(line)


    print()
    print(f"😀 {name1}: WASD")
    print(f"😎 {name2}: Arrow Keys")



def move(player, dx, dy, maze):

    x,y = player

    nx = x + dx
    ny = y + dy


    if maze[ny][nx] != "#":

        player[0] = nx
        player[1] = ny



def player1_control(player, maze):

    while True:

        if keyboard.is_pressed("w"):
            move(player,0,-1,maze)
            time.sleep(.15)

        if keyboard.is_pressed("s"):
            move(player,0,1,maze)
            time.sleep(.15)

        if keyboard.is_pressed("a"):
            move(player,-1,0,maze)
            time.sleep(.15)

        if keyboard.is_pressed("d"):
            move(player,1,0,maze)
            time.sleep(.15)



def player2_control(player, maze):

    while True:

        if keyboard.is_pressed("up"):
            move(player,0,-1,maze)
            time.sleep(.15)

        if keyboard.is_pressed("down"):
            move(player,0,1,maze)
            time.sleep(.15)

        if keyboard.is_pressed("left"):
            move(player,-1,0,maze)
            time.sleep(.15)

        if keyboard.is_pressed("right"):
            move(player,1,0,maze)
            time.sleep(.15)



def main():

    clear()

    name1 = input("Player 1 name: ")
    name2 = input("Player 2 name: ")


    input("\nPress ENTER to start...")


    # ONE maze only
    maze = generate_maze()


    # Same starting position
    p1 = [1,1]
    p2 = [1,1]


    goal = [
        WIDTH-2,
        HEIGHT-2
    ]


    start_time = time.time()


    threading.Thread(
        target=player1_control,
        args=(p1,maze),
        daemon=True
    ).start()


    threading.Thread(
        target=player2_control,
        args=(p2,maze),
        daemon=True
    ).start()



    while True:

        draw(
            maze,
            p1,
            p2,
            name1,
            name2
        )


        if p1 == goal:

            winner = name1
            loser = name2
            break


        if p2 == goal:

            winner = name2
            loser = name1
            break


        time.sleep(.05)



    time_used = round(
        time.time() - start_time,
        2
    )


    print(
        f"\n🎉 {winner} wins!"
    )


    Maze_record(
        player_name=winner,
        game_type="Two Player",
        opponent_name=loser,
        steps=0,
        time_used=time_used,
        winner=winner,
        status="Win"
    ).add_info()



if __name__ == "__main__":
    main()