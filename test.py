from Matrix import *
from Network import *

n = NeuralNetwork(2, 2, 2)
inputs = [1, 0]
# output = [n.FeedForward(input)]
targets = [1, 0]
n.Train(inputs, targets, True)
# print(output)

training data = [
    {
    "inputs": [0, 1],
    "targets": [1]
    },
    {
    "inputs": [0, 0],
    "targets": [0]
    },
    {
    "inputs": [1, 0],
    "targets": [1]
    },
    {
    "inputs": [1, 1],
    "targets": [0]
    },
]
