from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from square import Square

class Board:
    def __init__(self):
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
        self.initialize_board()

    def initialize_board(self):
        # Initialize pawns
        for x in range(8):
            self.squares[x][1].piece = Pawn('white', self.squares[x][1])
            self.squares[x][6].piece = Pawn('black', self.squares[x][6])
            # Initialize rooks
            self.squares[0][0].piece = Rook('white', self.squares[0][0])
            self.squares[7][0].piece = Rook('white', self.squares[7][0])
            self.squares[0][7].piece = Rook('black', self.squares[0][7])
            self.squares[7][7].piece = Rook('black', self.squares[7][7])
            # Initialize knights
            self.squares[1][0].piece = Knight('white', self.squares[1][0])
            self.squares[6][0].piece = Knight('white', self.squares[6][0])
            self.squares[1][7].piece = Knight('black', self.squares[1][7])
            self.squares[6][7].piece = Knight('black', self.squares[6][7])
            # Initialize bishops
            self.squares[2][0].piece = Bishop('white', self.squares[2][0])
            self.squares[5][0].piece = Bishop('white', self.squares[5][0])
            self.squares[2][7].piece = Bishop('black', self.squares[2][7])
            self.squares[5][7].piece = Bishop('black', self.squares[5][7])
            # Initialize queens
            self.squares[3][0].piece = Queen('white', self.squares[3][0])
            self.squares[3][7].piece = Queen('black', self.squares[3][7])
            # Initialize kings
            self.squares[4][0].piece = King('white', self.squares[4][0])
            self.squares[4][7].piece = King('black', self.squares[4][7])