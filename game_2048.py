import random
import os
from pynput.keyboard import Key, Listener

def shift_left(rc):
	x = rc.count(0)
	for i in range(x):
		rc.remove(0)
		rc.append(0)
	return rc

def compute(rc):
	for x in range(3):
		if rc[x] != rc[x+1]:
			continue
		if rc[x] == 0:
			break
		if rc[x] == rc[x+1]: 
			rc[x] = rc[x] + rc[x+1]
			global score
			score = score + rc[x]
			rc[x+1] = 0
			shift_left(rc)
	return rc

def row_col_flip(rowcols):
	rcs = []
	for x in range(4):
		rc = []
		rc.extend(l[x] for l in rowcols)
		rcs.append(rc)
	return rcs

def split(grid):
	rcs = []
	for i in range(0,16,4):
		rcs.append(grid[i:i+4])
	return rcs

def merge(rcs):
	grid = []
	for rc in rcs:
		grid.extend(rc)
	return grid

def rev(rcs):
	for rc in rcs:
		rc.reverse()
	return rcs

def to_str(n):
	if n == 0:
		return ' '
	return str(n)

def display_grid(grid):
	print(to_str(grid[0]) + '\t' + to_str(grid[1]) + '\t' + to_str(grid[2]) + '\t' + to_str(grid[3]) + '\n')
	print(to_str(grid[4]) + '\t' + to_str(grid[5]) + '\t' + to_str(grid[6]) + '\t' + to_str(grid[7]) + '\n')
	print(to_str(grid[8]) + '\t' + to_str(grid[9]) + '\t' + to_str(grid[10]) + '\t' + to_str(grid[11]) + '\n')
	print(to_str(grid[12]) + '\t' + to_str(grid[13]) + '\t' + to_str(grid[14]) + '\t' + to_str(grid[15]) + '\n')

def is_over(grid):
	if grid.count(0) > 0:
		return False
	rows = split(grid)
	for row in rows:
		for i in range(3):
			if row[i] == row[i+1]:
				return False
	cols = row_col_flip(rows)
	for col in cols:
		for i in range(3):
			if col[i] == col[i+1]:
				return False
	return True

def listify(grid, direction):
	if direction == 'left':
		rows = split(grid)
		return rows
	if direction == 'up':
		cols = row_col_flip(split(grid))
		return cols
	if direction == 'right':
		rows = rev(split(grid))
		return rows
	if direction == 'down':
		cols = rev(row_col_flip(split(grid)))
		return cols

def delistify(rcs, direction):
	if direction == 'left':
		grid = merge(rcs)
		return grid
	if direction == 'up':
		grid = merge(row_col_flip(rcs))
		return grid
	if direction == 'right':
		grid = merge(rev(rcs))
		return grid
	if direction == 'down':
		grid = merge(row_col_flip(rev(rcs)))
		return grid

def move(grid, direction):
	rcs = listify(grid, direction)
	for rc in rcs:
		rc = compute(shift_left(rc))
	grid = delistify(rcs, direction)
	return grid

def random_index(grid):
	indices = [i for i, val in enumerate(grid) if val==0]
	if len(indices) != 0:
		return random.choice(indices)
	return -1
	
# grid = [1024,512,2,128,32,256,128,16,8,16,32,2,2,4,8,2]
grid = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
score = 0
grid[random_index(grid)] = random.choice([2,4])
grid[random_index(grid)] = random.choice([2,4])

def on_release(key):
	if key == Key.up:
		dir.append('up')
	elif key == Key.down:
		dir.append('down')
	elif key == Key.left:
		dir.append('left')
	elif key == Key.right:
		dir.append('right')		
	return False

print('2048')
input('Press any key to start ...')
while not is_over(grid):
	os.system('cls')
	print(f'score : {score}')
	print('')
	display_grid(grid)
	for n in grid:
		if n == 2048:
			reply = input('You reached 2048 !!! Nice ... Do you want to keep going(y/n)? ')
			if not reply == 'y' or not reply == 'Y':
				break
	dir = list()
	with Listener(on_release=on_release) as listener:
		listener.join()
	# dir = input('A/S/W/D : ')
	# if dir == 'A' or dir == 'a':
	# 	dir = 'left'
	# elif dir == 'S' or dir == 's':
	# 	dir = 'down'
	# elif dir == 'W' or dir == 'w':
	# 	dir = 'up'
	# elif dir == 'D' or dir == 'd':
	# 	dir = 'right'
	# else:
	# 	continue
	before_move = grid
	if len(dir) != 0:
		grid = move(grid, dir[0])
	if grid != before_move:
		x = random_index(grid)
		if x != -1:
			#grid[x] = random.choice([2,4])
			grid[x] = 2			

os.system('cls')
display_grid(grid)		
print('')
print(f'final score : {score}')
print('GAME OVER')				