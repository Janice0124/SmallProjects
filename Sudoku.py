def find_target(grid):
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j] == -1:
				return (i, j)

def is_valid(grid):
	n = len(grid)
	for i in range(n):
		if not valid_line(grid[i]):
			return False
		col = [grid[x][i] for x in range(n)]
		if not valid_line(col):
			return False

	for i in range(1,4):
		for j in range(1, 4):
			box = grid[(i-1)*3][(j-1)*3:j*3]
			box.extend(grid[(i-1)*3+1][(j-1)*3:j*3])
			box.extend(grid[(i-1)*3+2][(j-1)*3:j*3])
			if not valid_line(box):
				return False
	return True

def valid_line(lst):
	lst = [x for x in lst if x != -1]
	return len(lst) == len(set(lst))

def solve(grid):
	n = len(grid)
	target = find_target(grid)
	if target is None:
		return True
	r, c = target
	for i in range(1, n+1):
		grid[r][c] = i
		if is_valid(grid) and solve(grid):
			return True
		grid[r][c] = -1
	return False

def solve_sudoku(grid):
	print_grid(grid)
	if solve(grid):
		print_grid(grid)
	else:
		print "No Solution"

def print_grid(grid):
	for i in range(len(grid)):
		print grid[i]

grid = [[5,8,-1,-1,-1,4,-1,6,-1],[3,-1,-1,6,-1,-1,-1,-1,8],[-1,-1,7,3,-1,-1,-1,4,-1],[8,-1,-1,-1,7,9,1,-1,-1],[-1,7,5,1,3,6,2,8, -1],[-1,-1,1,4,8,-1,-1,-1,5],[-1,9,-1,-1,-1,1,8,-1,-1],[7,-1,-1,-1,-1,3,-1,-1,1],[-1,1,-1,8,-1,-1,-1,2,7]]

grid2 = [[-1,7,-1,2,5,3,-1,-1,-1],[-1,1,-1,-1,7,-1,-1,-1,-1],[2,-1,-1,-1,-1,-1,-1,-1,6], [5,-1,-1,-1,-1,-1,1,-1,-1],[8,6,-1,3,-1,7,-1,5,9],[-1,-1,9,-1,-1,-1,-1,-1,3],[1,-1,-1,-1,-1,-1,-1,-1,7],[-1,-1,-1,-1,3,-1,-1,2,-1],[-1,-1,-1,9,2,6,-1,8,-1]]

solve_sudoku(grid)


