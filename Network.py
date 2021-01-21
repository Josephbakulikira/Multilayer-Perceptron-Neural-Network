from Matrix import *
import math

def Sigmoid(x):
    return 1 / (1 + math.exp(-x))

class NeuralNetwork:
    def __init__(self, n_inputs, n_hiddenLayers, n_outputs):
        self.input_layers = n_inputs
        self.hidden_layers = n_hiddenLayers
        self.output_layers = n_outputs

        self.hiddenInputWeights = Matrix(self.hidden_layers, self.input_layers)
        self.hiddenInputWeights.randomize()
        self.hiddenOutputWeights = Matrix(self.output_layers, self.hidden_layers)
        self.hiddenOutputWeights.randomize()

        self.hiddenBias = Matrix(self.hidden_layers, 1)
        self.hiddenBias.randomize()
        self.outputBias = Matrix(self.output_layers, 1)
        self.outputBias.randomize()



    def FeedForward(self, inputs):
        inputs = Matrix.fromArray(inputs)

        hidden = Matrix.matrix_multiplication(self.hiddenInputWeights, inputs)
        hidden.add(self.hiddenBias)
        hidden.map(Sigmoid)

        output = Matrix.matrix_multiplication(self.hiddenOutputWeights , hidden)
        output.add(self.outputBias)
        output.map(Sigmoid)

        return output.toArray()

    def Train(self, inputs, targets, debug = False):
        outputs = self.FeedForward(inputs)

        outputs = Matrix.fromArray(outputs)
        outputs.label = "Outputs"
        targets = Matrix.fromArray(targets)
        targets.label = "Targets"

        err = targets - outputs
        err.label = "Error"

        transposed_hiddenOutputs = Matrix.transpose(self.hiddenOutputWeights)
        hidden_errors = Matrix.matrix_multiplication(transposed_hiddenOutputs, err)
        
        #debug
        if debug == True:
            outputs.Debug()
            targets.Debug()
            err.Debug()
