from traceback import print_tb
from perceptron import Perceptron
import matplotlib.pyplot as plt

def main():
    useTable = "AND"  # Choose OR, AND or XOR.
    stopFlag = True # True for stop when error < 10% , False for continue.
    errThreshold = 0.001  # Error threshold.
    iterations = 300
    lastIteration = 0
    index = 0
    i = 0
    perceptron = Perceptron()
    historicalW1 = []
    historicalW2 = []
    historicalW3 = []
    errorList = []
    orTable = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]
    ]

    andTable = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 1]
    ]

    xorTable = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0]
    ]

    # Train the perceptron with the table.
    if useTable == "OR":
        while True:
            row = orTable[index]
            index += 1
            if index == len(orTable):
                index = 0
            perceptron.processInput(row, row[3])
            perceptron.updateWeights()
            historicalW1.append(perceptron.weights[0])
            historicalW2.append(perceptron.weights[1])
            historicalW3.append(perceptron.weights[2])
            errorList.append(perceptron.error)
            i += 1
            if perceptron.error < errThreshold and perceptron.error > -errThreshold and stopFlag == True:
                print(f"Iteration to have less than {errThreshold} error: ", i)
                print(perceptron.error)
                lastIteration = i
                break
    elif useTable == "AND":
        while True:
            row = andTable[index]
            index += 1
            if index == len(andTable):
                index = 0
            perceptron.processInput(row, row[3])
            perceptron.updateWeights()
            historicalW1.append(perceptron.weights[0])
            historicalW2.append(perceptron.weights[1])
            historicalW3.append(perceptron.weights[2])
            errorList.append(perceptron.error)
            i += 1
            if perceptron.error < errThreshold and perceptron.error > -errThreshold and stopFlag == True:
                print(f"Iteration to have less than {errThreshold} error: ", i)
                print(perceptron.error)
                lastIteration = i
                break
    else:
        while True:
            row = xorTable[index]
            index += 1
            if index == len(xorTable):
                index = 0
            perceptron.processInput(row, row[3])
            perceptron.updateWeights()
            historicalW1.append(perceptron.weights[0])
            historicalW2.append(perceptron.weights[1])
            historicalW3.append(perceptron.weights[2])
            errorList.append(perceptron.error)
            i += 1
            if perceptron.error < errThreshold and perceptron.error > -errThreshold and stopFlag == True:
                print(f"Iteration to have less than {errThreshold} error: ", i)
                print(perceptron.error)
                lastIteration = i
                break

    plotInfo(historicalW1, range(lastIteration))
    plotInfo(historicalW2, range(lastIteration))
    plotInfo(historicalW3, range(lastIteration))
    plotInfo(errorList, range(lastIteration))

    # Test prediction.
    print("Let's predict, please enter 2 numbers without space, for example: 10")
    while True:
        values = formatInput(input('Enter values: '))
        for i in range(len(values)):
            values[i] = int(values[i])
        output = perceptron.predict(values)
        print('Output: ',   round(output))

# Format input from str to int, and check if is valid.
def formatInput(values):
    try:
        valueList = []
        for i in range(len(values)):
            if len(values) == 2:
                val = values[i]
                if val == '0' or val == '1':
                    valueList.append(int(val))
            else:
                raise ValueError("Inputs must be 0 or 1, example: 01")
        return valueList
    except ValueError:
        print('Inputs must be 2 bits without space, example: 10')
        return formatInput(input('Enter values: '))

def plotInfo(value, iterations):
    plt.title('Perceptron')
    plt.xlabel('iterations')
    plt.ylabel('weights')
    plt.grid(True)
    plt.plot(iterations, value)
    plt.show()

if __name__ == '__main__':
    main()
