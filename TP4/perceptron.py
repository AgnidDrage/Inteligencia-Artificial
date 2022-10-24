import random
import math


class Perceptron:
    def __init__(self, cantWeights):
        self.weights = [random.uniform(-1, 1) for i in range(cantWeights)]
        self.Hweights = []
        self.inputs = []
        self.LR = 0.9
        self.error = 0
        self.spectedOutput = 0  # spected output
        self.realOutput = 0  # real output

    def processInput(self, inputs, spectedOutput=0):
        self.inputs = inputs
        self.spectedOutput = spectedOutput
        sumVal = 0
        for i in range(len(inputs)):
            sumVal += inputs[i] * self.weights[i]
        self.realOutput = self.__activationFunction(sumVal)

    def updateWeights(self, delta):
        soc = self.realOutput * (1-self.realOutput) * delta
        for i in range(len(self.weights)):
            self.weights[i] += self.LR * self.inputs[i] * soc
        

    def __activationFunction(self, sumVal):
        # if sumVal > 0:
        #     return 1
        # else:
        #     return 0
        return 1 / (1 + math.e ** (-sumVal))

    def __str__(self):
        return str(self.weights)


class OutputPerceptron:
    def __init__(self, cantWeights):
        self.weights = [random.uniform(-1, 1) for i in range(cantWeights + 1)]
        self.Hweights = []
        self.inputs = []
        self.LR = 0.9
        self.error = 0
        self.delta = 0
        self.spectedOutput = 0  # spected output
        self.realOutput = 0  # real output

    def processInput(self, inputs, spectedOutput=0):
        self.inputs = inputs
        self.spectedOutput = spectedOutput
        sumVal = 0
        for i in range(len(inputs)):
            sumVal += inputs[i] * self.weights[i]
        self.realOutput = self.__activationFunction(sumVal)

    def updateWeights(self):
        self.error = self.spectedOutput - self.realOutput
        self.delta = self.realOutput * (1-self.realOutput) * self.error
        for i in range(len(self.weights)):
            self.weights[i] += self.LR * self.inputs[i] * self.delta 

    def __activationFunction(self, sumVal):
        # if sumVal > 0:
        #     return 1
        # else:
        #     return 0
        return 1 / (1 + math.e ** (-sumVal))

    def __str__(self):
        return str(self.weights)
