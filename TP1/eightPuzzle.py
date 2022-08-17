import random
import copy


class EightPuzzle:
    def __init__(self, matrix=[3, 3], mix=50):
        self.matrix = matrix
        self.mix = mix
        self.goal = self.__generateGrid()
        self.grid = self.__mixedGrid()

    def __str__(self):
        return str(self.matrix)

    # Create ordered grid
    def __generateGrid(self):
        matrix = self.matrix
        grid = [
            [j*matrix[0] + i + 1 for i in range(matrix[0])] for j in range(matrix[1])]
        grid[-1][-1] = 0
        return grid

    # mix grid
    def __mixedGrid(self):
        mix = self.mix
        grid = copy.deepcopy(self.goal)
        for i in range(mix):
            grid = self.move(grid)
        return grid

    # move grid
    def move(self, grid):
        # find empty tile
        empty = self.findEmpty(grid)
        # find possible moves
        moves = self.findMoves(empty)
        # choose random move
        move = random.choice(moves)
        # swap empty tile with move
        grid[empty[0]][empty[1]] = grid[move[0]][move[1]]
        grid[move[0]][move[1]] = 0
        return grid

    # find empty tile
    def findEmpty(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return [i, j]

    # find possible moves
    def findMoves(self, empty):
        moves = []
        if empty[0] > 0:
            moves.append([empty[0]-1, empty[1]])
        if empty[0] < len(self.goal)-1:
            moves.append([empty[0]+1, empty[1]])
        if empty[1] > 0:
            moves.append([empty[0], empty[1]-1])
        if empty[1] < len(self.goal[0])-1:
            moves.append([empty[0], empty[1]+1])
        return moves
