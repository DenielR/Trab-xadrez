from piece import Piece
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = '♗' if color == 'white' else '♝'

    def get_valid_moves(self, board):
        moves = []
        x, y = self.position.x, self.position.y

        # Diagonal superior direita
        for i in range(1, 8):
            if 0 <= x + i < 8 and 0 <= y + i < 8:
                if board.squares[x + i][y + i].is_occupied():
                    if board.squares[x + i][y + i].get_piece().color != self.color:
                        moves.append(board.squares[x + i][y + i])
                    break
                moves.append(board.squares[x + i][y + i])
            else:
                break

        # Diagonal superior esquerda        
        for i in range(1, 8):
            if 0 <= x - i < 8 and 0 <= y + i < 8:
                if board.squares[x - i][y + i].is_occupied():
                    if board.squares[x - i][y + i].get_piece().color != self.color:
                        moves.append(board.squares[x - i][y + i])
                    break
                moves.append(board.squares[x - i][y + i])
            else:
                break
        
        # Diagonal inferior direita
        for i in range(1, 8):
            if 0 <= x + i < 8 and 0 <= y - i < 8:
                if board.squares[x + i][y - i].is_occupied():
                    if board.squares[x + i][y - i].get_piece().color != self.color:
                        moves.append(board.squares[x + i][y - i])
                    break
                moves.append(board.squares[x + i][y - i])
            else:
                break
        
        # Diagonal inferior esquerda
        for i in range(1, 8):
            if 0 <= x - i < 8 and 0 <= y - i < 8:
                if board.squares[x - i][y - i].is_occupied():
                    if board.squares[x - i][y - i].get_piece().color != self.color:
                        moves.append(board.squares[x - i][y - i])
                    break
                moves.append(board.squares[x - i][y - i])
            else:
                break

        return moves