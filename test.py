from Matrix import *
from Network import *
import random

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
n = NeuralNetwork(2, 2, 1)

for i in range(50000):
    data = training_data[random.randint(0, len(training_data) - 1)]
    n.Train(data["inputs"], data["targets"])


guess = n.FeedForward([0, 0])
print(guess)
guess = n.FeedForward([0, 1])
print(guess)
guess = n.FeedForward([1, 1])
print(guess)
guess = n.FeedForward([1, 0])
print(guess)
