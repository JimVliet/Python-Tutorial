import Sudoku
rij = 9
kolom = 9

Matrix = [[-1 for y in range(rij)] for x in range(kolom)] 

Matrix[0][0] = 8
Matrix[4][0] = 4

Sudoku.Sudoku(Matrix).print()