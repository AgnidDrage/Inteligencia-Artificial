from perceptron import Perceptron, OutputPerceptron
import matplotlib.pyplot as plt
import numpy as np
import random


def main():
    global layer, outputPerceptron, error1, error2, error3, error4
    BIAS = 1
    xorTable = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    orTable = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    error1 = []
    error2 = []
    error3 = []
    error4 = []
    epoch = 10000
    layer, outputPerceptron = instanciatePerceptrons(perceptronCount=3)
    breakpoint()
    for i in range(epoch):
        print("Epoch: ", i)
        # forward propagation
        xor = xorTable[i % len(xorTable)]
        inputs = [xor[0], xor[1], BIAS]
        breakpoint()
        spectedOutput = xor[2]
        for per in range(len(layer)):
            layer[per].processInput(inputs)
        inputs = [per.realOutput for per in layer]
        inputs.append(BIAS)
        outputPerceptron.processInput(inputs, spectedOutput)
        # backward propagation
        err = backwardPropagation()
        if i % 4 == 0:
            error1.append(err)
        elif i % 4 == 1:
            error2.append(err)
        elif i % 4 == 2:
            error3.append(err)
        elif i % 4 == 3:
            error4.append(err)

        # print("pesos")
        # print(layer[0].weights)
        # print(layer[1].weights)
        # print(layer[2].weights)
        # print(outputPerceptron.weights)
    plt.plot(error1, 'r')
    plt.plot(error2, 'g')
    plt.plot(error3, 'b')
    plt.plot(error4, 'y')
    plt.show()


def backwardPropagation():
    global layer, outputPerceptron, err
    # backward propagation
    outputPerceptron.updateWeights()
    delta = outputPerceptron.delta
    for i in range(len(layer)):
        layer[i].updateWeights(delta)
    err = outputPerceptron.error
    return err


def instanciatePerceptrons(perceptronCount=3):
    layer = []
    for i in range(perceptronCount):
        layer.append(Perceptron(cantWeights=3))
    outputPerceptron = OutputPerceptron(cantWeights=len(layer))
    # per1 = Perceptron(0.9, 0.7, 0.5)
    # per2 = Perceptron(0.3, -0.9, -1)
    # per3 = Perceptron(0.8, 0.35, .01)
    # layer.extend([per1, per2, per3])
    # outputPerceptron = OutputPerceptron(-0.23, -0.79, 0.56, 0.6)
    return layer, outputPerceptron


if __name__ == '__main__':
    main()
