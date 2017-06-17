#SnakeProject2, June2017
#printerpack.py

#PublicLibraries
import os
#SnakeClass
import snakeclass

def clear():
    os.system("cls")
    #TODO:ItsNotCrossPlatform

def showmap(mysnake, now_move, mapdims, mapchars, textpack):
    #UNPACK DATA
    mapsize = mapdims[0]
    mapwidth = mapdims[1]

    chr_bcgr = mapchars["0chr_bckg"]
    chr_brdr = mapchars["0chr_brdr"]
    chr_head = mapchars["0chr_head"]
    chr_tail = mapchars["0chr_tail"]

    text_game = textpack["0text_title_0"]
    text_posx = textpack["0text_snake_x"]
    text_posy = textpack["0text_snake_y"]
    text_leng = textpack["0text_snake_l"]
    text_move = textpack["0text_moves_c"]

    #READ FROM OBJECT
    snake_pos = snakeclass.Snake.readpos(mysnake)
    snake_len = snakeclass.Snake.readlength(mysnake)
    #READ TAIL
    snake_tail = snakeclass.Snake.readtail(mysnake)
    #COMPUTE COORDINATES
    snake_x = snake_pos % mapwidth
    snake_y = (snake_pos-snake_x) // mapwidth

    #BEGIN PRINTING
    clear()
    print(text_game)

    #TOP BORDER
    print("", chr_brdr * (mapwidth+2))
    print("", chr_brdr, end = "")

    #MAP ITSELF
    for i in range(mapsize):
        if i % mapwidth == 0:
            if i != 0:
                print(chr_brdr ,"\n", chr_brdr, end = "")
        #---#-v-#IsNotBorder#-v-#---#
        if i == snake_pos:
            print (chr_head, end = "")
        elif i in snake_tail:
            print(chr_tail, end = "")
        else:
            print(chr_bcgr, end = "")

    #BOTTOM BORDER
    print(chr_brdr, end = "")
    print("\n", chr_brdr * (mapwidth+2), "\n")

    #INFO
    print(text_posx, snake_x)
    print(text_posy, snake_y)
    print(text_leng, snake_len)
    print(text_move, now_move)

#EndofDef
