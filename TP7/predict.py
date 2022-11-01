from DatasetInput import DatasetInput
from perceptron import Perceptron, OutputPerceptron
import matplotlib.pyplot as plt
import numpy as np
import pickle

DATASETPATH = "./Dataset2"


def main():
    BIAS = 1
    dataset = DatasetInput(DATASETPATH, getExtras=True)
    images = dataset.images
    layer, outputPerceptron = instanciatePerceptrons(perceptronCount=100, numOfInputs=80*96)
    layerWeights, outputPerceptronWeights = loadWeights()
    for i in range(len(layer)):
        layer[i].weights = layerWeights[i]
    outputPerceptron.weights = outputPerceptronWeights
    for i in range(len(images)):
        image = images[i]
        inputs = image[0].flatten().tolist()
        inputs.append(BIAS)
        for i in range(len(layer)):
            layer[i].processInput(inputs)
        inputs = [i.realOutput for i in layer]
        inputs.append(BIAS)
        outputPerceptron.processInput(inputs)
        print("Salida real: ", round(outputPerceptron.realOutput))
        print("Salida esperada: ", image[1])


def instanciatePerceptrons(perceptronCount=60, numOfInputs=3):
    '''
        Funciona bien para perceptronCount => 60.
    '''
    layer = []
    for i in range(perceptronCount):
        layer.append(Perceptron(numOfInputs))
    outputPerceptron = OutputPerceptron(perceptronCount)
    return layer, outputPerceptron

def loadWeights():
    with open('weights.pickle', 'rb') as f:
        data = pickle.load(f)
        layerWeights = data[0]
        outputPerceptronWeights = data[1]
    return layerWeights, outputPerceptronWeights


if __name__ == "__main__":
    main()