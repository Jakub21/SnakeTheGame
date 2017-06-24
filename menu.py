import iocontrol
import msvcrt

def printmenu(settings, index, limit):
    iocontrol.clear()
    print(settings["menu_header"])
    for q in range(1, limit+1):
        dict_key = "menu_opt" + str(q)
        try:
            current_name = settings[dict_key]
        except:
            current_name = dict_key + "---!localisation_error"
        if q == index:
            pointer = ">"
            print(" ", pointer, current_name)
        else:
            print("   ", current_name)

def main(settings):
    #Vars that should be moved to Settings
    break_keys = [int(settings["key_confirm"]), 3]
    max_index = 4
    #Locals
    key = 1
    index = 1
    limit = int(settings["numof_menu_opts"])
    while True:
        printmenu(settings, index, limit)
        key = ord(msvcrt.getch())
        #check key
        if key == int(settings["key_move_up"]):
            index -= 1
        elif key == int(settings["key_move_down"]):
            index +=  1
        elif key == int(settings["key_confirm"]):
            break
        elif key == 3:
            return 0
        #else: return index
        #close index loop
        if index == limit+1:
            index = 1
        if index == 0:
            index = limit
        #---
    return index
