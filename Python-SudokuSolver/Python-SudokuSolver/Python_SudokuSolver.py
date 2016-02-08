import Sudoku
rij = 9
kolom = 9

Matrix = [[-1 for y in range(rij)] for x in range(kolom)] 

rowList = ['800040000',
		   '006050009',
		   '109070300',
		   '400160000',
		   '081307090',
		   '600400015',
		   '000000001',
		   '374000960',
		   '000896034']
for i in range(len(rowList)):
	for j in range(len(rowList[i])):
		string = rowList[i]
		Matrix[j][i] = string[j]

Sudoku.Sudoku(Matrix).print()