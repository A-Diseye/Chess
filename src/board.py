from pieces import *

class Board():
    def __init__(self):
        self.__board = [[None for i in range(8)] for j in range(8)]
    
    def getPiece(self, x, y):
        return self.__board[x][y]

    def updateBoard(self, pieces):
        for piece in pieces:
            (pos_x, pos_y) = piece.getPos()
            self.__board[pos_x][pos_y] = piece
    
    def removePiece(self, pos):
        self.__board[pos[0]][pos[1]] = None
