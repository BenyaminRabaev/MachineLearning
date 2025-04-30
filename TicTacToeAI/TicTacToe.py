import random
import time

Board = ["0",   "0",    "0", 
        
            "0",   "0",    "0",

            "0",   "0",    "0"]
PossibleOptions = [1,2,3,4,5,6,7,8,9]

def MakeAMoveX(PossibleOptions,Board):
    w = 0
    x = random.randint(1,len(PossibleOptions)) -1
    Board[PossibleOptions[x]-1] = "X"
    if Board[0] == "X" and Board[1] == "X" and Board[2] == "X" or Board[2] == "X" and Board[5] == "X" and Board[8] or Board[0] == "X" and Board[3] == "X" and Board[6] == "X" or Board[0] == "X" and Board[4] == "X" and Board[8] == "X" or Board[6] == "X" and Board[7] == "X" and Board[8] == "X" or Board[6] == "X" and Board[4] == "X" and Board[2] == "X":
        w = 1
    PossibleOptions.pop(x)
    return PossibleOptions, Board, w
def MakeAMoveO(PossibleOptions, Board):
    w = 0
    if Board[0] == "O" and Board[1] == "O" and Board[2] == "O" or Board[2] == "O" and Board[5] == "O" and Board[8] or Board[0] == "O" and Board[3] == "O" and Board[6] == "O" or Board[0] == "O" and Board[4] == "O" and Board[8] == "O" or Board[6] == "O" and Board[7] == "O" and Board[8] == "O" or Board[6] == "O" and Board[4] == "O" and Board[2] == "O":
        w = 1
    x = random.randint(1,len(PossibleOptions)) -1
    Board[PossibleOptions[x]-1] = "X"
    PossibleOptions.pop(x)
    return PossibleOptions, Board, w

x,Board,w= MakeAMoveO(PossibleOptions, Board)
for i in range(4):
    z,Board,w =MakeAMoveX(x,Board)
    print(print('\n',Board[0],Board[1],Board[2],'\n',Board[3], Board[4],Board[5],'\n',Board[6],Board[7],Board[8]))
    if w == 1:
        print("Player2 wins!")
        break
    x,Board,w= MakeAMoveO(z, Board)
    print(print('\n',Board[0],Board[1],Board[2],'\n',Board[3], Board[4],Board[5],'\n',Board[6],Board[7],Board[8]))
    if w == 1:
        print("Player1 wins!")
        break
























'''
print("you are O")
for i in range(4,0,-1):
    Move = input("Where would you like to move")
    Board[int(Move)-1] = "O"
    print('\n',Board[0],Board[1],Board[2],'\n',Board[3], Board[4],Board[5],'\n',Board[6],Board[7],Board[8])
    if Board[0] == "O" and Board[1] == "O" and Board[2] == "O" or Board[2] == "O" and Board[5] == "O" and Board[8] or Board[0] == "O" and Board[3] == "O" and Board[6] == "O" or Board[0] == "O" and Board[4] == "O" and Board[8] == "O" or Board[6] == "O" and Board[7] == "O" and Board[8] == "O" or Board[6] == "O" and Board[4] == "O" and Board[2] == "O":
        print("Player1 Wins!")
        break


    PossibleOptions.remove(int(Move))
    time.sleep(1)
    print("My Turn!")
    x = random.randint(1,len(PossibleOptions)) -1
    print(x)
    print(PossibleOptions)

    Board[PossibleOptions[x]-1] = "X"
    if Board[0] == "X" and Board[1] == "X" and Board[2] == "X" or Board[2] == "X" and Board[5] == "X" and Board[8] or Board[0] == "X" and Board[3] == "X" and Board[6] == "X" or Board[0] == "X" and Board[4] == "X" and Board[8] == "X" or Board[6] == "X" and Board[7] == "X" and Board[8] == "X" or Board[6] == "X" and Board[4] == "X" and Board[2] == "X":
        print("Player1 Wins!")
        break   
    PossibleOptions.pop(x)
    print('\n',Board[0],Board[1],Board[2],'\n',Board[3], Board[4],Board[5],'\n',Board[6],Board[7],Board[8])
    time.sleep(0.5)


Board[int(Move)-1] = "O"
print('\n',Board[0],Board[1],Board[2],'\n',Board[3], Board[4],Board[5],'\n',Board[6],Board[7],Board[8])

'''