from NeuralNetwork import ForwardPass
from WeightsAndBiases import  HiddenLayer1, HiddenLayer2,FinalLayer, save_to_json, BiasLayer1, BiasLayer2,FinalBias
Board = [0,   0,    0, 
        
            0,   0,    0,

            0,   0,    0]
print(ForwardPass(Board,HiddenLayer1, HiddenLayer2,FinalLayer, BiasLayer1, BiasLayer2,FinalBias))