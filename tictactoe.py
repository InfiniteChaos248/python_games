###################################################################
def input_details():
	'''
	function to get details of player name and marker
	Arguments : none
	Return : dictionary with name and marker of players 1 and 2
	'''
	det = {'p1':[],'p2':[]}
	det['p1'].append(input('Enter your name player1 : '))
	det['p2'].append(input('Enter your name player2 : '))
	while True: 
		print(f"{det['p1'][0]} X or O ? ")
		m = input()
		if(m == 'X' or m == 'O'):
			break
	det['p1'].append(m)
	if det['p1'][1]=='X':
		det['p2'].append('O')
	else:
		det['p2'].append('X')
	return det
########################################################################	
def display_tiles():
	'''
	prints the numbers corresponding to the location to place markers
	Arguments : none
	Return : none
	'''
	print('7|8|9')
	print('-----')
	print('4|5|6')
	print('-----')
	print('1|2|3')	
	print('When your turn comes, type in a number from the above grid to place your marker there.')
#######################################################################
def display_board(markers):
	'''
	displays the tic tac toe board with the markers indicated by the list
	Argument : list containing the markers
	Return : none
	'''
	print(f'{markers[6]}|{markers[7]}|{markers[8]}')
	print('-----')
	print(f'{markers[3]}|{markers[4]}|{markers[5]}')
	print('-----')
	print(f'{markers[0]}|{markers[1]}|{markers[2]}')
#######################################################################
def check(m):
	'''
	Function to check if there is a win condition present on the board
	Arguments : List of markers
	Return : True if win condition is met else returns False
	'''
	if m[0] == m[1] == m[2] != ' ': #=='X' or m[0] == m[1] == m[2] =='O':
		return True
	if m[3] == m[4] == m[5] != ' ': #=='X' or m[3] == m[4] == m[5] =='O':
		return True	
	if m[6] == m[7] == m[8] != ' ': #=='X' or m[6] == m[7] == m[8] =='O':
		return True		
	if m[0] == m[3] == m[6] != ' ': #=='X' or m[0] == m[3] == m[6] =='O':
		return True		
	if m[1] == m[4] == m[7] != ' ': #=='X' or m[1] == m[4] == m[7] =='O':
		return True		
	if m[2] == m[5] == m[8] != ' ': #=='X' or m[0] == m[4] == m[8] =='O':
		return True		
	if m[2] == m[4] == m[6] != ' ': #=='X' or m[2] == m[4] == m[6] =='O':
		return True		
	return False
	
#################### START OF PROGRAM #########################	
print('TIC-TAC-TOE')
input('Start?')
d = input_details()
#display which player has which marker - make into function
print(f"{d['p1'][0]} has marker {d['p1'][1]} and {d['p2'][0]} has marker {d['p2'][1]}")
input('Proceed?')
#again is True then loop executes
again = True
while again:
	#l is the List of markers
	l = [' '] * 9
	display_tiles()
	#this while cycles through each roatation of moves - p1 and p2
	while True:
		#this while is to make sure marker is now overwritten by p1
		while True:
			k = int(input(f"{d['p1'][0]}'s Turn : "))
			if l[k-1] == ' ':
				break
			else:
				print('Marker already placed there, Try again.')
		#place the marker of p1		
		l[k-1] = d['p1'][1]
		#display the board after move of player 1
		display_board(l)
		#this checks win condition - checked after every individual move
		if check(l):
			print(f"{d['p1'][0]} wins :)")
			print(f"Better luck next time {d['p2'][0]}")
			break
		#this checks the draw condition	
		if not ' ' in l:
			print('Draw')
			break		
		##check and break here -- done
		#this while is to make sure marker is now overwritten by p2
		while True:
			k = int(input(f"{d['p2'][0]}'s Turn : "))
			if l[k-1] == ' ':
				break
			else:
				print('Marker already placed there, Try again.')
		#place the marker of p1			
		l[k-1] = d['p2'][1]
		#display the board after move of player 1
		display_board(l)
		#this checks win condition - checked after every individual move
		if check(l):
			print(f"{d['p2'][0]} wins :)")
			print(f"Better luck next time {d['p1'][0]}")
			break
		##check and break here -- done
		##add logic to not overwrite values -- done
		##add logic to say if match is draw -- done
		#keep asking till yes or no, make function if possible
	again = 'yes' in input('Do you want to play again?(yes/no) : ').lower()
print('done')		
##add logic to ask replay or quit -- done
#################### END OF PROGRAM ###########################
#add logic to change marker if needed, ask during proceed
#at start ask for single player vs AI or 2 player
#add AI
#add random player first logic

