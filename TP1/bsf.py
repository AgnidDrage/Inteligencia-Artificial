import copy
from eightPuzzle import EightPuzzle


def main():
    eightPuzzle = EightPuzzle([3, 3], 50)
    goal = eightPuzzle.goal
    startGrid = eightPuzzle.grid
    # startGrid = [[1,2,3], [4,5,6], [7,0,8]]
    initialState = copy.deepcopy(startGrid)
    q = []  # queue
    v = []  # visited
    steps = 0
    q.append(startGrid)

    for grid in q:
        steps += 1
        print(steps)
        if grid == goal:
            break
        empty = findEmpty(grid)
        moves = findMoves(empty, grid)
        for move in moves:
            newgrid = copy.deepcopy(grid)
            newgrid[empty[0]][empty[1]] = newgrid[move[0]][move[1]]
            newgrid[move[0]][move[1]] = 0
            q.append(newgrid)
    print(grid)
    with open('./reports/bsfMethod.txt', 'a') as f:
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
