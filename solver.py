'''mostly borrowed from 1.py
pass 2-d array assignement to methods
initiate it in main
'''

def read_input(s): #s is a string of 81 digits (0-9)
	assert len(s)==81, "Wrong input size; should have 81 digits! "
	data = [int(x) for x in list(s)]
	return [ data[9*i:9*i+9] for i in range(9) ]

def print_board(arr):
	for row in arr:
		print(row)

def valid(arr, r, c, val):
	return rowValid(arr, r, val) and colValid(arr, c, val) and boxValid(arr, r, c, val)

def rowValid(arr, row, val):
	for i in range(9):
		if arr[row][i]==val: return False
	return True

def colValid(arr, col, val):
	for i in range(9):
		if arr[i][col]==val: return False
	return True

def boxValid(arr, row, col, val):
	boxRow = row - row % 3;
	boxCol = col - col % 3;
	for i in range(3):
		for j in range(3):
			if arr[boxRow+i][boxCol+j]==val: return False
	return True

def done(arr):
	return all([arr[i][j] != 0 for i in range(9) for j in range(9)])

def find_open_cell(arr):
	for i in range(9):
		for j in range(9):
			if arr[i][j]==0:
				return (i, j)
	return (-1, -1)

def solve(arr): # re
	if done(arr): return True #all cells are assigned, solution found
	else:
		row, col = find_open_cell(arr)
		for x in range(1,10):
			if valid(arr, row, col, x): #if the value doesn't violate sudoku rules
				arr[row][col] = x # make temporary assignment
				if solve(arr):
					return True
				else:
					arr[row][col] = 0 # backtrack
		return False

if __name__=="__main__":
	s1 = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
	#s2 = "390060807020030050000005096900502400000000000003907002810600000030050080502090043"
	assignment = read_input(s1)
	solve(assignment)
	print_board(assignment)
