import random
import time



def MakeAMoveX(PossibleOptions,Board):

    w = 0
    x = random.randint(1,len(PossibleOptions)) -1
    Board[PossibleOptions[x]-1] = 0.5
    if Board[0] == 0.5 and Board[1] == 0.5 and Board[2] == 0.5 or Board[2] == 0.5 and Board[5] == 0.5 and Board[8] or Board[0] == 0.5 and Board[3] == 0.5 and Board[6] == 0.5 or Board[0] == 0.5 and Board[4] == 0.5 and Board[8] == 0.5 or Board[6] == 0.5 and Board[7] == 0.5 and Board[8] == 0.5 or Board[6] == 0.5 and Board[4] == 0.5 and Board[2] == 0.5:
        w = 1
    PossibleOptions.pop(x)
    return PossibleOptions, Board, w
def MakeAMoveO(PossibleOptions, Board):
    w = 0
    if Board[0] == 1 and Board[1] == 1 and Board[2] == 1 or Board[2] == 1 and Board[5] == 1 and Board[8] or Board[0] == 1 and Board[3] == 1 and Board[6] == 1 or Board[0] == 1 and Board[4] == 1 and Board[8] == 1 or Board[6] == 1 and Board[7] == 1 and Board[8] == 1 or Board[6] == 1 and Board[4] == 1 and Board[2] == 1:
        w = 1
    x = random.randint(1,len(PossibleOptions)) -1
    Board[PossibleOptions[x]-1] = 1
    PossibleOptions.pop(x)
    return PossibleOptions, Board, w


'''
def SimulateGame():
    Board = ["0",   "0",    "0", 
            
                "0",   "0",    "0",
    
                "0",   "0",    "0"]
    PossibleOptions = [1,2,3,4,5,6,7,8,9]
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
SimulateGame()
'''


