import Sudoku
import numpy as np
import heapq
import TestingGrounds as TG
#Standaard functies

def start():
	rowList = ['800040000',
		   '006050009',
		   '109070300',
		   '400160000',
		   '081307090',
		   '600400015',
		   '000000001',
		   '374000960',
		   '000896034']
	Sud = Sudoku.Sudoku(TG.arrayToMatrix(rowList))
	print("\n \n")
	Sud.print()
	print("\n \n")
	Sud.updateAll()
	Sud.updateQueue()
	Sud.printQueue()

start()