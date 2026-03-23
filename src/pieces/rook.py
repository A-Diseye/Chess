from pieces.piece import Piece

class Rook(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
    
    def getMoves(self, board):
        moves = []
        pos = self.getPos
        for i in range(1, 8):
            if pos[0] + i < 8:
                if board.getPiece(pos[0] + i, pos[1]) is None:
                    moves.append((pos[0] + i, pos[1] + i))
                elif (
                    board.getPiece(pos[0] + i, pos[1]).getColor != self.getColor
                ):
                    moves.append((pos[0] + i, pos[1]))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if pos[0] - i >= 0:
                if board.getPiece(pos[0] - i, pos[1]) is None:
                    moves.append((pos[0] - i, pos[1]))
                elif (
                    board.getPiece(pos[0] - i, pos[1]).getColor != self.getColor
                ):
                    moves.append((pos[0] - i, pos[1]))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if pos[1] - i >= 0:
                if board.getPiece(pos[0], pos[1]) is None:
                    moves.append((pos[0], pos[1] - i))
                elif (
                    board.getPiece(pos[0], pos[1] - i).getColor != self.getColor
                ):
                    moves.append((pos[0], pos[1] - i))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if pos[1] + i < 8:
                if board.getPiece(pos[0], pos[1] + i) is None:
                    moves.append((pos[0], pos[1] + i))
                elif (
                    board.getPiece(pos[0], pos[1] + i).getColor != self.getColor
                ):
                    moves.append((pos[0], pos[1] + i))
                    break
                else:
                    break
        if self.atStartingPos:
            moves.extend(self.castle(board))
        return moves
    
    def castle(self, board):
        castling = []
        if self.getColor == "white":
            king = board.getPiece(4,0)
            if king is not None:
                if king.getType() == "King" and king.atStartingPos and not king.check(board):
                    pos = self.getPos
                    if pos[1] == 0:
                        if pos[0] < 4:
                            temp_pos = king.getPos
                            king.move((2,0))
                            if not (king.check(board) or king.checkMate(board) or board.getPiece(1,0) is not None or board.getPiece(2,0) is not None or board.getPiece(3,0) is not None):
                                castling.append((3,0))
                            king.move(temp_pos)
                        else:
                            temp_pos = king.getPos
                            king.move((6,0))
                            if not (king.check(board) or king.checkMate(board) or board.getPiece(5,0) is not None or board.getPiece(6,0) is not None):
                                castling.append((5,0))
                            king.move(temp_pos)
        else:
            king = board.getPiece(4,7)
            if king is not None:
                if pos[0] < 4:
                    temp_pos = king.getPos
                    king.move((2,7))
                    if not (king.check(board) or king.checkMate(board) or board.getPiece(1,7) is not None or board.getPiece(2,7) is not None or board.getPiece(3,7) is not None):
                        castling.append((3,0))
                    king.move(temp_pos)
                else:
                    temp_pos = king.getPos
                    king.move((6,7))
                    if not (king.check(board) or king.checkMate(board) or board.getPiece(5,7) is not None or board.getPiece(6,7) is not None):
                        castling.append((5,7))
                    king.move(temp_pos)
        return castling
                    