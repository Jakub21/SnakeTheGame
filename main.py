#----#----#----#----#----#----
#SnakeTheGame, JakubP
#----#----#----#----#----#----
#IMPORT LIBRARIES
#----#----#----
#Public
from msvcrt import getch
#----#----#----
#Local
import stg_fnct_pack_00

#----#----#----#----#----#----
#VARS DECLARATION
#----#----#----
#Objects' appearance in Console	(ASCII)
char_bcgr = 0
char_wall = 87
char_tail = 83
char_head = 72
char_prize = 80

#----#----#----
#Map system
map_size = 144
width = 12
forbidden = map_size-1
map0 = [char_bcgr for q in range(map_size)]

#----#----#----
#Step system
max_step = 1024*8
notamove = 0
step = 0
illegal = 0
head_pos = (map_size//2)-( (width//2) +1)
position0 = head_pos
location_history = [forbidden for q in range(max_step)]

#----#----#----
#Input system
move = 100

#----#----#----
#Score system
score = 0
count_targets = 0

#----#----#----
#Difficulties
extension_rate = 2
lenght = 2


#----#----#----#----#----#----
#INITIALIZATION
#----#----#----
#Add walls on map's perimeter
map0 = stg_fnct_pack_00.add_perimeter0(map0, map_size, width, char_wall)


#----#----#----#----#----#----
#MAIN GAME LOOP
#----#----#----
for incr0 in range(max_step):
	#InitializeStep
	if notamove == 0:
		step += 1
	notamove = 0
	location_history[step] = head_pos

	#Add new step-specified data
	for incr1 in range(step-lenght, step):
		if location_history[incr1] != forbidden:
			map0[ location_history[incr1] ] = char_tail
	map0[head_pos] = char_head

	#InitializePrizes
	if count_targets == 0:
		prize_location = stg_fnct_pack_00.rand_prize0(map0, map_size, forbidden, char_bcgr)
		if prize_location != forbidden:
			map0[prize_location] = char_prize
			count_targets += 1
	else:
		map0[prize_location] = char_prize

	#Print map
	stg_fnct_pack_00.print_map0(map0, map_size, width, score, illegal)

	#Remove old step-specified data from map
	map0 = stg_fnct_pack_00.remove_old_data0(map0, map_size, char_head, char_tail, char_bcgr)
	#Reset variables
	illegal = 0

	#Input key
	move = ord(getch())

	#Check key
	position0 = head_pos
	#Vertical move
	if move == 119:
		head_pos -= width
	elif move == 115:
		head_pos += width
	#Horisontal move
	elif move == 97:
		head_pos -= 1
	elif move == 100:
		head_pos += 1
	#Leave game
	elif move == 8: #Backspace
		break
	elif move == 3:	#CtrlC
		break
	#Keys that are not specified here
	else:
		notamove = 1

	#Check if move is legal
	#CASE: Player hits the wall
	if map0[head_pos] == char_wall:
		illegal = 1
	#CASE: When player hits tail
	elif map0[head_pos] == char_tail:
		illegal = 1
	#CASE: Prize is found
	elif map0[head_pos] == char_prize:
		count_targets -= 1
		score += 1
		if score % extension_rate == 0:
			lenght += 1
	#Applied to every illegal move
	if illegal == 1:
		head_pos = position0
		notamove = 1

	#----#----#----
	#ENDOF GameLoop


#----#----#----
#Executed when leaving
stg_fnct_pack_00.clear0()
print("Score: ", score)


#----#----#----
#ENDOF Program
