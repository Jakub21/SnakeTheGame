#Snake the Game
from msvcrt import getch
from random import randint
import os
def clear():
	os.system("cls")
clear()
w, h = 30, 30
area = w*h
table = [0 for a in range(area)]
player_pos = area//2+(w//2)
player_pos_old = area//2+(w//2)
player_pos_history = [area-1 for i in range((area**2)*2)]
last_dir = 0
move = 0
move_count = 0
prize_count = 0
debug_mode = 0
illegal_move = 0
score = 0
for c in range(area):
	if c%w == 0:
		table[c] = 88
	if c%w == w-1:
		table[c] = 88
	if c <= w:
		table[c] = 88
	if c > area-w:
		table[c] = 88
while True:
	it_wasnt_move = 0
	if prize_count == 0:
		while not prize_count:
			prize_location = randint(0,area-(w+1))
			if table[prize_location] == 0:
				table[prize_location] = 35
				prize_count += 1
	clear()
	for c in range(area):
		if c == player_pos:
			if last_dir == 1:
				print(chr(30), end = " ")
			elif last_dir == 2:
				print(chr(16), end = " ")
			elif last_dir == 3:
				print(chr(31), end = " ")
			elif last_dir == 4:
				print(chr(17), end = " ")
		else:
			print(chr(table[c]), end = " ")
			if (c % w)+1 == w:
				print('\r')
	print('Score:  ', score)
	print('Move count', move_count)
	if illegal_move == 1:
		print("You cannon move here!\r")
		illegal_move = 0
	if debug_mode == 1:
		print('Info for development', 2*chr(25))
		print(chr(26), '\tPlayer position', player_pos)
		print(chr(26), '\tPrize position', prize_location)
		print(chr(26), '\tPrize count', prize_count)
		print(chr(26), '\tKey ID', move)
		print(chr(26), '\tID of block under your head ', table[player_pos])
		print(chr(26), '\tPlayerPosHistory(Tail) ')
		print('\t', end = '')
		for i in range(move_count, move_count-score, -1):
			print(player_pos_history[i], end = ", ")
		print('\n')
	player_pos_older = player_pos_old
	player_pos_old = player_pos
	old_last_dir = last_dir
	move = ord(getch())
	if move == 119:
		player_pos = player_pos-w
		last_dir = 1
	elif move == 115:
		player_pos = player_pos+w
		last_dir = 3
	elif move == 97:
		player_pos = player_pos-1
		last_dir = 4
	elif move == 100:
		player_pos = player_pos+1
		last_dir = 2
	elif move == 104:
		#DebugMode
		if debug_mode == 0:
			debug_mode = 1
		else:
			debug_mode = 0
		it_wasnt_move = 1
	elif move == 8:
		it_wasnt_move = 1
		clear()
		break
	if table[player_pos] == 88:
		player_pos = player_pos_old
		illegal_move = 1
	else:
		if it_wasnt_move == 0:
			move_count += 1
	if table[player_pos] == 35:
		prize_count += -1
		table[player_pos] = 0
		score += 1
	for i in range(w, area-w):
		if table[i] == 111:
			table[i] = 0
	for i in range(move_count, move_count-score, -1):
		table[player_pos_history[i]] = 111
	player_pos_history[move_count] = player_pos
	#-#-#-#-#-#-
	#INFO
	#-#-#-#-#-#-
	#ASCII Codes
	#		#Wall			88
	#		#HeadingU		30
	#		#HeadingD		31
	#		#HeadingL		17
	#		#HeadingR		16
	#		#TailUnit		111
	#-#-#-#-#-#-
	#Key Codes
	#		#MoveU			LetterW				119
	#		#MoveD			LetterS				115
	#		#MoveL			LetterA				97
	#		#MoveR			LetterD				100
	#		#ViewDebug		LetterH				104
	#		#Exit			Backspace			8
	#-#-#-#-#-#-
	#Platforms
	#		#Function clear() may not work properly on some platforms
	#		#Program tested on up-to-date Windows 7 x64 in mid-2017
	#-#-#-#-#-#-
	#Copyright
	#		#Written by JakubP, May 2017
	#		#Free to distribute and modify code
	#-#-#-#-#-#-
