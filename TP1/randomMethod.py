from os.path import exists
from os import mkdir
import random
import copy
from eightPuzzle import EightPuzzle


def main():

    for i in range(50):
        eightPuzzle = EightPuzzle([3, 3], 50)
        goal = eightPuzzle.goal
        grid = eightPuzzle.grid
        initialState = copy.deepcopy(grid)
        steps = 0
        print(i)
        while grid != goal:
            steps += 1
            empty = findEmpty(grid)
            moves = findMoves(empty, goal)
            move = random.choice(moves)
            grid[empty[0]][empty[1]] = grid[move[0]][move[1]]
            grid[move[0]][move[1]] = 0

        if exists('./reports/randomMethod.txt'):
            with open('./reports/randomMethod.txt', 'a') as f:
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
            with open('./reports/randomMethod.txt', 'w') as f:
                f.write('steps: ' + str(steps))
                f.write('\n')
                f.write('initial state: ' + str(initialState))
                f.write('\n')
                f.write('end state: ' + str(grid))
                f.write('\n\n')

# find empty tile


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
