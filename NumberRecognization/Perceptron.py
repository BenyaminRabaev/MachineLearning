import random
from random import randint
import math
from WeightsAndValues import save_to_json
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
        

HiddenLayer1=CreateRandomNestedList(128,784)
HiddenLayer2=CreateRandomNestedList(128,128)
FinalLayer=CreateRandomNestedList(10,128)
BiasLayer1 = CreateRandomList(128)
BiasLayer2 = CreateRandomList(128)
FinalBias = CreateRandomList(10)

#784 inputs
#128 Neurons, 784 weights
#128 Neurons, 128 weights
#10 Neurons, 128 weights

save_to_json(HiddenLayer1,HiddenLayer2,FinalLayer,BiasLayer1,BiasLayer2,FinalBias)