class BlockInfo:
	def __init__(self, avalPos, Getal, VakNR):
		self.avalPos = avalPos
		self.Getal = Getal
		self.VakNR = VakNR
		self.isNotInList = False

	def __lt__(self, other):
		return len(self.avalPos) < len(other.avalPos)

	def __repr__(self):
		return "%i,%i,%s" % (self.Getal, self.VakNR, self.avalPos)

	def removeAvalRow(self, rowNumb):
		self.avalPos = [pos for pos in self.avalPos if pos//3 != rowNumb]
		return self.isNotInList

	def removeAvalKol(self, kolNumb):
		self.avalPos = [pos for pos in self.avalPos if pos%3 != kolNumb]
		return self.isNotInList

	def removeAvalPos(self, position):
		try:
			self.avalPos.remove(position)
			return self.isNotInList
		except ValueError:
			return False