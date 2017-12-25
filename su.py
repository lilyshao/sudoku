class Sudoku:
	def __init__(self, input_string):
		self.s = input_string
		self.assignment = self.read_input(self.s);

	def solve(self):
		l = [0,0]
		if not self.find_open_cell(self.assignment, l): return True #all cells are assigned, solution found
		else:
			row, col = l[0], l[1]
			for x in range(1,10):
				if self.valid(row, col, x): #if the value doesn't violate sudoku rules
					self.assignment[row][col] = x # make temporary assignment
					if self.solve():
						return True
					else:
						self.assignment[row][col] = 0 # backtrack
			return False

	def find_open_cell(self, arr, l):
		for i in range(9):
			for j in range(9):
				if self.assignment[i][j]==0:
					l[0] = i
					l[1] = j
					# print("next open cell is: ", l, "\n")
					return True
		return False

	def valid(self, r,c,val):
		return self.rowValid(r,val) and self.colValid(c,val) and self.boxValid(r,c,val)

	def rowValid(self, row, val):
		for i in range(9):
			if self.assignment[row][i]==val: return False
		return True

	def colValid(self, col, val):
		for i in range(9):
			if self.assignment[i][col]==val: return False
		return True

	def boxValid(self, row, col, val):
		boxRow = row - row % 3;
		boxCol = col - col % 3;
		for i in range(3):
			for j in range(3):
				if self.assignment[boxRow+i][boxCol+j]==val: return False
		return True;

	def printBoard(self):
		for row in self.assignment:
			print(row)

	@staticmethod
	def read_input(s): #s is a string of 81 digits (0-9)
		assert len(s)==81, "Wrong input size; should have 81 digits! "
		data = [int(x) for x in list(s)]
		return [ data[9*i:9*i+9] for i in range(9) ]

if __name__=="__main__":
	s1 = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
	#s2 = "390060807020030050000005096900502400000000000003907002810600000030050080502090043"
	sudoku1 = Sudoku(s1)
	if sudoku1.solve():
		sudoku1.printBoard()
