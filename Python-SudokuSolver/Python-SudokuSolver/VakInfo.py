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

	def __lt__(self, other):
		return self.Score > other.Score
	
	def __repr__ (self):
		return str(self.Score)
	