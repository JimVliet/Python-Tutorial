import numpy as np
import heapq
import VakInfo
class Sudoku:
    #Sudoku class
	def __init__(self, Matrix):
		self.rij = Matrix.shape[0]
		self.kolom = Matrix.shape[1]
		self.kLijst = np.zeros((9,9), dtype=np.bool)
		self.rLijst = np.zeros((9,9), dtype=np.bool)
		self.vLijst = np.zeros((9,9), dtype=VakInfo.VakInfo)
		self.CIV = [0] * 9
		self.Map = Matrix
		self.priorQ = []

	def updateAll(self):
		
		for y in range(9):
			for x in range(9):
				number = self.Map[x][y]
				VakCode = (x//3)+3*(y//3)
				if number != 0:
					self.kLijst[x][(number-1)] = True
					self.rLijst[y][(number-1)] = True
					self.CIV[VakCode] += 1
					self.vLijst[VakCode][number-1] = None

		print(self.rLijst)

		for vakNR in range(9):
			for Getal in range(9):
				if self.vLijst[vakNR][Getal] is None:
					continue
				rijNum = (vakNR//3)*3
				kolomNum = (vakNR%3)*3
				#Add bools together to count the number of rows
				aantRij = (0 + self.rLijst[rijNum][Getal] + 
						self.rLijst[rijNum+1][Getal] + 
						self.rLijst[rijNum+2][Getal])
				aantKolom = (0 + self.kLijst[kolomNum][Getal] + 
						self.kLijst[kolomNum+1][Getal] +
						self.kLijst[kolomNum+2][Getal])
				self.vLijst[vakNR][Getal] = VakInfo.VakInfo(Getal+1, vakNR, aantRij, aantKolom, self.CIV[Getal])
		

	def updateQueue(self):
		self.priorQ = np.ravel(self.vLijst).tolist()
		self.priorQ = list(filter(None, self.priorQ))
		heapq.heapify(self.priorQ)

	def printQueue(self):
		for i in range(len(self.priorQ)):
			obj = heapq.heappop(self.priorQ)
			print("%i - %i,%i - %i,%i" %(obj.Score, obj.NMP, self.CIV[obj.Getal-1], obj.VakKolom, obj.VakRij))

	def print(self):
		rij = len(self.Map)
		kolom = len(self.Map[0])
		print("012345678")
		for i in range(rij):
			for j in range(kolom):
				if(self.Map[j][i] == 0):
					print("-", end="")
				else:
					print(self.Map[j][i], end="")
			print(" " + str(i))