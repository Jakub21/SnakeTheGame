#----#----#----#----#----#----
#JakubP
#SnakeTheGame Function Pack 00
#----#----#----#----#----#----
from random import randint
from os import system
#----#----#----
#Clears screen
def clear0():
	 system("cls")
	 print("# SnakeTheGame # JakubP # 2017 #")

#----#----#----
#Shows map and notifications on screen
def print_map0(map_table, map_size, map_width, player_score, moves_illegal):
	#Clear screen and print Header
	clear0()
	#Print map itself
	for incr_f0 in range(map_size):
		if incr_f0 % map_width == 0:
			print("\r")
		print(chr( map_table[incr_f0] ), end = " ")
	#Print notifications
	print("\nScore: ", player_score)
	if moves_illegal != 0:
		print("You cannot move here!")

#----#----#----
#Chooses location of new prize
def rand_prize0(map_table, map_size, forbd_loc, chr_bcgr):
	#Search for 0 cells in map_table
	#Save their IDs to empty_cells_list
	incr_f0 = 0
	empty_cells_list = [forbd_loc for q in range(map_size+5)]
	for incr_f1 in range(map_size):
		if map_table[incr_f1] == chr_bcgr:
			empty_cells_list[incr_f0] = incr_f1
			incr_f0 += 1
	#Return random cell from empty_cells_list table
	random_id = randint(0, map_size)
	return empty_cells_list[random_id]

#----#----#----
#Adds walls on map's perimeter
def add_perimeter0(map_table, map_size, width, chr_wall):
	for incr_f0 in range(map_size):
		if incr_f0 < width:
			map_table[incr_f0] = chr_wall
		elif incr_f0 %width == 0:
			map_table[incr_f0] = chr_wall
		elif incr_f0 %width == width-1:
			map_table[incr_f0] = chr_wall
		elif incr_f0 > map_size -width:
			map_table[incr_f0] = chr_wall
	return map_table

#----#----#----
#Removes StepSpecified data from map
def remove_old_data0(map_table, map_size, chr_head, chr_tail, chr_bcgr):
	for incr1 in range(map_size):
		if map_table[incr1] == chr_head:
			map_table[incr1] = chr_bcgr
		elif map_table[incr1] == chr_tail:
				map_table[incr1] = chr_bcgr
	return map_table
