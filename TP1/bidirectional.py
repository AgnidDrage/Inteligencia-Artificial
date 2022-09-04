from os.path import exists
from os import mkdir
import copy
from eightPuzzle import EightPuzzle


def main():
    executions = 10
    totalSteps = []
    for i in range(executions):
        print("execution number: " + str(i+1))
        eightPuzzle = EightPuzzle([3, 3], 50)
        finalGrid = eightPuzzle.goal
        startGrid = eightPuzzle.grid
        grid = copy.deepcopy(startGrid)
        goal = copy.deepcopy(finalGrid)
        qGrid = []  # queue
        vGrid = []  # visited
        temp = []
        qGoal = []
        vGoal = []
        tempGoal = []
        steps = 0
        qGrid.append(startGrid)
        qGoal.append(finalGrid)

        while True:
            grid = qGrid.pop(0)
            empty = findEmpty(grid)
            moves = findMoves(empty, grid)
            for move in moves:
                newgrid = copy.deepcopy(grid)
                newgrid[empty[0]][empty[1]] = newgrid[move[0]][move[1]]
                newgrid[move[0]][move[1]] = 0
                if newgrid not in vGrid:
                    temp.append(newgrid)
            vGrid.append(grid)

            goal = qGoal.pop(0)
            empty = findEmpty(goal)
            moves = findMoves(empty, goal)
            for move in moves:
                newgrid = copy.deepcopy(grid)
                newgrid[empty[0]][empty[1]] = newgrid[move[0]][move[1]]
                newgrid[move[0]][move[1]] = 0
                if newgrid not in vGoal:
                    tempGoal.append(newgrid)
            vGoal.append(goal)

            common = checkCommon(vGrid, vGoal)

            if common is not None:
                break

            if qGrid == [] or len(qGrid) == 0 or qGoal == [] or len(qGoal) == 0:
                qGrid = copy.deepcopy(temp)
                qGoal = copy.deepcopy(tempGoal)
                temp = []
                tempGoal = []
                steps += 1

        totalSteps.append(steps*2)

        if exists('./reports/bidirectional.txt'):
            with open('./reports/bidirectional.txt', 'a') as f:
                f.write("Excution number: " + str(i+1))
                f.write("\n")
                f.write('steps: ' + str(steps*2))
                f.write('\n')
                f.write('initial state: ' + str(startGrid))
                f.write('\n')
                f.write('common state: ' + str(common))
                f.write('\n')
                f.write('final state: ' + str(finalGrid))
                f.write('\n\n')
        else:
            try:
                mkdir('./reports')
            except FileExistsError:
                pass
            with open('./reports/bidirectional.txt', 'w') as f:
                f.write("Excution number: " + str(i+1))
                f.write("\n")
                f.write('steps: ' + str(steps*2))
                f.write('\n')
                f.write('initial state: ' + str(startGrid))
                f.write('\n')
                f.write('common state: ' + str(common))
                f.write('\n')
                f.write('final state: ' + str(finalGrid))
                f.write('\n\n')

    with open('./reports/bidirectional.txt', 'a') as f:
        f.write("=========End of Report=========")
        f.write('\n')
        f.write("Execution times: " + str(executions))
        f.write('\n')
        f.write('average steps: ' + str(sum(totalSteps)/len(totalSteps)))
        f.write('\n')
        f.write("===============================")
        f.write('\n\n')


# Check if v and vGoal have any common elements and return it
def checkCommon(vGrid, vGoal):
    for i in vGrid:
        for j in vGoal:
            if i == j:
                return i
    return None


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


if __name__ == '__main__':
    main()
