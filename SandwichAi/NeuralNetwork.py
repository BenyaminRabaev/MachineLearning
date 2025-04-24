from Perceptron import Perceptron
from Perceptron import CreateRandomList
from SandwichCreator import CreateSandwich
from SandwichValues import Ingredients, IngredientsValues, HiddenLayer1, HiddenLayer2,FinalLayer, save_to_json
import random




def NeuralNetwork():
    v = []
    Layer1 = []
    Layer2 = []
    FL = []
    for i in range(len(Ingredients)):
        v.append(IngredientsValues[Ingredients[i]])
    for i in range(16):
        b = random.randint(1,10) / 1000
        w = HiddenLayer1[i]
        Layer1.append(Perceptron.NewPerceptron(w,v,b))
    for i in range(7):
        b = random.randint(1,10) /1000
        w = HiddenLayer2[i]
        Layer2.append(Perceptron.NewPerceptron(w,Layer1,b))
    FL.append(Perceptron.NewPerceptron(FinalLayer,Layer2,b))
    



    



'''
Visual Representation of Neural Network
x       X
        X       X
x       X
        X       X
x       X
        X       X   X
x       X
        X       X
x       X
        X       X   X
x       X
        X       X
x       X
        X       X
x       X
'''