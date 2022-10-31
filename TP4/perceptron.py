import random
import math
import numpy as np


class Perceptron:
    def __init__(self, cantWeights):
        self.weights = np.array([random.uniform(-1, 1)
                                for i in range(cantWeights)])
        self.Hweights = np.array([])
        self.inputs = np.array([])
        self.LR = 0.9
        self.error = 0
        self.spectedOutput = 0  # spected output
        self.realOutput = 0  # real output

    def processInput(self, inputs, spectedOutput=0):
        self.inputs = np.array(inputs)
        self.spectedOutput = spectedOutput
        sumVal = np.sum(self.inputs * self.weights)
        self.realOutput = self.__activationFunction(sumVal)

    def updateWeights(self, delta):
        soc = self.realOutput * (1-self.realOutput) * delta
        self.weights = self.LR * self.inputs * soc

    def __activationFunction(self, sumVal):
        return 1/(1+np.exp(-sumVal))

    def __str__(self):
        return str(self.weights)


class OutputPerceptron:
    def __init__(self, cantWeights):
        self.weights = np.array([random.uniform(-1, 1) for i in range(cantWeights + 1)])
        self.Hweights = np.array([])
        self.inputs = np.array([])
        self.LR = 0.9
        self.error = 0
        self.delta = 0
        self.spectedOutput = 0  # spected output
        self.realOutput = 0  # real output

    def processInput(self, inputs, spectedOutput=0):
        self.inputs = np.array(inputs)
        self.spectedOutput = spectedOutput
        sumVal = np.sum(self.inputs * self.weights)
        self.realOutput = self.__activationFunction(sumVal)

    def updateWeights(self):
        self.error = self.spectedOutput - self.realOutput
        self.delta = self.LR * self.error
        self.weights += self.inputs * self.delta

    def __activationFunction(self, sumVal):
        return 1/(1+np.exp(-sumVal))

    def __str__(self):
        return str(self.weights)
