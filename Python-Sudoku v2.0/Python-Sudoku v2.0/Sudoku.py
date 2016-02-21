import numpy as np
import BlockInfo as BI
import itertools
import heapq
class Sudoku:
	def __init__(self, map):
		self.map = map
		self.blockList = np.zeros((9,9), dtype=BI.BlockInfo)
		self.rowList = np.zeros((9,9), dtype=np.bool)
		self.kolList = np.zeros((9,9), dtype=np.bool)
		self.avalPosInBlock = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
		self.priorQ = []

	def updateAll(self):
		
		for y in range(9):
			for x in range(9):
				number = self.map[y][x] -1
				if number != -1:
					BlockCode = (x//3)+3*(y//3)
					self.rowList[y][number] = True
					self.kolList[x][number] = True
					self.blockList[BlockCode][number] = None
				else:
					BlockCode = (x//3)+3*(y//3)
					self.avalPosInBlock[BlockCode].append(x%3 + 3*(y%3))
		
		
		for blockNumber in range(9):
			for Getal in range(9):
				if self.blockList[blockNumber][Getal] is None:
					continue
				Block = BI.BlockInfo(self.avalPosInBlock[blockNumber], Getal +1, blockNumber)
				rijNum = (blockNumber//3)*3
				kolomNum = (blockNumber%3)*3
				if self.rowList[rijNum][Getal]:
					Block.removeAvalRow(0)
				if self.rowList[rijNum+1][Getal]:
					Block.removeAvalRow(1)
				if self.rowList[rijNum+2][Getal]:
					Block.removeAvalRow(2)
				if self.kolList[kolomNum][Getal]:
					Block.removeAvalKol(0)
				if self.kolList[kolomNum+1][Getal]:
					Block.removeAvalKol(1)
				if self.kolList[kolomNum+2][Getal]:
					Block.removeAvalKol(2)
				self.blockList[blockNumber][Getal] = Block

		self.priorQ = np.ravel(self.blockList).tolist()
		self.priorQ = [obj for obj in self.priorQ if obj is not None]
		heapq.heapify(self.priorQ)
	
	def solve(self):
		self.updateAll()
		while True:
			try:
				obj = heapq.heappop(self.priorQ)
				if self.tryNumber(obj):
					obj.isNotInList = True
			except IndexError:
				break
		
	def tryNumber(self, InputObj):
		objLen = len(InputObj.avalPos)
		if objLen != 1:
			return True
		obj = InputObj
		VakID = obj.VakNR
		rijNum = (VakID//3)*3
		kolomNum = (VakID%3)*3
		Nummer = obj.Getal-1
		if len(obj.avalPos) == 1:
			corLoc = obj.avalPos[0]
			xCorLoc = kolomNum + (corLoc%3)
			yCorLoc = rijNum + (corLoc//3)
			self.map[yCorLoc][xCorLoc] = Nummer +1

			#Update adjacent blocks
			for updateNumber in range(9):
				updateVak = self.blockList[VakID][updateNumber]
				if updateVak is not None:
					if updateVak.removeAvalPos(corLoc):
						heapq.heappush(self.priorQ, updateVak)
			
			updateBlockID = (VakID+3)%9
			blockToUpdate = self.blockList[updateBlockID][Nummer]
			if blockToUpdate is not None:
				if blockToUpdate.removeAvalKol(xCorLoc%3):
					heapq.heappush(self.priorQ, blockToUpdate)

			updateBlockID = (VakID+6)%9
			blockToUpdate = self.blockList[updateBlockID][Nummer]
			if blockToUpdate is not None:
				if blockToUpdate.removeAvalKol(xCorLoc%3):
					heapq.heappush(self.priorQ, blockToUpdate)

			updateBlockID = (VakID//3)*3 + (VakID+1)%3
			blockToUpdate = self.blockList[updateBlockID][Nummer]
			if blockToUpdate is not None:
				if blockToUpdate.removeAvalRow(yCorLoc%3):
					heapq.heappush(self.priorQ, blockToUpdate)

			updateBlockID = (VakID//3)*3 + (VakID+2)%3
			blockToUpdate = self.blockList[updateBlockID][Nummer]
			if blockToUpdate is not None:
				if blockToUpdate.removeAvalRow(yCorLoc%3):
					heapq.heappush(self.priorQ, blockToUpdate)
			return False
