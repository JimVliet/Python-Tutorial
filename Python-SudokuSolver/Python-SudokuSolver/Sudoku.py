class Sudoku:
    #Sudoku class
	def __init__(self, matrix):
		self.Map = matrix

	def print(self):
		rij = len(self.Map)
		kolom = len(self.Map[0])
		print(rij,kolom)
		print("012345678")
		for i in range(rij):
			for j in range(kolom):
				if(self.Map[j][i] == -1):
					print("-", end="")
				else:
					print(self.Map[j][i], end="")
			print(" " + str(i))