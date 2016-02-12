import numpy as np
import heapq
import VakInfo
def arrayToMatrix(arrayList):
	Width = len(arrayList[1])
	Length = len(arrayList)
	Matrix = np.zeros((Width,Length), dtype=np.int)
	for i in range(Length):
		for j in range(Width):
			string = arrayList[i]
			number = int(string[j])
			Matrix[j][i] = number
	return Matrix

def scoreCalc():
	scoreLijst = [0, 3, 5, 6, 7, 8]
	priorQ = []
	for i in scoreLijst:
		for j in range(9):
			heapq.heappush(priorQ, (2**i+2**j, i, j))

	priorQ = heapq.nlargest(len(priorQ), priorQ)
	for i in range(len(priorQ)):
		print(i, ": - ", priorQ[i][0], " - %i,%i - "%(priorQ[i][1],priorQ[i][2]), (priorQ[i][1] == 8 or priorQ[i][2] == 8))

def printMatrix(matrix):
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			print(matrix[j][i], end="")
		print("")

def testFunc():
	vLijst = np.empty((2,2), dtype=VakInfo.VakInfo)
	vLijst[0][0] = VakInfo.VakInfo(1, 0, 10)
	vLijst[1][0] = VakInfo.VakInfo(1, 1, 20)
	vLijst[0][1] = VakInfo.VakInfo(2, 0, 30)
	vLijst[1][1] = VakInfo.VakInfo(2, 1, 40)
	priorQ = np.ravel(vLijst)
	priorQ = heapq.nlargest(len(priorQ), priorQ)
	print(priorQ)
	print(heapq.heappop(priorQ))
	vLijst[1][1].Score = 0
	print(heapq.heappop(priorQ))
	print(priorQ)