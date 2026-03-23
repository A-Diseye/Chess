from pieces.piece import Piece

class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
    def getMoves(self, board):
        moves = []
        # Define all possible knight moves
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dx, dy in knight_moves:
            new_x = self.getPos[0] + dx
            new_y = self.getPos[1] + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.getPiece(new_x,new_y) is None:
                    moves.append((new_x, new_y))
                elif board.getPiece(new_x,new_y).getColor != self.getColor:
                    moves.append((new_x, new_y))
        return moves