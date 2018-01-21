'''
- fill diagonal boxes first:
box 1,5,9 are independent, just need to check boxValid
- recursively fill out the rest: using solve()
- remove k cells from the complete board
'''
import random
import solver

# calls fill_box() for box 1,5,9
def fill_diagonal(grid):
	for i in range(0, 9, 3):
		fill_box(grid, i, i)

def fill_box(grid, start_row, start_col):
	for i in range(3):
		for j in range(3):
			while True:
				val = random.randint(1, 9)
				if solver.boxValid(grid, start_row, start_col, val):
					break
			grid[start_row+i][start_col+j] = val

# problem?: not unique solution?
def fill_rest(grid):
	solver.solve(grid)

def remove_cells(grid, k):
	count = 0
	while count < k:
		val = random.randint(0, 80)
		r, c = val // 9, val % 9
		if grid[r][c] != 0:
			grid[r][c] = 0
			count += 1

def gen_sudoku(num_cells=60):
	board = [[0]*9 for i in range(9)]
	fill_diagonal(board)
	fill_rest(board)
	remove_cells(board, 81-num_cells)
	solver.print_board(board)
	return board

# def gen_sudoku_unique():

if __name__=="__main__":
	gen_sudoku()
