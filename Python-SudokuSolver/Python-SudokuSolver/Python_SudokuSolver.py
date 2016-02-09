import Sudoku
#Standaard functies
def printMatrix(matrix):
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			print(matrix[j][i], end="")
		print("")


rowList = ['800040000',
		   '006050009',
		   '109070300',
		   '400160000',
		   '081307090',
		   '600400015',
		   '000000001',
		   '374000960',
		   '000896034']
Sud = Sudoku.Sudoku(rowList)
printMatrix(Sud.getNumbers(0,2,0,2))
print("\n \n")
Sud.print()