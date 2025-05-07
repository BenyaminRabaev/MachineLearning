import random
import time



def MakeAMoveX(PossibleOptions,Board):
    x = random.randint(1,len(PossibleOptions)) -1
    Board[PossibleOptions[x]-1] = 0.5

    PossibleOptions.pop(x)
    return PossibleOptions, Board
def MakeAMoveO(PossibleOptions, Board):

    x = random.randint(1,len(PossibleOptions)) -1
    Board[PossibleOptions[x]-1] = 1
    PossibleOptions.pop(x)
    return PossibleOptions, Board
def CheckWinner(Board):
    w = 0
    if Board[0] == 1 and Board[1] == 1 and Board[2] == 1 or Board[2] == 1 and Board[5] == 1 and Board[8] or Board[0] == 1 and Board[3] == 1 and Board[6] == 1 or Board[0] == 1 and Board[4] == 1 and Board[8] == 1 or Board[6] == 1 and Board[7] == 1 and Board[8] == 1 or Board[6] == 1 and Board[4] == 1 and Board[2] == 1:
        w = 1
    if Board[0] == 0.5 and Board[1] == 0.5 and Board[2] == 0.5 or Board[2] == 0.5 and Board[5] == 0.5 and Board[8] or Board[0] == 0.5 and Board[3] == 0.5 and Board[6] == 0.5 or Board[0] == 0.5 and Board[4] == 0.5 and Board[8] == 0.5 or Board[6] == 0.5 and Board[7] == 0.5 and Board[8] == 0.5 or Board[6] == 0.5 and Board[4] == 0.5 and Board[2] == 0.5:
        w = 1
    return w



