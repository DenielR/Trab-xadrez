import random
from player import Player

class AI(Player):
    def __init__(self, color):
        super().__init__(color)

    def make_random_move(self, board):
        all_valid_moves = self.get_valid_moves(board)
        if not all_valid_moves:
            return

        # Escolhe um movimento aleatório
        move = random.choice(all_valid_moves)
        piece, target_square = move
        from_square = piece.position

        from_square.piece = None
        target_square.piece = piece
        piece.position = target_square
        piece.has_moved = True
