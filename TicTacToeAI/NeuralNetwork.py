from Perceptron import Perceptron
from WeightsAndBiases import  HiddenLayer1, HiddenLayer2,FinalLayer, save_to_json, BiasLayer1, BiasLayer2,FinalBias
from TicTacToe import MakeAMoveO,MakeAMoveX
import math
def Sigmoid(input):
    return(1 / (math.exp(input)))
def SigmoidDerivate(input):
    return input * (1-input)
def ForwardPass(Board, HiddenLayer1, HiddenLayer2,FinalLayer, BiasLayer1, BiasLayer2,FinalBias):
    NewHiddenLayer1 = []
    NewHiddenLayer2 = []
    NewFinalLayer = []
    for i in range(18):
        NewHiddenLayer1.append(Sigmoid(Perceptron.PerceptronValue(HiddenLayer1[i],Board,BiasLayer1[i])))
    for i in range(18):
        NewHiddenLayer2.append(Sigmoid(Perceptron.PerceptronValue(HiddenLayer2[i],NewHiddenLayer1,BiasLayer2[i])))
    for i in range(9):
        NewFinalLayer.append(Sigmoid(Perceptron.PerceptronValue(FinalLayer[i],NewHiddenLayer2,FinalBias[i])))
        return NewFinalLayer

'''
Visual Representation of Neural Network
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X
X       X       X       X
        X       X

'''