#Snake
#JakubP, June 2017

#IMPORTS
from random import randint
from msvcrt import getch
from os import system

#DEFINE FUNCTIONS
def clear():
	 system("cls")
	 print("# ConsoleSnake # JakubP # 2017 #\n")

def rand_prize(map0):
	#Search for 0 cells in map0
	#Save their IDs to empty_cells_list
	incr2 = 20
	empty_cells_list = [forbidden for q in range(map_size+5)]
	for incr1 in range(map_size):
		if map0[incr1] == 0:
			empty_cells_list[incr2] = incr1
			incr2 += 1
	#Return random cell from empty_cells_list
	random_id = randint(0, map_size)
	return empty_cells_list[random_id]

#BASIC VARS
#Map
map_size = 144	#24**2 = 576
width = 12		#24
#Game runs out of declared memory after this amount of steps
max_step = 1024*4
#Ascii characters representing objects (Console only)
char_bcgr = 0
char_wall = 87
char_tail = 83
char_head = 72
char_prize = 80
#Just for system
forbidden = map_size-1
#Declaring those to avoid errors
move = 100	#D
notamove = 0
step = 0
illegal = 0
#Prizes system
score = 0
count_targets = 0
#Difficulty
extending_ratio = 2	#Add +1 lenght every $ score gained
#Define map table
map0 = [char_bcgr for q in range(map_size)]

#CREATE WALLS ON MAP'S PERIMETER
for incr0 in range(map_size):
	if incr0 < width:
		map0[incr0] = char_wall
	elif incr0 %width == 0:
		map0[incr0] = char_wall
	elif incr0 %width == width-1:
		map0[incr0] = char_wall
	elif incr0 > map_size -width:
		map0[incr0] = char_wall

#SNAKE DATA
lenght = 5
#Set start position
head_pos = map_size//2
head_pos -= width//2
head_pos -= 1
#----#----#----
position0 = head_pos
#Define table for tail data
location_history = [forbidden for q in range(max_step)]


#----#----#----#----#----#----
#MAIN GAME LOOP
for incr0 in range(max_step):
	#InitializeStep
	if notamove == 0:
		step += 1
	notamove = 0
	location_history[step] = head_pos

	#Clear step-specified data
	for incr1 in range(map_size):
		if map0[incr1] == char_head:
			map0[incr1] = char_bcgr
		elif map0[incr1] == char_tail:
				map0[incr1] = char_bcgr

	#Fill map
	for incr1 in range(step-lenght, step):
		if location_history[incr1] != forbidden:
			map0[ location_history[incr1] ] = char_tail
	map0[head_pos] = char_head

	#InitializePrizes
	if count_targets == 0:
		prize_location = rand_prize(map0)
		if prize_location != forbidden:
			map0[prize_location] = char_prize
			count_targets += 1
	else:
		map0[prize_location] = char_prize

	#Print map
	clear()
	for incr1 in range(map_size):
		if incr1 % width == 0:
			print("\r")
		print(chr(map0[incr1]), end = " ")
		#print(map0[incr1], end = "\t")

	#Notifications and others
	print("\r")
	print("Score: ", score)
	#DEVELOPMENT
	print("Lenght: ", lenght)
	print("PrLoc:", prize_location, "(Row: ", prize_location//width, ")")
	#----#----#---
	if illegal != 0:
		print("You cannot move here!")
	illegal = 0

	#Input
	move = ord(getch())

	#Move head
	#Set it to current position
		#Original can be reverted in case of illegal move
	position0 = head_pos

	#Vertical
	if move == 119:
		head_pos -= width
	elif move == 115:
		head_pos += width
	#Horisontal
	elif move == 97:
		head_pos -= 1
	elif move == 100:
		head_pos += 1
	#Leave game
	elif move == 8: #Backspace
		break
	elif move == 3:	#CtrlC
		break
	#Other key
	else:
		notamove = 1

	#Check if move is legal
	#When player hits wall
	if map0[head_pos] == char_wall:
		illegal = 1
	#When player hits tail
	elif map0[head_pos] == char_tail:
		illegal = 1
	#Prize is found
	elif map0[head_pos] == char_prize:
		count_targets -= 1
		score += 1
		if score % extending_ratio == 0:
			lenght += 1
	#Common
	if illegal == 1:
		head_pos = position0
		notamove = 1

	#ENDOF Game Loop

clear()
print("Score: ", score)
#ENDOF Program
