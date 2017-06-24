class Snake:


    def __init__(self, settings):
        def starting_position(self, settings):
            width = int(settings["map_xsize"])
            height = int(settings["map_ysize"])
            posx = width//2
            posy = height//2
            position = (posy * width) + posx
            return position
        self.length = int(settings["snake_len"])
        self.head_pos = starting_position(self, settings)
        self.tail = []

    #READERS

    def read_head(self):
        return self.head_pos
    def read_len(self):
        return self.length
    def read_tail(self):
        return self.tail

    #MODIFIERS

    def changelen(self, amount):
        self.length += amount


    def appendtail(self, position):
        prevtail = self.tail
        length = self.length
        prevtail.append(position)
        if len(prevtail) > length:
            del prevtail[0]
        self.tail = prevtail

    #
    def movehead(self, settings, level, direction):
        width = int(settings["map_xsize"])
        height = int(settings["map_ysize"])
        current = self.head_pos
        newposition = current
        if   direction == "n":
            newposition = current - width
        elif direction == "s":
            newposition = current + width
        elif direction == "w":
            newposition = current -1
        elif direction == "e":
            newposition = current +1

        valid_togo = [
            int(settings["mapsystem_empty"]),
            int(settings["mapsystem_food"])
        ]

        if level[newposition] not in valid_togo:
            newposition = current
            return 0

        if newposition != current:
            self.head_pos = newposition
            return 1
        else:
            return 0
