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

#BASIC VARS
#Map
map_size = 576	#144
width = 24		#12
#Game runs out of declared memory after this amount of steps
max_step = 1024*2
#Ascii characters representing objects (Console only)
char_bcgr = 0
char_wall = 87
char_tail = 83
char_head = 72
#Just for system
forbidden = map_size-1
#Declaring those to avoid errors
move = 'j'
notamove = 0
step = 0
illegal = 0
#Define map table
ground = [char_bcgr for q in range(map_size)]

#CREATE WALLS ON MAP'S PERIMETER
for q in range(map_size):
	 if q < width:
		  ground[q] = char_wall
	 elif q%width == 0:
		  ground[q] = char_wall
	 elif q%width == width-1:
		  ground[q] = char_wall
	 elif q > map_size- width:
		  ground[q] = char_wall

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

#MAIN GAME LOOP
for incr0 in range(max_step):
	#InitializeStep
	if notamove == 0:
		step += 1
	notamove = 0
	location_history[step] = head_pos

	#Clear step-specified data
	for incr1 in range(map_size):
		if ground[incr1] == char_head:
			ground[incr1] = char_bcgr
		elif ground[incr1] == char_tail:
				ground[incr1] = char_bcgr

	#Fill map
	for incr1 in range(step-lenght, step):
		if location_history[incr1] != forbidden:
			ground[ location_history[incr1] ] = char_tail
	ground[head_pos] = char_head

	#Print map
	clear()
	for incr1 in range(map_size):
		if incr1 % width == 0:
			print("\r")
		print(chr(ground[incr1]), end = " ")

	#Notifications and others
	print("\r")
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
	if ground[head_pos] == char_wall:
		illegal = 1
	#When player hits tail
	if ground[head_pos] == char_tail:
		illegal = 1
	#Common
	if illegal == 1:
		head_pos = position0
		notamove = 1

	#ENDOF Game Loop

clear()
#ENDOF Program
