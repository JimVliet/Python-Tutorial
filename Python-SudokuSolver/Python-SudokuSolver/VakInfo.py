import Sudoku
class VakInfo:
	def __init__(self, Getal, VakNR, rijen, kolommen, CIV):
		self.Getal = Getal
		self.VakNR = VakNR
		self.VakRij = rijen
		self.VakKolom = kolommen
		#NMP > Non available places
		self.NMP = (3*(rijen+kolommen))-(rijen*kolommen)
		self.Score = (2**self.NMP) + (2**CIV)
		self.isNotInList = False

	def __lt__(self, other):
		return self.Score > other.Score
	
	def __repr__ (self):
		return "%i,%i,%i" % (self.Score, self.Getal, self.VakNR)

	def addKolom(self, CIV):
		self.VakKolom += 1
		self.NMP += 3-self.VakRij
		self.Score = (2**self.NMP) + (2**CIV)
		#If the VakInfo is not in the priority queue it
		#means it couldn't be saved last time. Since it
		#has been updated now it needs to be checked again
		#so that's why this is in here
		if self.isNotInList:
			return True
		return False
	
	def addRow(self, CIV):
		self.VakRij += 1
		self.NMP += 3-self.VakKolom
		self.Score = (2**self.NMP) + (2**CIV)
		if self.isNotInList:
			return True
		return False
	
	def addNumberToBlock(self, CIV):
		self.Score = (2**self.NMP) + (2**CIV)
		if self.isNotInList:
			return True
		return False