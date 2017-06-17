#SnakeProject2, June2017
#snakeclass.py

class Snake:
    #Initializer
    def __init__(self, startpos, startlength):
        self.position = startpos
        self.length = startlength
        self.tail = []


    #Readers
    def readpos(self):
        return self.position


    def readlength(self):
        return self.length


    def readtail(self):
        return self.tail


    #Writters
    def changelen(self, amount):
        self.length += amount


    def appendtail(self, position,):
        oldlist = self.tail
        length = self.length
        oldlist.append(position)
        if len(oldlist)-1 > length:
            del oldlist[0]
        self.tail = oldlist


    def movehead(self, direction, keyset, mapdims):
        #UNPACK
        mapsize = mapdims[0]
        mapwidth = mapdims[1]
        #READ SELF
        current = self.position

        move_dirs = {
            keyset["0key_move_north"]: -mapwidth,
            keyset["0key_move_south"]: mapwidth,
            keyset["0key_move_west"] : -1,
            keyset["0key_move_east"] : 1,
        }

        #Tries to enter eastern wall
        if direction == keyset["0key_move_east"]:
            if current % mapwidth == mapwidth-1:
                return 0
        #Tries to enter western wall
        if direction == keyset["0key_move_west"]:
            if current % mapwidth == 0:
                return 0

        addition = move_dirs.get(direction, 0)
        newpos = current + addition
        if newpos >= 0:
            if newpos < mapsize:
                self.position = newpos
                return 1
        return 0

#EndofClass
