from piece import Piece
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = '♖' if color == 'white' else '♜'

    def get_valid_moves(self, board):
        moves = []
        x, y = self.position.x, self.position.y

        # Linha horizontal direita
        for i in range(1, 8):
            if 0 <= x + i < 8:
                if board.squares[x + i][y].is_occupied():
                    if board.squares[x + i][y].get_piece().color != self.color:
                        moves.append(board.squares[x + i][y])
                    break
                moves.append(board.squares[x + i][y])
            else:
                break

        # Linha horizontal esquerda    
        for i in range(1, 8):
            if 0 <= x - i < 8:
                if board.squares[x - i][y].is_occupied():
                    if board.squares[x - i][y].get_piece().color != self.color:
                        moves.append(board.squares[x - i][y])
                    break
                moves.append(board.squares[x - i][y])
            else:
                break

        # Coluna vertical cima    
        for i in range(1, 8):
            if 0 <= y + i < 8:
                if board.squares[x][y + i].is_occupied():
                    if board.squares[x][y + i].get_piece().color != self.color:
                        moves.append(board.squares[x][y + i])
                    break
                moves.append(board.squares[x][y + i])
            else:
                break

        # Coluna vertical baixo    
        for i in range(1, 8):
            if 0 <= y - i < 8:
                if board.squares[x][y - i].is_occupied():
                    if board.squares[x][y - i].get_piece().color != self.color:
                        moves.append(board.squares[x][y - i])
                    break
                moves.append(board.squares[x][y - i])
            else:
                break

        return moves