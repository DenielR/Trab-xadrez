class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = []
        
    def get_valid_moves(self, board):
        moves = []
        for row in board.squares:
            for square in row:
                piece = square.get_piece()
                if piece and piece.color == self.color:
                    valid_moves = piece.get_valid_moves(board)
                    for move in valid_moves:
                        moves.append((piece, move))
        return moves
