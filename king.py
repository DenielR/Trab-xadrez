from piece import Piece
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = '♔' if color == 'white' else '♚'

    def get_valid_moves(self, board):
        moves = []
        x, y = self.position.x, self.position.y
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for dx, dy in deltas:
            if 0 <= x + dx < 8 and 0 <= y + dy < 8:
                if not board.squares[x + dx][y + dy].is_occupied() or board.squares[x + dx][y + dy].get_piece().color != self.color:
                    moves.append(board.squares[x + dx][y + dy])

        return moves