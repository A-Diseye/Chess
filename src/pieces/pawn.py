from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.enPassant = False

    def getMoves(self, board):
        moves = []
        pos = self.getPos
        if self.getColor == "white":
            new_y = pos[1]+1
            #move two spots check
            if self.atStartingPos:
                if board.getPiece(pos[0],new_y) is None and board.getPiece(pos[0],new_y+1) is None:
                    moves.append((pos[0], new_y+1))
        else:
            new_y = pos[1]-1
            #move two spots check
            if self.atStartingPos:
                if board.getPiece(pos[0],new_y) is None and board.getPiece(pos[0],new_y-1) is None:
                    moves.append((pos[0], new_y-1))
        #move forward
        if board.getPiece(pos[0],new_y) is None:
            moves.append((pos[0], new_y))
        #capture piece
        oppposing_pieces = board.getPiece((pos[0]+1, new_y))
        if oppposing_pieces is not None:
            if oppposing_pieces.getColor != self.getColor:
                moves.append((pos[0]+1, new_y))
        oppposing_pieces = board.getPiece((pos[0]-1, new_y))
        if oppposing_pieces is not None:
            if oppposing_pieces.getColor != self.getColor:
                moves.append((pos[0]-1, new_y))
        #en passant
        pawn = board.getPiece(pos[0]-1, pos[1])
        if pawn is not None:
            if pawn.getType() == "Pawn" and pawn.getColor != self.getColor and pawn.enPassant:
                moves.append((pos[0]-1, new_y))
        pawn = board.getPiece(pos[0]+1, pos[1])
        if pawn is not None:
            if pawn.getType() == "Pawn" and pawn.getColor != self.getColor and pawn.enPassant:
                moves.append((pos[0]+1, new_y))
        
        return moves

    def enPassantUpdate(self, allow):
        self.enPassant = allow
    
    def promotion(self):
        PROMOTION_ROW = {"white": 7, "black": 0}
        if self.getPos[1] == PROMOTION_ROW[self.getColor]:
            return True
        return False