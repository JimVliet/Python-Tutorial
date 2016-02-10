import numpy as np
import heapq
class Sudoku:
    #Sudoku class
	def __init__(self, lijst):
		self.rij = len(lijst)
		self.kolom = len(lijst[0])
		self.kLijst = np.empty((self.kolom,self.rij), dtype=np.bool)
		self.kLijst.fill(False)
		self.rLijst = np.empty((self.kolom,self.rij), dtype=np.bool)
		self.rLijst.fill(False)
		self.vLijst = np.empty((9,9))
		self.vLijst.fill((0,0))

		Matrix = np.zeros((self.kolom,self.rij), dtype=np.int)
		for i in range(len(lijst)):
			for j in range(len(lijst[i])):
				string = lijst[i]
				number = int(string[j])
				Matrix[j][i] = number
				#Check if there is a number, and if that's true say that the corresponding columns and rows contain that number
				if(number != 0):
					self.kLijst[j][(number-1)] = True
					self.rLijst[i][(number-1)] = True
				
		self.Map = Matrix

	def updateAll():
		for vakNr in range(9):
			xOff = vakNr % 3
			yOff = vakNr // 3

			for kolomNr in range(3):
				kolomNr = xOff*3 + kolomNr


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