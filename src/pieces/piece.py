from operator import ge


class Piece:
    def __init__(self, color, pos):
        self.__color = color
        self.__pos = pos
        self.__startingPos = True

    @property
    def getColor(self):
        return self.__color

    @property
    def getPos(self):
        return self.__pos

    @property
    def atStartingPos(self):
        return self.__startingPos

    @getPos.setter
    def move(self, new_pos):
        self.__startingPos = False
        self.__pos = new_pos