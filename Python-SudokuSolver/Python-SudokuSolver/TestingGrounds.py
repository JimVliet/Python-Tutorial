import numpy as np
import heapq
import VakInfo
import random
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


class testClass():
	def __init__(self, score, code):
		self.Score = score
		self.Code = code

	def __lt__(self, other):
		return self.Score > other.Score
	
	def __repr__ (self):
		return "{%i,%i}"%(self.Score, self.Code)

def testFunc():
	
	for corLoc in range(9):
		for VakNum in range(9):
			rijNum = (VakNum//3)*3
			kolomNum = (VakNum%3)*3
			xCorLoc = kolomNum + (corLoc%3)
			yCorLoc = rijNum + (corLoc//3)
			print("%i,%i + [%i,%i]"%(corLoc, VakNum, xCorLoc, yCorLoc))

def sliceTest():
	lijst = np.arange(81).reshape((9,9))
	VakNum = 8
	rijNum = (VakNum//3)*3
	kolomNum = (VakNum%3)*3
	print(lijst)
	print(lijst[kolomNum:kolomNum + 3,rijNum:rijNum + 3])