import random
from random import randint
import math
# Online Python - IDE, Editor, Compiler, Interpreter

def CreateRandomList(Length):
    list = []
    for i in range(Length):
        list.append(random.randint(1,100)/100)
    return list
    
class Perceptron:   
    def PerceptronValue(Weights, Values, Bias):
        for i in range(len(Weights)):
            x = Weights[i] * Values[i]
            x = x +  Bias
            x = 1 / (1  + math.exp(-x))
        return x
        

