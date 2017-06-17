#SnakeProject2, June2017
#main.py

#PublicLibraries
import msvcrt
#Private
import snakeclass
import printerpack

def getkey():
    return ord(msvcrt.getch())

def check_key(key,keyset):
    isvalid = 0
    if key == keyset["0key_move_north"]:
        isvalid = 1
    if key == keyset["0key_move_south"]:
        isvalid = 1
    if key == keyset["0key_move_west"]:
        isvalid = 1
    if key == keyset["0key_move_east"]:
        isvalid = 1
    return isvalid



def execute():
    #Variables
    mapheight = 12
    mapwidth  = 24
    mapsize = mapwidth * mapheight
    count_moves = 0

    mapdims = (mapsize, mapwidth, mapheight)
    #Keys used in game
    keyset = {
        "0key_move_north": ord("w"),
        "0key_move_south": ord("s"),
        "0key_move_west":  ord("a"),
        "0key_move_east":  ord("d"),
        "0key_exit_game":  ord("q"),
    }
    #Map charachers
    mapchars = {
        "0chr_bckg": " ",
        "0chr_brdr": "#",
        "0chr_head": "A",
        "0chr_tail": "*",
        #"":"",
    }
    #Localisation
    textpack = {
        #Ingame
        "0text_title_0": " Snake by JakubP (2017)\n",
        "0text_snake_x": "Snake X:\t",
        "0text_snake_y": "Snake Y:\t",
        "0text_snake_l": "Snake length:\t",
        "0text_moves_c": "Num of moves:\t",
        #"":"",
        #Menu
        #"":"",
    }

    #Starting Snake
    start_pos = mapsize//2
    start_len = 3
    mysnake = snakeclass.Snake(start_pos, start_len)

    #MainLoop
    while True:
        printerpack.showmap(mysnake, count_moves, mapdims, mapchars, textpack)
        key = getkey()

        isvalid = 0
        if check_key(key, keyset) == 1:
            isvalid = 1
        #if key in keyset:
        #    isvalid = 1
        if key != keyset["0key_exit_game"]:
            ismove = snakeclass.Snake.movehead(mysnake, key, keyset, mapdims)
            if ismove == 0:
                isvalid = 0
        else:
            break
            #ExitKey was hit

        if isvalid == 1:
            count_moves += 1
            pos = snakeclass.Snake.readpos(mysnake)
            snakeclass.Snake.appendtail(mysnake, pos)

    #EndofWhile
#EndofDef
