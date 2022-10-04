import random
import math


class Perceptron:
    def __init__(self, w1, w2, w3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.weights = [w1, w2, w3]
        # self.weights = [0, 0, 0]
        self.inputs = []
        self.LR = 0.1
        self.error = 0
        self.spectedOutput = 0  # spected output
        self.realOutput = 0  # real output

    def processInput(self, inputs, spectedOutput=0):
        self.inputs = inputs
        self.spectedOutput = spectedOutput
        c0 = inputs[0] * self.weights[0]
        c1 = inputs[1] * self.weights[1]
        c2 = inputs[2] * self.weights[2]
        sumVal = c0 + c1 + c2
        self.realOutput = self.__activationFunction(sumVal)

    def updateWeights(self):
        self.error = self.spectedOutput - self.realOutput
        delta = self.LR * self.error
        for i in range(len(self.weights)):
            deltaW = delta * self.inputs[i]
            self.weights[i] += deltaW
        print('Weights: ', self.weights)

    def predict(self, inputs):
        if len(inputs) == 2:
            c0 = 1 * self.weights[0]
            c1 = inputs[0] * self.weights[1]
            c2 = inputs[1] * self.weights[2]
            sumVal = c0 + c1 + c2
            return self.__activationFunction(sumVal)
        else:
            raise ValueError(
                "Inputs must be 2 bits without space, example: 11")

    def __activationFunction(self, sumVal):
        # if sumVal > 0:
        #     return 1
        # else:
        #     return 0
        return 1 / (1 + math.e ** (-sumVal))

    def __str__(self):
        return str(self.weights)


class OutputPerceptron:
    def __init__(self, w1, w2, w3, w4):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.weights = [w1, w2, w3, w4]
        # self.weights = [0, 0, 0]
        self.inputs = []
        self.LR = 0.1
        self.error = 0
        self.spectedOutput = 0  # spected output
        self.realOutput = 0  # real output

    def processInput(self, inputs, spectedOutput=0):
        self.inputs = inputs
        self.spectedOutput = spectedOutput
        c0 = inputs[0] * self.weights[0]
        c1 = inputs[1] * self.weights[1]
        c2 = inputs[2] * self.weights[2]
        c3 = inputs[3] * self.weights[3]
        sumVal = c0 + c1 + c2 + c3
        self.realOutput = self.__activationFunction(sumVal)

    def updateWeights(self):
        self.error = self.spectedOutput - self.realOutput
        delta = self.LR * self.error
        for i in range(len(self.weights)):
            deltaW = delta * self.inputs[i]
            self.weights[i] += deltaW
        print('Weights: ', self.weights)

    def predict(self, inputs):
        if len(inputs) == 2:
            c0 = 1 * self.weights[0]
            c1 = inputs[0] * self.weights[1]
            c2 = inputs[1] * self.weights[2]
            sumVal = c0 + c1 + c2
            return self.__activationFunction(sumVal)
        else:
            raise ValueError(
                "Inputs must be 2 bits without space, example: 11")

    def __activationFunction(self, sumVal):
        # if sumVal > 0:
        #     return 1
        # else:
        #     return 0
        return 1 / (1 + math.e ** (-sumVal))

    def __str__(self):
        return str(self.weights)
