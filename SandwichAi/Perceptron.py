import random
from random import randint
# Online Python - IDE, Editor, Compiler, Interpreter

def CreateRandomList(Length):
    list = []
    for i in range(Length):
        list.append(random.randint(1,100)/100)
    return list
    
class Perceptron:   
    def NewPerceptron(Weights, Values, Bias):
        y = 0  + Bias
        for i in range(4):
            x = Weights[i - 1] * Values[i-1]
            y = y + x
        return y 
        

