import time
from os import system

game1=[0,1,2,3,4,5,6,7,8]
player1=""
player2=""
while True:
    player1=input("Player1 please choose X or O: ").upper()
    if player1 == 'X':
        player2='O'
        break
    elif player1 == 'O':
        player2='X'
        break
    else:
        print(f"\nPlayer1 entered incorrect value...\n")
        continue
    print(f"\nPlayer1 is {player1} and Player2 is {player2}")

def print_game1():
    print()
    print(f" {game1[0]} | {game1[1]} | {game1[2]}")
    print(" .........")
    print(f" {game1[3]} | {game1[4]} | {game1[5]}")
    print(" .........")
    print(f" {game1[6]} | {game1[7]} | {game1[8]}")
    print()

def check_game1(x_or_o):
    if set(game1[0:3]) == {x_or_o} or set(game1[3:6]) == {x_or_o} or set(game1[6:9]) == {x_or_o}:
        return "WIN"
    elif set([game1[0],game1[3],game1[6]]) == {x_or_o} or set([game1[1],game1[4],game1[7]]) == {x_or_o} or set([game1[2],game1[5],game1[8]]) == {x_or_o}:
        return "WIN"
    elif set([game1[0],game1[4],game1[8]]) == {x_or_o} or set([game1[2],game1[4],game1[6]]) == {x_or_o}:
        return "WIN"
    elif set(game1) == {'O','X'}:
        return "NOWIN"

turn="Player1"
while True:
    print_game1()

    choice=input(f"{turn} choose the number from the above cells: ")
    system('cls')
    if choice in ['0','1','2','3','4','5','6','7','8']:
        choice=int(choice)
    else:
        print(f"\n{turn} value not matched cell value.\n")
        continue

    if game1[choice] == 'O' or game1[choice] == 'X':
        print(f"\nCell {choice} is not empty. Try again...\n")
        continue
    else:
        if turn == "Player1":
            game1[choice]=player1
            status=check_game1(player1)
            if status == "WIN":
                print("\n***** Player1 is the winner *****")
                print_game1()
                time.sleep(10)
                break
            turn="Player2"
        else:
            game1[choice]=player2
            status=check_game1(player2)
            if status == "WIN":
                print("\n***** Player2 is the winner *****")
                print_game1()
                time.sleep(10)
                break
            turn="Player1"

        if status == "NOWIN":
            print("\n***** No one is the winner *****\n")
            print_game1()
            time.sleep(10)
            break
