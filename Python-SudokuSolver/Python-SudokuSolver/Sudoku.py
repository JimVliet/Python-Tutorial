
class Sudoku:
    #Sudoku class
	def __init__(self, lijst):
		self.rij = len(lijst)
		self.kolom = len(lijst[0])
		Matrix = [[-1 for y in range(self.rij)] for x in range(self.kolom)]
		for i in range(len(lijst)):
			for j in range(len(lijst[i])):
				string = lijst[i]
				Matrix[j][i] = string[j]
		self.Map = Matrix

	def print(self):
		rij = len(self.Map)
		kolom = len(self.Map[0])
		print("012345678")
		for i in range(rij):
			for j in range(kolom):
				if(int(self.Map[j][i]) == 0):
					print("-", end="")
				else:
					print(self.Map[j][i], end="")
			print(" " + str(i))
	def getNumber(self, xCoord, yCoord):
		return self.Map[xCoord][yCoord]

	def getNumbers(self, xStart, xEind, yStart, yEind):
		return self.Map[xStart:(xEind+1),yStart:(yEind+1)]