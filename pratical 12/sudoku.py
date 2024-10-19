import random
import math

def create_sudoku_puzzle(gs,num):
	l=len(gs)
	size=len(gs)**2
	required_positions=math.ceil(num*size/100)
	candidates=[]
	c=list(range(0,size))
	for _ in range(required_positions):
		p=candidates.append((random.choice(c)//l,random.choice(c)%l))

	for r,cr in candidates:
		gs[r][cr]='X'

	return gs,candidates

def initialize():
	layout_size=int(input("enter the grid size"))
	d = [['' for _ in range(layout_size)] for _ in range(layout_size)]  
	game_state=d
	game_state=fill_sudoku(game_state)
	display_grid(game_state)
	levels={1:('Very Easy',20),2:("Easy",30),3:("Medium",50),4:("Hard",70),5:("Very Hard",75)}
	print(f"There are {len(levels)} levels :")
	for i,l in enumerate(levels):
		print(f"  level {i+1} : ")
	gl=int(input("Enter level Number"))
	game_state=create_sudoku_puzzle(game_state,levels[gl][1])
	return game_state




def fill_sudoku(game_state):
	size=len(game_state)
	
	p=set(range(1,size+1))
	for row in range(size):
		for col in range(size):
			
			
			a=set(game_state[row]+[r[col] for r in game_state])
			
			candidate=list(p-a)
			game_state[row][col]=candidate[random.randint(0,len(candidate)-1)]
			
			
	return game_state
		


def display_grid(d):
	row=len(d)
	col=len(d[0])
	
	print(('.'+'-'*3)*(row)+'.')
	for i in range(row):
		print('|',end='')
		for j in range(col):
			print(f'{d[i][j]}'.center(3),end='|')
		print()
		print(('.'+'-'*3)*(row)+'.')

			
	return 0

def start(gs, ep):
    user_sol = [row[:] for row in gs]  # Make a copy of the grid for user input
    display_grid(user_sol)
    print(f"Now you need to provide values:")
    
    for r, c in ep:  # Use the empty positions from ep
        user_sol[r][c] = int(input(f"row: {r+1} col: {c+1} ({r+1},{c+1}): "))
    
    return user_sol


def stop(gs,user_sol):
	for row in range(len(gs)):
		for col in range(len(gs)):
			if gs[row][col]!=user_sol[row][col]:
				return False
	return True


def sudoku():
	gs,ep=initialize()
	user_sol=start(gs,ep)
	if stop(gs,user_sol):
		print("Congrats!, you have won the match")
	else:
		print("ohhh! your guess was wrong")


		
sudoku()