from perceptron import Perceptron, OutputPerceptron


def main():
    input, hidden, output = instanciatePerceptrons()
    BIAS = 1
    # xorTable = [
    #     [0, 0, 0],
    #     [0, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 0]
    # ]
    xorTable = [[0,0,0]]
    
    for i in range(1):
        for row in xorTable:
            # input layer
            input[0].processInput([BIAS, row[0], row[1]])
            input[1].processInput([BIAS, row[0], row[1]])
            # hidden layer
            hidden[0].processInput(
                [BIAS, input[0].realOutput, input[1].realOutput])
            hidden[1].processInput(
                [BIAS, input[0].realOutput, input[1].realOutput])
            hidden[2].processInput(
                [BIAS, input[0].realOutput, input[1].realOutput])
            # output layer
            output[0].processInput(
                [BIAS, hidden[0].realOutput, hidden[1].realOutput, hidden[2].realOutput])
            print("Real output: ", output[0].realOutput)


def instanciatePerceptrons():
    input = []
    hidden = []
    output = []
    per1 = Perceptron(0.9, 0.7, 0.5)
    per2 = Perceptron(0.3, -0.9, -1)
    per3 = Perceptron(0.8, 0.35, .01)
    per4 = Perceptron(-0.23, -0.79, 0.56)
    per5 = Perceptron(0.6, -0.6, 0.22)
    per6 = OutputPerceptron(-0.22, -0.55, 0.31, -0.32)
    input.extend([per1, per2])
    hidden.extend([per3, per4, per5])
    output.extend([per6])
    return input, hidden, output

if __name__ == '__main__':
    main()
