import copy


# full bomb grid function
def allbomb(r, c, grid):
	for i in range(r):
		for j in range(c):
			grid[i][j] = 'O'
	return grid


def bomberman(n, grid):
	# width and height
	r = len(grid)
	c = len(grid[0])

	# strings to lists
	grid = [list(i) for i in grid]

	# if n is even grid is full
	if n % 2 == 0:
		grid = allbomb(r, c, grid)

	# exsplosion
	elif n % 4 == 3:
		# create full bomb grid copy
		temp_grid = allbomb(r, c, copy.deepcopy(grid))

		# get indexes from grid and explode on temp
		for x, i in enumerate(grid):
			for y, j in enumerate(i):
				if j == 'O':
					# detonate center
					temp_grid[x][y] = '.'

					# detonate left cell
					if y > 0:
						temp_grid[x][y-1] = '.'

					# detonate right cell
					if y < c - 1:
						temp_grid[x][y+1] = '.'

					# detonate upper cell
					if x > 0:
						temp_grid[x-1][y] = '.'

					# detonate lower cell
					if x < r - 1:
						temp_grid[x+1][y] = '.'
		grid = temp_grid
	return grid

try:
	n = int(input('Please, enter number of seconds: '))

	if n < 1:
		raise ValueError('Please, enter the positive integer!')

	grid =[
	    '.......', 
	    '...O...', 
	    '....O..', 
	    '.......', 
	    'OO.....', 
	    'OO.....'
	    ]

	final = bomberman(n, grid)

	for i in final:
		print(''.join(i))

except ValueError as e:
	print(e)
except Exception as e:
	print(e)