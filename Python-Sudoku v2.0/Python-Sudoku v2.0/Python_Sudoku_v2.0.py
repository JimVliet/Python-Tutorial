import numpy as np
import BlockInfo as BI
import itertools
import Sudoku as SU
import time
SudokuMap = np.array([[8, 0, 0, 0, 4, 0, 0, 0, 0],
					  [0, 0, 6, 0, 5, 0, 0, 0, 9],
					  [1, 0, 9, 0, 7, 0, 3, 0, 0],
					  [4, 0, 0, 1, 6, 0, 0, 0, 0],
					  [0, 8, 1, 3, 0, 7, 0, 9, 0],
					  [6, 0, 0, 4, 0, 0, 0, 1, 5],
					  [0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [3, 7, 4, 0, 0, 0, 9, 6, 0],
					  [0, 0, 0, 8, 9, 6, 0, 3, 4]])

start = time.time()
obj = SU.Sudoku(SudokuMap)
obj.solve()
print(time.time()-start)
print(obj.map)