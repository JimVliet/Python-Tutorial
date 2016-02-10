import Sudoku
import numpy as np
import heapq
#Standaard functies
def printMatrix(matrix):
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			print(matrix[j][i], end="")
		print("")

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
	Sud = Sudoku.Sudoku(rowList)
	printMatrix(Sud.Map[:8][:5])
	print("\n \n")
	Sud.print()

def scoreCalc():
	scoreLijst = [0, 3, 5, 6, 7, 8]
	priorQ = []
	for i in scoreLijst:
		for j in range(9):
			heapq.heappush(priorQ, (2**i+2**j, i, j))

	priorQ = heapq.nlargest(len(priorQ), priorQ)
	for i in range(len(priorQ)):
		print(i, ": - ", priorQ[i][0], " - %i,%i - "%(priorQ[i][1],priorQ[i][2]), (priorQ[i][1] == 8 or priorQ[i][2] == 8))

scoreCalc()