from traceback import print_tb
from eightPuzzle import EightPuzzle

def main():
    matrix = [3,3]
    eightPuzzle = EightPuzzle(matrix, 1)
    print(eightPuzzle.goal)
    print(eightPuzzle.grid)




if __name__ == "__main__":
    main()