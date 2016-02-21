import Sudoku
import numpy as np
import heapq
import TestingGrounds as TG
import time
#Standaard functies

rowList = ['800040000',
		   '006050009',
		   '109070300',
		   '400160000',
		   '081307090',
		   '600400015',
		   '000000001',
		   '374000960',
		   '000896034']
matrix = TG.arrayToMatrix(rowList)
startingTime = time.time()
Sud = Sudoku.Sudoku(matrix)
Sud.solve()
timeDif = time.time() - startingTime
print("Time to run: " + str(timeDif))
Sud.print()