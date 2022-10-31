from perceptron import Perceptron, OutputPerceptron
import matplotlib.pyplot as plt
import copy
import numpy as np


def main():
    BIAS = 1
    xorTable = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    error1 = []
    error2 = []
    error3 = []
    error4 = []
    epoch = 10000
    layer, outputPerceptron = instanciatePerceptrons(perceptronCount=6)

    for i in range(epoch):
        # counter from 1 to 4
        counter = i % 4 + 1
        print("Epoch: ", i)
        # forward propagation
        xor = xorTable[i % len(xorTable)]
        inputs = [xor[0], xor[1], BIAS]
        spectedOutput = xor[2]
        for i in range(len(layer)):
            layer[i].processInput(inputs)
        inputs = [i.realOutput for i in layer]
        inputs.append(BIAS)
        outputPerceptron.processInput(inputs, spectedOutput)

        # backward propagation
        err = spectedOutput - outputPerceptron.realOutput
        delta = outputPerceptron.LR * err
        
        outputPerceptron.Hweights = np.append(outputPerceptron.Hweights, outputPerceptron.weights)
        for i in range(len(outputPerceptron.weights)):
            outputPerceptron.weights[i] += delta * outputPerceptron.inputs[i]

        for i in range(len(layer)):
            layer[i].Hweights = np.append(layer[i].Hweights, layer[i].weights)
            soc = layer[i].realOutput * (1 - layer[i].realOutput) * delta
            for j in range(len(layer[i].weights)):
                layer[i].weights[j] += layer[i].LR * soc * layer[i].inputs[j]

        # save errors
        if counter == 1:
            error1.append(err)
        elif counter == 2:
            error2.append(err)
        elif counter == 3:
            error3.append(err)
        elif counter == 4:
            error4.append(err)


    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.plot(error1, 'r')
    plt.plot(error2, 'g')
    plt.plot(error3, 'b')
    plt.plot(error4, 'y')
    plt.legend(['error1', 'error2', 'error3', 'error4'])
    plt.show()

    #plot weights
    if len(layer) <= 8:
        legend = []
        legendCounter = 0
        for i in range(len(layer)):
            plt.plot(layer[i].Hweights[::3])
            plt.plot(layer[i].Hweights[1::3])
            plt.plot(layer[i].Hweights[2::3])
            legend.append(f"w{legendCounter}")
            legend.append(f"w{legendCounter+1}")
            legend.append(f"w{legendCounter+2}")
            legendCounter += 3
        plt.legend(legend)
        plt.show()
    else:
        print("No se pueden graficar los pesos de la red, demasiados perceptrones.")

    
    

def instanciatePerceptrons(perceptronCount=6, cantWeights=3):
    '''
        Si perceptronCount < 6, existe riesgo de divergencia de errores en la red.
        Para perceptronCount > 6, parece siempre converger a 0.
    '''
    layer = []
    for i in range(perceptronCount):
        layer.append(Perceptron(cantWeights))
    outputPerceptron = OutputPerceptron(perceptronCount)
    return layer, outputPerceptron


if __name__ == "__main__":
    main()