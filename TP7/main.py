from operator import le
from turtle import pos
from perceptron import Perceptron, OutputPerceptron
from DatasetInput import DatasetInput
import matplotlib.pyplot as plt
import numpy as np

DATASETPATH = "./Dataset"


def main():
    BIAS = 1
    dataset = DatasetInput(DATASETPATH)
    images = dataset.images
    errors = [[] for i in range(len(images))]
    epoch = 1000
    layer, outputPerceptron = instanciatePerceptrons(perceptronCount=100, numOfInputs=80*96)
    for i in range(epoch):
        print("Epoch: ", i)
        # forward propagation
        index = i % len(images)
        image = images[index]
        inputs = image[0].flatten().tolist()
        inputs.append(BIAS)
        spectedOutput = image[1]
        for i in range(len(layer)):
            layer[i].processInput(inputs)
        inputs = [i.realOutput for i in layer]
        inputs.append(BIAS)
        outputPerceptron.processInput(inputs, spectedOutput)

        # backward propagation
        outputPerceptron.updateWeights()
        err = outputPerceptron.error

        for i in range(len(layer)):
            layer[i].updateWeights(outputPerceptron.delta)

        # save errors
        errors[index].append(err)
        
            
    # plot errors
    legend = []
    for i in range(len(errors)):
        legend.append("Error " + str(i))
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Error vs Epoch')
    for i in range(len(errors)):
        plt.plot(errors[i])
    plt.legend(legend)
    plt.show()


    print("A predecir: deberia salir 0101")
    print(predict(layer, outputPerceptron, images[0][0].flatten().tolist()))
    print(predict(layer, outputPerceptron, images[1][0].flatten().tolist()))
    print(predict(layer, outputPerceptron, images[2][0].flatten().tolist()))
    print(predict(layer, outputPerceptron, images[3][0].flatten().tolist()))

def instanciatePerceptrons(perceptronCount=60, numOfInputs=3):
    '''
        Funciona bien para perceptronCount => 60.
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
    return round(outputPerceptron.realOutput)

if __name__ == "__main__":
    main()