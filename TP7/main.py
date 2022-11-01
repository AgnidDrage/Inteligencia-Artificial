from operator import le
from turtle import pos
from perceptron import Perceptron, OutputPerceptron
from DatasetInput import DatasetInput
import matplotlib.pyplot as plt
import numpy as np
import pickle

DATASETPATH = "./Dataset"


def main():
    BIAS = 1
    dataset = DatasetInput(DATASETPATH)
    images = dataset.images
    dataset = DatasetInput(DATASETPATH, getExtras=True)
    imagesExt = dataset.images
    dataExtA = []
    dataExtB = []
    errors = [[] for i in range(len(images))]
    epoch = 200
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

        # predict
        for i in range(len(imagesExt)):
            image = imagesExt[i]
            inputs = image[0].flatten().tolist()
            spectedOutput = image[1]
            output = predict(layer, outputPerceptron, inputs)
            if spectedOutput == 0:
                dataExtA.append(output)
            else:
                dataExtB.append(output)
        
            
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

    # plot dataExt
    plt.xlabel('Epoch')
    plt.ylabel('Output')
    plt.title('Output vs Epoch')
    plt.plot(dataExtA[::3])
    plt.plot(dataExtA[1::3])
    plt.plot(dataExtA[2::3])
    plt.plot(dataExtB[::3])
    plt.plot(dataExtB[1::3])
    plt.plot(dataExtB[2::3])
    plt.legend(["A1", "A2", "A3", "B1", "B2", "B3"])
    plt.show()

    saveWeights(layer, outputPerceptron)

def instanciatePerceptrons(perceptronCount=60, numOfInputs=3):
    '''
        Funciona bien para perceptronCount => 60.
    '''
    layer = []
    for i in range(perceptronCount):
        layer.append(Perceptron(numOfInputs))
    outputPerceptron = OutputPerceptron(perceptronCount)
    return layer, outputPerceptron

def predict(layer, outputPerceptron, imgInput):
    BIAS = 1
    inputs = imgInput
    inputs.append(BIAS)
    for i in range(len(layer)):
        layer[i].processInput(inputs)
    inputs = [i.realOutput for i in layer]
    inputs.append(BIAS)
    outputPerceptron.processInput(inputs)
    return outputPerceptron.realOutput

def saveWeights(layer, outputPerceptron):
    print("Guardando pesos...")
    with open('weights.pickle', 'wb') as f:
        hiddenWeights = []
        for i in range(len(layer)):
            hiddenWeights.append(layer[i].weights)
        data = (hiddenWeights, outputPerceptron.weights)
        pickle.dump(data, f)



if __name__ == "__main__":
    main()