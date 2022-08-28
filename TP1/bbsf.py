from os.path import exists
from os import mkdir
import copy
from eightPuzzle import EightPuzzle


def main():
    eightPuzzle = EightPuzzle([3, 3], 50)
    finalState = eightPuzzle.goal
    initialState = eightPuzzle.grid
    # initialState = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    q = []  # queue
    qGoal = []  # queue for goal
    v = []  # visited
    vGoal = []  # visited for goal
    steps = 0
    grid = copy.deepcopy(initialState)
    goal = copy.deepcopy(finalState)
    
    while ~gridInGoal(grid, goal):
        steps += 1
        print(steps) 
        # proceed with goal
        empty = findEmpty(goal)
        moves = findMoves(empty, goal)
        for move in moves:
            newgrid = copy.deepcopy(goal)
            newgrid[empty[0]][empty[1]] = newgrid[move[0]][move[1]]
            newgrid[move[0]][move[1]] = 0
            if newgrid not in vGoal:
                qGoal.append(newgrid)
        vGoal.append(goal)
        # proceed with grid
        empty = findEmpty(grid)
        moves = findMoves(empty, grid)
        for move in moves:
            newgrid = copy.deepcopy(grid)
            newgrid[empty[0]][empty[1]] = newgrid[move[0]][move[1]]
            newgrid[move[0]][move[1]] = 0
            if newgrid not in v:
                q.append(newgrid)
        v.append(grid)

        #pop from queue
        grid = q.pop(0)
        goal = qGoal.pop(0)

    grid = findIntersection(grid, goal)

    if exists('./reports/bsfMethod.txt'):
        with open('./reports/bsfMethod.txt', 'a') as f:
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
            f.write('steps: ' + str(steps))
            f.write('\n')
            f.write('initial state: ' + str(initialState))
            f.write('\n')
            f.write('end state: ' + str(grid))
            f.write('\n\n')

def gridInGoal(grid, goal):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != goal[i][j]:
                return False
    return True

def findIntersection(grid, goal):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == goal[i][j]:
                return [i, j]
    return [-1, -1]

def findEmpty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return [i, j]

def findMoves(empty, grid):
    moves = []
    if empty[0] > 0:
        moves.append([empty[0]-1, empty[1]])
    if empty[0] < len(grid)-1:
        moves.append([empty[0]+1, empty[1]])
    if empty[1] > 0:
        moves.append([empty[0], empty[1]-1])
    if empty[1] < len(grid[0])-1:
        moves.append([empty[0], empty[1]+1])
    return moves

if __name__ == '__main__':
    main()