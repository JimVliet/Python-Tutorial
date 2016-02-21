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

		#Loop through all vakken
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
		#Update the queue
		self.priorQ = np.ravel(self.vLijst).tolist()
		self.priorQ = list(filter(None, self.priorQ))
		heapq.heapify(self.priorQ)


	def solve(self):
		self.updateAll()
		#Check if the list is empty
		while True:
			try:
				vakInfoObject = heapq.heappop(self.priorQ)
				self.tryNumber(vakInfoObject)
			except IndexError:
				break

	#Main function for solving numbers
	#
	#
	#
	#input is the block
	def tryNumber(self, objInput):
		#Create the variables
		obj = objInput
		VakNum = obj.VakNR
		rijNum = (VakNum//3)*3
		kolomNum = (VakNum%3)*3
		Nummer = obj.Getal-1
		#This is supposed to filter out the unavaible places
		#This is done by providing statements which filter out
		#numbers from the array. Each number in the array corresponds 
		#with the position in the blocks, starting from the upper left
		#corner.

		#Tested: Yes, worked fine
		locList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		if(self.rLijst[rijNum][Nummer]):
			locList = filter(lambda x: x > 2,locList)
		if(self.rLijst[rijNum+1][Nummer]):
			locList = filter(lambda x: x < 3 or x > 5,locList)
		if(self.rLijst[rijNum+2][Nummer]):
			locList = filter(lambda x: x < 6,locList)
		if(self.kLijst[kolomNum][Nummer]):
			locList = filter(lambda x: x%3 != 0,locList)
		if(self.kLijst[kolomNum+1][Nummer]):
			locList = filter(lambda x: x%3 != 1,locList)
		if(self.kLijst[kolomNum+2][Nummer]):
			locList = filter(lambda x: x%3 != 2,locList)

		#This is supposed to test the available positions
		#This is done by flattening the block so it fits with the
		#filtered array
		vakArray = self.Map[kolomNum:kolomNum + 3,rijNum:rijNum + 3].flatten('F')
		locList = filter(lambda pos: vakArray[pos] == 0, locList)
		#Check if there is only one correct location
		locList = list(locList)
		if len(locList) == 1:
			corLoc = locList[0]
			xCorLoc = kolomNum + (corLoc%3)
			yCorLoc = rijNum + (corLoc//3)
			self.Map[xCorLoc][yCorLoc] = Nummer + 1
			#Update relevant stuff
			self.kLijst[xCorLoc][Nummer] = True
			self.rLijst[yCorLoc][Nummer] = True
			self.CIV[VakNum] += 1

			#Update current block, because a number has been added
			for numbToUpdate in range(9):
				updateVak = self.vLijst[VakNum][numbToUpdate]
				if updateVak is not None:
					if updateVak.addNumberToBlock(self.CIV[VakNum]):
						heapq.heappush(self.priorQ, updateVak)

			#Update score of adjacent notes
			updateVakNum = (VakNum+3)%9
			updateVak = self.vLijst[updateVakNum][Nummer]
			if updateVak is not None:
				if updateVak.addKolom(self.CIV[updateVakNum]):
					heapq.heappush(self.priorQ, updateVak)
			#--------------------------------------

			updateVakNum = (VakNum+6)%9
			updateVak = self.vLijst[updateVakNum][Nummer]
			if updateVak is not None:
				if updateVak.addKolom(self.CIV[updateVakNum]):
					heapq.heappush(self.priorQ, updateVak)
			#--------------------------------------

			updateVakNum = (VakNum//3)*3 + (VakNum+2)%3
			updateVak = self.vLijst[updateVakNum][Nummer]
			if updateVak is not None:
				if updateVak.addRow(self.CIV[updateVakNum]):
					heapq.heappush(self.priorQ, updateVak)
			#--------------------------------------

			updateVakNum = (VakNum//3)*3 + (VakNum+1)%3
			updateVak = self.vLijst[updateVakNum][Nummer]
			if updateVak is not None:
				if updateVak.addRow(self.CIV[updateVakNum]):
					heapq.heappush(self.priorQ, updateVak)

			#Remove the info from the info list
			self.vLijst[VakNum][Nummer] = None
			return
		obj.isNotInList = True

	def printQueue(self):
		for i in heapq.nsmallest(len(self.priorQ), self.priorQ):
			print("%i - %i,%i - %i,%i" %(i.Score, i.NMP, self.CIV[i.Getal-1], i.VakKolom, i.VakRij))

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