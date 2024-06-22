from piece import Piece
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = '♙' if color == 'white' else '♟'
        self.direction = 1 if color == 'white' else -1
        self.has_moved = False

    def get_valid_moves(self, board):
        moves = []
        x, y = self.position.x, self.position.y
        direction = self.direction

        # Movimento para frente
        if 0 <= y + direction < 8 and not board.squares[x][y + direction].is_occupied():
            moves.append(board.squares[x][y + direction])

        # Movimento duplo para frente na primeira jogada
        if not self.has_moved and not board.squares[x][y + direction].is_occupied() and not board.squares[x][y + 2 * direction].is_occupied():
            moves.append(board.squares[x][y + 2 * direction])

        # Captura na diagonal esquerda
        if 0 <= x - 1 < 8 and 0 <= y + direction < 8 and board.squares[x - 1][y + direction].is_occupied() and board.squares[x - 1][y + direction].get_piece().color != self.color:
            moves.append(board.squares[x - 1][y + direction])
        
        # Captura na diagonal direita
        if 0 <= x + 1 < 8 and 0 <= y + direction < 8 and board.squares[x + 1][y + direction].is_occupied() and board.squares[x + 1][y + direction].get_piece().color != self.color:
            moves.append(board.squares[x + 1][y + direction])

        return moves