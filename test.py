from Matrix import *
from Network import *

n = NeuralNetwork(2, 2, 2)
inputs = [1, 0]
# output = [n.FeedForward(input)]
targets = [1, 0]
n.Train(inputs, targets)
# print(output)
