#CONSOLE IOSTREAM CONTROL FOR SNAKE

def getkey():
    import msvcrt
    return ord(msvcrt.getch())


def clear():
    import os
    os.system("cls")

def getspacing(settings):
    try:
        unit_type = settings["map_spacing_mode"]
    except:
        unit_type = "spaces"
    unit_amount = int(settings["map_spacing_amount"])
    types = {
        "tabs"  : "\t",
        "spaces": " ",
    }
    spacing = ""
    for q in range(unit_amount):
        spacing += types[unit_type]
    return spacing


def message(settings, mode="default"):
    if mode == "default":
        print(settings["err_message_mode"])
    elif mode == "leave":
        clear()
        print(settings["atleave_header"])
        print(settings["atleave_extend"])


def printstep(settings, level, cleanscreen = "clean"):
    width = int(settings["map_xsize"])
    size = width * int(settings["map_ysize"])
    cleankeys = ["clean", "yes", "cls", "cln"]
    spacing = getspacing(settings)
    if cleanscreen in cleankeys:
        clear()
    print(settings["ingame_header"])
    for index in range(size):
        if index % width == 0:
            print("")
        if level[index] == int(settings["mapsystem_empty"]):
            #print(int(settings["mapsystem_empty"]), end = spacing)
            print(chr(int(settings["mapchar_empty"])), end = spacing)

        elif level[index] == int(settings["mapsystem_wall"]):
            #print(int(settings["mapsystem_wall"]), end = spacing)
            print(chr(int(settings["mapchar_wall"])), end = spacing)

        elif level[index] == int(settings["mapsystem_head"]):
            #print(int(settings["mapsystem_head"]), end = spacing)
            print(chr(int(settings["mapchar_head"])), end = spacing)

        elif level[index] == int(settings["mapsystem_tail"]):
            #print(int(settings["mapsystem_tail"]), end = spacing)
            print(chr(int(settings["mapchar_tail"])), end = spacing)

        elif level[index] == int(settings["mapsystem_food"]):
            #print(int(settings["mapsystem_food"]), end = spacing)
            print(chr(int(settings["mapchar_food"])), end = spacing)

        #print(level[index], end = "\t")
        #print(index, end = "\t")
    print("")
