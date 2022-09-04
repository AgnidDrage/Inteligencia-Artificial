from os.path import exists
from os import mkdir
import copy
from queue import Empty
from eightPuzzle import EightPuzzle


def main():
    executions = 10
    totalSteps = []
    for i in range(executions):
        print("execution number: " + str(i+1))
        eightPuzzle = EightPuzzle([3, 3], 50)
        goal = eightPuzzle.goal
        startGrid = eightPuzzle.grid
        initialState = copy.deepcopy(startGrid)
        grid = []
        q = []  # queue
        v = []  # visited
        temp = []
        steps = 0
        q.append(startGrid)

        while grid != goal:
            grid = q.pop(0)
            empty = findEmpty(grid)
            moves = findMoves(empty, grid)
            for move in moves:
                newgrid = copy.deepcopy(grid)
                newgrid[empty[0]][empty[1]] = newgrid[move[0]][move[1]]
                newgrid[move[0]][move[1]] = 0
                if newgrid not in v:
                    temp.append(newgrid)
            v.append(grid)
            if q == [] or len(q) == 0:
                q = copy.deepcopy(temp)
                temp = []
                steps += 1

        totalSteps.append(steps)

        if exists('./reports/bsfMethod.txt'):
            with open('./reports/bsfMethod.txt', 'a') as f:
                f.write("Excution number: " + str(i+1))
                f.write("\n")
                f.write('steps: ' + str(steps))
                f.write('\n')
                f.write('initial state: ' + str(initialState))
                f.write('\n')
                f.write('end state: ' + str(grid))
                f.write('\n\n')
        else:
            try:
                mkdir('./reports')
            except FileExistsError:
                pass
            with open('./reports/bsfMethod.txt', 'w') as f:
                f.write("Excution number: " + str(i+1))
                f.write("\n")
                f.write('steps: ' + str(steps))
                f.write('\n')
                f.write('initial state: ' + str(initialState))
                f.write('\n')
                f.write('end state: ' + str(grid))
                f.write('\n\n')

    with open('./reports/bsfMethod.txt', 'a') as f:
        f.write("=========End of Report=========")
        f.write('\n')
        f.write("Execution times: " + str(executions))
        f.write('\n')
        f.write('average steps: ' + str(sum(totalSteps)/len(totalSteps)))
        f.write('\n')
        f.write("===============================")
        f.write('\n\n')


def findEmpty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return [i, j]


def findMoves(empty, goal):
    moves = []
    if empty[0] > 0:
        moves.append([empty[0]-1, empty[1]])
    if empty[0] < len(goal)-1:
        moves.append([empty[0]+1, empty[1]])
    if empty[1] > 0:
        moves.append([empty[0], empty[1]-1])
    if empty[1] < len(goal[0])-1:
        moves.append([empty[0], empty[1]+1])
    return moves


if __name__ == "__main__":
    main()
