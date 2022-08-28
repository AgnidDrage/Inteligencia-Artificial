from perceptron import Perceptron


def main():
    useOr = True  # True for OR, False for AND
    index = 0
    perceptron = Perceptron()
    orTable = [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]
    ]

    andTable = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 1]
    ]

    # Train the perceptron with the table.
    if useOr:
        for i in range(300):
            row = orTable[index]
            index += 1
            if index == len(orTable):
                index = 0
            perceptron.processInput(row, row[3])
            perceptron.updateWeights()
    else:
        for i in range(300):
            row = andTable[index]
            index += 1
            if index == len(andTable):
                index = 0
            perceptron.processInput(row, row[3])
            perceptron.updateWeights()

    # Test prediction.
    print("Let's predict, please enter 3 numbers without space, for example: 111")
    while True:
        values = formatInput(input('Enter values: '))
        print(values)
        for i in range(len(values)):
            values[i] = int(values[i])
        print(values)
        output = perceptron.predict(values)
        print('Output: ',   round(output))

# Format input from str to int, and check if is valid.
def formatInput(values):
    try:
        valueList = []
        for i in range(len(values)):
            if len(values) == 3:
                val = values[i]
                if val == '0' or val == '1':
                    valueList.append(int(val))
            else:
                raise ValueError("Inputs must be 0 or 1, example: 111")
        return valueList
    except ValueError:
        print('Inputs must be 3 bits without space, example: 110')
        return formatInput(input('Enter values: '))


if __name__ == '__main__':
    main()
