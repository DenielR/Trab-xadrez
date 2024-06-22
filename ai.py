from player import Player
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class AI(Player):
    def calculate_best_move(self, board):
        best_move = None
        best_score = float('-inf')
        for row in board.squares:
            for square in row:
                piece = square.get_piece()
                if piece and piece.color == self.color:
                    valid_moves = piece.get_valid_moves(board)
                    for move in valid_moves:
                        original_square = piece.position
                        target_piece = move.get_piece()
                        original_square.piece = None
                        move.piece = piece
                        piece.position = move
                        score = self.minimax(board, 2, False)
                        move.piece = target_piece
                        original_square.piece = piece
                        piece.position = original_square
                        if score > best_score:
                            best_move = (piece, original_square, move)
                            best_score = score
        return best_move

    def minimax(self, board, depth, maximizing_player):
        if depth == 0:
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for row in board.squares:
                for square in row:
                    piece = square.get_piece()
                    if piece and piece.color == self.color:
                        valid_moves = piece.get_valid_moves(board)
                        for move in valid_moves:
                            original_square = piece.position
                            target_piece = move.get_piece()
                            original_square.piece = None
                            move.piece = piece
                            piece.position = move
                            eval = self.minimax(board, depth - 1, False)
                            move.piece = target_piece
                            original_square.piece = piece
                            piece.position = original_square
                            max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for row in board.squares:
                for square in row:
                    piece = square.get_piece()
                    if piece and piece.color != self.color:
                        valid_moves = piece.get_valid_moves(board)
                        for move in valid_moves:
                            original_square = piece.position
                            target_piece = move.get_piece()
                            original_square.piece = None
                            move.piece = piece
                            piece.position = move
                            eval = self.minimax(board, depth - 1, True)
                            move.piece = target_piece
                            original_square.piece = piece
                            piece.position = original_square
                            min_eval = min(min_eval, eval)
            return min_eval

    def evaluate_board(self, board):
        evaluation = 0
        for row in board.squares:
            for square in row:
                piece = square.get_piece()
                if piece:
                    value = 0
                    if isinstance(piece, Pawn):
                        value = 10
                    elif isinstance(piece, Knight) or isinstance(piece, Bishop):
                        value = 30
                    elif isinstance(piece, Rook):
                        value = 50
                    elif isinstance(piece, Queen):
                        value = 90
                    elif isinstance(piece, King):
                        value = 900
                    value = value if piece.color == self.color else -value
                    evaluation += value
        return evaluation