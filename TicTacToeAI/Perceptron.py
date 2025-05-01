import random
from random import randint
import math
from WeightsAndBiases import save_to_json
# Online Python - IDE, Editor, Compiler, Interpreter

def CreateRandomNestedList(Lists,Length):
    list = []
    NestedList = []
    for j in range(Lists):
        if j >= 1:
            NestedList.append(list)
        list = []
        for i in range(Length):
            list.append(random.randint(1,100)/100)

    return NestedList

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
'''
HiddenLayer1 = CreateRandomNestedList(18,9)
HiddenLayer2 = CreateRandomNestedList(18,18)
FinalLayer = CreateRandomNestedList(9,18)
BiasLayer1 = CreateRandomList(18)
BiasLayer2 = CreateRandomList(18)
FinalBias = CreateRandomList(9)
save_to_json(HiddenLayer1, HiddenLayer2, FinalLayer, BiasLayer1, BiasLayer2, FinalBias)
'''