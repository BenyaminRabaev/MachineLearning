from Perceptron import Perceptron
from WeightsAndValues import HiddenLayer1, HiddenLayer2,FinalLayer, save_to_json, BiasLayer1, BiasLayer2,FinalBias
from GetNumbers import Data
import math
import random


def SigmoidActivationFunction(input_value):
    return 1 / (1 + math.exp(-input_value))
def MeanSquareError(true_output, predicted_output):
    return (1/2) * (true_output - predicted_output) ** 2

def GetInput(i,x,y):
    Greyscale,Label = Data.GetImage(i,x,y)
    return Greyscale,Label
def ForwardPass(HiddenLayer1,HiddenLayer2,FinalLayer,Bias1,Bias2,FinalBias):
    x,y = Data.LoadData()
    Layer1 = []
    Layer2 = []
    FinalList = []
    v = GetInput(1,x,y)
    for i in range(128):
        Layer1.append(SigmoidActivationFunction(Perceptron.PerceptronValue(HiddenLayer1[i-1],v[0],Bias1[i])))
    for i in range(128):
        Layer2.append(SigmoidActivationFunction(Perceptron.PerceptronValue(HiddenLayer2[i-1],Layer1,Bias2[i])))
    for i in range(10):
        FinalList.append(SigmoidActivationFunction(Perceptron.PerceptronValue(FinalLayer[i-1],Layer2,FinalBias[i])))
    return FinalList

def PickedNumber(Inputs):
    x = Inputs.copy()
    Inputs.sort()
    for i in range(10):
        if Inputs[9] == x[i]:
            return i
def True_Output(Number):
    list = []
    for i in range(10):
        if i == Number:
            list.append(1)
        else:
            list.append(0)

    

def pdLoss(true_output, predicted_output):
    return [predicted_output[i] - true_output[i] for i in range(10)]

def pdLossToWeights(input_list, derivative_Loss_with_respect_to_z):
    return [[derivative_Loss_with_respect_to_z * input_value for input_value in sublist] for sublist in input_list]

def pdLossToBiases(input_list, derivative_Loss_with_respect_to_z):
    return [derivative_Loss_with_respect_to_z * input_value for input_value in input_list]
'''
def UpdateWeightsWithGradient(weight_list, gradient_list, learning_rate):
    updated_weights = []
    for i in range(len(weight_list)):
        sub_weights = []
        for j in range(len(weight_list[i])):
            new_weight = weight_list[i][j] - learning_rate * gradient_list[i][j]
            sub_weights.append(new_weight)
        updated_weights.append(sub_weights)
    return updated_weights
def UpdateBiasesWithGradient(bias_list, gradient_list, learning_rate):
    updated_biases = []
    for i in range(len(bias_list)):
        updated_bias = bias_list[i] - learning_rate * gradient_list[i]
        updated_biases.append(updated_bias)
    return updated_biases

def GradientDescent(Sandwich):
    Weights1 = HiddenLayer1
    Weights2 = HiddenLayer2
    Weights3 = FinalLayer
    Bias1 = BiasLayer1
    Bias2 = BiasLayer2
    Bias3 = FinalBias
    LearningRate = 0.01  
    Total_Epochs = 1000000
    CorrectSandwiches = 0
    for epochs in range(Total_Epochs):
        Sandwich = CreateSandwich()
        true_output = SigmoidActivationFunction(EvaluateSandwich(Sandwich))
        v = []
        for ingredient in Ingredients:
            if ingredient in Sandwich.ingredients:
                v.append(1)
            else:
                v.append(0)
        z1 = [Perceptron.PerceptronValue(Weights1[i], v, Bias1[i]) for i in range(16)]
        a1 = [SigmoidActivationFunction(z) for z in z1]
        z2 = [Perceptron.PerceptronValue(Weights2[i], a1, Bias2[i]) for i in range(7)]
        a2 = [SigmoidActivationFunction(z) for z in z2]
        z3 = Perceptron.PerceptronValue(Weights3[0], a2, Bias3[0])
        predicted_output = SigmoidActivationFunction(z3)
        loss = MeanSquareError(true_output, predicted_output)
        delta3 = (predicted_output - true_output) * pdSigmoid(predicted_output)
        grad_w3 = [[delta3 * a for a in a2]]
        grad_b3 = [delta3]
        delta2 = [delta3 * Weights3[0][j] * pdSigmoid(a2[j]) for j in range(7)]
        grad_w2 = [[delta2[i] * a for a in a1] for i in range(7)]
        grad_b2 = delta2
        delta1 = [sum(delta2[k] * Weights2[k][i] for k in range(7)) * pdSigmoid(a1[i]) for i in range(16)]
        grad_w1 = [[delta1[i] * inp for inp in v] for i in range(16)]
        grad_b1 = delta1
        Weights1 = UpdateWeightsWithGradient(Weights1, grad_w1, LearningRate)
        Weights2 = UpdateWeightsWithGradient(Weights2, grad_w2, LearningRate)
        Weights3 = UpdateWeightsWithGradient(Weights3, grad_w3, LearningRate)
        Bias1 = UpdateBiasesWithGradient(Bias1, grad_b1, LearningRate)
        Bias2 = UpdateBiasesWithGradient(Bias2, grad_b2, LearningRate)
        Bias3 = UpdateBiasesWithGradient(Bias3, grad_b3, LearningRate)
        if epochs % 10000 == 0:
            print(f"Epoch {epochs}: MeanLoss = {loss}: TrueLoss = {true_output-predicted_output}")

        if true_output - predicted_output < 0.1 and true_output-predicted_output > -0.1:
            CorrectSandwiches += 1
        

    print("Final Prediction:", predicted_output)
    print("Final Weights:", Weights3)
    print("Final Bias:", Bias3)
    print("Correct Sandwiches,",CorrectSandwiches)
'''


x = ForwardPass(HiddenLayer1,HiddenLayer2,FinalLayer,BiasLayer1,BiasLayer2,FinalBias)
print(PickedNumber(x))

'''
Visual Representation of Neural Network
x       X
        X       X
x       X
        X       X
x       X
        X       X   
x       X
        X       X       x
x       X
        X       X   
x       X
        X       X
x       X
        X       X
x       X
'''