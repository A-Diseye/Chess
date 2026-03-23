from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)

    def getMoves(self, board):
        moves = []
        pos = self.getPos
        for i in range(1, 8):
            if pos[0] + i < 8 and pos[1] + i < 8:
                if board.getPiece(pos[0] + i, pos[1] + i) is None:
                    moves.append((pos[0] + i, pos[1] + i))
                elif (
                    board.getPiece(pos[0] + i, pos[1] + i).getColor != self.getColor
                ):
                    moves.append((pos[0] + i, pos[1] + i))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if pos[0] - i >= 0 and pos[1] - i >= 0:
                if board.getPiece(pos[0] - i, pos[1] - i) is None:
                    moves.append((pos[0] - i, pos[1] - i))
                elif (
                    board.getPiece(pos[0] - i, pos[1] - i).getColor != self.getColor
                ):
                    moves.append((pos[0] - i, pos[1] - i))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if pos[0] + i < 8 and pos[1] - i >= 0:
                if board.getPiece(pos[0] + i, pos[1] - i) is None:
                    moves.append((pos[0] + i, pos[1] - i))
                elif (
                    board.getPiece(pos[0] + i, pos[1] - i).getColor != self.getColor
                ):
                    moves.append((pos[0] + i, pos[1] - i))
                    break
                else:
                    break
            else:
                break
        for i in range(1, 8):
            if pos[0] - i >= 0 and pos[1] + i < 8:
                if board.getPiece(pos[0] - i, pos[1] + i) is None:
                    moves.append((pos[0] - i, pos[1] + i))
                elif (
                    board.getPiece(pos[0] - i, pos[1] + i).getColor != self.getColor
                ):
                    moves.append((pos[0] - i, pos[1] + i))
                    break
                else:
                    break
        return moves