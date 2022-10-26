from perceptron import Perceptron, OutputPerceptron
from DatasetInput import DatasetInput
import numpy as np
import matplotlib.pyplot as plt
import copy

DATASETPATH = "./Dataset"


def main():
    BIAS = 1
    dataset = DatasetInput(DATASETPATH)
    images = dataset.images
    errorsA = []
    errorsB = []
    epoch = 100
    layer, outputPerceptron = instanciatePerceptrons(perceptronCount=10, numOfInputs=80*96)
    for i in range(epoch):
        print("Epoch: ", i)
        # forward propagation
        image = images[i % len(images)]
        inputs = image[0].flatten().tolist()
        inputs.append(BIAS)
        spectedOutput = image[1]
        for i in range(len(layer)):
            layer[i].processInput(inputs)
        inputs = [i.realOutput for i in layer]
        inputs.append(BIAS)
        outputPerceptron.processInput(inputs, spectedOutput)

        # backward propagation
        err = spectedOutput - outputPerceptron.realOutput
        delta = outputPerceptron.LR * err

        outputPerceptron.Hweights.extend(
            copy.deepcopy(outputPerceptron.weights))
        for i in range(len(outputPerceptron.weights)):
            outputPerceptron.weights[i] += delta * outputPerceptron.inputs[i]

        for i in range(len(layer)):
            layer[i].Hweights.extend(copy.deepcopy(layer[i].weights))
            soc = layer[i].realOutput * (1 - layer[i].realOutput) * delta
            for j in range(len(layer[i].weights)):
                layer[i].weights[j] += layer[i].LR * soc * layer[i].inputs[j]

        # save errors
        if spectedOutput == 0:
            errorsA.append(err)
        elif spectedOutput == 1:
            errorsB.append(err)

    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.plot(errorsA, label='A')
    plt.plot(errorsB, label='B')
    plt.legend()
    plt.show()

    print(predict(layer, outputPerceptron, images[0][0].flatten().tolist()))

def instanciatePerceptrons(perceptronCount=6, numOfInputs=3):
    '''
        Si perceptronCount < 6, existe riesgo de divergencia de errores en la red.
        Para perceptronCount > 6, parece siempre converger a 0.
    '''
    layer = []
    for i in range(perceptronCount):
        layer.append(Perceptron(numOfInputs))
    outputPerceptron = OutputPerceptron(perceptronCount)
    return layer, outputPerceptron

def predict(layer, outputPerceptron, inputs):
    BIAS = 1
    inputs.append(BIAS)
    for i in range(len(layer)):
        layer[i].processInput(inputs)
    inputs = [i.realOutput for i in layer]
    inputs.append(BIAS)
    outputPerceptron.processInput(inputs)
    return outputPerceptron.realOutput

if __name__ == "__main__":
    main()