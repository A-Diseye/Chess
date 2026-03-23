from pieces.piece import Piece


class King(Piece):
    def __init__(self, color):
        if color == "white":
            super().__init__(color, (4,0))
        else:
            super().__init__(color, (4,7))

    def getMoves(self, board):
        move_rules = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        moves = []
        for dx, dy in move_rules:
            new_x = self.pos[0] + dx
            new_y = self.pos[1] + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.getPiece(new_x, new_y) is None:
                    moves.append((new_x, new_y))
                elif board.getPiece(new_x, new_y).getColor != self.getColor:
                    temp_pos = self.pos
                    self.move((new_x, new_y))
                    if not self.checkMate(board) and not self.check(board):
                        moves.append((new_x, new_y))
                    self.pos = temp_pos
        if self.atStartingPos and not self.check(board):
            moves.extend(self.castle(board))
        return moves

    def castle(self, board):
        castling = []
        if self.getColor == "white":
            castle_1 = board.getPiece(0,0)
            castle_2 = board.getPiece(7,0)
            if castle_1 is not None:
                if castle_1.getType() == "Rook" and castle_1.atStartingPos:
                    temp_pos = self.getPos
                    self.move((2,0))
                    if not (self.check(board) or self.checkMate(board) or board.getPiece(1,0) is not None or board.getPiece(2,0) is not None or board.getPiece(3,0) is not None):
                        castling.append((2,0))
                    self.move(temp_pos)
            if castle_2 is not None:
                if castle_2.getType() == "Rook" and castle_2.atStartingPos:
                    temp_pos = self.getPos
                    self.move((6,0))
                    if not (self.check(board) or self.checkMate(board) or board.getPiece(5,0) is not None or board.getPiece(6,0) is not None):
                        castling.append((6,0))
                    self.move(temp_pos)
        else:
            castle_1 = board.getPiece(0,7)
            castle_2 = board.getPiece(7,7)
            if castle_1 is not None:
                if castle_1.getType() == "Rook" and castle_1.atStartingPos:
                    temp_pos = self.getPos
                    self.move((2,7))
                    if not (self.check(board) or self.checkMate(board) or board.getPiece(1,7) is not None or board.getPiece(2,7) is not None or board.getPiece(3,7) is not None):
                        castling.append((2,7))
                    self.move(temp_pos)
            if castle_2 is not None:
                if castle_2.getType() == "Rook" and castle_2.atStartingPos:
                    temp_pos = self.getPos
                    self.move((6,7))
                    if not (self.check(board) or self.checkMate(board) or board.getPiece(5,7) is not None or board.getPiece(6,7) is not None):
                        castling.append((6,7))
                    self.move(temp_pos)
        return castling
                    


    def checkMate(self, board):
        possible_moves = self.getMoves(board)
        if possible_moves:
            return False
        return True

    def check(self, board):
        for i in range(8):
            for j in range(8):
                piece = board.getPiece(i, j)
                if piece is not None and piece.getColor != self.getColor:
                    if (self.pos[0], self.pos[1]) in piece.getMoves(board):
                        return True
        return False
