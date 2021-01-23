from Matrix import *
from Network import *
import random

# example data
training_data = [
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

# initialize a NeuralNetwork with NeuralNetwork(number of inputs, number of hidden layers nodes, number of outputs node)
neuron = NeuralNetwork(2, 2, 1)

# train the NeuralNetwork with the Example data above
for i in range(50000):
    data = training_data[random.randint(0, len(training_data) - 1)]
    neuron.Train(data["inputs"], data["targets"])


# try the Neural Network
guess = neuron.FeedForward([0, 0])
print(guess)
guess = neuron.FeedForward([0, 1])
print(guess)
guess = neuron.FeedForward([1, 1])
print(guess)
guess = neuron.FeedForward([1, 0])
print(guess)
