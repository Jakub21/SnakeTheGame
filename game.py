
def generatemap(settings):
    width = int(settings["map_xsize"])
    height = int(settings["map_ysize"])
    size = width * height
    ####
    id_empty = int(settings["mapsystem_empty"])
    id_wall = int(settings["mapsystem_wall"])
    #Define level
    level = [id_empty for q in range(size)]
    for q in enumerate(level):
        index = q[0]
        if index < width:
            level[index] = id_wall
        if index > size-width:
            level[index] = id_wall
        if index % width == 0:
            level[index] = id_wall
        elif index % width == width-1:
            level[index] = id_wall

    return level

def init(settings):
    import snake_class

    width = int(settings["map_xsize"])
    height = int(settings["map_ysize"])
    size = width * height
    #Get map
    level = generatemap(settings)
    #Create snake
    newsnake = snake_class.Snake(settings)
    #Play
    execute(settings, level, newsnake)


def execute(settings, level, newsnake):
    import iocontrol
    import snake_class
    import msvcrt
    import time

    width = int(settings["map_xsize"])
    height = int(settings["map_ysize"])
    size = width * height

    #Declarations
    direction = ""
    count_moves = 0

    while True:
        #Clear and read updated snake
        for q in enumerate(level):
            index = q[0]
            if level[index] == int(settings["mapsystem_head"]):
                level[index] = int(settings["mapsystem_empty"])
            if level[index] == int(settings["mapsystem_tail"]):
                level[index] = int(settings["mapsystem_empty"])


        headpos = snake_class.Snake.read_head(newsnake)
        tail = snake_class.Snake.read_tail(newsnake)

        #Write new snake on map
        for q in enumerate(level):
            index = q[0]
            if index in tail:
                level[index] = int(settings["mapsystem_tail"])
        level[headpos] = int(settings["mapsystem_head"])

        #Print map
        iocontrol.printstep(settings, level)

        #Steering
        time.sleep(float(settings["step_time"]))
        if msvcrt.kbhit():
            key = iocontrol.getkey()
            if key == int(settings["key_move_up"]):
                direction = "n"
            if key == int(settings["key_move_down"]):
                direction = "s"
            if key == int(settings["key_move_left"]):
                direction = "w"
            if key == int(settings["key_move_right"]):
                direction = "e"

        #Check move
        vld = snake_class.Snake.movehead(newsnake, settings, level, direction)
        if vld == 1:
            count_moves += 1
            snake_class.Snake.appendtail(newsnake, headpos)

        #EndofWHILE

    #EndofDEF
